import os
import json
import uuid
import mysql.connector


def feed():

    path_to_json_files = "./fingerprints"
    json_file_names = [
        filename
        for filename in os.listdir(path_to_json_files)
        if filename.endswith(".json")
    ]

    mydb = mysql.connector.connect(
        host="",
        user="",
        password="",
        database="domain_team_1_ddos_data;",
    )

    mycursor = mydb.cursor()

    for json_file_name in json_file_names:
        with open(os.path.join(path_to_json_files, json_file_name)) as json_file:
            json_text = json.load(json_file)

            fingerprint_id = json_text["key"]
            target = json_text["target"]
            location = json_text["location"]

            # here the write to table Fingerprint:
            sql = "INSERT INTO Fingerprints (fingerprint_id, target, location) VALUES (%s, %s, %s)"
            val = (fingerprint_id, target, location)
            mycursor.execute(sql, val)

            for v in json_text["attack_vectors"]:
                attack_vector_id = uuid.uuid4()
                # fingerprint_id from above...
                service = v["service"]
                protocol = v["protocol"]
                time_start = v["time_start"]
                duration_seconds = v["duration_seconds"]
                nr_packets = v["nr_packets"]
                nr_megabytes = v["nr_megabytes"]
                detection_thershold = v["detection_threshold"]

                # here the write to tabel AttackVector:
                sql = "INSERT INTO AttackVector (attack_vector_id, fingerprint_id, service, protocol, time_start, duration_seconds, nr_packets, nr_megabytes, detection_thershold) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (
                    attack_vector_id,
                    fingerprint_id,
                    service,
                    protocol,
                    time_start,
                    duration_seconds,
                    nr_packets,
                    nr_megabytes,
                    detection_thershold,
                )
                mycursor.execute(sql, val)

                for ip in v["source_ips"]:
                    source_ip_id = uuid.uuid4()
                    # attack_vector_id from above...
                    source_ip = ip
                    nr_packets = v["nr_packets_by_source"][ip]

                    # here the write to table SourceIP
                    sql = "INSERT INTO SourceIP (source_ip_id, attack_vector_id, source_ip, nr_packets) VALUES (%s, %s, %s, %s)"
                    val = (source_ip_id, attack_vector_id, source_ip, nr_packets)
                    mycursor.execute(sql, val)

                for ip, ttls in v["ttl_by_source"].items():
                    for ttl in ttls:
                        ttl_id = uuid.uuid4()
                        # attack_vector_id form above...
                        ttl_value = ttl
                        source_ip = ip

                        # here the write to table TTL
                        sql = "INSERT INTO TTL (ttl_id, attack_vector_id, ttl_value, source_ip) VALUES (%s, %s, %s, %s)"
                        val = (ttl_id, attack_vector_id, ttl_value, source_ip)
                        mycursor.execute(sql, val)


if __name__ == "__main__":
    feed()
