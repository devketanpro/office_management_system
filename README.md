# Office Managament

This system serves as a centralized platform for managing all aspects related to tasks, requests, users, workers, and office locations within an organization or building. It provides functionalities to efficiently handle tasks and requests submitted by users, assign them to available workers, and track their status and priority. Additionally, it facilitates user and worker management, ensuring smooth interaction and coordination among different stakeholders.

## Table of Contents
  - [Project Structure](#project_structure)
  - [Prerequisites](#prerequisites)
  - [Functionality](#functionality)
  - [Installation](#installation)
- [Usage](#usage)
- [Postman Collection](#postman_collection)
- [License](#license)


### Project Structure

The project has the following user types, each with specific permissions:

1. Admin Management: The project includes a admin model (Admin) that extends the built-in Django user model. This model includes fields such as email, phone, first name, last name, and role. It handle all action like User, Worker, Assignment(like change status, manage priority), also assign worker.

2. User Management: The project includes a custom user model (User) that extends the built-in Django user model. This model includes fields such as email, phone, first name, last name, and role. It allows different types of users to access the system with different privileges, including admin, regular users, and workers.

3. Request Management: Users can submit requests (UserRequest) to the system for various purposes such as cleaning, complaints, or problem-solving. Each request has a type, title, preferred timeframe, and is submitted by a user associated with an office location (UserOffice).

4. Assignment Management: Requests submitted by users are assigned (Assignment) to available workers for handling. Assignments track the status, priority, and last update time of each request. Workers are marked as busy when assigned a task to avoid assigning multiple tasks simultaneously.

5. Office Management: The project manages office locations within a building (Office). Each office has attributes such as building name, floor number, and office number. This helps in associating users with specific office locations.

### Prerequisites

List the software and tools that need to be installed before running the project. Provide links to installation instructions if necessary.

- Python: [Installation Guide](https://www.python.org/downloads/)
- Django: [Installation Guide](https://www.djangoproject.com/download/)
- Virtualenv [Installation Guide](pip3 install virtualenv)


### Functionality

   1. `User Management`: Register Users.
   2. `Worker Management`: Register worker and perform related operations.
   3. `Office Management`: Create Office and assign user on request.

   #### User Types and Permissions

   - `Admin`: Full access to all functionalities
   - `User`: SignUp yourself and manage own offices and raise request for own ofiice.
   - `Worker`: Take care of assign Assignment bassed on user request.


### Installation

1. Clone this repository:

   ```bash
   git clone  https://github.com/devketanpro/office_management_system.git
   ```

2. Checkout in to the branch:

   ```bash
   git checkout main
   ```

3. create virtual environment to install requierment:

   ```bash
   virtualenv venv
   ```
4. Activate created virtual environment:

   ```bash
   source venv/bin/activate
   ```

5. Install requierment for this project:

   ```bash
   pip install -r requierment.txt
   ```

6. Start server:

   ```bash
   python manage.py runserver
   ```

### Usage

1. Start the development server:

   ```bash
   python manage.py runserver
   ```

2. Access the application at 
   `http://localhost:8000/`

3. Get the api user signup at 
   `http://localhost:8000/sign-up/`

4. Get the api user login at 
   `http://localhost:8000/api/token/`

5. Use this User API (`http://localhost:8000/users/`) to perform users   related action with admin permission.

6. Use this workers API (`http://localhost:8000/workers/`) to perform worker related action with admin permission.

7. Use this workers API (`http://localhost:8000/workers/`) to perform worker related action with admin permission.

8. Use this office API (`http://localhost:8000/offices/`) to perform office related action with admin permission.

9. Use this user-office API (`http://localhost:8000/user-office/`) to perform user office related action with admin permission to assign office to selected user.

10. Use this user-office API (`http://localhost:8000/user-office-list/`) to get user office data. if user is normal user then it will list out their offices or if user is admin then it will list all user's offices.

11. Use this raise-request API (`http://localhost:8000/raise-request/`) to raise a request for own office. only user can access this api to raise request.

12. Use this track-request api (`http://localhost:8000/track-request/`) to track own requested. here if admin call this api then it will see all requestes with their progress but if user call this api then return the list of currently requested user offices and if worker call this aoi then it will see only those request which is part of in it.

13. This api (`http://localhost:8000/manage-assignment/<str:pk>/`) is basically for Admin to manae Assignment bassed on user request,  it take assignment_id and manage this like change priority, manage status, assign worker.

## Postman Collection
Here we find postman collection [Postman Collection](./Office%20Management.postman_collection.json)
## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the [LICENSE.md](LICENSE.md) file for details.
