CREATE TABLE volunteer_fitness_data (
  volunteer_id INT,
  oxygen_saturation INT,
  pulse_rate INT,
  temp DECIMAL(5,2),
  bp VARCHAR(10),
  diabetes INT,
  step_count INT,
  timestamp TIMESTAMP,
  CONSTRAINT volunteer_fitness_data_pk PRIMARY KEY (volunteer_id),
  CONSTRAINT volunteer_fitness_data_fk FOREIGN KEY (volunteer_id) REFERENCES volunteer_personal_data (volunteer_id),
  CONSTRAINT volunteer_fitness_data_chk CHECK (diabetes BETWEEN 80 AND 300)
);
------------------------------------------------------------------
CREATE TABLE volunteer_personal_data (
  volunteer_id INT NOT NULL,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  gender VARCHAR(10),
  age INT,
  vaccination_type VARCHAR(50),
  contact_number VARCHAR(20),
  location VARCHAR(50),
  no_of_dosage INT,
  PRIMARY KEY (volunteer_id),
  CONSTRAINT volunteer_personal_data_chk_1 CHECK (location IN ('Andhra Pradesh', 'Delhi', 'Karnataka', 'Maharashtra', 'Tamil Nadu'))
);

-------------------------------------------------------------------
CREATE TABLE patients (
    volunteer_id INT,
    unique_id VARCHAR(50)
    );
INSERT INTO patients (volunteer_id, unique_id) VALUES
(1, 'ABC123'),
(2, 'DEF456'),
(3, 'GHI789');
-----------------------------------------------------------------------
CREATE TABLE af_data (
  volunteer_id INT,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  gender VARCHAR(255),
  age INT,
  vaccination_type VARCHAR(255),
  contact_number VARCHAR(20),
  location VARCHAR(255),
  no_of_dosage INT,
  oxygen_saturation INT,
  pulse_rate INT,
  temp DECIMAL(5,2),
  bp VARCHAR(10),
  diabetes INT,
  step_count INT,
  timestamp TIMESTAMP,
  message VARCHAR(50),
  CONSTRAINT af_data_chk_1 CHECK (diabetes BETWEEN 80 AND 300)
);


use v_dataset;
-------------------------------------------------------------------------
CREATE TABLE responses (
  volunteer_id INT,
  response VARCHAR(255),
  timestamp TIMESTAMP
);
------------------------------------------------------------------------
    
select * from patients;
-----------------------------------------------------------------------
drop table people_data1;
CREATE TABLE people_data1 (
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
---------------------------------------
select * from people_data;












































-------------------------------------------------------------------
CREATE TABLE patients (
    volunteer_id INT,
    unique_id VARCHAR(50)
    );
INSERT INTO patients (volunteer_id, unique_id) VALUES
(1, 'ABC123'),
(2, 'DEF456'),
(3, 'GHI789');
-----------------------------------------------------------------------
CREATE TABLE af_data (
  volunteer_id INT,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  gender VARCHAR(255),
  age INT,
  vaccination_type VARCHAR(255),
  contact_number VARCHAR(20),
  location VARCHAR(255),
  no_of_dosage INT,
  oxygen_saturation INT,
  pulse_rate INT,
  temp DECIMAL(5,2),
  bp VARCHAR(10),
  diabetes INT,
  step_count INT,
  timestamp TIMESTAMP,
  message VARCHAR(50),
  CONSTRAINT af_data_chk_1 CHECK (diabetes BETWEEN 80 AND 300)
);



-------------------------------------------------------------------------
CREATE TABLE responses (
  volunteer_id INT,
  response VARCHAR(255),
  timestamp TIMESTAMP
);
------------------------------------------------------------------------
use v_dataset;
select * from volunteer_personal_data;

-----------------------------------------------------------------------------
drop table participant ;
CREATE TABLE participant (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    gender ENUM('Male', 'Female', 'Other'),
    age INT,
    location VARCHAR(255),
    contact_number VARCHAR(20),
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
    eligibility_status  VARCHAR(255)
    
);
select * from af_data ;