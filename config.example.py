import logging
from bike import Bike

# Logging
log_level = logging.INFO

# Interval in seconds
interval = 120

# Pushover credentials
pushover_user_key = "PUSHOVER USER"
pushover_api_token = "PUSHOVER TOKEN"

# List of bikes to check
bike_map = []
# bike_map.append(
#     Bike("Endurace Allroad Metal Berry",
#         "https://www.canyon.com/en-gr/road-bikes/endurance-bikes/endurace/allroad/endurace-allroad/4164.html?dwvar_4164_pv_rahmenfarbe=R138_P02&dwvar_4164_pv_rahmengroesse=2XL",
#         "2XL"
#         )
# )
bike_map.append(
    Bike("Endurace Allroad Metal Berry",
         "https://www.canyon.com/en-gr/road-bikes/endurance-bikes/endurace/allroad/endurace-allroad/4164.html?dwvar_4164_pv_rahmenfarbe=R138_P02&dwvar_4164_pv_rahmengroesse=M",
         "M"
         )
)