from fastapi import FastAPI
import psycopg2

app = FastAPI()

def get_connection():
    return psycopg2.connect(
        dbname="hospital_analytics",
        user="postgres",
        password="Chaithu@3110",
        host="127.0.0.1",
        port="5432"
    )

@app.get("/")
def root():
    return {"message": "Hospital Analytics API is running"}

@app.get("/kpi/alos")
def get_alos():
    try:
        conn = get_connection()
        cur = conn.cursor()

        query = """
        SELECT AVG(EXTRACT(EPOCH FROM (discharge_time - admission_time)) / 86400)
        FROM admissions
        WHERE discharge_time IS NOT NULL;
        """
        cur.execute(query)

        result = cur.fetchone()
        alos = result[0] if result and result[0] is not None else 0

        cur.close()
        conn.close()

        return {
            "average_length_of_stay_days": round(alos, 2)
        }

    except Exception as e:
        print("🔥 ERROR:", e)
        return {"error": str(e)}

@app.get("/kpi/total-admissions")
def total_admissions():
    try:
        conn = get_connection()
        cur = conn.cursor()

        query = "SELECT COUNT(*) FROM admissions;"
        cur.execute(query)

        total = cur.fetchone()[0]

        cur.close()
        conn.close()

        return {
            "total_admissions": total
        }

    except Exception as e:
        print("ERROR:", e)
        return {"error": str(e)}

@app.get("/kpi/admission-type")
def admission_type():
    try:
        conn = get_connection()
        cur = conn.cursor()

        query = """
        SELECT admission_type, COUNT(*)
        FROM admissions
        GROUP BY admission_type;
        """
        cur.execute(query)

        rows = cur.fetchall()

        cur.close()
        conn.close()

        result = {row[0]: row[1] for row in rows}

        return result

    except Exception as e:
        print("🔥 ERROR:", e)
        return {"error": str(e)}

@app.get("/kpi/admissions-by-department")
def admissions_by_department():
    try:
        conn = get_connection()
        cur = conn.cursor()

        query = """
        SELECT department, COUNT(*)
        FROM admissions
        GROUP BY department;
        """
        cur.execute(query)

        rows = cur.fetchall()

        cur.close()
        conn.close()

        result = {row[0]: row[1] for row in rows}

        return result

    except Exception as e:
        print("🔥 ERROR:", e)
        return {"error": str(e)}