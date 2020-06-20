nessus_data_endpoint = "https://vulners.com/api/v3/archive/collection/?type=nessus%27"

nessus_data_config = {
    "api_key": "ITLVLMN4GPADKBLTK3CKG7Y62TX3E62I8FAMDL2MLV2T357QFHC8VOVME0I522FP"
}

db_config = dict(
    endpoint="localhost:9200",
    index="nessus",
    type="nessus"
)
