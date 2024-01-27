from sqlalchemy import create_engine, text
import os
db_connection_string = os.environ['DB_CONNNECTION_STRING']

engine = create_engine(db_connection_string, connect_args={
    "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"
    }
})

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = [dict(row._asdict()) for row in result]
  return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("select * from jobs where id = :id"),{"id": id}
    )
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0]._asdict())