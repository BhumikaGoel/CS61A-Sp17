.read fa16data.sql
.read sp17data.sql

CREATE TABLE obedience AS
  select seven, hilfinger from students;

CREATE TABLE smallest_int AS
  select time, smallest from students WHERE smallest > 16 ORDER BY smallest LIMIT 20;

CREATE TABLE greatstudents AS
  select a.date, a.color, a.pet, a.number, b.number
    from students AS a, fa16students AS b
    where a.date = b.date AND a.pet = b.pet AND a.color = b.color;

CREATE TABLE sevens AS
  select a.seven
  FROM students as a, checkboxes as b
  WHERE a.number = 7 AND b.'7' = 'True' AND a.time = b.time;

CREATE TABLE matchmaker AS
  select a.pet, a.song, a.color, b.color
  from students AS a, students AS b
    where a.pet = b.pet AND a.song = b.song AND a.time < b.time;
