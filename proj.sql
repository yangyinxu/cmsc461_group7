--OFFICE TABLE
CREATE TABLE office (
	office_name TEXT PRIMARY KEY,
	city TEXT NOT NULL,
	square_footage REAL NOT NULL
);

--MANAGED
CREATE TABLE managed (
	office_name TEXT PRIMARY KEY,
	rental_id TEXT NOT NULL
);

--RENTAL AGREEMENT
CREATE TABLE rental_agreement (
	rental_id INTEGER PRIMARY KEY,
	rent_amount REAL NOT NULL,
	end_date TEXT
);

--PARTY
CREATE TABLE party(
	rental_id INTEGER PRIMARY KEY,
	agency_id INTEGER
);

--CUSTOMER AGENCY
CREATE TABLE customer_agency(
	agency_id INTEGER PRIMARY KEY,
	agency_name TEXT NOT NULL,
	address TEXT NOT NULL,
	city TEXT NOT NULL,
	phone_number TEXT NOT NULL
);