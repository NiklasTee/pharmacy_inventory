/* STEP 1: Create & Connect to Database */


-- DROP DATABASE pharmacy;
-- CREATE DATABASE pharmacy; -- connect to database afterwards


/* STEP 2: Create Tables */

CREATE TABLE arzneimittel (
	pzn INT NOT NULL PRIMARY KEY,
	bezeichnung VARCHAR(255),
	herkue VARCHAR(255),
	darr VARCHAR(255),
	menge VARCHAR(255),
	warengruppe VARCHAR(255),
	me VARCHAR(255),
	rezeptflichtig BOOLEAN,
	apothekenpflichtig BOOLEAN,
	lagerort VARCHAR(255));

CREATE TABLE auftrag (
	auftrag INT NOT NULL,
	datum DATE NOT NULL,
	PRIMARY KEY(auftrag, datum)
);

CREATE TABLE hersteller (
	herkue VARCHAR(255) NOT NULL PRIMARY KEY);

CREATE TABLE lager (
	lagerort VARCHAR(255) NOT NULL PRIMARY KEY,
	lagerortname VARCHAR(255));

CREATE TABLE transaktion (
	id SERIAL NOT NULL PRIMARY KEY,
	auftrag INT,
	datum DATE,
	uhrzeit TIME,
	pzn INT,
	anzahl INT,
	retoure BOOLEAN,
	verfalldaten DATE,
	nachlieferungsmenge INT);

CREATE TABLE warengruppe (
	warengruppe VARCHAR(255) NOT NULL PRIMARY KEY,
	warengruppenbezeichnung_1 VARCHAR(255),
	warengruppenbezeichnung_2 VARCHAR(255),
	warengruppenbezeichnung_3 VARCHAR(255));



/* STEP 3: Establish Relations between Tables */


ALTER TABLE arzneimittel ADD CONSTRAINT fk_arzneimittel_hersteller FOREIGN KEY (lagerort) REFERENCES lager (lagerort);
ALTER TABLE arzneimittel ADD CONSTRAINT fk_arzneimittel_lager FOREIGN KEY (herkue) REFERENCES hersteller (herkue);
ALTER TABLE arzneimittel ADD CONSTRAINT fk_arzneimittel_warengruppe FOREIGN KEY (warengruppe) REFERENCES warengruppe (warengruppe);

ALTER TABLE transaktion ADD CONSTRAINT fk_transaktion_arzneimittel FOREIGN KEY (pzn) REFERENCES arzneimittel (pzn);
ALTER TABLE transaktion ADD CONSTRAINT fk_transaktion_auftrag FOREIGN KEY (auftrag, datum) REFERENCES auftrag (auftrag, datum);





/* STEP 4: Load Data into Tables */

COPY hersteller(herkue)
FROM 'C:\Users\Niklas\pharmacy_inventory\data\tables_preprocessed\hersteller.csv'
DELIMITER ','
CSV HEADER;

COPY lager(lagerort, lagerortname)
FROM 'C:\Users\Niklas\pharmacy_inventory\data\tables_preprocessed\lager.csv'
DELIMITER ','
CSV HEADER;

COPY warengruppe(warengruppe, warengruppenbezeichnung_1, warengruppenbezeichnung_2, warengruppenbezeichnung_3)
FROM 'C:\Users\Niklas\pharmacy_inventory\data\tables_preprocessed\warengruppe.csv'
DELIMITER ','
CSV HEADER;

COPY arzneimittel(pzn, bezeichnung, herkue, darr, menge, warengruppe, me, rezeptflichtig, apothekenpflichtig, lagerort)
FROM 'C:\Users\Niklas\pharmacy_inventory\data\tables_preprocessed\arzneimittel.csv'
DELIMITER ','
CSV HEADER;

COPY auftrag(auftrag, datum)
FROM 'C:\Users\Niklas\pharmacy_inventory\data\tables_preprocessed\auftrag.csv'
DELIMITER ','
CSV HEADER;

COPY transaktion(auftrag, datum, uhrzeit, pzn, anzahl, retoure, verfalldaten , nachlieferungsmenge)
FROM 'C:\Users\Niklas\pharmacy_inventory\data\tables_preprocessed\transaktion.csv'
DELIMITER ','
CSV HEADER;