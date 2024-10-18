from datetime import datetime
from enum import Enum
import logging, json


class SourceName(str, Enum):
    mongodb = "mongodb"
    file = "file"
    sql = "sql"


logger = logging.getLogger(__name__)  # todo


def load_json_records_from_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"File {file_path} not found.")
        return []


def is_within_date_range(record, start_date: datetime, end_date: datetime):
    return start_date.timestamp() <= record["originationTime"] <= end_date.timestamp()


def get_curl_string(start_date, end_date, phone=None, voicemail=None, user_id=None, cluster_id=None):
    builder = [f"http://127.0.0.1:8000/records/file/?start_date={start_date}&end_date={end_date}&api_key=test_api_key"]
    if phone:
        builder.append(f"phone={phone}")
    if voicemail:
        builder.append(f"voicemail={voicemail}")
    if user_id:
        builder.append(f"user_id={user_id}")
    if cluster_id:
        builder.append(f"cluster_id={cluster_id}")
    "Authorization: Bearer your_bearer_token_here"
    return f"curl -H \"Authorization: Bearer token\" \"{'&'.join(builder)}\""

# records/?start_date=2022-07-01T00:00:00&end_date=2022-07-03T23:59:59&phone=SEP123123234234&api_key=test_api_key
# print(get_curl_string("2022-07-01", "2022-07-03", phone='SEP123123234234', voicemail='555666777VM'))
# print(get_curl_string("2024-07-01", "2024-09-03", phone='SEP678678678901'))
# print(datetime.fromtimestamp(1723144000))
# dt = datetime(2024,8,8,15,6,40)
# print(dt)
# print(dt.timestamp())
