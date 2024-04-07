--Отримати всі завдання певного користувача
SELECT * FROM tasks WHERE user_id = 1; -- Припустимо, що 1 це ID користувача
--Вибрати завдання за певним статусом
SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = 'new');
--Оновити статус конкретного завдання
UPDATE tasks SET status_id = (SELECT id FROM status WHERE name = 'in progress') WHERE id = 1; -- Припустимо, що 1 це ID завдання
-- Отримати список користувачів, які не мають жодного завдання
SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks);
--Додати нове завдання для конкретного користувача
INSERT INTO tasks (title, description, status_id, user_id) VALUES ('Нове завдання', 'Опис нового завдання', 1, 1); -- Припустимо, що 1 це ID статусу та користувача
--Отримати всі завдання, які ще не завершено
SELECT * FROM tasks WHERE status_id != (SELECT id FROM status WHERE name = 'completed');
-- Видалити конкретне завдання
DELETE FROM tasks WHERE id = 1; -- Припустимо, що 1 це ID завдання
--Знайти користувачів з певною електронною поштою
SELECT * FROM users WHERE email LIKE '%example.com%'; -- Пошук користувачів з електронною поштою на домені example.com
--Оновити ім'я користувача
UPDATE users SET fullname = 'Нове імя' WHERE id = 1; -- Припустимо, що 1 це ID користувача
--Отримати кількість завдань для кожного статусу
SELECT status_id, COUNT(*) FROM tasks GROUP BY status_id;
--Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти
SELECT tasks.* FROM tasks
JOIN users ON tasks.user_id = users.id
WHERE users.email LIKE '%@example.com';
--Отримати список завдань, що не мають опису
SELECT * FROM tasks WHERE description IS NULL OR description = '';
--Вибрати користувачів та їхні завдання, які є у статусі 'in progress'
SELECT users.*, tasks.* FROM tasks
JOIN users ON tasks.user_id = users.id
JOIN status ON tasks.status_id = status.id
WHERE status.name = 'in progress';
--Отримати користувачів та кількість їхніх завдань
SELECT users.id, users.fullname, COUNT(tasks.id) AS tasks_count FROM users
LEFT JOIN tasks ON users.id = tasks.user_id
GROUP BY users.id;
