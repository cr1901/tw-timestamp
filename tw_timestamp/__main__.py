#!/usr/bin/env python

import argparse
import dateutil.parser
import pyperclip
import pytz
import sys


def parse_as_tw_timestamp(inp, tz, dst):
    try:
        naive_dt = dateutil.parser.parse(inp)
    # Large ints will be parsed as Unix time and Overflow, ignore them.
    except (dateutil.parser._parser.ParserError, OverflowError):
        return inp

    return (tz.localize(naive_dt, is_dst=dst).astimezone(pytz.utc)
              .strftime("%Y%m%d%H%M%S%f")[:-3])


def main():
    parser = argparse.ArgumentParser(
        description="Clipboard hook for converting dates to TiddlyWiki"
        "format.")
    parser.add_argument("-t", "--time-zone", type=str,
                        help="Local Time Zone assumed for copied dates.")
    parser.add_argument("-d", "--dst", choices=["True", "False", "None"],
                        help="Assume DST, no DST, or guess by default"
                             " (and error if ambiguous).",
                        default="None")
    parser.add_argument("--dump", action="store_true",
                        help="Dump list of valid Time Zones and exit.")
    args = parser.parse_args()

    if args.dump:
        print("List of available Time Zones:")
        for tz in pytz.common_timezones:
            print(tz)
        sys.exit(0)

    if args.dst == "None":
        dst = None
    elif args.dst == "True":
        dst = True
    else:
        dst = False

    if not args.time_zone:
        print("Time Zone must be provided. Use --dump option for list.")
        sys.exit(-1)
    tz = pytz.timezone(args.time_zone)

    print("TW date conversion active")

    try:
        while True:
            # Will not run twice for the same exact copied input.
            inp = pyperclip.waitForNewPaste()
            tw_time_or_inp = parse_as_tw_timestamp(inp, tz, dst)
            if inp != tw_time_or_inp:
                print(inp, "=>", tw_time_or_inp)
            else:
                print(inp)
            pyperclip.copy(tw_time_or_inp)
    except KeyboardInterrupt:
        pass

    print("TW date conversion disabled")


if __name__ == "__main__":
    main()
