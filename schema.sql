DROP TABLE if exists LogTable;
CREATE TABLE LogTable (
  id SERIAL PRIMARY KEY,
  Date_Entry VARCHAR,
  Time_Entry VARCHAR,
  Job VARCHAR,
  Description VARCHAR,
  Outcome VARCHAR,
  Comments VARCHAR,
  Date_Time_Stamp TIMESTAMP
  );