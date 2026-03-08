Features to be added
* For dev version 1.1.8 > Handle ACK, send _id  {"_id":<integer>}  verify receive {"type":"ack","value":<integer>}
* Set origin for http requests
* Settings
  * Powerstate after outage - "state_after_powerloss":	2=Previous state, 1=On, 0=Off
  * Dimmer minimum - "dimmer_min_dim": 0.0-1.0
  * Double click for 100% dim level - "disable_multi_press": 0=enabled, 1=disabled
  * 433 Mhz
    * When transmitters is used with dimmer device, use this as "on" level - "dimmer_on_start_level": 0.0-1.0 
    * When transmitters is used with dimmer device, use this as "off" level - "dimmer_off_level": 0.0-1.0 
    * Configure allow ON from transmitters - "disable_on_transmitters": 0=enabled, 1=disabled
    * Configure allow OFF from transmitters - "disable_off_transmitters": 0=enabled, 1=disabled
    * Enable ON to toggle device from transmitters - "toggle_433": 0=disabled, 1=enabled
	* Blink LED when device is receiving from transmitter - "blink_on_433_on":	0 = disable, 1=enabled
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