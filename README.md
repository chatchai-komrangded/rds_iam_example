# rds_iam_example on RDS MySQL with MySQL cli, and Python code

MySQL, PostgreSQL RDS Support IAM database authentication and/or native database authentication Mechanisms

This is example how to use RDS with AWS IAM Authentication, There are consideration as below:

- Authentication tokens are used to validate the user.
- Tokens have a lifetime of 15 minutes
- Connections per second are limited by the instance type of the database.
- IAM auth maps DB user to IAM user or role.

MySQL authentication can be managed externally using IAM
Authentication tokens are used to validate the user
Tokens have a lifetime of 15 minutes
Connections per second are limited by the instance type of the database
IAM auth maps DB user to IAM user or role
IAM auth. limited to ~200 auth. requests/sec

MySQL RDS Supports two types of authentication Mechanisms
Native MySQL credentials
IAM authentication
MySQL 5.6, minor version 5.6.34 or higher.
MySQL 5.7, minor version 5.7.16 or higher.
MySQL 8.0, minor version 8.0.16 or higher.
Active Directory
MySQL version 8.0.13, 8.0.15, and 8.0.16
MySQL version 5.7.24, 5.7.25, and 5.7.26
Uses AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD) as the authentication source
The client must be part of the AWS Managed Microsoft AD domain
Integrated with AWS Secrets Manager for credential management and rotation of native credentials