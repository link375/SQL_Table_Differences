import db
import csv
import functions as utilities
import sqlQueries as Query

# convert tuples to lists so they can be modified
firstDB_list = list(Query.results_firstDB)
secondDB_list = list(Query.results_secondDB)

# create a list of items without and index
# we will use this to compare each row to all items
secondDB_items = utilities.extract_items(secondDB_list)

# find all unique users
uniqueUsersList = utilities.find_unique_users(firstDB_list, secondDB_items)

# remove joomla 2.5 headings and insert joomla 3.5 headings and values
final = utilities.create_final(uniqueUsersList)

headings = "name", "username", "email", "password", "block", "sendEmail", \
           "registerDate", "lastvisitDate", "activation", "params", "lastResetTime", \
           "resetCount", "otpKey", "otep", "requireReset"

#########TESTING#######
# insert the final list to the database
db.test_c.executemany(Query.insert_row, final)
db.testDB.commit()
db.testDB.close()

# create a csv file and write final list to it
with open("users.csv", "w") as csvfile:
    csv_writer = csv.writer(csvfile)

    # write the headings to the csv file based on the new database
    csv_writer.writerow(headings)

    # write the headings to the csv file based on the joomla 3.5 users headings
    #csv_writer.writerow([i[0] for i in db.secondDB_c.description])

    # write the final rows
    csv_writer.writerows(final)

