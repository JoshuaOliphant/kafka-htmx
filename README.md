# Kafka HTMX

Kafka HTMX is a Flask application that allows you to send messages to a Kafka cluster. The application provides a simple web interface where you can specify the topic, the number of messages to send, and the Kafka cluster to send the messages to.

## Setup

To set up the Kafka HTMX application, you need to have Python 3.8 or later and Poetry installed on your machine.

1. Clone the repository:

```bash
git clone https://github.com/yourusername/kafka_htmx.git
cd kafka_htmx

2. Install the dependencies:
`poetry install`

3. Create a .env file in the root directory of the project and add your configuration variables:
`echo "FLASK_APP=kafka_htmx" > .env`

## Running the Application

To run the Kafka HTMX application, use the flask run command:
`poetry run flask run`
This will start the application on localhost:5000.
