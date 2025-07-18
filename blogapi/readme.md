# Blog API

A simple RESTful API for managing blog posts
## Features

- Create, read, update, and delete blog posts
- User authentication (JWT)
- Commenting system
- Pagination and filtering
- Error handling

## Technologies Used


- JWT for authentication


### Authentication

- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login and receive a token

### Blog Posts

- `GET /api/posts` - Get all posts (supports pagination)
- `GET /api/posts/:id` - Get a single post
- `POST /api/posts` - Create a new post (authenticated)
- `PUT /api/posts/:id` - Update a post (authenticated)
- `DELETE /api/posts/:id` - Delete a post (authenticated)

### Comments

- `POST /api/posts/:id/comments` - Add a comment to a post
- `GET /api/posts/:id/comments` - Get 



