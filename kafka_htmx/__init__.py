from flask import Flask, request, render_template
from kafka import KafkaProducer
import json


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            topic = request.form.get('topic')
            num_messages = int(request.form.get('num_messages'))
            cluster = request.form.get('cluster')

            try:
                producer = KafkaProducer(bootstrap_servers=[cluster],
                                        value_serializer=lambda v: json.dumps(v).encode('utf-8'))

                for _ in range(num_messages):
                    message = {"content": "Random Message"}
                    producer.send(topic, message)

                producer.flush()
            except Exception as e:
                app.logger.error(f"Error sending to Kafka: {e}")

        return render_template('index.html')

    return app
