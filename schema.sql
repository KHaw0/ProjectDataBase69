DROP TABLE IF EXISTS class_equipment;
DROP TABLE IF EXISTS booking;
DROP TABLE IF EXISTS gym_class;
DROP TABLE IF EXISTS equipment;
DROP TABLE IF EXISTS trainer;
DROP TABLE IF EXISTS member;

SHOW TABLES

-- ============================================================
--  schema.sql — ระบบฟิตเนส (นิสิตออกแบบและเขียนเอง)
--  กติกา: การจอง = M:N (member × gym_class), อุปกรณ์ต่อคลาส = M:N (gym_class × equipment),
--         แต่ละคลาสมีเทรนเนอร์ (1:M จาก trainer)
-- ============================================================
CREATE TABLE member (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    gender CHAR(1) NOT NULL CHECK (gender IN ('M', 'F', 'O')),
    join_date DATE NOT NULL,
    package_type VARCHAR(50) NOT NULL
    -- TODO: name, gender, join_date, package_type
);
CREATE TABLE trainer (
    trainer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    specialty VARCHAR(100) NOT NULL,
    phone VARCHAR(15)
    -- TODO: name, specialty, phone
);
CREATE TABLE gym_class (          -- 1:M จาก trainer
    class_id INT AUTO_INCREMENT PRIMARY KEY,
    trainer_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    room VARCHAR(50) NOT NULL,
    capacity INT NOT NULL,
    schedule_time DATETIME NOT NULL,

    FOREIGN KEY (trainer_id) REFERENCES trainer (trainer_id)
    -- TODO: trainer_id (FK), name, room, capacity, schedule_time
);
CREATE TABLE booking (            -- M:N: member × gym_class
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    class_id INT NOT NULL,
    book_date DATE NOT NULL,
    status VARCHAR(15) NOT NULL DEFAULT 'pending',

    FOREIGN KEY (member_id) REFERENCES member (member_id),
    FOREIGN KEY (class_id) REFERENCES gym_class (class_id),
    CHECK (status IN ('confirmed', 'cancelled','pending'))
    -- TODO: member_id (FK), class_id (FK), book_date, status
);
CREATE TABLE equipment (
    equip_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    zone VARCHAR(10) NOT NULL,
    status VARCHAR(30) DEFAULT 'available',

    CHECK (status IN ('available','in_use','maintenance'))
    -- TODO: name, zone, status
);
CREATE TABLE class_equipment (    -- M:N: gym_class × equipment
    -- TODO: class_id (FK), equip_id (FK), quantity ; PRIMARY KEY (class_id, equip_id)
    class_id INT,
    equip_id INT,
    quantity INT NOT NULL DEFAULT 1,

    FOREIGN KEY (class_id) REFERENCES gym_class(class_id),
    FOREIGN KEY (equip_id) REFERENCES equipment(equip_id),
    PRIMARY KEY (class_id, equip_id)
);
-- TODO: INSERT ข้อมูลตัวอย่างทุกตาราง
-- ============================================================
-- 1. INSERT ข้อมูลสมาชิก (member)
-- ============================================================
INSERT INTO member (name, gender, join_date, package_type) VALUES
('สมชาย สายฟิต', 'M', '2024-01-10', 'Yearly'),
('สมหญิง รักสุขภาพ', 'F', '2024-02-15', 'Monthly'),
('กิตติศักดิ์ พลังกล้าม', 'M', '2024-03-01', 'Monthly'),
('วิภาดา โยคะเพลิน', 'F', '2024-03-12', 'Daily'),
('อนันต์ มุ่งมั่น', 'M', '2024-04-05', 'Yearly');

-- ============================================================
-- 2. INSERT ข้อมูลเทรนเนอร์ (trainer)
-- ============================================================
INSERT INTO trainer (name, specialty, phone) VALUES
('โค้ชเอก', 'Weight Training & Bodybuilding', '081-111-2222'),
('ครูแนน', 'Yoga & Pilates', '082-333-4444'),
('โค้ชเบิร์ด', 'HIIT & Boxing', '083-555-6666');

-- ============================================================
-- 3. INSERT ข้อมูลคลาส (gym_class)
-- * อ้างอิง trainer_id 1, 2, 3
-- ============================================================
INSERT INTO gym_class (trainer_id, name, room, capacity, schedule_time) VALUES
(2, 'Morning Flow Yoga', 'Studio A', 15, '2024-06-01 08:00:00'),
(1, 'Power Body Pump', 'Main Gym', 20, '2024-06-01 10:30:00'),
(3, 'Burn Fat HIIT', 'Studio B', 12, '2024-06-01 17:00:00'),
(2, 'Evening Gentle Yoga', 'Studio A', 15, '2024-06-02 18:00:00');

-- ============================================================
-- 4. INSERT ข้อมูลอุปกรณ์ (equipment)
-- ============================================================
INSERT INTO equipment (name, zone, status) VALUES
('Yoga Mat', 'Zone A', 'available'),
('Dumbbell Set (10kg)', 'Zone B', 'available'),
('Kettlebell (16kg)', 'Zone B', 'available'),
('Resistance Band', 'Zone A', 'available'),
('Punching Bag & Gloves', 'Zone C', 'available');

-- ============================================================
-- 5. INSERT การจองคลาสของสมาชิก (booking) - M:N (member × gym_class)
-- * อ้างอิง member_id และ class_id
-- ============================================================
INSERT INTO booking (member_id, class_id, book_date, status) VALUES
(1, 2, '2024-05-28', 'confirmed'),
(2, 1, '2024-05-29', 'confirmed'),
(2, 4, '2024-05-29', 'confirmed'),
(3, 2, '2024-05-30', 'confirmed'),
(3, 3, '2024-05-30', 'pending'),
(4, 1, '2024-05-31', 'confirmed'),
(5, 3, '2024-05-31', 'cancelled');

-- ============================================================
-- 6. INSERT อุปกรณ์ที่ใช้ในแต่ละคลาส (class_equipment) - M:N (gym_class × equipment)
-- * อ้างอิง class_id และ equip_id พร้อมจำนวน
-- ============================================================
INSERT INTO class_equipment (class_id, equip_id, quantity) VALUES
(1, 1, 15),  -- Morning Flow Yoga ใช้ Yoga Mat 15 ผืน
(2, 2, 20),  -- Power Body Pump ใช้ Dumbbell Set 20 คู่
(3, 3, 10),  -- Burn Fat HIIT ใช้ Kettlebell 10 ลูก
(3, 4, 12),  -- Burn Fat HIIT ใช้ Resistance Band 12 เส้น
(4, 1, 15);  -- Evening Gentle Yoga ใช้ Yoga Mat 15 ผืน