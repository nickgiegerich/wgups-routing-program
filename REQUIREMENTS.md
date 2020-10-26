# WGUPS ROUTING PROGRAM

The following is a detailed outline of the rubric requirements for this project

## A: Algorithm Selection

This program utilizes the 2-opt search algorithm to try and find the shortest path between addresses.
The 2-opt algorithm tries to organize a route so that it does not cross over itself, which in turn
can find an optimal path. The 2-opt algorithm runs in O(n^2) similar to the NN algorithm but to me 
it seems like a more elegant solution to this problem. My goal was to keep my runtime around
O(n^2) otherwise I could've chosen 3-opt which runs in O(n^3)

code for my 2-opt is in delivery_process.py @ line 221

## B1: Logic Comments
The following explanation describes the process of how my program solves this problem:

`The Western Governors University Parcel Service (WGUPS) needs to determine the best route and delivery distribution for their Daily Local Deliveries (DLD) because packages are not currently being consistently delivered by their promised deadline. The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to deliver each day; each package has specific criteria and delivery requirements.`

`Your task is to determine the best algorithm, write code, and present a solution where all 40 packages, listed in the attached “WGUPS Package File,” will be delivered on time with the least number of miles added to the combined mileage total of all trucks. The specific delivery locations are shown on the attached “Salt Lake City Downtown Map” and distances to each location are given in the attached “WGUPS Distance Table.”`

`While you work on this assessment, take into consideration the specific delivery time expected for each package and the possibility that the delivery requirements—including the expected delivery time—can be changed by management at any time and at any point along the chosen route. In addition, you should keep in mind that the supervisor should be able to see, at assigned points, the progress of each truck and its packages by any of the variables listed in the “WGUPS Package File,” including what has been delivered and what time the delivery occurred.`

`The intent is to use this solution (program) for this specific location and to use the same program in many cities in each state where WGU has a presence. As such, you will need to include detailed comments, following the industry-standard Python style guide, to make your code easy to read and to justify the decisions you made while writing your program.`

### Solution Explanation

##### Load/store package data given to us in an excel/csv format
- Read the csv file to parse each data row.
- Take those parsed rows and create a package object.
- Store those package objects into a hash table.

##### Load/store distance data given to us in an excel/csv format
- Read the csv file to parse each data row.
- Clean the parsed data so that it is usable.
- Store the data so that it is easily iterable/retrievable.

##### Run the main program that delivers the packages 
- A call to the `deliver_packages()` will instantiate three truck objects, then using the those truck objects
along with package data will sort package objects into truck 1, 2, or 3 based on constraints. 
- While trucks are sorted with packages, address list are created and stored with which addresses will need 
to be visited with a certain truck.
- Once the trucks are loaded with packages and each truck has a list of addresses to visit the list of addresses
are optimized using the distance data loaded earlier.
- To optimize the addresses each list is passed into the `optimize()` function that will look at each address and
iteratively run a 2-opt swap then compare the distance total to the previous version of the route. If the new version 
is shorter that becomes the best route. The 2-opt swap essentially swaps every addresses with every other address until
an optimal route is found.
- Each time a route is 2-opt swapped it is run through the `cost()` function which totals the distance to visit each address
in the given address list starting at index 0.

#### Command Line Interface (CLI)
- The rest of the program utilizes a CLI so that end users can do the following things:
- insert a package into the hash table
- look up a package by id
- look up a package by id and time
- see details of all packages

## B2: Application of Programming Models