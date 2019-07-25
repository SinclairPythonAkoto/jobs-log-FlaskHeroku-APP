DROP TABLE if exists LogTable;
CREATE TABLE LogTable (
  id SERIAL PRIMARY KEY,
  Date_Entry TIMESTAMP,
  Time_Entry TIMESTAMP,
  Job VARCHAR,
  Description VARCHAR,
  Outcome VARCHAR,
  Comments VARCHAR,
  Date_Stamp TIMESTAMP,
  Time_Stamp TIMESTAMP
);