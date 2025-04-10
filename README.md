# Real-time Collaborative Markdown Editor

This repository hosts the code for a real-time collaborative Markdown editor. The application allows multiple users to edit Markdown documents simultaneously, with changes reflected instantly for all connected users.

## Features

### User Authentication and Authorization
- **Account Management**:
    - Create accounts with a username, email, and password.
    - Secure login and logout functionality.
- **Access Control**:
    - Only authenticated users can create and edit documents.
    - Document ownership and sharing:
        - Owners can share documents with specific users.
        - Permissions include:
            - **View**: Users can view the document in real-time.
            - **Edit**: Users can make changes visible to everyone.

### Document Management
- Create and manage Markdown documents.
- Assign titles to documents.
- View a list of:
    - Owned documents.
    - Documents shared with the user.
- Open and edit documents based on permissions.
- Autosave functionality to periodically save changes.

### Real-time Collaborative Editing
- Real-time updates:
    - Changes made by one user are instantly visible to others.
- Basic conflict resolution:
    - Implement "last write wins" or advanced techniques like operational transformation.
- Optional: Display names or avatars of users currently editing the document.

### Markdown Editing and Preview
- Text area for Markdown input and editing.
- Real-time preview of rendered Markdown.
- Support for common Markdown syntax:
    - Headings, lists, bold, italics, links, and code blocks.

### Technology Stack
- **Backend**:
    - Django (web framework, ORM, authentication).
- **Real-time Communication**:
    - Django Channels (WebSockets integration).
- **Database**:
    - PostgreSQL (recommended) or SQLite (for initial development).
- **Frontend**:
    - HTML, CSS, JavaScript.
- **Markdown Rendering**:
    - JavaScript libraries like Marked.js or Showdown.js.

## Getting Started

### Prerequisites
- Python 3.x
- Node.js (for frontend dependencies, if applicable)
- PostgreSQL (or SQLite for development)

### Installation
1. Clone the repository:
     ```bash
     git clone https://github.com/your-username/real-time-markdown-editor.git
     cd real-time-markdown-editor
     ```
2. Set up a virtual environment and install dependencies:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     pip install -r requirements.txt
     ```
3. Configure the database in `settings.py` and apply migrations:
     ```bash
     python manage.py migrate
     ```
4. Start the development server:
     ```bash
     python manage.py runserver
     ```

### Usage
- Access the application at `http://127.0.0.1:8000/`.
- Create an account, log in, and start collaborating on Markdown documents.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
