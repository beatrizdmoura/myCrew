# myCrew Code Challenge - Edition User Service

## Deliverable

Necessary a docker-compose file.

## Questions to be answered

- Instead of JSON Web Tokens, would you rather use a different approach for authentication and why?

Being super easy to use and implement JSON Web Tokens and being more familiar with this approach than others, I wouldn’t rather use a different approach unless this approach didn’t make sense in the context in which the API will be used.

- Why did you choose that specific data store and what are the advantages or disadvantages over other alternative technologies?

Taking advantage of Docker to facilitate the setup of the API, I chose to store the users profile data in a postgres database using a Docker service linked to the service running the API. This way it’s easier to setup the API without needing a different setup for the database, it’s easier to update both, and if we need to add another service using the same api we just have to say that it depends on the db service.

- How do you make sure the API is compatible with mobile clients out there if future changes change the interfaces?

The first thing that comes to my mind is versioning the API, adding the version prefix to all requests and keeping legacy versions of the API running when a new version is launched.
This makes sure the API is compatible with mobile clients out there if future changes change the interface but still it’s always best to prevent or to keep to a minimum breaking changes through the development of the API.

- Why did you chose to implement the profile picture storage the way you did it?

I chose to implement the profile picture storage using Amazon S3 because that way the files are safely kept but still easily accessible without taking space on the server.

## Notes on the Task

- Login existing users

Login by username - necessary to change the login to allow using the email instead

- Reset password (this is an optional task)

To add the functionality of resetting the password sending an email with a code to reset the password, I would add Celery to the Django application using Redis as the message broker. To create the emails I would have used the post_office package, and to actually send them I would have created a celery task to send the emails in queue.
