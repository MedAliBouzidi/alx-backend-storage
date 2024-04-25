-- SQL script that creates a table users

CREATE TABLE IF NOT EXISTS users (
  id int PRIMARY KEY AUTO_INCREMENT NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255),
  country enum('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
)

