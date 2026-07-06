# Importing basic Python libraries:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ---------------------------------------------------------------------------------------------
# STEP 1. Import and Append Datasets
# ---------------------------------------------------------------------------------------------

# =========================
# 1. CHARACTERISTICS
# =========================

characteristics_dfs = []

for year in range(2020, 2025):
    file = f"datasets/caracteristiques-{year}.csv"

    df = pd.read_csv(file, sep=";", engine="python")

    # clean column names
    df.columns = df.columns.str.replace('"', '').str.strip()

    # fix schema difference (2022 issue)
    df.rename(columns={"Accident_Id": "Num_Acc"}, inplace=True)

    # add year column
    df["year"] = year

    characteristics_dfs.append(df)

characteristics = pd.concat(characteristics_dfs, ignore_index=True)


# =========================
# 2. LOCATIONS (LIEUX)
# =========================

location_dfs = []

for year in range(2020, 2025):
    file = f"datasets/lieux-{year}.csv"

    df = pd.read_csv(file, sep=";", engine="python")

    # clean column names
    df.columns = df.columns.str.replace('"', '').str.strip()

    # add year column
    df["year"] = year

    location_dfs.append(df)

locations = pd.concat(location_dfs, ignore_index=True)


# =========================
# 3. VEHICLES (VEHICULES)
# =========================

vehicle_dfs = []

for year in range(2020, 2025):
    file = f"datasets/vehicules-{year}.csv"

    df = pd.read_csv(file, sep=";", engine="python")

    # clean column names
    df.columns = df.columns.str.replace('"', '').str.strip()

    # add year column
    df["year"] = year

    vehicle_dfs.append(df)

vehicles = pd.concat(vehicle_dfs, ignore_index=True)


# =========================
# 4. USERS (USAGERS)
# =========================

user_dfs = []

for year in range(2020, 2025):
    file = f"datasets/usagers-{year}.csv"

    df = pd.read_csv(file, sep=";", engine="python")

    df.columns = df.columns.str.replace('"', '').str.strip()

    # fix missing "id_usager" column in 2020 table automatically
    if "id_usager" not in df.columns:
        df.insert(1, "id_usager", pd.NA)

    # add year column
    df["year"] = year

    user_dfs.append(df)

users = pd.concat(user_dfs, ignore_index=True)


# =========================
# QUICK CHECKS
# =========================

print("Characteristics:", characteristics.shape)
print("Locations:", locations.shape)
print("Vehicles:", vehicles.shape)
print("Users:", users.shape)

print("\n==================== CHARACTERISTICS ====================")
print(characteristics.head())

print("\n==================== LOCATIONS ====================")
print(locations.head())

print("\n==================== VEHICLES ====================")
print(vehicles.head())

print("\n==================== USERS ====================")
print(users.head())

# ------------------------------------------------------------------------------------------
# STEP 2. Save all appended tables
# ------------------------------------------------------------------------------------------

output_path = r"D:\PycharmProjects\Paris_Road_Traffic_Analysis\datasets\processed"

import os
os.makedirs(output_path, exist_ok=True)

# 1. Save CHARACTERISTICS

characteristics.to_csv(
    os.path.join(output_path, "characteristics.csv"),
    sep=";",
    index=False,
    encoding="utf-8"
)

# 2. Save LOCATIONS

locations.to_csv(
    os.path.join(output_path, "locations.csv"),
    sep=";",
    index=False,
    encoding="utf-8"
)

# 3. Save VEHICLES

vehicles.to_csv(
    os.path.join(output_path, "vehicles.csv"),
    sep=";",
    index=False,
    encoding="utf-8"
)

# 4. Save USERS

users.to_csv(
    os.path.join(output_path, "users.csv"),
    sep=";",
    index=False,
    encoding="utf-8"
)

# ------------------------------------------------------------------------------------------
# STEP 3. Summary Tables
# ------------------------------------------------------------------------------------------

# Load processed files

import pandas as pd
import os

processed_path = r"D:\PycharmProjects\Paris_Road_Traffic_Analysis\datasets\processed"

characteristics = pd.read_csv(
    os.path.join(processed_path, "characteristics.csv"),
    sep=";"
)

locations = pd.read_csv(
    os.path.join(processed_path, "locations.csv"),
    sep=";"
)

vehicles = pd.read_csv(
    os.path.join(processed_path, "vehicles.csv"),
    sep=";"
)

users = pd.read_csv(
    os.path.join(processed_path, "users.csv"),
    sep=";"
)

# Summary Tables for each dataset

def create_summary(df):
    summary = pd.DataFrame({
        "Column Name": df.columns,
        "Data Type": df.dtypes.values,
        "Missing Values": df.isnull().sum().values,
        "Missing %": df.isnull().mean().values * 100,
        "Unique Values": df.nunique().values
    })
    return summary

print("\n==================== CHARACTERISTICS ====================")
characteristics_summary = create_summary(characteristics)
print(characteristics_summary)

print("\n==================== LOCATIONS ====================")
locations_summary = create_summary(locations)
print(locations_summary)

print("\n==================== VEHICLES ====================")
vehicles_summary = create_summary(vehicles)
print(vehicles_summary)

print("\n==================== USERS ====================")
users_summary = create_summary(users)
print(users_summary)

# Shapes of Tables

print("Characteristics shape:", characteristics.shape)
print("Locations shape:", locations.shape)
print("Vehicles shape:", vehicles.shape)
print("Users shape:", users.shape)


# ------------------------------------------------------------------------------------------
# STEP 4. Data Cleaning
# ------------------------------------------------------------------------------------------

# 1. Rename the columns for all datasets:

characteristics = characteristics.rename(columns={
    'Num_Acc': 'accident_id',
    'jour': 'accident_day',
    'mois': 'accident_month',
    'an': 'accident_year',
    'hrmn': 'accident_time',
    'lum': 'lighting_conditions',
    'dep': 'department_id',
    'com': 'municipality_id',
    'agg': 'location',
    'int': 'intersection',
    'atm': 'atmospheric_conditions',
    'col': 'collision_type',
    'adr': 'address',
    'lat': 'latitude',
    'long': 'longitude'
})

locations = locations.rename(columns={
    'Num_Acc': 'accident_id',
    'catr': 'road_category',
    'voie': 'road_number',
    'v1': 'road_number_index',
    'v2': 'road_alphanumeric_index',
    'circ': 'traffic_regime',
    'nbv': 'number_of_traffic_lanes',
    'vosp': 'reserved_lane_type',
    'prof': 'road_profile',
    'pr': 'upstream_terminal_number',
    'pr1': 'distance_to_upstream_terminal',
    'plan': 'plan_layout',
    'lartpc': 'central_reservation_width',
    'larrout': 'carriageway_width',
    'surf': 'surface_condition',
    'infra': 'infrastructure',
    'situ': 'accident_location',
    'vma': 'max_speed_permitted'
})

vehicles = vehicles.rename(columns={
    'Num_Acc': 'accident_id',
    'id_vehicle': 'vehicle_id',
    'Num_Veh': 'vehicle_code',
    'senc': 'travel_direction',
    'catv': 'vehicle_category',
    'obs': 'fixed_obstacle_struck',
    'obsm': 'mobile_obstacle_struck',
    'choc': 'initial_impact_point',
    'manv': 'main_manoeuvre_before_the_accident',
    'motor': 'vehicle_engine_type',
    'occutc': 'occupants_in_public_transport'
})

users = users.rename(columns={
    'Num_Acc': 'accident_id',
    'id_usager': 'user_id',
    'id_vehicle': 'vehicle_id',
    'num_veh': 'vehicle_code',
    'place': 'seat_place',
    'catu': 'user_category',
    'grav': 'injury_severity',
    'sexe': 'gender',
    'An_nais': 'birth_year_user',
    'trajet': 'travel_reason',
    'secu1': 'safety_equipment1',
    'secu2': 'safety_equipment2',
    'secu3': 'safety_equipment3',
    'locp': 'pedestrian_location',
    'actp': 'pedestrian_action',
    'etatp': 'pedestrian_presence'
})

# Drop "year" column from all datasets

characteristics = characteristics.drop(columns=['year'])
locations = locations.drop(columns=['year'])
vehicles = vehicles.drop(columns=['year'])
users = users.drop(columns=['year'])

# Check the column names:

print("Characteristics columns:", characteristics.columns.tolist())
print("Locations columns:", locations.columns.tolist())
print("Vehicles columns:", vehicles.columns.tolist())
print("Users columns:", users.columns.tolist())

# 2. Update Data Format and Replace Numeric Codes with Labels

# 2.1 Update "Characteristics" Dataframe

# Mapping dictionary
lighting_map = {
    '1': 'Broad daylight',
    '2': 'Dusk or dawn',
    '3': 'Night without street lighting',
    '4': 'Night with street lighting off',
    '5': 'Night with street lighting on'
}

# Ensure the column is treated as string before mapping (in case it's read as int/float)
characteristics['lighting_conditions'] = (
    characteristics['lighting_conditions']
    .astype(str)
    .str.strip()          # remove any stray whitespace
    .str.split('.').str[0]  # handles cases where it was read as float, e.g. '1.0' -> '1'
    .map(lighting_map)
    .fillna('Unknown')
    .astype('category')
)

location_map = {
    '1': 'Outside urban areas',
    '2': 'Within built-up areas'
}

characteristics['location'] = (
    characteristics['location']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(location_map)
    .fillna('Unknown')
    .astype('category')
)

intersection_map = {
    '1': 'Outside intersection',
    '2': 'X-shaped intersection',
    '3': 'T-junction',
    '4': 'Y-junction',
    '5': 'Intersection with more than 4 branches',
    '6': 'Roundabout',
    '7': 'Square',
    '8': 'Level crossing',
    '9': 'Other intersection'
}

characteristics['intersection'] = (
    characteristics['intersection']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(intersection_map)
    .fillna('Unknown')
    .astype('category')
)

atmospheric_conditions_map = {
    '-1': 'Not specified',
    '1': 'Normal',
    '2': 'Light rain',
    '3': 'Heavy rain',
    '4': 'Snow - hail',
    '5': 'Fog - Smoke',
    '6': 'Strong wind - storm',
    '7': 'Glare',
    '8': 'Overcast weather',
    '9': 'Other'
}

characteristics['atmospheric_conditions'] = (
    characteristics['atmospheric_conditions']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(atmospheric_conditions_map)
    .fillna('Unknown')
    .astype('category')
)

collision_type_map = {
    '-1': 'Not specified',
    '1': 'Two vehicles - head-on',
    '2': 'Two vehicles - rear-end',
    '3': 'Two vehicles - side',
    '4': 'Three or more vehicles - chain collision',
    '5': 'Three or more vehicles - multiple collisions',
    '6': 'Other collision',
    '7': 'No collision'
}

characteristics['collision_type'] = (
    characteristics['collision_type']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(collision_type_map)
    .fillna('Unknown')
    .astype('category')
)

# 2.2 Update "Locations" Dataframe

road_category_map = {
    '1': 'Motorway',
    '2': 'National road',
    '3': 'Departmental road',
    '4': 'Municipal roads',
    '5': 'Off public network',
    '6': 'Car parks open to public traffic',
    '7': 'Urban metropolitan roads',
    '9': 'Other'
}

locations['road_category'] = (
    locations['road_category']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(road_category_map)
    .fillna('Unknown')
    .astype('category')
)

traffic_regime_map = {
    '-1': 'Not specified',
    '1': 'One-way',
    '2': 'Two-way',
    '3': 'Separate carriageways',
    '4': 'With variable lanes'
}

locations['traffic_regime'] = (
    locations['traffic_regime']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(traffic_regime_map)
    .fillna('Unknown')
    .astype('category')
)

reserved_lane_type_map = {
    '-1': 'Not specified',
    '0': 'Not applicable',
    '1': 'Cycle path',
    '2': 'Cycle lane',
    '3': 'Reserved lane'
}

locations['reserved_lane_type'] = (
    locations['reserved_lane_type']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(reserved_lane_type_map)
    .fillna('Unknown')
    .astype('category')
)

road_profile_map = {
    '-1': 'Not specified',
    '1': 'Flat',
    '2': 'Slope',
    '3': 'Top of hill',
    '4': 'Bottom of hill'
}

locations['road_profile'] = (
    locations['road_profile']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(road_profile_map)
    .fillna('Unknown')
    .astype('category')
)

plan_layout_map = {
    '-1': 'Not specified',
    '1': 'Straight section',
    '2': 'Left-hand curve',
    '3': 'Curve to the right',
    '4': 'S-shaped'
}

locations['plan_layout'] = (
    locations['plan_layout']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(plan_layout_map)
    .fillna('Unknown')
    .astype('category')
)

surface_condition_map = {
    '-1': 'Not specified',
    '1': 'Normal',
    '2': 'Wet',
    '3': 'Puddles',
    '4': 'Flooded',
    '5': 'Snowy',
    '6': 'Muddy',
    '7': 'Icy',
    '8': 'Fats - oil',
    '9': 'Other'
}

locations['surface_condition'] = (
    locations['surface_condition']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(surface_condition_map)
    .fillna('Unknown')
    .astype('category')
)

infrastructure_map = {
    '-1': 'Not specified',
    '0': 'None',
    '1': 'Underground - tunnel',
    '2': 'Bridge - flyover',
    '3': 'Interchange or junction slip road',
    '4': 'Railway line',
    '5': 'Improved crossroads',
    '6': 'Pedestrian zone',
    '7': 'Toll area',
    '8': 'Construction site',
    '9': 'Other'
}

locations['infrastructure'] = (
    locations['infrastructure']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(infrastructure_map)
    .fillna('Unknown')
    .astype('category')
)

accident_location_map = {
    '-1': 'Not specified',
    '0': 'None',
    '1': 'On the road',
    '2': 'On emergency lane',
    '3': 'On the shoulder',
    '4': 'On pavement',
    '5': 'On cycle path',
    '6': 'On other special lanes',
    '8': 'Other'
}

locations['accident_location'] = (
    locations['accident_location']
    .astype(str)
    .str.strip()
    .str.split('.').str[0]
    .map(accident_location_map)
    .fillna('Unknown')
    .astype('category')
)



# Checking the updated columns

print(characteristics['lighting_conditions'].value_counts(dropna=False))
print(characteristics['location'].value_counts(dropna=False))
print(characteristics['intersection'].value_counts(dropna=False))
print(characteristics['atmospheric_conditions'].value_counts(dropna=False))
print(characteristics['collision_type'].value_counts(dropna=False))
print(locations['road_category'].value_counts(dropna=False))
print(locations['traffic_regime'].value_counts(dropna=False))
print(locations['reserved_lane_type'].value_counts(dropna=False))
print(locations['road_profile'].value_counts(dropna=False))
print(locations['plan_layout'].value_counts(dropna=False))
print(locations['surface_condition'].value_counts(dropna=False))
print(locations['infrastructure'].value_counts(dropna=False))
print(locations['accident_location'].value_counts(dropna=False))




pd.set_option('display.max_columns', None)
pd.set_option('display.width', 0)      # 0 tells pandas to detect terminal width, but often works better than None for wrapping issues
pd.set_option('display.expand_frame_repr', False)  # this is the key one — stops line wrapping entirely

print("=== characteristics ===")
print(characteristics.head(5))

print("\n=== locations ===")
print(locations.head(5))