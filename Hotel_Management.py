import mysql.connector
con = mysql.connector.connect(host="localhost", user="root", password="tiger", database="Hotel_Manage")
cur = con.cursor()

print("*"*140)
print("=== HOTEL MANAGEMENT SYSTEM ===".center(140))

while True:
    print("*"*140)
    print("[1] Hotel Management")
    print("[2] Room Management")
    print("[3] Reservations & Bookings")
    print("[4] Exit System")
    print("*"*140)
    choi1 = input("Select an option [1-4]\t:\t").strip()
    print("*"*140)


    if choi1 == "1":
        print("-"*140)
        print("HOTEL MANAGEMENT".center(140))
        print("-"*140)
        print("[1] Add a Hotel")
        print("[2] View Hotels")
        print("-"*140)
        choi2 = input("Select an option [1-2]\t:\t").strip()

        if choi2 == "1":
            print("-"*140)
            print("Adding a Hotel".center(140))
            print("-"*140)
            ID = input("Hotel ID\t\t:\t").strip()
            Name =  input("Hotel Name\t\t:\t").strip()
            City = input("City\t\t\t:\t").strip()
            print("-"*140)
            query = "INSERT INTO Hotels VALUES ('{}', '{}', '{}');".format(ID, Name, City)
            cur.execute(query)
            con.commit()
            print("[SUCCESS] Hotel {} has been added to the database".format(ID).center(140))
            print("-"*140)

        elif choi2 == "2":
            print("-"*140)
            print("Displaying all Hotels".center(140))
            print("-"*140)
            cur.execute("SELECT * FROM Hotels;")
            data = cur.fetchall()
            if data == []:
                print("[INFO] No data found".center(140))
            else:
                print("","-"*9,"-"*32,"-"*22, "", sep = "+")
                print("", "Hotel ID".ljust(9), "Hotel Name".ljust(32), "City".ljust(22), "", sep = "|")
                print("","-"*9,"-"*32,"-"*22, "", sep = "+")
                for i in data:
                    print("", i[0].ljust(9), i[1].ljust(32), i[2].ljust(22), "", sep = "|")
                print("","-"*9,"-"*32,"-"*22, "", sep = "+")

        else:
            print("-"*140)
            print("[ERROR] Invalid selection. Please choose a valid number".center(140))
            print("-"*140)


    elif choi1 == "2":
        print("*"*140)
        print("ROOM MANAGEMENT".center(140))
        print("-"*140)
        print("[1] Add a Room")
        print("[2] View all Rooms")
        print("[3] Update Room Info")
        print("[4] Delete a Room")
        print("-"*140)
        choi2 = input("Select an option [1-4]\t:\t")

        if choi2 == "1":
            print("-"*140)
            print("Adding a Room".center(140))
            print("-"*140)
            Num = input("Room Number\t\t\t:\t").strip()
            Cat = input("Category of Room\t\t:\t").strip()
            Pri = int(input("Price (Per Night)\t\t:\t"))
            Occu = int(input("Room's Maximum Occupany\t\t:\t"))
            Stat = input("Room Status\t\t\t:\t").strip()
            ID = input("Hotel ID\t\t\t:\t").strip()
            print("-"*140)
            query = "INSERT INTO Room_Info VALUES ('{}', '{}', {}, {}, '{}', '{}');".format(Num, Cat, Pri, Occu, Stat, ID)
            cur.execute(query)
            con.commit()
            print("[SUCCESS] Room {} has been added to the database".format(Num).center(140))
            print("-"*140)

        elif choi2 == "2":
            print("-"*140)
            print("Displaying all Rooms".center(140))
            print("-"*140)
            cur.execute("SELECT * FROM Room_Info;")
            data = cur.fetchall()
            if data == []:
                print("[INFO] No data found".center(140))
            else:
                print("","-"*12,"-"*20,"-"*7,"-"*14,"-"*12,"-"*9, "", sep = "+")
                print("", "Room Number".ljust(12), "Category".ljust(20), "Price".ljust(7), "Max Occupancy".ljust(14), "Room Status".ljust(12), "Hotel ID".ljust(9), "", sep = "|")
                print("","-"*12,"-"*20,"-"*7,"-"*14,"-"*12,"-"*9, "", sep = "+")
                for i in data:
                    print("", i[0].ljust(12), i[1].ljust(20), str(i[2]).ljust(7), str(i[3]).ljust(14), i[4].ljust(12), i[5].ljust(9), "", sep = "|")
                print("","-"*12,"-"*20,"-"*7,"-"*14,"-"*12,"-"*9, "", sep = "+")

        elif choi2 == "3":
            print("-"*140)
            print("Updating Room Information".center(140))
            print("-"*140)
            Hotel_ID = input("Hotel ID\t:\t").strip()
            Room_Num = input("Room Number\t:\t").strip()
            print("-"*140)
            query1 = "SELECT * FROM Room_Info WHERE Hotel_ID = '{}' AND Room_Num = '{}';".format(Hotel_ID, Room_Num)
            cur.execute(query1)
            data=cur.fetchone()
            if data == None:
                print("[INFO] Room not found".center(140))
            else:
                Cat = data[1]
                Pri = data[2]
                Occu = data[3]
                Stat = data[4]
                print("New details (Leave blank and press ENTER to keep existing) :-")
                New_Cat = input("Updated Category (Current : {})\t:\t".format(Cat)).strip()
                if New_Cat == "":
                    New_Cat = Cat
                New_Pri = input("Updated Price (Current : {})\t\t:\t".format(Pri)).strip()
                if New_Pri == "":
                    New_Pri = Pri
                New_Occu = input("Updated Max Occupancy (Current : {})\t:\t".format(Occu)).strip()
                if New_Occu == "":
                    New_Occu = Occu
                New_Stat = input("Updated Status (Current : {})\t:\t".format(Stat)).strip()
                if New_Stat == "":
                    New_Stat = Stat
                New_Pri = int(New_Pri)
                New_Occu = int(New_Occu)
                query2 = '''UPDATE Room_Info SET Category='{}', Price={}, Max_Occupancy={}, Status='{}'
                        WHERE Hotel_ID='{}' AND Room_Num='{}';'''.format(New_Cat, New_Pri, New_Occu, New_Stat, Hotel_ID, Room_Num)
                cur.execute(query2)
                con.commit()
                print("-"*140)
                print("[SUCCESS] Room details successfully updated".center(140))
                print("-"*140)
                
        elif choi2 == "4":
            print("-"*140)
            print("Deleting Room Information".center(140))
            print("-"*140)
            Hotel_ID = input("Hotel ID\t:\t").strip()
            Room_Num = input("Room Number\t:\t").strip()
            print("-"*140)
            query1 = "SELECT * FROM Room_Info WHERE Hotel_ID = '{}' AND Room_Num = '{}';".format(Hotel_ID, Room_Num)
            cur.execute(query1)
            data=cur.fetchone()
            if data == None:
                print("[INFO] Room not found".center(140))
            else:
                confirm = input("[WARNING] Are you sure you want to delete room {} at {} (Y/N)\t:\t".format(Room_Num, Hotel_ID)).strip()
                if confirm.upper() == "Y":
                    query2 = "DELETE FROM Room_Info WHERE Hotel_ID = '{}' AND Room_Num = '{}';".format(Hotel_ID, Room_Num)
                    cur.execute(query2)
                    con.commit()
                    print("-"*140)
                    print("[SUCCESS] Room details deleted successfully!".center(140))
                    print("-"*140)
                elif confirm.upper() == "N":
                    print("-"*140)
                    print("[INFO] Deletion cancelled. No records were deleted".center(140))
                    print("-"*140)
                else:
                    print("-"*140)
                    print("[INVALID INPUT] Please type 'Y' to confirm or 'N' to cancel".center(140))
                    print("-"*140)

        else:
            print("-"*140)
            print("[ERROR] Invalid selection. Please choose a valid number".center(140))
            print("-"*140)


    elif choi1 == "3":
        print("-"*140)
        print("BOOKING MANAGEMENT".center(140))
        print("-"*140)
        print("[1] Make a Booking")
        print("[2] View all Bookings")
        print("[3] Search a Booking")
        print("[4] Update a Booking")
        print("[5] Cancel a Booking")
        print("-"*140)
        choi2 = input("Select an option [1-5]\t:\t").strip()

        if choi2 == "1":
            print("-"*140)
            print("Making a Booking".center(140))
            print("-"*140)
            Guest = input("Guest's Name\t\t\t:\t").strip()
            Phone = input("Guest's Phone Number\t\t:\t").strip()
            ID_Type = input("Guest's ID Type\t\t\t:\t").strip()
            ID_Num = input("ID Number\t\t\t:\t").strip()
            Hotel_ID = input("Hotel ID\t\t\t:\t").strip()
            Room_Num = input("Room Number\t\t\t:\t").strip()
            Check_In = input("Check in Date (YYYY-MM-DD)\t:\t").strip()
            Check_Out = input("Check out Date (YYYY-MM-DD)\t:\t").strip()
            Status = input("Booking Status\t\t\t:\t").strip()
            print("-"*140)
            query1 = '''SELECT Check_In, Check_Out FROM Bookings WHERE Hotel_ID='{}' AND Room_Num='{}' AND Status!='Cancelled'
                        AND Check_In < '{}' AND Check_Out > '{}';'''.format(Hotel_ID, Room_Num, Check_Out, Check_In)
            cur.execute(query1)
            conflict = cur.fetchall()
            if conflict == [] :
                query = '''INSERT INTO Bookings(Guest_Name, Guest_Phone, Guest_ID_Type, ID_Num, Hotel_ID, Room_Num, Check_In, Check_Out, Status) VALUES
                        ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');'''.format(Guest, Phone, ID_Type, ID_Num, Hotel_ID, Room_Num, Check_In, Check_Out, Status)
                cur.execute(query)
                con.commit()
                print("[SUCCESS] Booking confirmed successfully".center(140))
                print("-"*140)
            else:
                print("[DECLINED] Room {} at {} is already booked".format(Room_Num, Hotel_ID).center(140))
                print("-"*140)
                print("The conflicting reservations for the room:")
                for i, j in conflict :
                    print("From {} to {}".format(i, j))
                print("-"*140)

        elif choi2 == "2":
            print("-"*140)
            print("Displaying all Bookings".center(140))
            print("-"*140)
            Hotel_ID = input("Hotel ID to view Bookings\t:\t").strip()
            print("-"*140)
            query = "SELECT * FROM Bookings WHERE Hotel_ID = '{}';".format(Hotel_ID)
            cur.execute(query)
            data = cur.fetchall()
            if data == []:
                print("[INFO] No data found".center(140))
            else:
                print("", "-"*11, "-"*22, "-"*13, "-"*9, "-"*13, "-"*9, "-"*12, "-"*11, "-"*11, "-"*15, "", sep = "+")
                print("", "Booking ID".ljust(11), "Guest Name".ljust(22), "Phone Number".ljust(13), "ID Type".ljust(9), "ID Number".ljust(13),
                      "Hotel ID".ljust(9), "Room Number".ljust(12), "Check In".ljust(11), "Check Out".ljust(11), "Status".ljust(15), "", sep = "|")
                print("", "-"*11, "-"*22, "-"*13, "-"*9, "-"*13, "-"*9, "-"*12, "-"*11, "-"*11, "-"*15, "", sep = "+")
                for i in data:
                    print("", str(i[0]).ljust(11), i[1].ljust(22), i[2].ljust(13), i[3].ljust(9), i[4].ljust(13), i[5].ljust(9), i[6].ljust(12),
                          str(i[7]).ljust(11), str(i[8]).ljust(11), i[9].ljust(15), "", sep = "|")
                print("", "-"*11, "-"*22, "-"*13, "-"*9, "-"*13, "-"*9, "-"*12, "-"*11, "-"*11, "-"*15, "", sep = "+")
            print("-"*140)

        elif choi2 == "3":
            print("-"*140)
            print("Searching Booking Information".center(140))
            print("-"*140)
            Phone = input("Guest's Phone Number\t:\t").strip()
            query = "SELECT * FROM Bookings WHERE Guest_Phone = '{}';".format(Phone)
            print("-"*140)
            cur.execute(query)
            data = cur.fetchall()
            if data == []:
                print("[INFO] No bookings found for this phone number".center(140))
            else:
                print("", "-"*11, "-"*22, "-"*13, "-"*9, "-"*13, "-"*9, "-"*12, "-"*11, "-"*11, "-"*15, "", sep = "+")
                print("", "Booking ID".ljust(11), "Guest Name".ljust(22), "Phone Number".ljust(13), "ID Type".ljust(9), "ID Number".ljust(13),
                      "Hotel ID".ljust(9), "Room Number".ljust(12), "Check In".ljust(11), "Check Out".ljust(11), "Status".ljust(15), "", sep = "|")
                print("", "-"*11, "-"*22, "-"*13, "-"*9, "-"*13, "-"*9, "-"*12, "-"*11, "-"*11, "-"*15, "", sep = "+")
                for i in data:
                    print("", str(i[0]).ljust(11), i[1].ljust(22), i[2].ljust(13), i[3].ljust(9), i[4].ljust(13), i[5].ljust(9), i[6].ljust(12),
                          str(i[7]).ljust(11), str(i[8]).ljust(11), i[9].ljust(15), "", sep = "|")
                print("", "-"*11, "-"*22, "-"*13, "-"*9, "-"*13, "-"*9, "-"*12, "-"*11, "-"*11, "-"*15, "", sep = "+")
            print("-"*140)

        elif choi2 == "4":
            print("-"*140)
            print("Updating Booking Information".center(140))
            print("-"*140)
            Phone = input("Guest's Phone Number\t:\t").strip()
            query1 = "SELECT * FROM Bookings WHERE Guest_Phone = '{}';".format(Phone)
            print("-"*140)
            cur.execute(query1)
            data1 = cur.fetchall()
            if data1 == []:
                print("[INFO] No bookings found for this phone number".center(140))
            else:
                print("", "-"*11, "-"*22, "-"*13, "-"*9, "-"*13, "-"*9, "-"*12, "-"*11, "-"*11, "-"*15, "", sep = "+")
                print("", "Booking ID".ljust(11), "Guest Name".ljust(22), "Phone Number".ljust(13), "ID Type".ljust(9), "ID Number".ljust(13),
                      "Hotel ID".ljust(9), "Room Number".ljust(12), "Check In".ljust(11), "Check Out".ljust(11), "Status".ljust(15), "", sep = "|")
                print("", "-"*11, "-"*22, "-"*13, "-"*9, "-"*13, "-"*9, "-"*12, "-"*11, "-"*11, "-"*15, "", sep = "+")
                for i in data1 :
                    print("", str(i[0]).ljust(11), i[1].ljust(22), i[2].ljust(13), i[3].ljust(9), i[4].ljust(13), i[5].ljust(9), i[6].ljust(12),
                          str(i[7]).ljust(11), str(i[8]).ljust(11), i[9].ljust(15), "", sep = "|")
                print("", "-"*11, "-"*22, "-"*13, "-"*9, "-"*13, "-"*9, "-"*12, "-"*11, "-"*11, "-"*15, "", sep = "+")
            print("-"*140)
            ID = input("Booking ID to Update\t:\t").strip()
            print("-"*140)  
            query2 = "SELECT * FROM Bookings WHERE Booking_ID = '{}';".format(ID)
            cur.execute(query2)
            data2 = cur.fetchone()
            if data2 == None:
                print("[ERROR] No booking found with ID: {}".format(ID).center(140))
            else:
                Name = data2[1]
                Phone = data2[2]
                ID_Type = data2[3]
                ID_Num = data2[4]
                Check_In = data2[7]
                Check_Out = data2[8]
                Stat = data2[9]
                print("New details (Leave blank and press ENTER to keep existing) :-")
                New_Name = input("Updated Name (Current : {})\t\t:\t".format(Name)).strip()
                if New_Name == "":
                    New_Name = Name
                New_Phone = input("Updated Phone Number (Current : {})\t:\t".format(Phone)).strip()
                if New_Phone == "":
                    New_Phone = Phone
                New_ID_Type = input("Updated ID Type (Current : {})\t\t:\t".format(ID_Type)).strip()
                if New_ID_Type == "":
                    New_ID_Type = ID_Type
                New_ID_Num = input("Updated ID Number (Current : {})\t:\t".format(ID_Num)).strip()
                if New_ID_Num == "":
                    New_ID_Num = ID_Num
                New_Check_In = input("Updated Check in Date (Current : {})\t:\t".format(Check_In)).strip()
                if New_Check_In == "":
                    New_Check_In = Check_In
                New_Check_Out = input("Updated Check out Date (Current : {})\t:\t".format(Check_Out)).strip()
                if New_Check_Out == "":
                    New_Check_Out = Check_Out
                New_Stat = input("Updated Status (Current : {})\t\t:\t".format(Stat)).strip()
                if New_Stat == "":
                    New_Stat = Stat
                query1 = '''SELECT Check_In, Check_Out FROM Bookings WHERE Hotel_ID='{}' AND Room_Num='{}' AND Status!='Cancelled' AND Booking_ID!='{}'
                        AND Check_In < '{}' AND Check_Out > '{}';'''.format(data2[5], data2[6], ID, New_Check_Out, New_Check_In)
                cur.execute(query1)
                conflict = cur.fetchall()
                if conflict == [] :
                    query3 = '''UPDATE Bookings SET Guest_Name='{}', Guest_Phone='{}', Guest_ID_Type='{}', ID_Num='{}', Check_In='{}', Check_Out='{}', Status='{}'
                                WHERE Booking_ID={};'''.format(New_Name, New_Phone, New_ID_Type, New_ID_Num, New_Check_In, New_Check_Out, New_Stat, ID)
                    cur.execute(query3)
                    con.commit()
                    print("-"*140)
                    print("[SUCCESS] Booking details successfully updated".center(140))
                    print("-"*140)
                else:
                    print("\t\t[DECLINED] Room {} at {} is already booked".format(data2[6], data2[5]))
                    print("-"*140)
                    print("The conflicting reservations for the room:")
                    for i, j in conflict :
                        print("From {} to {}".format(i, j))
                    print("-"*140)
                
        elif choi2 == "5":
            print("-"*140)
            print("Cancelling a Booking".center(140))
            print("-"*140)
            Phone = input("Guest's Phone Number\t:\t").strip()
            query1 = "SELECT * FROM Bookings WHERE Guest_Phone = '{}';".format(Phone.strip())
            print("-"*140)
            cur.execute(query1)
            data1 = cur.fetchall()
            if data1 == []:
                print("[INFO] No bookings found for this phone number".center(140))
            else:
                print("", "-"*11, "-"*22, "-"*13, "-"*9, "-"*13, "-"*9, "-"*12, "-"*11, "-"*11, "-"*15, "", sep = "+")
                print("", "Booking ID".ljust(11), "Guest Name".ljust(22), "Phone Number".ljust(13), "ID Type".ljust(9), "ID Number".ljust(13),
                      "Hotel ID".ljust(9), "Room Number".ljust(12), "Check In".ljust(11), "Check Out".ljust(11), "Status".ljust(15), "", sep = "|")
                print("", "-"*11, "-"*22, "-"*13, "-"*9, "-"*13, "-"*9, "-"*12, "-"*11, "-"*11, "-"*15, "", sep = "+")
                for i in data1 :
                    print("", str(i[0]).ljust(11), i[1].ljust(22), i[2].ljust(13), i[3].ljust(9), i[4].ljust(13), i[5].ljust(9), i[6].ljust(12),
                          str(i[7]).ljust(11), str(i[8]).ljust(11), i[9].ljust(15), "", sep = "|")
                print("", "-"*11, "-"*22, "-"*13, "-"*9, "-"*13, "-"*9, "-"*12, "-"*11, "-"*11, "-"*15, "", sep = "+")
                print("-"*140)
                ID = input("Booking ID to Cancel\t:\t").strip()
                print("-"*140)
                confirm = input("[WARNING] Are you sure you want to delete the booking (Y/N)\t:\t").strip()
                if confirm.upper() == "Y":
                    query2 = "UPDATE Bookings SET Status = 'Cancelled' WHERE Booking_ID = {};".format(ID)
                    cur.execute(query2)
                    con.commit()
                    print("-"*140)
                    print("[SUCCESS] Booking successfully cancelled".center(140))
                    print("-"*140)
                elif confirm.upper() == "N":
                    print("-"*140)
                    print("[INFO] Cancellation aborted".center(140))
                    print("-"*140)
                else:
                    print("-"*140)
                    print("[INVALID INPUT] Please type 'Y' to confirm or 'N' to cancel".center(140))
                    print("-"*140)

        else:
            print("-"*140)
            print("[ERROR] Invalid selection. Please choose a valid number.".center(140))
            print("-"*140)


    elif choi1 == "4":
        con.close()
        break


    else:
        print("-"*140)
        print("[ERROR] Invalid selection. Please choose a valid number.".center(140))
        print("-"*140)
