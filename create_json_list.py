import json

json_documents = [
    {
        "_id": 12345,
        "originationTime": 1656788800,
        "clusterId": "domainserver1",
        "userId": "1" * 9,
        "devices": {
            "phone": "SEP123123234234",
            "voicemail": "555666777VM"
        }
    },
    {
        "_id": 12346,
        "originationTime": 1656875200,
        "clusterId": "domainserver2",
        "userId": "2" * 9,
        "devices": {
            "phone": "SEP987987654321",
            "voicemail": "555666778VM"
        }
    },
    {
        "_id": 12347,
        "originationTime": 1657048000,
        "clusterId": "domainserver3",
        "userId": "3" * 9,
        "devices": {
            "phone": "SEP567567567890",
            "voicemail": "555666779VM"
        }
    },
    {
        "_id": 12348,
        "originationTime": 1657134400,
        "clusterId": "domainserver4",
        "userId": "4" * 9,
        "devices": {
            "phone": "SEP456456456123",
            "voicemail": "555666780VM"
        }
    },
    {
        "_id": 12349,
        "originationTime": 1657220800,
        "clusterId": "domainserver5",
        "userId": "5" * 9,
        "devices": {
            "phone": "SEP345345345234",
            "voicemail": "555666781VM"
        }
    },
    {
        "_id": 12350,
        "originationTime": 1657307200,
        "clusterId": "domainserver6",
        "userId": "6" * 9,
        "devices": {
            "phone": "SEP234234234345",
            "voicemail": "555666782VM"
        }
    },
    {
        "_id": 12351,
        "originationTime": 1691521600,
        "clusterId": "domainserver7",
        "userId": "7" * 9,
        "devices": {
            "phone": "SEP123123123456",
            "voicemail": "555666783VM"
        }
    },
    {
        "_id": 12352,
        "originationTime": 1723144000,
        "clusterId": "domainserver8",
        "userId": "8" * 9,
        "devices": {
            "phone": "SEP678678678901",
            "voicemail": "555666783VM"
        }
    },
]

file_path = 'json_list.json'

with open(file_path, 'w') as f:
    json.dump(json_documents, f, indent=4)

