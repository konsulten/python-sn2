Features to be added
* For dev version 1.1.8 > Handle ACK, send _id  {"_id":<integer>}  verify receive {"type":"ack","value":<integer>}
* Set origin for http requests
* Information data
 * Uptime in seconds - "u"
 * \# of Paired transmitters - "tsc"
 * Device temperature - "t"
 * Clock syncronized - "cs": True, False
 * Sunrise/Sunset hour+minute - "sr_h", "sr_n", "ss_h", "ss_m"
 * Timezone - "tz_i"
 * Timezone offset - "tz_o"
 * Timezone daylight saving time - "tzdst": 0=disabled, 1=enabled
 * Longitude - "lat"
 * Latitude - "long"

Unknown settings:
* "auto_on_seconds"
* "auto_off_seconds"
* "enable_local_security"
* "vacation_mode"
* "disable_network_ctrl"
* "button_type"
* "position_man_set"
* "remote_log"
* "notifcation_on" / "notification_on"
* "notifcation_off" / "notification_off"

Unknown information:
* "fhs" integer
* "c" bool
* "rr" integer