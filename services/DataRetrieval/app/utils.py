import bson
import datetime


def convert_bson_types(obj):

    """Recursively convert BSON-specific types to JSON-friendly values."""
    if isinstance(obj, dict):
        return {k: convert_bson_types(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [convert_bson_types(i) for i in obj]
    if isinstance(obj, (bson.objectid.ObjectId, datetime.datetime)):
        return str(obj)

    return obj
