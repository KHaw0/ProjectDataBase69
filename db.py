# ============================================================
#  db.py — ชั้นติดต่อฐานข้อมูล  ★★★ นิสิตเขียน SQL ในไฟล์นี้ ★★★
#  มองหาคำว่า  # TODO  ทุกฟังก์ชัน — ใช้ %s เป็น placeholder เสมอ (กัน SQL injection)
# ============================================================
import mysql.connector
import config

def get_connection():
    return mysql.connector.connect(
        host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASSWORD,
        database=config.DB_NAME, port=config.DB_PORT)


def run_query(sql, params=None):
    """รัน SELECT คืนผลเป็น list ของ dict"""
    conn = get_connection(); cur = conn.cursor(dictionary=True)
    cur.execute(sql, params or ()); rows = cur.fetchall()
    cur.close(); conn.close(); return rows


def run_command(sql, params=None):
    """รัน INSERT / UPDATE / DELETE แล้ว commit"""
    conn = get_connection(); cur = conn.cursor()
    cur.execute(sql, params or ()); conn.commit()
    out = {"new_id": cur.lastrowid, "affected": cur.rowcount}
    cur.close(); conn.close(); return out


def _todo(name):
    raise NotImplementedError(f"TODO: ยังไม่ได้เขียนฟังก์ชัน {name} ใน db.py")


# ---------- สมาชิก (member) ----------
# def search_members(filters):
#     """ค้นหา สมาชิก ตามเงื่อนไข (name, gender, package_type)
#     คำใบ้: เริ่มจาก sql = "SELECT * FROM member WHERE 1=1"
#     แล้วต่อเงื่อนไขเฉพาะ filter ที่มีค่า (ข้อความใช้ LIKE %s, อื่น ๆ ใช้ = %s)"""
#     # TODO: เขียน SQL ค้นหาแบบยืดหยุ่นตาม filters (ใช้ %s เสมอ)
#     _todo("search_members")

def search_members(filters):
    sql = "SELECT * FROM member WHERE 1=1"
    params= [] 
    if filters.get("name"):
        sql += " AND name LIKE %s"
        params.append("%" + filters["name"] + "%")
    if filters.get("gender"):
        sql += " AND gender = %s"
        params.append(filters["gender"])
    if filters.get("package_type"):
        sql += " AND package_type = %s"
        params.append(filters["package_type"])
    sql += " ORDER BY member_id"
    return run_query(sql, params)

# def get_member(member_id):
#     """ดึง สมาชิก 1 รายการตาม member_id (ใช้ตอนเปิดฟอร์มแก้ไข)"""
#     # TODO: SELECT * FROM member WHERE member_id = %s แล้วคืนแถวเดียว
#     _todo("get_member")

def get_member(member_id):
    rows = run_query("SELECT * FROM member WHERE member_id = %s", (member_id,))
    return rows[0] if rows else None

def create_member(data):
    """เพิ่ม สมาชิก ใหม่ — data มีคีย์: name, gender, join_date, package_type"""
    # TODO: INSERT INTO member (...) VALUES (%s, ...)
    _todo("create_member")


def update_member(member_id, data):
    """แก้ไข สมาชิก ตาม member_id"""
    # TODO: UPDATE member SET ... WHERE member_id=%s
    _todo("update_member")


def delete_member(member_id):
    """ลบ สมาชิก ตาม member_id"""
    # TODO: DELETE FROM member WHERE member_id=%s
    _todo("delete_member")

# ---------- คลาสเรียน (gym_class) ----------
def search_classes(filters):
    """ค้นหา คลาสเรียน ตามเงื่อนไข (name, room)
    คำใบ้: เริ่มจาก sql = "SELECT * FROM gym_class WHERE 1=1"
    แล้วต่อเงื่อนไขเฉพาะ filter ที่มีค่า (ข้อความใช้ LIKE %s, อื่น ๆ ใช้ = %s)"""
    # TODO: เขียน SQL ค้นหาแบบยืดหยุ่นตาม filters (ใช้ %s เสมอ)
    _todo("search_classes")


def get_class(class_id):
    """ดึง คลาสเรียน 1 รายการตาม class_id (ใช้ตอนเปิดฟอร์มแก้ไข)"""
    # TODO: SELECT * FROM gym_class WHERE class_id = %s แล้วคืนแถวเดียว
    _todo("get_class")


def create_class(data):
    """เพิ่ม คลาสเรียน ใหม่ — data มีคีย์: name, trainer_id, room, capacity, schedule_time"""
    # TODO: INSERT INTO gym_class (...) VALUES (%s, ...)
    _todo("create_class")


def update_class(class_id, data):
    """แก้ไข คลาสเรียน ตาม class_id"""
    # TODO: UPDATE gym_class SET ... WHERE class_id=%s
    _todo("update_class")


def delete_class(class_id):
    """ลบ คลาสเรียน ตาม class_id"""
    # TODO: DELETE FROM gym_class WHERE class_id=%s
    _todo("delete_class")

# ---------- การจอง (booking) ----------
def search_bookings(filters):
    """ค้นหา การจอง ตามเงื่อนไข (member_id, class_id, status)
    คำใบ้: เริ่มจาก sql = "SELECT * FROM booking WHERE 1=1"
    แล้วต่อเงื่อนไขเฉพาะ filter ที่มีค่า (ข้อความใช้ LIKE %s, อื่น ๆ ใช้ = %s)"""
    # TODO: เขียน SQL ค้นหาแบบยืดหยุ่นตาม filters (ใช้ %s เสมอ)
    _todo("search_bookings")


def get_booking(booking_id):
    """ดึง การจอง 1 รายการตาม booking_id (ใช้ตอนเปิดฟอร์มแก้ไข)"""
    # TODO: SELECT * FROM booking WHERE booking_id = %s แล้วคืนแถวเดียว
    _todo("get_booking")


def create_booking(data):
    """เพิ่ม การจอง ใหม่ — data มีคีย์: member_id, class_id, book_date, status"""
    # TODO: INSERT INTO booking (...) VALUES (%s, ...)
    _todo("create_booking")


def update_booking(booking_id, data):
    """แก้ไข การจอง ตาม booking_id"""
    # TODO: UPDATE booking SET ... WHERE booking_id=%s
    _todo("update_booking")


def delete_booking(booking_id):
    """ลบ การจอง ตาม booking_id"""
    # TODO: DELETE FROM booking WHERE booking_id=%s
    _todo("delete_booking")


# ============================================================
#  REPORT (รายงาน — ใช้ JOIN + GROUP BY + subquery)
# ============================================================
def report_summary():
    """ตัวเลขสรุปบนการ์ด dashboard — คืน dict เช่น {"members": 10, ...}
    คำใบ้: ใช้ COUNT(*) หลายครั้ง"""
    # TODO: นับจำนวนรวมต่าง ๆ เพื่อแสดงบนการ์ด
    _todo("report_summary")

def report_popular_classes():
    """📈 คลาสยอดนิยม (Most Booked)
    คำใบ้: JOIN booking→gym_class, GROUP BY class, COUNT, ORDER BY DESC, LIMIT 5"""
    # TODO: เขียน SQL รายงานนี้ (เขียน JOIN แบบ explicit INNER JOIN ... ON ...)
    _todo("report_popular_classes")

def report_trainers_above_avg():
    """🏅 เทรนเนอร์ที่มีผู้จองมากกว่าค่าเฉลี่ย (Above Average)
    คำใบ้: JOIN booking→gym_class→trainer, GROUP BY trainer, HAVING COUNT(*) > (subquery AVG)"""
    # TODO: เขียน SQL รายงานนี้ (เขียน JOIN แบบ explicit INNER JOIN ... ON ...)
    _todo("report_trainers_above_avg")

def report_class_equipment():
    """🧰 อุปกรณ์ที่ใช้ในแต่ละคลาส (Join 3 Tables)
    คำใบ้: JOIN class_equipment→gym_class, class_equipment→equipment"""
    # TODO: เขียน SQL รายงานนี้ (เขียน JOIN แบบ explicit INNER JOIN ... ON ...)
    _todo("report_class_equipment")
