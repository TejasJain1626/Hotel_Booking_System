# Hotel_Booking_System CLI
A Command Line Interface (CLI) application built with Python and MySQL for managing hotel rooms and reservations with basic date-overlap checks.

## Features
- Add and view Hotels, Rooms, and Bookings.
- Date overlap check to prevent double-booking the same room.
- Cancel bookings by updating reservation status.
- Terminal-based output formatting.

## Setup Instructions
Open your MySQL command line, and run this exact schema script:
```sql
CREATE DATABASE Hotel_Manage;
USE Hotel_Manage;

-- 1. Hotels Table
CREATE TABLE hotels (
    Hotel_ID CHAR(5) PRIMARY KEY,
    Hotel_Name VARCHAR(30) NOT NULL UNIQUE,
    City VARCHAR(20) NOT NULL
);

-- 2. Room_Info Table
CREATE TABLE room_info (
    Room_Num VARCHAR(4) PRIMARY KEY,
    Category VARCHAR(20) NOT NULL,
    price INT NOT NULL,
    Max_occupancy INT NOT NULL,
    STATUS VARCHAR(30) DEFAULT 'Available',
    Hotel_ID CHAR(5) NOT NULL,
    FOREIGN KEY (Hotel_ID) REFERENCES hotels(Hotel_ID)
);

-- 3. Bookings Table
CREATE TABLE bookings (
    Booking_ID INT AUTO_INCREMENT PRIMARY KEY,
    Guest_Name VARCHAR(50) NOT NULL,
    Guest_Phone CHAR(10) NOT NULL,
    Guest_ID_Type VARCHAR(8) NOT NULL,
    ID_Num VARCHAR(12) NOT NULL,
    Hotel_ID CHAR(5) NOT NULL,
    Room_Num VARCHAR(4),
    Check_In DATE NOT NULL,
    Check_Out DATE NOT NULL,
    Status VARCHAR(20) DEFAULT 'Confirmed',
    FOREIGN KEY (Hotel_ID) REFERENCES hotels(Hotel_ID),
    FOREIGN KEY (Room_Num) REFERENCES room_info(Room_Num)
);
```
Install the required Python MySQL connector in your terminal:

```bash
pip install mysql-connector-python
```
Update the host, user, and password inside Hotel_Management.py to match your local MySQL credentials.

Run the application:

```bash
python Hotel_Management.py
```
