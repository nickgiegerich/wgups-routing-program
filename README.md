# Data Structures and Algorithms II – C950
## WGUPS Routing Program
This is a project specified by WGU to solve a package delivery routing problem,
which is essentially the TSP problem. For my solution I implemented the 2-opt 
algorithm, which is a known solution to the TSP that runs in `O(n^2)`.
## Usage
To get the code run this from the command line: 
```commandline
git clone https://github.com/nickgiegerich/wgups-routing-program.git
```

Once that is done, in the main directory where `main.py` is located run:
```commandline
python3 main.py
```

depending on python version^^^

From there you should see the Command Line Interface like this:
```commandline
***********************************************
* WELCOME TO THE WGUPS COMMAND LINE INTERFACE *
***********************************************


Delivery Details
--------------
Truck 1 Delivered all its packages in 27.8 miles
T1 left the HUB at: 08:00:00
T1 returned to the HUB at: 09:32:40 

--------------
Truck 2 Delivered all its packages in 35.400000000000006 miles
T2 left the HUB at: 09:05:00
T2 returned to the HUB at: 11:03:00 

--------------
Truck 3 Delivered all its packages in 22.5 miles
T3 left the HUB at: 10:30:00
T3 returned to the HUB at: 11:45:00 

--------------------------
TOTAL TRUCK MILEAGE: 85.7
--------------------------

*********************** COMMANDS ***********************

 - to insert a package into the table type [a]dd
 - for package inquiry type [i]nquiry
 - to see package details at a specific time type [t]ime
 - to print details of all packages type [d]etails

!!!! To exit or quit the program type [q]uit !!!!

*********************** END COMMANDS ***********************
Enter command here (to see all commands type [h]elp):
```

