CREATE TABLE signee_new
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        surname TEXT NOT NULL,
        email TEXT NOT NULL,
        dob DATE NOT NULL,
        is_successful INTEGER -- 0 for NO, 1 for YES
        score
    )