# Data Discovery in a DDoS Data Mesh Network
Distributed Denial-of-Service (DDoS) attacks have been a persistent and challenging issue on the Internet, leading to numerous proposals for countering these attacks from both centralized and distributed (cooperative) perspectives. One promising approach is the adoption of cooperative defense strategies. These can offer various benefits such as reducing the burden on individual domains, enhancing detection and mitigation capabilities and blocking malicious traffic closer to its source. However, implementing a cooperative defense in the highly diverse Internet environment is a complex task. The environment is extremely heterogeneous and encompasses diverse technologies, organizational structures and legal frameworks that pose their respecting set of challenges.

This repository aims to complement the work done as part of my bachelor thesis. It contains files necessary to replicate the design and implementation proposed in the thesis. 

## What is a DDoS Data Mesh Network?
A DDoS data mesh network describes a collaborative DDoS defense architecture. In a data mesh architecture, decentralized and autonomous domain teams hold data in local repositories. In the case of the ddos data mesh network, that data consists of DDoS attack data. A data mesh network then allows the domain teams to query and exchange the data held by other domain teams. In the specific use case of a DDoS attack, this allows you to get an overview of the attack by combining the decentralized data stored at the domain teams. Data mesh networks, therefore, offer a decentralized approach to managing data inside an organization. Further, data mesh networks promote distributed architectures and domain-driven ownership of the data. Check out the official [data mesh architecture](https://www.datamesh-architecture.com/#why) website for more information.

## How does it work?
The idea behind this architecture is to run three core components on every domain team of the data mesh:
- Data Storage
- A Data Exchange Interface
- A Data Discovery Service

The DDoS attack data of every domain team is stored inside the data storage component. A data exchange interface allows other domain teams to query and join that data with the DDoS attack data from other domain teams. The data discovery service finally allows for visualization and BI based on the data retrieved. The below visualization depicts a DDoS data mesh architecture with three domain teams. Each domain team runs the three core components:
<p align="center">
<img src="assets/ddos_data_mesh_design.png" alt="ddos_data_mesh_design" width="500", height="600"/>
</p>

## Implementation
In the thesis, we doployed the data mesh with three VMs acting as the domain teams. Each of the VMs implemented and deployed the three core services described above. For the implementation of the services, we use the following tools:
- [MySQL](https://dev.mysql.com/doc/)
- [Trino](https://trino.io/docs/current/)
- [Apache Superset](https://superset.apache.org/docs/intro/)

On each domain team, we run MySQL instances to store the DDoS attack data. We use Trino as a distributed query engine that is able to query multiple, heterogenous, data sources simultaniously. This allows us to query DDoS attack data from multiple domain teams (data sources / MySQL instances) in a single SQL statement. Finally, we use Apache Superset as a data discovery and BI tool. We can run queries against the data mesh from inside Superset and directly use the data retrieved to create visualizations.

Trino is deployed as a cluster. The cluster consists of at least one coordinator node and one or multiple worker nodes. Queries are sent to the coordinator node which analyzes and optimizes the query. The coordinator node then distributes the query across the available worker nodes. The worker nodes retrieve the data from the data sources and perform the computation of the query. The resulting data is then returned to the coordinator node, which returns the result to the client that submitted the query. In the design and implementation proposed in the thesis, we run one Trino coordinator node and two Trino worker nodes. The below figure depicts the topology of the data mesh: 
<p align="center">
<img src="assets/ddos_data_mesh_impl.png" alt="ddos_data_mesh_impl" width="700", height="600"/>
</p>

## Deployment
This section explains how to install, configure and run the tools necessary for the DDoS Data Mesh Architecture. Note that this is the set up for a single domain team. You can replicate this process on every domain team that is part of the collaborative defense to create your own DDoS Data Mesh Network. 

### 1. Prepare the Data
Explain that we are working with samle data generated and located in forlder...
Maybe cut, or distribute or only use a part of the prints in the table...

### 2. Setting up MySQL
Install MySQL
Set up MySQL schemas and Tables and users -> init.sql?
Feed prints into MySQL with script
Check if prints are in MySQL correctly...
Check if MySQL is available on port... and with user ...

### 3. Setting up Trino
Explain that we run Trino in a container -> Docker is a requirement
Explain the folder with the configs -> Give explanation for each config file in bullet point style
That folder/config is mounted into the container
Explain how to run it -> Docker run ...

### 4. Setting up Superset
We run with docker as well -> docker compose is a requirement
cd into dir
make changes for Trino Dirver
then just do docker compose
then configure DB connection to use Trino coord. node in Superset webapp settings. 

## Data Discovery
Once the hardware is running, you can query the mesh from Superset. Here is a video that shows this:
Video...

