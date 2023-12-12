create database SilverLine_database;
use SilverLine_database;
drop database SilverLine_database;
------------------------------------------------------------------

CREATE TABLE registered_people_data (
  id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  gender VARCHAR(10),
  age INT,
  location VARCHAR(255),
  contact_number VARCHAR(20),
  mail_id VARCHAR(255),
  health_care_worker TINYINT(1),
  previous_covid TINYINT(1),
  igg_igm TINYINT(1),
  female_pregnancy TINYINT(1),
  allergy TINYINT(1),
  immunosuppressant TINYINT(1),
  corticosteroids TINYINT(1),
  asplenia TINYINT(1),
  bleeding_disorder TINYINT(1),
  alcohol_drug_abuse TINYINT(1),
  immunoglobulins TINYINT(1),
  clinical_trial TINYINT(1),
  live_vaccine TINYINT(1),
  days_since_live_vaccine INT,
  inactivated_vaccine TINYINT(1),
  days_since_inactivated_vaccine INT,
  fever TINYINT(1),
  autoimmune_immunodeficiency TINYINT(1),
  consent_accepted TINYINT(1),
  Status varchar(30),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  
);
--------------------------------------------------------------------
drop table registered_people_data;
--------------------------------------------------------------------
select  * from registered_people_data;
--------------------------------------------------------------------
CREATE TABLE paticipant_study (
  id INT PRIMARY KEY,
  conditions VARCHAR(255),
  vaccine_type VARCHAR(255),
  FOREIGN KEY (ID) REFERENCES registered_people_data(id)
);

-------------------------------------------------------------
select * from paticipant_study;
-------------------------------------------------------------
CREATE TABLE volunteer_personal_data (
  ID INT PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  gender VARCHAR(10),
  age INT,
  location VARCHAR(255),
  contact_number VARCHAR(20),
  mail_id VARCHAR(255),
  conditions VARCHAR(255),
  vaccine_type VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (ID) REFERENCES registered_people_data(id)
);
-----------------------------------------------
select count(*) from volunteer_personal_data;
-----------------------------------------------


SET SQL_SAFE_UPDATES = 0;
drop table volunteer_fitness_data;

-----------------------------------------------
CREATE TABLE volunteer_fitness_data (
  ID INT PRIMARY KEY AUTO_INCREMENT,
  Oxygen FLOAT,
  PulseRate FLOAT,
  Temperature FLOAT,
  Diabities INT,
  bp_systolic INT,
  bp_diastolic INT
);
--------------------------------
drop table volunteer_fitness_data;
------------------------------------------------
select * from volunteer_fitness_data;
------------------------------------------------
CREATE TABLE feedback_table (
    id INT,
    current_time1 TIMESTAMP,
    response VARCHAR(255),
    fatigue INT,
    pain_or_soreness INT,
    headache INT,
    muscle_or_joint_pain INT,
    low_grade_fever INT,
    additional_side_effects TEXT
);

-----------------------------------------------
select * from feedback_table;
drop table feedback_table;

select * from paticipant_study;
-------------------------------------------------
CREATE VIEW eligible_data AS
SELECT rd.ID, rd.first_name, rd.last_name, rd.gender, rd.age, rd.location, rd.contact_number, rd.mail_id,
       ps.conditions, ps.vaccine_type, vf.Oxygen, vf.PulseRate, vf.Temperature, vf.bp_systolic, vf.bp_diastolic
FROM (
    SELECT id FROM registered_people_data WHERE Status = 'eligible' ORDER BY RAND() LIMIT 40
) AS random_ids
JOIN registered_people_data rd ON rd.ID = random_ids.id
JOIN paticipant_study ps ON rd.ID = ps.id
JOIN volunteer_personal_data vp ON rd.ID = vp.ID
JOIN volunteer_fitness_data vf ON vp.ID = vf.ID;
select * from eligible_data;

---------------------------------------------------------------------------------
CREATE TABLE complete_data (
  ID INT PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  gender VARCHAR(10),
  age INT,
  location VARCHAR(255),
  contact_number VARCHAR(20),
  mail_id VARCHAR(255),
  conditions VARCHAR(255),
  vaccine_type VARCHAR(255),
  Oxygen FLOAT,
  PulseRate FLOAT,
  Temperature FLOAT,
  bp_systolic INT,
  bp_diastolic INT,
  zone VARCHAR(255),
  identified_conditions VARCHAR(255),
  prescription VARCHAR(255),
  response VARCHAR(255),
  Fatigue INT,
  pain_or_soreness INT,
  headache INT,
  muscle_or_joint_pain INT,
  low_grade_fever INT,
  additional_side_effects TEXT,
  current_time1 TIMESTAMP,
  doctor_note VARCHAR(255)
);
------------------------------------------
select * from complete_data;

------------------------------------------
CREATE TABLE patients (
    volunteer_id INT,
    unique_id VARCHAR(50)
    );
INSERT INTO patients (volunteer_id, unique_id) VALUES
(1, 'ABC001'),
(2, 'DEF002'),
(3, 'GHI003'),
(4, 'JKL004'),
(5, 'MNO005'),
(6, 'PQR006'),
(7, 'STU007'),
(8, 'VWX008'),
(9, 'YZA009'),
(10, 'BCD010'),
(11, 'EFG011'),
(12, 'HIJ012'),
(13, 'KLM013'),
(14, 'NOP014'),
(15, 'QRS015'),
(16, 'TUV016'),
(17, 'WXY017'),
(18, 'ZAB018'),
(19, 'CDE019'),
(20, 'FGH020'),
(21, 'IJK021'),
(22, 'LMN022'),
(23, 'OPQ023'),
(24, 'RST024'),
(25, 'UVW025'),
(26, 'XYZ026'),
(27, 'ABC027'),
(28, 'DEF028'),
(29, 'GHI029'),
(30, 'JKL030'),
(31, 'MNO031'),
(32, 'PQR032'),
(33, 'STU033'),
(34, 'VWX034'),
(35, 'YZA035'),
(36, 'BCD036'),
(37, 'EFG037'),
(38, 'HIJ038'),
(39, 'KLM039'),
(40, 'NOP040'),
(41, 'QRS041'),
(42, 'TUV042'),
(43, 'WXY043'),
(44, 'ZAB044'),
(45, 'CDE045'),
(46, 'FGH046'),
(47, 'IJK047'),
(48, 'LMN048'),
(49, 'OPQ049'),
(50, 'RST050'),
(51, 'UVW051'),
(52, 'XYZ052'),
(53, 'ABC053'),
(54, 'DEF054'),
(55, 'GHI055'),
(56, 'JKL056'),
(57, 'MNO057'),
(58, 'PQR058'),
(59, 'STU059'),
(60, 'VWX060'),
(61, 'YZA061'),
(62, 'BCD062'),
(63, 'EFG063'),
(64, 'HIJ064'),
(65, 'KLM065'),
(66, 'NOP066'),
(67, 'QRS067'),
(68, 'TUV068'),
(69, 'WXY069'),
(70, 'ZAB070'),
(71, 'CDE071'),
(72, 'FGH072'),
(73, 'IJK073'),
(74, 'LMN074'),
(75, 'OPQ075'),
(76, 'RST076'),
(77, 'UVW077'),
(78, 'XYZ078'),
(79, 'ABC079'),
(80, 'DEF080'),
(81, 'GHI081'),
(82, 'JKL082'),
(83, 'MNO083'),
(84, 'PQR084'),
(85, 'STU085'),
(86, 'VWX086'),
(87, 'YZA087'),
(88, 'BCD088'),
(89, 'EFG089'),
(90, 'HIJ090'),
(91, 'KLM091'),
(92, 'NOP092'),
(93, 'QRS093'),
(94, 'TUV094'),
(95, 'WXY095'),
(96, 'ZAB096'),
(97, 'CDE097'),
(98, 'FGH098'),
(99, 'IJK099'),
(100, 'LMN100'),
(101, 'OPQ101'),
(102, 'RST102'),
(103, 'UVW103'),
(104, 'XYZ104'),
(105, 'ABC105'),
(106, 'DEF106'),
(107, 'GHI107'),
(108, 'JKL108');





