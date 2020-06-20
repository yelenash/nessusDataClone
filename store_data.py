from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from config import db_config


def store_data(data):
    if data is None or data == []:
        return
    es = Elasticsearch()
    mapping = '''
    {  
      "mappings":{  
          "properties":{  
            "pluginID":{  
              "type":"keyword"
            }
          }
        }
      }
    }'''
    es.indices.create(index=db_config["index"], ignore=400, body=mapping)

    data = [parse_fields(entry) for entry in data]
    bulk(es, data)


def parse_fields(entry):
    entry = parse_metadata_fields(entry)
    # optional TODO: parse only API required fields
    return entry


def parse_metadata_fields(entry):
    entry["_source"]["original_id"] = entry["id"]
    del entry["id"]
    del entry["index"]
    entry["_index"] = db_config["index"]
    return entry
