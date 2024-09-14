CREATE TABLE role_multipliers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role_name TEXT NOT NULL,
    multiplier REAL NOT NULL DEFAULT 0.0
);

INSERT INTO role_multipliers (role_name, multiplier)
    VALUES
        ('MANAGER', 1.1),
        ('SPECIALIST', 1.1),
        ('SENIOR', 1.15),
        ('DIRECTOR', 1.30),
        ('ANALYST', 1.15),
        ('CEO', 2.0),
        ('OFFICER', 1.3),
        ('HEAD', 1.4),
        ('VP', 1.75),
        ('VICE', 1.75),
        ('PRESIDENT', 2.00),
        ('PRINCIPAL', 1.75),
        ('ENGINEER', 1.5),
        ('OPERATIONS', 1.25),
        ('TECHNOLOGY', 1.25),
        ('ENGINEERING', 1.25),
        ('SPACE', 2.00),
        ('AEROSPACE', 1.5),
        ('ASTRONOMY', 1.5),
        ('ASTROPHYSICS', 1.5),
        ('PLANETARY', 1.5),
        ('GEOLOGY', 1.4),
        ('GEOPHYSICS', 1.4),
        ('BIOLOGIST', 1.4),
        ('ENVIRONMENTAL', 1.4),
        ('PROPULSION', 1.4),
        ('AVIATION', 1.3),
        ('TELECOMMUNICATIONS', 1.2)
    ;

