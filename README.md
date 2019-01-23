# myCrew Code Challenge - Edition User Service

## Intro

This code challenge is a part of the myCrew tech recruitment process. It is intended to give our tech team an insight about your skill set in solving a complex tech problem. Candidates usually finish the task in about 3-4 hours. However, this is just a guideline. If the task takes you more or less than 4 hours, it does not have any implications on your performance evaluation.

## Task

Please implement a simple API representing an user service using a language of your choice. Upon successful signup or authentication, the service should provide the client with a JSON Web Token that the client sends along in the HTTP Header to access authenticated resources. The API shall have the following views / functionality:

- Signup a new user and create a profile with

  - Username

  - Password

  - Email address

  - First and last name

  - Gender

  - Profile Picture

- Login existing users

  - Using username or email

  - Using the password

- Return the users profile (authenticated)

  - Return username, firstname, lastname, email, gender and URL to download a profile picture

- List all registered user IDs and count male / female

  - Returns a JSON in the following structure e.g.

  ```json
  {
    "user_ids": [1, 2, 3, 4],
    "count_female": 3,
    "count_male": 1,
    "count_unspecified": 0
  }
  ```

- Reset password (this is an optional task)

  - Send an email with a code to reset the password

Please store the user profile in a database. Please choos an appropriate data store for it. Please implement a strategy on how to store the profile picture in a scalable manner.

Please imagine this would be a real service for production use. Consider data security, readability, compatibility for future changes and maintainability of the code. Prove that your implementation works.

### Questions to be answered

- Instead of JSON Web Tokens, would you rather use a different approach for authentication and why?

- Why did you chose that specific data store and what are the advantages or disadvantages over other alternative technologies?

- How do you make sure the API is compatible with mobile clients out there if future changes change the interfaces?

- Why did you chose to implement the profile picture storage the way you did it?

## Deliverable

In order to get you started, we have prepared a little docker-compose file and a scaffold example app using Django that you can find [here](https://github.com/midnightrunners/recruiting-userservice). You don't have to use this setup!

However, please commit the code to a Git-repository and create a pull request. Please show us somehow that the code you wrote is actually working. One way to acomplish that is by submitting it as a docker-compose file. This way we can easily deploy your service into our Kubernetes cluster. Please make it easy for us to run/test your code.

Once you are done and ready to hand the task in, please send an email to daniel@mycrew.com and tell us how much time you actually needed to implement the service.

🍀 Good luck and have fun!🦄

## Support

If you have questions, please feel free to send an email to daniel@mycrew.com
