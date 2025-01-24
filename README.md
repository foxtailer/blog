# Blog  

A simple blog platform where users can create folders with Markdown files to generate HTML pages based on 
templates dynamically. In order to understand Django more clearly, the goal of this project is to write 
some functionality that Django provides as a framework, without using Django itself.

## Features

- **Markdown-Based Content:**
  - Users organize blog posts as text files with Markdown syntax.
- **Automatic HTML Generation:**
  - Converts Markdown files into styled HTML pages using predefined templates.
- **Folder Organization:**
  - Each folder corresponds to a post of the blog.
- **Deployment:**
  - Powered by a WSGI Python application as backend part.
  - Uses Nginx as a reverse proxy and Gunicorn as the application server.

