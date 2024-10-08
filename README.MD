# FIRECHAT

FIRECHAT is a real-time group chat application built with Django and Firestore. It features a responsive UI using Tailwind CSS & Daisy UI, allowing users to communicate seamlessly while providing a smooth user experience.

## Features

- **Real-time Chatting**: Instant messaging with friends and groups.
- **User Authentication**: Secure login and registration for users.
- **Profile Management**: Update your profile information easily.
- **User Profile Viewing**: View the profiles of available users.
- **Online Status**: Show your online status to other users.
- **Dynamic Online Status Update**: Online status updates are reflected in real-time.
- **Login Streak**: Track your login streak to encourage daily usage.

## Technologies Used

- **Backend**: Django
- **Database**: Firestore
- **Frontend**: Tailwind CSS, DaisyUI, HTML, JavaScript

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Tailwind](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![DaisyUI](https://img.shields.io/badge/daisyUI-1ad1a5?style=for-the-badge&logo=daisyui&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![jQuery](https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white)
![Font Awesome](https://img.shields.io/badge/Font_Awesome-339AF0?style=for-the-badge&logo=fontawesome&logoColor=white)

## Installation

### Prerequisites

- Python 3.x
- Django
- Firebase Account
- Firestore Database

### Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/mohit-trootech/firestore-chatting
   cd firecfirestore-chattinghat
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Firebase**:

```text
   - Set up a Firebase project.
   - Create a Firestore database.
   - Download the service account key JSON file and add it to your project directory.
   - Update your Django settings to include Firebase configuration.
```

5. **Run migrations**:

   ```bash
   python manage.py migrate
   ```

6. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

7. **Access the application**:

   Open your web browser and go to `http://127.0.0.1:8000`.

## Usage

- **Register**: Create a new account using the registration form.
- **Login**: Use your credentials to log in.
- **Chat**: Start chatting in groups and with individual users.
- **Update Profile**: Modify your profile details as needed.
- **Check Online Status**: See who is online and view user profiles.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/MyFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/MyFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

```text
- Django team for creating an amazing framework.
- Firebase for providing real-time database solutions.
- Tailwind CSS for the beautiful and responsive UI.
- Daisy UI Components
```

## Contact

For any questions or issues, please contact:

- **GitHub**: ![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)
