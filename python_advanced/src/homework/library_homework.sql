DROP TABLE IF EXISTS borrow_records CASCADE;
DROP TABLE IF EXISTS employees CASCADE;
DROP TABLE IF EXISTS library_branches CASCADE;
DROP TABLE IF EXISTS book_copies CASCADE;
DROP TABLE IF EXISTS books CASCADE;
DROP TABLE IF EXISTS users CASCADE;


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255) UNIQUE NOT NULL,
    registered_date DATE NOT NULL,
    date_of_birth DATE NOT NULL,
    address TEXT
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    publish_date DATE,
    isbn VARCHAR(20) UNIQUE NOT NULL
);

CREATE TABLE book_copies (
    id SERIAL PRIMARY KEY,
    book_id INT REFERENCES books(id),
    copy_number INT NOT NULL,
    is_borrowed BOOLEAN DEFAULT FALSE
);

CREATE TABLE library_branches (
    id SERIAL PRIMARY KEY,
    branch_name VARCHAR(100) NOT NULL,
    location TEXT NOT NULL
);

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    hire_date DATE NOT NULL,
    library_branch_id INT REFERENCES library_branches(id)
);

CREATE TABLE borrow_records (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    book_copy_id INT REFERENCES book_copies(id),
    borrow_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE,
    library_branch_id INT REFERENCES library_branches(id)
);

INSERT INTO users (first_name, last_name, email, registered_date, date_of_birth, address) VALUES
('Іван', 'Петренко', 'ivan.petrenko@example.com', '2023-01-01', '1990-05-15', 'Київ'),
('Марія', 'Коваленко', 'maria.kovalenko@example.com', '2023-02-10', '1992-07-22', 'Львів'),
('Олег', 'Сидоренко', 'oleg.sydorenko@example.com', '2023-03-05', '1985-03-12', 'Одеса'),
('Анна', 'Мельник', 'anna.melnyk@example.com', '2023-04-12', '1998-10-30', 'Харків'),
('Павло', 'Шевченко', 'pavlo.shevchenko@example.com', '2023-05-01', '1987-09-01', 'Дніпро'),
('Ірина', 'Ткаченко', 'iryna.tkachenko@example.com', '2023-06-15', '1995-12-25', 'Тернопіль'),
('Сергій', 'Гриценко', 'serhii.hrytsenko@example.com', '2023-07-20', '1983-11-11', 'Чернігів'),
('Катерина', 'Лисенко', 'kateryna.lysenko@example.com', '2023-08-09', '1991-04-08', 'Полтава'),
('Володимир', 'Кравчук', 'volodymyr.kravchuk@example.com', '2023-09-13', '1989-06-06', 'Вінниця'),
('Оксана', 'Романюк', 'oksana.romaniuk@example.com', '2023-10-05', '1997-01-19', 'Житомир');

INSERT INTO books (title, author, publish_date, isbn) VALUES
('Кобзар', 'Тарас Шевченко', '1840-01-01', 'ISBN0001'),
('Захар Беркут', 'Іван Франко', '1883-01-01', 'ISBN0002'),
('Лісова пісня', 'Леся Українка', '1911-01-01', 'ISBN0003'),
('Сто років самотності', 'Габріель Гарсія Маркес', '1967-01-01', 'ISBN0004'),
('Майстер і Маргарита', 'Михайло Булгаков', '1966-01-01', 'ISBN0005'),
('1984', 'Джордж Орвелл', '1949-01-01', 'ISBN0006'),
('Пригоди Тома Сойєра', 'Марк Твен', '1876-01-01', 'ISBN0007'),
('Війна і мир', 'Лев Толстой', '1869-01-01', 'ISBN0008'),
('Фауст', 'Йоганн Ґете', '1808-01-01', 'ISBN0009'),
('Гаррі Поттер і філософський камінь', 'Дж. К. Ролінг', '1997-01-01', 'ISBN0010');

INSERT INTO book_copies (book_id, copy_number, is_borrowed) VALUES
(1, 1, FALSE), (1, 2, TRUE),
(2, 1, FALSE), (3, 1, FALSE),
(4, 1, TRUE),  (5, 1, FALSE),
(6, 1, FALSE), (7, 1, FALSE),
(8, 1, TRUE),  (9, 1, FALSE);

INSERT INTO library_branches (branch_name, location) VALUES
('Центральна бібліотека', 'Київ'),
('Філія №1', 'Львів'),
('Філія №2', 'Одеса'),
('Філія №3', 'Харків'),
('Філія №4', 'Дніпро'),
('Філія №5', 'Тернопіль'),
('Філія №6', 'Полтава'),
('Філія №7', 'Вінниця'),
('Філія №8', 'Чернівці'),
('Філія №9', 'Житомир');

INSERT INTO employees (first_name, last_name, hire_date, library_branch_id) VALUES
('Олександр', 'Іванов', '2020-01-01', 1),
('Марина', 'Петренко', '2021-02-15', 2),
('Ігор', 'Коваль', '2022-03-10', 3),
('Світлана', 'Шевченко', '2019-04-05', 4),
('Віктор', 'Бондаренко', '2018-05-20', 5),
('Наталія', 'Мороз', '2021-06-11', 6),
('Дмитро', 'Сергієнко', '2020-07-07', 7),
('Юлія', 'Тимошенко', '2022-08-18', 8),
('Роман', 'Данилюк', '2019-09-09', 9),
('Людмила', 'Гаврилюк', '2020-10-12', 10);

INSERT INTO borrow_records (user_id, book_copy_id, borrow_date, due_date, return_date, library_branch_id) VALUES
(1, 2, '2023-01-10', '2023-02-10', '2023-02-05', 1),
(2, 4, '2023-02-15', '2023-03-15', NULL, 2),
(3, 5, '2023-03-20', '2023-04-20', '2023-04-15', 3),
(4, 6, '2023-04-25', '2023-05-25', NULL, 4),
(5, 7, '2023-05-30', '2023-06-30', '2023-06-28', 5),
(6, 8, '2023-06-10', '2023-07-10', NULL, 6),
(7, 9, '2023-07-15', '2023-08-15', '2023-08-10', 7),
(8, 10, '2023-08-20', '2023-09-20', NULL, 8),
(9, 3, '2023-09-25', '2023-10-25', '2023-10-20', 9),
(10, 1, '2023-10-30', '2023-11-30', NULL, 10);


SELECT * FROM users;
SELECT * FROM books;
SELECT * FROM borrow_records;

