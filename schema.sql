DROP TABLE if exists LogTable;
CREATE TABLE LogTable (
  id SERIAL PRIMARY KEY,
  Date_Entry TIMESTAMP NOT NULL,
  Time_Entry TIMESTAMP NOT NULL,
  Job VARCHAR,
  Description VARCHAR,
  Outcome VARCHAR,
  Comments VARCHAR,
  Date_Stamp TIMESTAMP,
  Time_Stamp TIMESTAMP
);