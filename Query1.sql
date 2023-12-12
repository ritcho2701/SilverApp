create database vpdata;
drop database vfdata;
use vpdata;
show tables;
Alter table volunteer_pd drop column volunteer_pdcol;
CREATE TABLE volunteer_pd (
    volunteer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name CHAR(50),
    last_name CHAR(50),
    gender CHAR(10),
    age INT,
    vaccine_type CHAR(50),
    contact_no CHAR(20),
    location CHAR(100),
    cold BOOLEAN,
    fever BOOLEAN,
    cough BOOLEAN
);
select * from volunteer_pd;
drop table volunteer_pd,volunteer_fd; 
INSERT INTO volunteer_pd (first_name, last_name, gender, age, vaccine_type, contact_no, location, cold, fever, cough)
VALUES ('Rushi', 'Patil', 'Male', 22, 'Covishield', '9158877595', 'MH', TRUE, FALSE, TRUE),
('Ritik', 'Rajput', 'Male', 24, 'Covaxin', '9158757395', 'BR', TRUE, True, False),
('Piya', 'kolhapure', 'Female', 24, 'Sputnik V', '9159474576', 'KA', TRUE, True, False),
('Monoj', 'Singh', 'Male', 30, 'Covaxin', '9159474455', 'PJ', TRUE, False, False),
('Dinesh', 'Kumar', 'Male', 31, 'Sputnik V', '9159474656', 'DH', TRUE, True, False),
('Harish', 'Mendhe', 'Male', 27, 'Covishield', '9159478774', 'MH', False, True, False);



##################################################################################################
CREATE TABLE volunteer_fd (
    metric_id INT AUTO_INCREMENT PRIMARY KEY,
    heart_rate INT,
    step_count INT,
    sleep_duration INT,
    activity VARCHAR(255),
    activity_duration INT,
    oxygen_saturation FLOAT,
    timestamp TIMESTAMP,
    volunteer_id INT,
    FOREIGN KEY (volunteer_id) REFERENCES volunteer_pd(volunteer_id)
);
select * from volunteer_pd;

INSERT INTO volunteer_fd (heart_rate, step_count, sleep_duration, activity, activity_duration, oxygen_saturation, timestamp, volunteer_id)
VALUES
    (75, 8000, 7, 'Walking', 60, 98.5, '2023-05-22 10:00:00', 1),
    (80, 10000, 6, 'Running', 45, 97.8, '2023-05-22 11:30:00', 2),
    (70, 5000, 8, 'Cycling', 30, 98.2, '2023-05-22 12:45:00', 3),
    (85, 12000, 7, 'Swimming', 90, 98.9, '2023-05-22 14:15:00', 4),
    (90, 15000, 6, 'Gym workout', 75, 97.5, '2023-05-22 15:30:00', 5),
    (92, 5000, 6, 'Cycling', 70, 92.5, '2023-05-22 13:30:00', 6);
    
Alter table volunteer_fd ;
drop table users;
Alter table volunteer_pd drop column zone;
create table users(
username varchar(20),
hashed_password varchar(20),
role varchar(20));
create table messages(
message varchar(50));
insert into users(username,hashed_password)values('rushi','pass');
select * from messages;

######################################################
CREATE TABLE volunteer_pd (
    volunteer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name CHAR(50),
    last_name CHAR(50),
    gender CHAR(10),
    age INT,
    vaccine_type CHAR(50),
    contact_no CHAR(20),
    location CHAR(100),
    cold BOOLEAN,
    fever BOOLEAN,
    cough BOOLEAN,
    message varchar(50)
);