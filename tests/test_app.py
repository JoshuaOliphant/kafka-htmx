from unittest.mock import ANY
from kafka_htmx import create_app


def test_create_app(mocker):
    # Create a mock KafkaProducer
    mock_kafka_producer = mocker.patch('kafka_htmx.KafkaProducer')
    mock_producer_instance = mock_kafka_producer.return_value

    # Create an instance of the app with a test configuration
    app = create_app({
        'TESTING': True,
        'DATABASE': 'sqlite:///:memory:',
    })

    # Create a test client
    client = app.test_client()

    # Send a POST request to the index route
    response = client.post('/', data={
        'topic': 'test_topic',
        'num_messages': 5,
        'cluster': 'localhost:9092'
    }, content_type='application/x-www-form-urlencoded')

    # Assert that the response status code is 200
    assert response.status_code == 200

    # Assert that KafkaProducer was called
    mock_kafka_producer.assert_called_once_with(
        bootstrap_servers=['localhost:9092'],
        value_serializer=ANY
    )

    # Assert that the send method of the KafkaProducer instance was called
    assert mock_producer_instance.send.call_count == 5