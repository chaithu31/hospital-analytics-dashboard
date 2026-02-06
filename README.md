Resource Utilization • Capacity Planning • Operational Intelligence

Overview

Hospitals generate large volumes of operational data, but decision-makers often lack clear, real-time visibility into patient flow, resource utilization, and department workload. This leads to overcrowding, delayed discharges, inefficient staffing, and poor capacity planning.

This project presents an interactive Hospital Operations Analytics Dashboard that enables hospital administrators to monitor performance, identify bottlenecks, and optimize resource utilization across departments in a mid-sized multi-specialty hospital network.

The system transforms raw operational data into actionable insights using standardized healthcare metrics and simple visualizations that are interpretable by non-technical staff.

Problem Statement

Hospital operations teams require real-time analytics to:

Monitor patient admissions and discharge flow

Track bed occupancy and resource utilization

Identify operational bottlenecks and peak workload periods

Balance doctor workload and staffing requirements

Compare department performance and patient outcomes

Support short-term operational decisions and long-term capacity planning

Traditional reporting systems are static, delayed, and difficult to interpret. This solution provides an interactive, data-driven analytics platform.

Solution

The system integrates a PostgreSQL data warehouse, a FastAPI backend, and a Power BI interactive dashboard to deliver real-time operational analytics.

It provides:

Real-time KPI monitoring

Interactive drill-down by department, case type, and patient demographics

Bottleneck detection and workload analysis

Trend visualization for capacity planning

Operational insights for resource optimization

Key Features
Core KPIs

Total Admissions

Emergency Case Percentage

Average Length of Stay (ALOS)

Department Workload

Doctor Case Load (Utilization Proxy)

Patient Outcome Distribution

Cost per Patient (based on billing data)

Analytics Capabilities

Trend analysis (daily / monthly)

Cross-department comparison

Emergency vs scheduled workload monitoring

Interactive filtering and drill-down

Bottleneck identification

Operational performance monitoring

Dashboard Insights

The dashboard provides:

Admissions trend to identify peak demand periods

Department workload distribution for staffing optimization

Emergency pressure monitoring

Doctor workload visualization

Filter-based exploration of patient flow and operational efficiency

These insights help administrators improve resource allocation, reduce operational delays, and enhance decision-making.

Technology Stack

Backend

Python 3.12

FastAPI

SQLAlchemy

Database

PostgreSQL (on-premise)

Analytics & Visualization

Power BI Desktop

Data Processing

ETL scripts for hospital operational data

System Architecture

PostgreSQL Database → FastAPI Backend → Power BI Dashboard

PostgreSQL stores operational hospital data

FastAPI handles data processing and KPI computation

Power BI provides interactive visualization and analytics

Data Model

The system uses a healthcare star-schema style structure:

Admissions (Fact Table)

Patients (Dimension)

Departments (Dimension)

Doctors (Dimension)

This enables efficient KPI computation and cross-department analysis.

Use Cases

This platform helps hospital operations teams:

Monitor patient flow in real time

Detect department overload and operational bottlenecks

Improve staffing decisions

Optimize resource utilization

Support capacity planning

Improve operational efficiency

Future Enhancements

Bed occupancy analytics

Predictive resource demand forecasting

Readmission rate tracking

Multi-hospital branch comparison

Automated monthly performance reports

Real-time alert system for operational bottlenecks

Demo

A live demonstration video shows:

Dashboard overview

Interactive drill-down

KPI monitoring

Operational insights

(See submission video link)

Conclusion

This project demonstrates how hospital operations can be transformed using data-driven analytics. By converting raw operational data into actionable insights, the platform enables smarter decision-making, improved resource utilization, and more efficient healthcare operation

![Power BI Dashboard](powerbi.jpeg)
