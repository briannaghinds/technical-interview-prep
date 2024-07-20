## Depth First Search
Simply put, a depth-first graph search continues down a path until it reaches the end. It is helpful for determining if a path exists between two vertices. DFS has many applications, including topological sorting and detecting cycles, but one of the more interesting real-world applications is that it can be used to solve problems that have a singular correct answer (a path between the start state and end state), such as a sudoku exercise.
## Breadth First Search
On the other hand, a breadth-first graph search approach checks the values of all neighboring vertices before moving into another level of depth. This is an incredibly inefficient way to find just any path between two vertices, but it’s an excellent way to identify the shortest path between them. Because of this, BFS is helpful for figuring out directions from one place to another.

## Graph Traversal Order
What if we don't need to find a path but instead just get a list of all the values in the graph? We can do this with graph traversal. There are 3 types:

(1) Preorder: each vertex is added to a "visited" list and added to the output list BEFORE getting added to the stack

(2) Postorder: each vertex is added to the "visited" list and added to the output lits AFTER being popped off the stack

(3) Reverse Postorder: (Topological Sort) returns an output list that is exactly the reverse of the post-order list
## Dijkstra's Algorithm
Dijkstra’s algorithm is a method for finding the shortest distance from a given point to every other point in a weighted graph. The algorithm works by keeping track of all the distances and updating the distances as it conducts a breadth-first search. A common application of this algorithm is to find the quickest route from one destination to another.

**Dijkstra’s Algorithm works as following (breadth):**

(1) Instantiate a dictionary that will eventually map vertices 
to their distance from the start vertex

(2) Assign the start vertex a distance of 0 in a min heap

(3) Assign every other vertex a distance of infinity in a min heap because we don't know the distances yet

(4) Remove the vertex with the smallest distance from the min heap and set that to the current vertex

(5) For the current vertex, consider all of its adjacent vertices and calculate the distance to them as (distance to the current vertex) + (edge weight of current vertex to adjacent vertex).

(6) If this new distance is less than the current distance, replace the current distance.

(7) Repeat 4 and 5 until the heap is empty

(8) After the heap is empty, return the distances

TIME COMPLEXITY: O((V+E)log V) -> in worst case we will visit all V+E vertices and edges, in each visit we may have to update our min-heap which takes log V time

## A* Search
As opposed to Dijkstra’s which finds the shortest path from any point to any other point, A* is used to find the shortest path from one specific point to another specific point in the Graph. This allows us to avoid searching for any other connecting paths, saving a lot of time in the process!