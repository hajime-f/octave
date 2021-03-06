CREATE DATABASE IF NOT EXISTS octave_db CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
CREATE USER IF NOT EXISTS ${OCTAVE_DB_USER}@'%' IDENTIFIED BY ${OCTAVE_DB_PASSWORD}
GRANT ALL PRIVILEGES ON octave_db.* TO 'octave_user'@'%';
FLUSH PRIVILEGES;
