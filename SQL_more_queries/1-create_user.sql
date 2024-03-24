-- creates the MySQL server user user_0d_1 and grant all priviledges
MYSQL_USER="user_0d_1"
MYSQL_PASSWORD="user_0d_1_pwd"

CREATE USER IF NOT EXISTS '${MYSQL_USER}'@'localhost' IDENTIFIED BY '${MYSQL_PASSWORD}';
GRANT ALL PRIVILEGES ON *.* TO '${MYSQL_USER}'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
