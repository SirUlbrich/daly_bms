import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor
from . import DalyBmsComponent, CONF_BMS_DALY_ID

CONF_CHARGING_MOS_ENABLED = "charging_mos_enabled"
CONF_DISCHARGING_MOS_ENABLED = "discharging_mos_enabled"
CONF_CELL_1_BALANCE_ACTIVE = "cell_1_balance_active"
CONF_CELL_2_BALANCE_ACTIVE = "cell_2_balance_active"
CONF_CELL_3_BALANCE_ACTIVE = "cell_3_balance_active"
CONF_CELL_4_BALANCE_ACTIVE = "cell_4_balance_active"
CONF_CELL_5_BALANCE_ACTIVE = "cell_5_balance_active"
CONF_CELL_6_BALANCE_ACTIVE = "cell_6_balance_active"
CONF_CELL_7_BALANCE_ACTIVE = "cell_7_balance_active"
CONF_CELL_8_BALANCE_ACTIVE = "cell_8_balance_active"
CONF_CELL_9_BALANCE_ACTIVE = "cell_9_balance_active"
CONF_CELL_10_BALANCE_ACTIVE = "cell_10_balance_active"
CONF_CELL_11_BALANCE_ACTIVE = "cell_11_balance_active"
CONF_CELL_12_BALANCE_ACTIVE = "cell_12_balance_active"
CONF_CELL_13_BALANCE_ACTIVE = "cell_13_balance_active"
CONF_CELL_14_BALANCE_ACTIVE = "cell_14_balance_active"
CONF_CELL_15_BALANCE_ACTIVE = "cell_15_balance_active"
CONF_CELL_16_BALANCE_ACTIVE = "cell_16_balance_active"


TYPES = [
    CONF_CHARGING_MOS_ENABLED,
    CONF_DISCHARGING_MOS_ENABLED,
    CONF_CELL_1_BALANCE_ACTIVE,
    CONF_CELL_2_BALANCE_ACTIVE,
    CONF_CELL_3_BALANCE_ACTIVE,
    CONF_CELL_4_BALANCE_ACTIVE,
    CONF_CELL_5_BALANCE_ACTIVE,
    CONF_CELL_6_BALANCE_ACTIVE,
    CONF_CELL_7_BALANCE_ACTIVE,
    CONF_CELL_8_BALANCE_ACTIVE,
    CONF_CELL_9_BALANCE_ACTIVE,
    CONF_CELL_10_BALANCE_ACTIVE,
    CONF_CELL_11_BALANCE_ACTIVE,
    CONF_CELL_12_BALANCE_ACTIVE,
    CONF_CELL_13_BALANCE_ACTIVE,
    CONF_CELL_14_BALANCE_ACTIVE,
    CONF_CELL_15_BALANCE_ACTIVE,
    CONF_CELL_16_BALANCE_ACTIVE,
]

DALY_BINARY_SCHEMA = binary_sensor.binary_sensor_schema()

CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(CONF_BMS_DALY_ID): cv.use_id(DalyBmsComponent),
            cv.Optional(CONF_CHARGING_MOS_ENABLED): DALY_BINARY_SCHEMA,
            cv.Optional(CONF_DISCHARGING_MOS_ENABLED): DALY_BINARY_SCHEMA,
            cv.Optional(CONF_CELL_1_BALANCE_ACTIVE): DALY_BINARY_SCHEMA,
            cv.Optional(CONF_CELL_2_BALANCE_ACTIVE): DALY_BINARY_SCHEMA,
            cv.Optional(CONF_CELL_3_BALANCE_ACTIVE): DALY_BINARY_SCHEMA,
            cv.Optional(CONF_CELL_4_BALANCE_ACTIVE): DALY_BINARY_SCHEMA,
            cv.Optional(CONF_CELL_5_BALANCE_ACTIVE): DALY_BINARY_SCHEMA,
            cv.Optional(CONF_CELL_6_BALANCE_ACTIVE): DALY_BINARY_SCHEMA,
            cv.Optional(CONF_CELL_7_BALANCE_ACTIVE): DALY_BINARY_SCHEMA,
            cv.Optional(CONF_CELL_8_BALANCE_ACTIVE): DALY_BINARY_SCHEMA,
            cv.Optional(CONF_CELL_9_BALANCE_ACTIVE): DALY_BINARY_SCHEMA,
            cv.Optional(CONF_CELL_10_BALANCE_ACTIVE): DALY_BINARY_SCHEMA,
            cv.Optional(CONF_CELL_11_BALANCE_ACTIVE): DALY_BINARY_SCHEMA,
            cv.Optional(CONF_CELL_12_BALANCE_ACTIVE): DALY_BINARY_SCHEMA,
            cv.Optional(CONF_CELL_13_BALANCE_ACTIVE): DALY_BINARY_SCHEMA,
            cv.Optional(CONF_CELL_14_BALANCE_ACTIVE): DALY_BINARY_SCHEMA,
            cv.Optional(CONF_CELL_15_BALANCE_ACTIVE): DALY_BINARY_SCHEMA,
            cv.Optional(CONF_CELL_16_BALANCE_ACTIVE): DALY_BINARY_SCHEMA,
        }
    ).extend(cv.COMPONENT_SCHEMA)
)


async def setup_conf(config, key, hub):
    if sensor_config := config.get(key):
        var = await binary_sensor.new_binary_sensor(sensor_config)
        cg.add(getattr(hub, f"set_{key}_binary_sensor")(var))


async def to_code(config):
    hub = await cg.get_variable(config[CONF_BMS_DALY_ID])
    for key in TYPES:
        await setup_conf(config, key, hub)