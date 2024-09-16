[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/AHFn7Vbn)
# Superjoin Hiring Assignment

### Welcome to Superjoin's hiring assignment! 🚀

### Objective
Build a solution that enables real-time synchronization of data between a Google Sheet and a specified database (e.g., MySQL, PostgreSQL). The solution should detect changes in the Google Sheet and update the database accordingly, and vice versa.

### Problem Statement
Many businesses use Google Sheets for collaborative data management and databases for more robust and scalable data storage. However, keeping the data synchronised between Google Sheets and databases is often a manual and error-prone process. Your task is to develop a solution that automates this synchronisation, ensuring that changes in one are reflected in the other in real-time.

### Requirements:
1. Real-time Synchronisation
  - Implement a system that detects changes in Google Sheets and updates the database accordingly.
   - Similarly, detect changes in the database and update the Google Sheet.
  2.	CRUD Operations
   - Ensure the system supports Create, Read, Update, and Delete operations for both Google Sheets and the database.
   - Maintain data consistency across both platforms.
   
### Optional Challenges (This is not mandatory):
1. Conflict Handling
- Develop a strategy to handle conflicts that may arise when changes are made simultaneously in both Google Sheets and the database.
- Provide options for conflict resolution (e.g., last write wins, user-defined rules).
    
2. Scalability: 	
- Ensure the solution can handle large datasets and high-frequency updates without performance degradation.
- Optimize for scalability and efficiency.

## Submission ⏰
The timeline for this submission is: **Next 2 days**

Some things you might want to take care of:
- Make use of git and commit your steps!
- Use good coding practices.
- Write beautiful and readable code. Well-written code is nothing less than a work of art.
- Use semantic variable naming.
- Your code should be organized well in files and folders which is easy to figure out.
- If there is something happening in your code that is not very intuitive, add some comments.
- Add to this README at the bottom explaining your approach (brownie points 😋)
- Use ChatGPT4o/o1/Github Co-pilot, anything that accelerates how you work 💪🏽. 

Make sure you finish the assignment a little earlier than this so you have time to make any final changes.

Once you're done, make sure you **record a video** showing your project working. The video should **NOT** be longer than 120 seconds. While you record the video, tell us about your biggest blocker, and how you overcame it! Don't be shy, talk us through, we'd love that.

We have a checklist at the bottom of this README file, which you should update as your progress with your assignment. It will help us evaluate your project.

- [✔️] My code's working just fine! 🥳
- [✔️] I have recorded a video showing it working and embedded it in the README ▶️
- [✔️] I have tested all the normal working cases 😎
- [✔️] I have even solved some edge cases (brownie points) 💪
- [✔️] I added my very planned-out approach to the problem at the end of this README 📜

## Got Questions❓
Feel free to check the discussions tab, you might get some help there. Check out that tab before reaching out to us. Also, did you know, the internet is a great place to explore? 😛

We're available at techhiring@superjoin.ai for all queries. 

All the best ✨.

## Developer's Section
https://drive.google.com/file/d/1-GdwAA7XKOdpx5xQKU944Tl_7NKkZjWD/view?usp=sharing
Here is the google drive link to my demonstration.

### Due to some MacBook issues and a test, I was unable to submit it within the 6:30pm deadline, but I would really appreciate it if you still considered my solution and gave me feedback for it. Thank you :)

Here is the process breakdown -

Once I received the assignment, I spent few hours researching about how I would go about this, based on the resources available, my current knowledge about APIs, and the time I was alloted. Accordingly, I came up with the below solution.
Why Python Over Node.js
I chose either Python or Node.js. After a short consideration, I decided to go with Python. I was more familiar with it, but I thought Python syntaxes are simple enough, and I've already used some things related to the web, particularly ones involving APIs and databases. Another reason why I chose Python is because of its libraries: googleapiclient for managing Google Sheets and mysql.connector for interacting with MySQL databases. I knew that this would make it easy for me to implement the logic of the project.

Setting Up Google Sheets and API Access
Having decided on using Python, the next step would be to set up the Google Sheets API. To accomplish this, I created a Google Sheet where the data was going to be stored and updated. Subsequent to creating the sheet, I had to enable the Google Sheets API from the Google Cloud Console. Without enabling the API, my Python script wouldn't communicate with Google Sheets.

I had downloaded the credentials.json file. The file is crucial because it contains the service account email, private key, and the project ID. I kept the file safe since it contains private information that cannot be shared around.

Reading and Writing Data to Google Sheets
With the Google Sheets API in place, I wrote Python functions for reading data and writing data to the sheet. Using the googleapiclient.discovery library, I wrote a function to extract data from a specific range in my Google Sheet. I also wrote a function that would update the sheet with an update being passed in. From here I tested my functions and was indeed able to make changes directly in the Google Sheet using Python.

Configuring MySQL Database
The MySQL database had to store the same data. It was created as simple as possible with columns matching the ones in my Google Sheet: ID, Name, Email, Age, etc. The mysql.connector Python library was used to connect to this database. With the library, I can run queries from Python to insert, fetch, update, or delete data in the MySQL database.

Syncing Data From Google Sheets to MySQL
Having set up both Google Sheets and MySQL, I then synced the data from both ends. For this purpose, I wrote a Python script - sync.py- which, essentially, does the following:
Fetch data from Google Sheets and insert it into MySQL
Fetch data from MySQL and update Google Sheets.
For syncing from Google Sheets to MySQL, I used the data that I fetched from the sheet and inserted that in MySQL. In return, for syncing from MySQL to Google Sheets, I formatted the data from the database and updated the sheet with new values.

Use of Flask for API End
I decided to begin with a Flask app so that the process of synchronization becomes available as a service. Flask is the Python web framework that is light-weight; therefore, I can define the API endpoints on it. Using these endpoints as /sync_sheet_to_db and /sync_db_to_sheet, which, when called, will trigger the process in both ways, i.e. either Google Sheets to MySQL or MySQL to Google Sheets respectively.

Why I chose Polling to mimic real time synchronization:
First, I wanted the sync to happen in real-time. Through all of the research, I discovered webhooks and polling. Webhooks are more efficient, as instant communication between Google Sheets and the database could be achieved. However, it required a more complex setup and some external hosting.

Instead, I used polling, which is a much easier way of doing this task. In polling my program periodically checks for changes in the Google Sheet and then updates the database. This method is not instantaneous but easier to implement as it was better suited for my needs at that particular time. I set up a loop in my script which scans for changes at regular intervals.

Conclusion
The system being completed of synchronizing data between Google Sheets and a MySQL database is fully functional at the end of this project. While the original goal was to real-time sync, for simplicity, this project implemented the polling method. With the time alloted whilst tackling my internship and college work, I am happy with the solution built for this. 
