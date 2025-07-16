
# Load Balacing

Below are some of the load balancing algorithms we'll discuss:

### Round Robin
Distributes incoming requests to servers in a cyclic order. It assigns the first request to the first server, the second to the second server, and so on. Handling sessions can be challeging with this method since each request may go to a differest server. It's also less effective when servers have different capacities.

### Least Connections
Distributes requests based on the number of active connections each server has. This leads to better resource utilization but can struggle during connection spikes, especially when connection duration are short, causing frequent rebalancing.

### Weighted Round Robin
Similar to Round Robin, but each server is assigned a weight based on its capacity or performance. More powerful servers receive a larger share of the load.

### Weighted Least Connections
Combines Weighted Round Robin and Least Connections. Each server has a weight, and requests are distributed considering both the number of active connections and the server's capacity. This allows more powerful servers to handle more concurrent sessions.

### IP Hash
Assigns client requests to servers based on the client's IP address. This ensures that the same client is consistencly routed to the same server, which is helpful for maintaining session persistence.

### Least Response Time
Routes requests to the server with the lowest recent response time. This helps ensure efficient use of resources and is ideal for services that require low latency.

### Random
Distributes requests to servers randomly. It's simple to implment, but can result in load imbalance, with some servers handling more requests than others.


