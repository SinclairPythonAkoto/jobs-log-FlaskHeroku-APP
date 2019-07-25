DROP TABLE if exists country;
CREATE TABLE country (
  id SERIAL PRIMARY KEY,
  Date TIMESTAMP NOT NULL,
  Time TIMESTAMP NOT NULL,
  Job VARCHAR,
  Description VARCHAR,
  Outcome VARCHAR,
  Comments VARCHAR,
  Date_Entry TIMESTAMP,
  Time_Entry TIMESTAMP
);