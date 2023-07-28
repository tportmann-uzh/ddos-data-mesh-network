CREATE SCHEMA domain_team_1_ddos_data;

USE domain_team_1_ddos_data;

CREATE TABLE Fingerprint ( 
  fingerprint_id VARCHAR(255) PRIMARY KEY NOT NULL, 
  target VARCHAR(255),
  location VARCHAR(155) 
  domain_team INT DEFAULT 1
);

CREATE TABLE AttackVector (
  attack_vector_id VARCHAR(255) PRIMARY KEY NOT NULL,
  fingerprint_id VARCHAR(255),
  service VARCHAR(255),
  protocol VARCHAR(255),
  time_start VARCHAR(255),
  duration_seconds FLOAT,
  nr_packets INT,
  nr_megabytes FLOAT,
  detection_threshold FLOAT,
  FOREIGN KEY (fingerprint_id) REFERENCES Fingerprint(fingerprint_id)
);

CREATE TABLE SourceIP (
  source_ip_id VARCHAR(255) PRIMARY KEY NOT NULL,
  attack_vector_id VARCHAR(255),
  source_ip VARCHAR(255),
  nr_packets INT,
  FOREIGN KEY (attack_vector_id) REFERENCES AttackVector(attack_vector_id)
);

CREATE TABLE TTL (
  ttl_id VARCHAR(255) PRIMARY KEY,
  attack_vector_id VARCHAR(255),
  ttl_value INT,
  source_ip VARCHAR(255),
  FOREIGN KEY (attack_vector_id) REFERENCES AttackVector(attack_vector_id)
);

CREATE USER 'username'@'remote_server_ip' IDENTIFIED BY 'password';

GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'username'@'remote_server_ip' WITH GRANT OPTION;

FLUSH PRIVILEGES;
