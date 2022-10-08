use autoclip_core::{AutoclipPlugin, PluginRegistrar};
use chrono::prelude::*;
use chrono_tz::{UTC, Tz};
use dtparse;
use iana_time_zone::get_timezone;

struct TwTimestamp {}

autoclip_core::export_plugin!("autoclip-tw-timestamp", TwTimestamp {});

impl AutoclipPlugin for TwTimestamp {
    fn on_clip(&self, contents: &str) -> Option<String> {
        let (naive_datetime, _) = dtparse::parse(contents).ok()?;
        let tz: Tz = get_timezone().ok()?.parse().ok()?;
        let local_time = tz.from_local_datetime(&naive_datetime).single()?;
        let utc_time = local_time.with_timezone(&UTC);
        
        let mut utc_string = utc_time.format("%Y%m%d%H%M%S%f").to_string();
        utc_string.truncate(utc_string.len() - 6);

        Some(utc_string)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_timestamps() {
        let twt = TwTimestamp {};
        println!("{:?}", "Friday, October 7, 2022 7:17 PM".parse::<DateTime<Local>>());
        assert_eq!(twt.on_clip("Friday, October 7, 2022 7:17 PM"), Some("20221007231700000".to_string()));
    }
}
