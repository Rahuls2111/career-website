from sqlalchemy import create_engine,text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']
#engine = create_engine('mysql+pymysql://admin:Rahulsrivastava@database-2.ctoqmcgqcl0b.ap-south-1.rds.amazonaws.com/gladiator', echo=True)

engine = create_engine(db_connection_string, echo=True)

def load_jobs_from_db():
  with engine.connect() as conn:
      result = conn.execute(text("select * from jobs limit 10"))
      jobs = []
      for row in result.all():
          jobs.append(dict(row._mapping))
     # print(jobs)
      return jobs
# with engine.connect() as conn:
#     result = conn.execute(text("select * from jobs limit 10"))
#     result_dict = []
#     for row in result.all():
#         result_dict.append(dict(row._mapping))
#     print(result_dict)
    # conn.execute(text("CREATE TABLE test (x int, y int)"))
    # conn.execute