# Course Management System

This repository contains a simple command-line Course Management System implemented in Python. The system allows users to create, update, delete, search, and print course details. Course data is stored in a binary file using the pickle module.

## Functionality

The Course Management System provides the following functionalities:

1. **Add Course**: Allows users to add a new course by providing the course ID, name, and prerequisite.
2. **Update Course**: Enables users to update the name and prerequisite of an existing course by specifying the course ID.
3. **Delete Course**: Allows users to delete a course from the system by providing the course ID.
4. **Search Course**: Allows users to search for a course by specifying the course ID and displays its details if found.
5. **Print All Courses**: Prints all the courses stored in the system, including their IDs, names, and prerequisites.
6. **Exit**: Terminates the program.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/course-management-system.git
   ```

2. Navigate to the project directory:

   ```bash
   cd course-management-system
   ```

3. Run the Python script:

   ```bash
   python main.py
   ```

4. Choose an action from the menu by entering the corresponding number and follow the instructions provided.

## File Structure

The code is organized as follows:

- `main.py`: The main Python script containing the implementation of the Course Management System.
- `Course.dat`: The binary file where course data is stored using the pickle module.
- `README.md`: This file, providing an overview of the project.

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- The implementation utilizes the pickle module for data serialization and deserialization.
- The system allows users to perform basic CRUD operations on course data.
- The code can be extended and customized for specific requirements.

Enjoy the Course Management System!
