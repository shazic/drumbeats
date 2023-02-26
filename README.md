# Kanban board API

## Overview

This repository is an attempt to simplify the agile story board and keep the bare minimum for tracking stories in an agile board.

### Features

1. __User management__: The application should allow administrators to create and manage users, including adding new users, deleting existing users, and modifying user information.

1. __Project management__: Each card should be associated with a specific project. Users should be able to create, modify, and delete projects, as well as view a list of existing projects.

1. __Role-based access control__: The application should define different roles for users, such as administrator, project manager, and team member. Each role should have a set of permissions that define what actions the user is allowed to perform, such as creating swim lanes, viewing cards, or moving cards to different swim lanes. The application should enforce these permissions and prevent unauthorized access to resources based on the user's role.

1. __Card management__: Users should be able to create, modify, and delete cards within a project. Cards should have standard fields like story description, story points, etc. and should be associated with a specific swim lane within the project.

1. __Swim lane management__: Users should be able to create, modify, and delete swim lanes within a project.

1. __Filtering and sorting__: Users should be able to filter and sort cards based on different criteria, such as swim lane, status, or story points, within a project.

1. __Authorization and authentication__: The API should be secured with an authentication mechanism that allows only authorized users to access the endpoints.

1. __Error handling__: The API should handle errors gracefully and provide informative error messages to users in case of failures.

1. The project does not cover UI implementation

### Usage
