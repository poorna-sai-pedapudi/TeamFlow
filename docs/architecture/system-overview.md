# TeamFlow System Overview

## 1. What problem does TeamFlow solve?

TeamFlow helps teams manage engineering and product work in one place. It allows organizations to create projects, break work into tasks, assign ownership, track progress, collaborate through comments, and maintain visibility across teams. Without a system like this, work can become scattered across messages, spreadsheets, meetings, and disconnected tools, making it hard to know who owns what and what is blocked.

---

## 2. Who are the users?

Primary users:
- Organization owner / admin
- Engineering manager
- Product manager
- Developer / engineer
- QA engineer
- Viewer / stakeholder

---

## 3. User Journey

A company signs up for TeamFlow.
The first user creates an Organization.
The Organization owner invites team members.
Admins create Projects.
Project members create Tasks.
Tasks are assigned to engineers.
Engineers update task status and add comments.
Managers review progress through dashboards.
System records important actions in audit logs.
Users receive notifications when tasks are assigned or updated.

---

## 4. Should companies see each other's data?

No, one company should never see another company’s data. Google employees should not see Microsoft’s projects because each organization’s data must be isolated. This is called multi-tenancy. In the database, most business records should include an organization_id so queries can safely filter data by organization.

This means every API request must be checked against the user's organization membership before returning or modifying data.
---

## 5. Core Entities

- Organization
- User
- OrganizationMember
- Project
- Task
- Comment
- TaskStatus
- TaskPriority
- Notification
- AuditLog
- Invitation

---

## 6. Initial Domain Model

Organization
- Owns projects
- Has many members
- Has many invitations
- Has many audit logs

User
- Can belong to multiple organizations
- Can create tasks
- Can be assigned tasks
- Can comment on tasks

OrganizationMember
- Connects users to organizations
- Stores the user role inside that organization

Project
- Belongs to one organization
- Has many tasks
- Has many members

Task
- Belongs to one project
- Has one reporter
- May have one assignee
- Has many comments
- Has a status and priority

Comment
- Belongs to one task
- Created by one user

Notification
- Belongs to one user
- Created when important events happen

AuditLog
- Belongs to one organization
- Records important actions


## 7. Why OrganizationMember?

We need OrganizationMember because the relationship between users and organizations is many-to-many. A user can belong to multiple organizations, and an organization can have multiple users. If we store organization_id directly on the User table, each user can belong to only one organization. OrganizationMember acts as a join table and also lets us store organization-specific fields like role, joined_at, status, and permissions.


---

## 8. Relationship Diagram

User
  |
  | many-to-many
  |
OrganizationMember
  |
  | many-to-one
  |
Organization
  |
  | one-to-many
  |
Project
  |
  | one-to-many
  |
Task
  |
  | one-to-many
  |
Comment


## 9. Entity Relationship Summary

- One Organization has many OrganizationMembers.
- One User has many OrganizationMemberships.
- One Organization has many Projects.
- One Project has many Tasks.
- One Task has many Comments.
- One User can create many Tasks.
- One User can be assigned many Tasks.
- One User can create many Comments.
- One Organization has many AuditLogs.
- One User has many Notifications.


- If a user tries to access /projects/10, what should the backend check before returning that project?
  
The backend should not return the project immediately.

It should first identify which Organization owns Project 10.

Then it should verify that the authenticated user has an active OrganizationMember record for that Organization.

Only if the membership exists (and the user's role has permission to view the project) should the backend return the project.

Otherwise, it should return 403 Forbidden (or 404 Not Found, depending on the application's security strategy).