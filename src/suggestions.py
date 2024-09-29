from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///traffic_pd.db'
db = SQLAlchemy(app)
class TrafficName(db.Model):
    __tablename__ = 'traffic_names'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

@app.route('/suggest', methods=['GET'])
def suggest_names():
    query = request.args.get('q', '').lower()
    if not query:
        return jsonify([])

    suggestions = TrafficName.query.filter(TrafficName.name.ilike(f'{query}%')).order_by(TrafficName.name.asc()).limit(5).all()

    result = [name.name for name in suggestions]

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
