# Full Stack API Final Project
This project was built as a requirement in Misk Academy-Udacity Full-Stack Developer Nanodegree.

## Full Stack Trivia

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a  webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out.

That's where I came in! I helped them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application does:

1) Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category.

### Technologies used in this project

* Python3
* Pip
* SQLAlchemy
* Flask
* Javascript
* ReactJs
* node Js
* Postman

Completing this trivia app gave me the ability to structure plan, implement, and test an API.

## Getting Started

### Pre-requisites and Local Development

Developers using this project should already have Python3, pip and node installed on their local machines.

View both of the frontend and backend README for more details on how to run local development:

1. [`./frontend/`](./frontend/README.md)
2. [`./backend/`](./backend/README.md)

## API Reference

### Getting Started

**Base Url:** This app can only be run locally and is not hosted as a base URL. The backend is hosted at the default, `http://127.0.0.1:5000/`.

**Authentication:** This version doesn't require any authentication.

### Error Handling

Errors are returned as JSON objects in the following format:

```JSON
{
    "success": False,
    "error": 400,
    "message": "Bad Request"
}
```

The API will return three error types when requests fail:

| Status Code    | Message      | Description  |
| :------------- | :----------: | -----------: |
| 400            | Bad Request  | The request cannot be fulfilled due to bad syntax.    |
| 404   | Not Found | The requested resource could not be found but may be available again in the future. Subsequent requests by the client are permissible.    |
| 422 | Unprocessable | The request was well-formed but was unable to be followed due to semantic errors.|

### Endpoint Library

#### Get `/categories`

* General

  * Returns a list of category objects.

* Sample

  * Request: `curl http://127.0.0.1:5000/categories`

  * Response:

    ```JSON
    {
        "categories": {
            "1": "Science",
            "2": "Art",
            "3": "Geography",
            "4": "History",
            "5": "Entertainment",
            "6": "Sports"
        }
    }
    ```

#### GET `/questions`

* General

  * Returns a list of question objects, success value, total number of questions, a list of category objects and the value of current category.

  * Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.

* Sample

  * Request: `curl http://127.0.0.1:5000/questions?page=2`

  * Response:
  
    ``` JSON
    {
        "categories": {
            "1": "Science",
            "2": "Art",
            "3": "Geography",
            "4": "History",
            "5": "Entertainment",
            "6": "Sports"
        },
        "current_category": null,
        "questions": [
            {
                "answer": "Agra",
                "category": 3,
                "difficulty": 2,
                "id": 15,
                "question": "The Taj Mahal is located in which Indian city?"
            },
            {
                "answer": "Escher",
                "category": 2,
                "difficulty": 1,                    "id": 16,
                "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
            },
            {
                "answer": "Mona Lisa",
                "category": 2,                    "difficulty": 3,
                "id": 17,
                "question": "La Giaconda is better known as what?"
            },
            {
                "answer": "One",
                "category": 2,
                "difficulty": 4,
                "id": 18,
                "question": "How many paintings did Van Gogh sell in his lifetime?"
            },
            {
                "answer": "Jackson Pollock",
                "category": 2,
                "difficulty": 2,
                "id": 19,                    "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
            },
            {
                "answer": "The Liver",
                "category": 1,
                "difficulty": 4,
                "id": 20,                    "question": "What is the heaviest organ in the human body?"
            },
            {
                "answer": "Alexander Fleming",
                "category": 1,
                "difficulty": 3,
                "id": 21,
                "question": "Who discovered penicillin?"
            },
            {
                "answer": "Blood",
                "category": 1,
                "difficulty": 4,                    "id": 22,
                "question": "Hematology is a branch of medicine involving the study of what?"
            },
            {
                "answer": "Scarab",
                "category": 4,
                "difficulty": 4,
                "id": 23,
                "question": "Which dung beetle was worshipped by the ancient Egyptians?"
                }
        ],
        "success": true,
        "total_questions": 19
    }
    ```

#### DELETE `/questions/{question_id}`

* General

  * Deletes the question of the given ID if it exists. Returns the id of the deleted question, success value, total number of questions and question list based on current page number to update the frontend.

* Sample

  * Request: `curl -X DELETE http://127.0.0.1:5000/questions/15?page=2`

  * Response:

    ```JSON
    {
        "deleted": 15,
        "questions": [
            {
                "answer": "Escher",
                "category": 2,
                "difficulty": 1,
                "id": 16,
                "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
            },
            {
                "answer": "Mona Lisa",
                "category": 2,
                "difficulty": 3,
                "id": 17,
                "question": "La Giaconda is better known as what?"
            },
            {
                "answer": "One",
                "category": 2,
                "difficulty": 4,
                "id": 18,
                "question": "How many paintings did Van Gogh sell in his lifetime?"
            },
            {
                "answer": "Jackson Pollock",
                "category": 2,
                "difficulty": 2,
                "id": 19,
                "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
            },
            {
                "answer": "The Liver",
                "category": 1,
                "difficulty": 4,
                "id": 20,
                "question": "What is the heaviest organ in the human body?"
            },
            {
                "answer": "Alexander Fleming",
                "category": 1,
                "difficulty": 3,
                "id": 21,
                "question": "Who discovered penicillin?"
            },
            {
                "answer": "Blood",
                "category": 1,
                "difficulty": 4,
                "id": 22,
                "question": "Hematology is a branch of medicine involving the study of what?"
            },
            {
                "answer": "Scarab",
                "category": 4,
                "difficulty": 4,
                "id": 23,
                "question": "Which dung beetle was worshipped by the ancient Egyptians?"
            }
        ],
        "success": true, 
        "total_questions": 18
    }
    ```

#### POST `/questions`

* General
  
  * Creates a new question using the submitted question, answer, category, and difficulty. Returns the id of the created question, success value, total number of questions, and question list based on current page to update the frontend.

* Sample

  * Request: `curl -X POST -H "Content-Type: application/json" -d '{"question": "What is the largest ocean of the world.", "answer": "Pacific Ocean", "category": 3, "difficulty": 2}' http://127.0.0.1:5000/questions?page=2`

  * Response:

    ```JSON
    {
        "created": 24,
        "questions": [
            {
                "answer": "Escher",
                "category": 2,
                "difficulty": 1,
                "id": 16,
                "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
            },
            {
                "answer": "Mona Lisa",
                "category": 2,
                "difficulty": 3,
                "id": 17,
                "question": "La Giaconda is better known as what?"
            },
            {
                "answer": "One",
                "category": 2,
                "difficulty": 4,
                "id": 18,
                "question": "How many paintings did Van Gogh sell in his lifetime?"
            },
            {
                "answer": "Jackson Pollock",
                "category": 2,
                "difficulty": 2,
                "id": 19,
                "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
            },
            {
                "answer": "The Liver",
                "category": 1,
                "difficulty": 4,
                "id": 20,
                "question": "What is the heaviest organ in the human body?"
            },
            {
                "answer": "Alexander Fleming",
                "category": 1,
                "difficulty": 3,
                "id": 21,
                "question": "Who discovered penicillin?"
            },
            {
                "answer": "Blood",
                "category": 1,
                "difficulty": 4,
                "id": 22,
                "question": "Hematology is a branch of medicine involving the study of what?"
            },
            {
                "answer": "Scarab",
                "category": 4,
                "difficulty": 4,
                "id": 23,
                "question": "Which dung beetle was worshipped by the ancient Egyptians?"
            },
            {
                "answer": "Pacific Ocean",
                "category": 3,
                "difficulty": 2,
                "id": 24,
                "question": "What is the largest ocean of the world."
            }
        ],
        "success": true,
        "total_questions": 19
    }
    ```

#### POST `/questions/search`

* General
  
  * Searches for a given text query string and retrieves a list of question objects where the questions object's question is a match. Returns a list of question objects, success value, total number of questions and the value of the current category.

* Sample

  * Request: `curl -X POST -H "Content-Type: application/json" -d '{"searchTerm": "title"}' http://127.0.0.1:5000/questions/search`

  * Response:

    ```JSON
    {
        "current_category": null,
        "questions": [
            {
                "answer": "Maya Angelou",
                "category": 4,
                "difficulty": 2,
                "id": 5,
                "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
            },
            {
                "answer": "Edward Scissorhands",
                "category": 5,
                "difficulty": 3,
                "id": 6,
                "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
                }
        ],
        "success": true,
        "total_questions": 2
    }
    ```

#### GET `/categories/{category_id}/questions`

* General
  
  * Retrieves all questions that are associated with the given category ID. Returns a list of question objects, success value, total number of questions and the value of current category.

* Sample
  
  * Request: `curl http://127.0.0.1:5000/categories/1/questions`

  * Response:

    ```JSON
    {
        "current_category": 1,
        "questions": [
            {
                "answer": "The Liver",
                "category": 1,
                "difficulty": 4,
                "id": 20,
                "question": "What is the heaviest organ in the human body?"
            },
            {
                "answer": "Alexander Fleming",
                "category": 1,
                "difficulty": 3,
                "id": 21,
                "question": "Who discovered penicillin?"
            },
            {
                "answer": "Blood",
                "category": 1,
                "difficulty": 4,
                "id": 22,
                "question": "Hematology is a branch of medicine involving the study of what?"
            }
        ],
        "success": true,
        "total_questions": 3
    }
    ```

#### POST `/quizzes`

* General

  * Retrieves randomized questions either by all categories or within a specific category. Returns a list of question objects, and a success value.

* Sample

  * Request: `curl -X POST -H "Content-Type: application/json" -d '{"quiz_category": {"type": "Science", "id": 1 }, "previous_questions":[]}' http://127.0.0.1:5000/quizzes`

  * Response:

    ```JSON
    {
        "question": {
            "answer": "Alexander Fleming",
            "category": 1,
            "difficulty": 3,
            "id": 21,
            "question": "Who discovered penicillin?"
        },
        "success": true
    }
    ```

---


## References
Please note that I have used these resources during my work on the project:

* [Python Assert Example | Assert Statement In Python
](https://appdividend.com/2019/01/18/python-assert-statement-tutorial-with-example/)

* [Stackoverflow: Check if string matches pattern](https://stackoverflow.com/questions/12595051/check-if-string-matches-pattern)

* [Stackoverflow: Case insensitive regular expression without re.compile?](https://stackoverflow.com/questions/500864/case-insensitive-regular-expression-without-re-compile)

* [HTTP STATUS DOGS](https://httpstatusdogs.com/)

* [Stackoverflow: Does Python have a string 'contains' substring method?](https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method)

* [Stackoverflow: What is Truthy and Falsy? How is it different from True and False?](https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false)

* [Stackoverflow: How to randomly select an item from a list?](https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list)