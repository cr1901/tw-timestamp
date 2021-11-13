#!/usr/bin/env python

import dateutil.parser
import pyperclip
import pytz

def parse_as_tw_timestamp(inp):
    eastern = pytz.timezone("US/Eastern")
    try:
        naive_dt = dateutil.parser.parse(inp)
    except dateutil.parser._parser.ParserError as e:
        return inp

    return eastern.localize(naive_dt, is_dst=None).strftime("%Y%m%d%H%M%S%f")[:-3]

if __name__ == "__main__":
    print("TW date conversion active")

    try:
        while True:
            inp = pyperclip.waitForNewPaste()
            tw_time_or_inp = parse_as_tw_timestamp(inp)
            if inp != tw_time_or_inp:
                print(inp, "=>", tw_time_or_inp)
            else:
                print(inp)
            pyperclip.copy(tw_time_or_inp)
    except KeyboardInterrupt:
        pass

    print("TW date conversion disabled")
