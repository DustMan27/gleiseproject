CREATE TABLE signee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    surname TEXT NOT NULL,
    email TEXT NOT NULL,
    dob DATE NOT NULL,
    is_successful INTEGER -- 0 for NO, 1 for YES.
);

CREATE TABLE signee_country (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    signee_id INTEGER,
    country TEXT,
    FOREIGN KEY (signee_id) REFERENCES signee(id) ON DELETE CASCADE
);

CREATE TABLE signee_professional_information (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    signee_id INTEGER,
    industry TEXT,
    job_title TEXT,
    salary REAL,
    FOREIGN KEY (signee_id) REFERENCES signee(id) ON DELETE CASCADE
);

CREATE TABLE signee_healthcare_information (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    signee_id INTEGER,
    provider TEXT,
    reference_number INTEGER,
    FOREIGN KEY (signee_id) REFERENCES signee(id) ON DELETE CASCADE
);