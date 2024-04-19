# My Custom Component daly_bms for ESPHome

This repository is a collection of my custom components for [ESPHome](https://esphome.io/)
Just tried on ESP32.

Extended sensors (measurements):
```
    bms1_fehlercode
    power:
    bms_watchdog:
    cycle:
    cell_voltage_difference:
```
Extended binary_sensors:
```
    cell_1_balance_active:
    ...
    cell_16_balance_active:
```
Extended sensors (level 1 + 2 setup - just reading):
```
    cell_level_1_alarm_high_voltage:
    cell_level_2_alarm_high_voltage:
    cell_level_1_alarm_low_voltage:
    cell_level_2_alarm_low_voltage:

    battpack_level_1_alarm_high_voltage:
    battpack_level_2_alarm_high_voltage:
    battpack_level_1_alarm_low_voltage:
    battpack_level_2_alarm_low_voltage:

    cell_level_1_alarm_difference_temperature:
    cell_level_2_alarm_difference_temperature:

    cell_level_1_alarm_difference_voltage:
    cell_level_2_alarm_difference_voltage:

    cell_nominal_capacity:
    cell_nominal_voltage:
```
## Usage

To use the components provided by this repository, simply add this to your `.yaml` definition:

```yaml
external_components:
  - source: github://SirUlbrich/daly_bms@components
    components: [daly_bms]
```

More information can be found [here](https://esphome.io/components/external_components.html).

## Components

### [daly_bms](daly_bms)


## How to use / example ESPHome configuration

configuration like original [ESPHome-Daly_BMS](https://esphome.io/components/sensor/daly_bms.html)

you can use more than one daly:
```
uart:
  - id: uart1
    tx_pin: GPIO17
    rx_pin: GPIO16
    baud_rate: 9600
  - id: uart2
    tx_pin: GPIO22
    rx_pin: GPIO21
    baud_rate: 9600

daly_bms:
  - uart_id: uart1
    id: bms1
    update_interval: 20s
  - uart_id: uart2
    id: bms2
    update_interval: 20s
```
you can get failure status code: 
change "template_sens" to your template sensor.

```daly_bms:
  - uart_id: uart1
    id: bms1
    update_interval: 20s
    on_failure_status: 
      - lambda: id(template_sens).publish_state(x[6]);
```

## Example .yaml file

Complete example esp32 .yaml file with all sensors:
```yaml
substitutions:
  node_name: esp32
  device_name3: Daly BMS
esp32:
  board: nodemcu-32s
  framework:
    type: arduino
    version: latest
esphome:
  name: $node_name
  friendly_name: ESP32-1
  comment: Daly-BMS
external_components:
  - source: 
      type: local
      path: my_components
logger:
  level: WARN
api:
  password: !secret ha_api_key
ota:
  password: !secret ha_ota_pw
wifi:
  ssid: !secret wlan
  password: !secret wlanpw
  manual_ip:
    static_ip: 192.168.178.158
    gateway: 192.168.178.1
    subnet: 255.255.255.0
    dns1: 192.168.178.1
  # Enable fallback hotspot (captive portal) in case wifi connection fails
  ap:
    ssid: "Esp32 Deye Fallback Hotspot"
    password: "123456789"
  reboot_timeout: 0s

uart:
  - id: uart_daly
    tx_pin: GPIO22
    rx_pin: GPIO21
    baud_rate: 9600
    rx_buffer_size: 256

daly_bms:
  - uart_id: uart_daly
    id: bms1
    update_interval: 20s
    on_failure_status: 
      - lambda: id(bms1_fehlercode).publish_state(x[6]);

binary_sensor:
  - platform: daly_bms
    bms_daly_id: bms1
    charging_mos_enabled:
      name: "BMS Laden MOS"
    discharging_mos_enabled:
      name: "BMS Entladen MOS"
    cell_1_balance_active:
      name: "${device_name3}-Zelle 1 Balance"
    cell_2_balance_active:
      name: "${device_name3}-Zelle 2 Balance"
    cell_3_balance_active:
      name: "${device_name3}-Zelle 3 Balance"
    cell_4_balance_active:
      name: "${device_name3}-Zelle 4 Balance"
    cell_5_balance_active:
      name: "${device_name3}-Zelle 5 Balance"
    cell_6_balance_active:
      name: "${device_name3}-Zelle 6 Balance"
    cell_7_balance_active:
      name: "${device_name3}-Zelle 7 Balance"
    cell_8_balance_active:
      name: "${device_name3}-Zelle 8 Balance"
    cell_9_balance_active:
      name: "${device_name3}-Zelle 9 Balance"
    cell_10_balance_active:
      name: "${device_name3}-Zelle 10 Balance"
    cell_11_balance_active:
      name: "${device_name3}-Zelle 11 Balance"
    cell_12_balance_active:
      name: "${device_name3}-Zelle 12 Balance"
    cell_13_balance_active:
      name: "${device_name3}-Zelle 13 Balance"
    cell_14_balance_active:
      name: "${device_name3}-Zelle 14 Balance"
    cell_15_balance_active:
      name: "${device_name3}-Zelle 15 Balance"
    cell_16_balance_active:
      name: "${device_name3}-Zelle 16 Balance"
text_sensor:
  - platform: daly_bms
    bms_daly_id: bms1
    status:
      name: "${device_name3}-Status"
sensor:
  - platform: wifi_signal # Reports the WiFi signal strength/RSSI in dB
    name: "${node_name}-WiFi Signal dB"
    id: wifi_signal_db
    update_interval: 60s
    entity_category: "diagnostic"
  - platform: copy # Reports the WiFi signal strength in %
    source_id: wifi_signal_db
    name: "${node_name}-WiFi Signal in Prozent"
    filters:
      - lambda: return min(max(2 * (x + 100.0), 0.0), 100.0);
    unit_of_measurement: "Signal %"
    entity_category: "diagnostic"
  - platform: template
    id: bms1_fehlercode
    name: "${device_name3}-fehlercode"
    accuracy_decimals: 0
  - platform: daly_bms
    bms_daly_id: bms1
    remaining_capacity:
      name: "Kapazitt-Speicher"
      unit_of_measurement: Ah
      state_class: "measurement"
    cells_number:
      name: "Zellenanzahl-Speicher"
    voltage:
      name: "Gesamtspannung-Speicher"
      unit_of_measurement: V
      state_class: "measurement"
    current:
      name: "Strom-Speicher"
      unit_of_measurement: A
      state_class: "measurement"
    power:
      name: "${device_name3}-Power"
      unit_of_measurement: W
      state_class: "measurement"
    battery_level:
      name: "SOC-Speicher"
      unit_of_measurement: '%'
      state_class: "measurement"
    cycle:
      name: "BMS-Zyklen"
      state_class: "measurement"
    bms_watchdog:
      name: "BMS-Watchdog"
      state_class: "measurement"
    max_temperature:
      name: "Temperatur Max-Speicher"
      unit_of_measurement: °C
      state_class: "measurement"
    max_temperature_probe_number:
      name: "Temperaturfühler Max-Speicher"
      unit_of_measurement: °C
      state_class: "measurement"
    min_temperature:
      name: "Temperatur Min-Speicher"
      unit_of_measurement: °C
      state_class: "measurement"
    min_temperature_probe_number:
      name: "Temperaturfühler Min-Speicher"
      unit_of_measurement: °C
      state_class: "measurement"
    temperature_1:
      name: "Zellentemperatur 1-Speicher"
      unit_of_measurement: °C
      state_class: "measurement"
    temperature_2:
      name: "Zellentemperatur 2-Speicher"
      unit_of_measurement: °C
      state_class: "measurement"
    max_cell_voltage:
      name: "Zellenspannung Max-Speicher"
      unit_of_measurement: V
      state_class: "measurement"
      accuracy_decimals: "3"
    max_cell_voltage_number:
      name: "Zellennummer Zellenspannung Max-Speicher"
      state_class: "measurement"
    min_cell_voltage:
      name: "Zellenspannung Min-Speicher"
      unit_of_measurement: V
      state_class: "measurement"
      accuracy_decimals: "3"
    min_cell_voltage_number:
      name: "Zellennummer Zellenspannung Min-Speicher"
      state_class: "measurement"
    cell_1_voltage:
      name: "Zelle 1 Spannung"
      unit_of_measurement: V
      state_class: "measurement"
    cell_2_voltage:
      name: "Zelle 2 Spannung"
      unit_of_measurement: V
      state_class: "measurement"
    cell_3_voltage:
      name: "Zelle 3 Spannung"
      unit_of_measurement: V
      state_class: "measurement"
    cell_4_voltage:
      name: "Zelle 4 Spannung"
      unit_of_measurement: V
      state_class: "measurement"
    cell_5_voltage:
      name: "Zelle 5 Spannung"
      unit_of_measurement: V
      state_class: "measurement"
    cell_6_voltage:
      name: "Zelle 6 Spannung"
      unit_of_measurement: V
      state_class: "measurement"
    cell_7_voltage:
      name: "Zelle 7 Spannung"
      unit_of_measurement: V
      state_class: "measurement"
    cell_8_voltage:
      name: "Zelle 8 Spannung"
      unit_of_measurement: V
      state_class: "measurement"
    cell_9_voltage:
      name: "Zelle 9 Spannung"
      unit_of_measurement: V
      state_class: "measurement"
    cell_10_voltage:
      name: "Zelle 10 Spannung"
      unit_of_measurement: V
      state_class: "measurement"
    cell_11_voltage:
      name: "Zelle 11 Spannung"
      unit_of_measurement: V
      state_class: "measurement"
    cell_12_voltage:
      name: "Zelle 12 Spannung"
      unit_of_measurement: V
      state_class: "measurement"
    cell_13_voltage:
      name: "Zelle 13 Spannung"
      unit_of_measurement: V
      state_class: "measurement"
    cell_14_voltage:
      name: "Zelle 14 Spannung"
      unit_of_measurement: V
      state_class: "measurement"
    cell_15_voltage:
      name: "Zelle 15 Spannung"
      unit_of_measurement: V
      state_class: "measurement"
    cell_16_voltage:
      name: "Zelle 16 Spannung"
      unit_of_measurement: V
      state_class: "measurement"
    cell_voltage_difference:
      name: "${device_name3}-Differenz Zellenspannung"
      unit_of_measurement: V
      state_class: "measurement"
      accuracy_decimals: "3"
    # eingestellte werte
    cell_level_1_alarm_high_voltage:
      name: "${device_name3}-Warnung Zellenspannung zu hoch"
    cell_level_2_alarm_high_voltage:
      name: "${device_name3}-Alarm Zellenspannung zu hoch"
    cell_level_1_alarm_low_voltage:
      name: "${device_name3}-Warnung Zellenspannung zu gering"
    cell_level_2_alarm_low_voltage:
      name: "${device_name3}-Alarm Zellenspannung zu gering"
    battpack_level_1_alarm_high_voltage:
      name: "${device_name3}-Warnung Battpackspannung zu hoch"
    battpack_level_2_alarm_high_voltage:
      name: "${device_name3}-Alarm Battpackspannung zu hoch"
    battpack_level_1_alarm_low_voltage:
      name: "${device_name3}-Warnung Battpackspannung zu gering"
    battpack_level_2_alarm_low_voltage:
      name: "${device_name3}-Alarm Battpackspannung zu gering"
    cell_level_1_alarm_difference_temperature:
      name: "${device_name3}-Warnung Temperaturdifferenz"
    cell_level_2_alarm_difference_temperature:
      name: "${device_name3}-Alarm Temperaturdifferenz"
    cell_level_1_alarm_difference_voltage:
      name: "${device_name3}-Warnung Spannungsdifferenz"
    cell_level_2_alarm_difference_voltage:
      name: "${device_name3}-Alarm Spannungsdifferenz"
    cell_nominal_capacity:
      name: "${device_name3}-nominale Kapazitt pro Zelle"
    cell_nominal_voltage:
      name: "${device_name3}-nominale Spannung pro Zelle"
```

Many thanks to ssieb for helping me.