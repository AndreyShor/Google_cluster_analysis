# Google Cluster Analysis

This project analyzes logs from Google's production clusters using big data tools (Hadoop, Hive) and Python for statistical analysis and visualization.

---

## Project Overview

We designed and implemented a data pipeline that includes:

- **Data Collection** from Google cluster trace logs (CSV format).
- **Data Storage** using Hadoop Distributed File System (HDFS).
- **Data Management** through Hive (SQL-like querying).
- **Data Processing** with MapReduce and HiveSQL.
- **Data Analysis and Visualization** with Python libraries.

The goal was to understand resource utilization, job/task behaviors, and system reliability in Google's large-scale computing environment.

---

## System Functional Design

The system consists of the following modules:

1. **Data Ingestion Module**: Collects raw data into HDFS.
2. **Data Storage Module**: Manages scalable data storage.
3. **Data Management Module**: Provides query capabilities via Hive.
4. **Data Processing Module**: Performs computation and data transformation.
5. **Data Analytics Module**: Conducts analysis and visualization using Python.


## Data Pipeline Overview

| Stage                  | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| **Collection**          | Collect CSV logs.                                                          |
| **Labeling & Combination** | Combine and structure logs.                                               |
| **Preprocessing**       | Remove outliers, handle missing values, normalize data.                    |
| **Analysis**            | Perform statistical analysis and clustering.                              |
| **Visualization**       | Create visual insights using Python (matplotlib, seaborn, etc.).           |

---

## Database Design

- **ER Diagram**:
  - **Machine Events**: Machine availability/configuration changes.
  - **Job Events**: Job lifecycle events (submission, scheduling, completion).
  - **Task Events**: Execution details of tasks.
  - **Task Resource Usage**: CPU and memory metrics during task execution.

- **Relationships**:
  - Task Events link to both Job Events and Machine Events.
  - Task Resource Usage links to both Task Events and Machine Events.

- **Key Focus**:
  - Proper primary/foreign keys to ensure efficient joins.
  - Unique indexing for consistency and performance.

---

## Preprocessing Steps

1. **Outlier Detection and Removal**: Used IQR method.
2. **String Hashing**: Label encoding for string identifiers.
3. **Scientific Notation Handling**: Limited to 6 decimal places for efficiency.
4. **ProcessID Creation**: Unique task identifier combining multiple fields.
5. **Automated SQL Script Writing**: For Hive ingestion.

---

## Data Analysis & Visualizations

- **Daily Active Users and Job Counts**: Tracked platform activity.
- **Average Tasks per Job by Priority**: Observed resource allocation by job importance.
- **Task Success vs Failure Rates**: Evaluated overall system reliability.
- **Task Duration Distributions**: Identified performance bottlenecks.
- **User Submission Behavior**: Found non-normal patterns in job submissions.
- **CPU Requested vs Actual Usage Clustering**: Found inefficiencies.
- **Machine Event Type Distribution**: Highlighted common operational events.
- **Heatmap of CPU Utilization**: Identified overused and underused machines.

---

## Limitations and Future Work

- **Partial Data**:
  - Analysis conducted on a subset due to size constraints.
- **Environment Constraints**:
  - Full-scale Hive analysis planned but delayed due to infrastructure issues.
- **Future Improvements**:
  - Finish full dataset analysis.
  - Implement Hive partitioning and bucketing for better performance.

---

## Authors

- Andrejs Sorstkins
- Yuzhi Chen
- Zhengyi Xu
- Zhen Lei

---

## Acknowledgements

- University SCC.411 Big Data course
- Google Cluster Data project

---