from fastapi import FastAPI, Depends
import logging
from starlette.middleware.cors import CORSMiddleware
from Model import QueryParam, RecordModel
from common import load_json_records_from_file, is_within_date_range
from sqlmodel import Session, select
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

records = load_json_records_from_file('json_list.json')


# @app.get("/records/file/", dependencies=[Depends(oauth2_scheme)])
@app.get("/records/file/")
def get_records_file(params: QueryParam = Depends()):
    logger.info(f"Retrieving records from json file with params: {params}")

    res = []
    for record in records:
        if (is_within_date_range(record, params.start_date, params.end_date) and
                (not params.phone or record["devices"].get("phone") == params.phone) and
                (not params.voicemail or record["devices"].get("voicemail") == params.voicemail) and
                (not params.user_id or record["userId"] == params.user_id) and
                (not params.cluster_id or record["clusterId"] == params.cluster_id)
        ):
            dic = record.copy()
            dic['phone'] = record["devices"].get("phone")
            dic['voicemail'] = record["devices"].get("voicemail")
            del dic['devices']
            res.append(dic)
    return {"results": res}


@app.get("/records/mongodb")
def get_records_mongodb(params: QueryParam):
    query = {
        "originationTime": {"$gte": params.start_date.timestamp(), "$lte": params.end_date.timestamp()}
    }

    if params.phone:
        query["devices.phone"] = params.phone
    if params.voicemail:
        query["devices.voicemail"] = params.voicemail
    if params.user_id:
        query["userId"] = params.user_id
    if params.cluster_id:
        query["clusterId"] = params.cluster_id

    results = list(collection.find(query))
    return {"results": list(results)}


@app.get("/records/mssql")
def get_records_mongodb(params: QueryParam):
    with Session(engine) as session:
        statement = select(RecordModel).where(RecordModel.originationTime >= params.start_date,
                                              RecordModel.originationTime <= params.end_date)
        if params.phone:
            statement = statement.where(RecordModel.phone == params.phone)
        if params.voicemail:
            statement = statement.where(RecordModel.voicemail == params.voicemail)
        if params.user_id:
            statement = statement.where(RecordModel.user_id == params.user_id)
        if params.cluster_id:
            statement = statement.where(RecordModel.cluster_id == params.cluster_id)

        results = session.exec(statement)
        return {"results": list(results)}
