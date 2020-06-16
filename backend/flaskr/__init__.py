import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import re

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
  # Get the current page, if not provided use 1 as default
  page = request.args.get('page', 1, type=int)
  # Define the first question 
  start = (page - 1) * QUESTIONS_PER_PAGE
  # Define last question
  end = start + QUESTIONS_PER_PAGE

  # Format questions to be retrieved as JSON
  questions = [question.format() for question in selection]
  current_questions = questions[start:end]
  return current_questions

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  # Set up Cors, allowing access for all origins (*)
  CORS(app)

  # Set access-control-allow for headers
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')

    return response


  @app.route('/categories')
  def retrieve_categories():
    # Get all available categories
    categories = Category.query.all()
    # Format the categories to be retrieved as JSON
    formatted_categories = {category.id: category.type for category in categories}
    return jsonify({"categories": formatted_categories})


  @app.route('/questions')
  def retrieve_questions():
    # Query all questions from db
    selection = Question.query.order_by(Question.id).all()
    # Paginate the question using the defined method above
    current_questions = paginate_questions(request, selection)
    # Query all categories from db
    categories = Category.query.all()
    # Format categories to have the id of category as keys and type as values as dicts
    formatted_categories = {category.id: category.type for category in categories}

    # If there are no questions return resource not found
    if len(current_questions) == 0:
      abort(404)

    return jsonify({
      'success': True,
      'questions': current_questions,
      'total_questions': len(selection),
      'categories': formatted_categories,
      'current_category': None
    })


  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    try:
      # Query the question using params to get id from the db, if it doesn't exist it returns none
      question = Question.query.filter(Question.id == question_id).one_or_none()

      # if the id doesn't exist return 404
      if question is None:
        abort(404)

      # else if the id does exist
      else:
        # Delete the question 
        question.delete()
        # Query all questions after deletion
        selection = Question.query.order_by(Question.id).all()
        # Paginate questions using the previous defined method
        current_questions = paginate_questions(request, selection)

        return jsonify({
          'success': True,
          'deleted': question_id,
          'questions': current_questions,
          'total_questions': len(selection)
        })

    except:
      # if couldn't delete the question return 422
      abort(422)


  @app.route('/questions', methods=['POST'])
  def create_question():
    # Get data from the body
    body = request.get_json()

    if not ('question' in body and 'answer' in body and 'category' in body and 'difficulty' in body):
      abort(422)

    # Get each value
    new_question = body.get('question')
    new_answer = body.get('answer')
    new_category = body.get('category')
    new_difficulty = body.get('difficulty')

    try:
      # Create a new instance from the question model
      question = Question(question=new_question, answer=new_answer, category=new_category, difficulty=new_difficulty)
      # Insert the question into the db
      question.insert()

      # Query all questions from the db
      selection = Question.query.order_by(Question.id).all()
      # Paginate questions
      current_questions = paginate_questions(request, selection)

      return jsonify({
        'success': True,
        'created': question.id,
        'questions': current_questions,
        'total_questions': len(selection)
      })

    except:
      abort(422)


  @app.route('/questions/search', methods=['POST'])
  def search_questions():
    # Get data from the body
    body = request.get_json()
    # Extract the search term from the body
    search_term = body.get('searchTerm')

    # If the search term is not empty
    if search_term:
      # Query all questions
      all_questions = Question.query.order_by(Question.id).all()
      # Filter the questions by checking if it matches the search term using regular expressions with ignoring case sensitive
      filtered_questions = [question for question in all_questions if re.search(search_term, question.question, re.IGNORECASE)]

      # If no results were found
      if len(filtered_questions) == 0:
        # Return 404
        abort(404)

      # Paginate results
      search_results = paginate_questions(request, filtered_questions)

      return jsonify({
        'success': True,
        'questions': search_results,
        'total_questions': len(search_results),
        'current_category': None
      })

    # If the search term is empty return 404
    abort(422)
    

  @app.route('/categories/<int:category_id>/questions')
  def get_questions_by_category(category_id):
    
    # If category id exists
    if Category.query.get(category_id):
      # Get all questions with passed category id
      selection = Question.query.filter(Question.category == category_id).all()
      # Paginate questions
      questions = paginate_questions(request, selection)

      return jsonify({
        'success': True,
        'questions': questions,
        'total_questions': len(selection),
        'current_category': category_id
      })

    # If category id does not exists return 404
    abort(404)



  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

 
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      'success': False,
      'error': 404,
      'message': 'Resource Not Found'
    }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      'success': False,
      'error': 422,
      'message': 'Unprocessable Entity'
    }), 422

  return app

    