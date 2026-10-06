# Exercise 3 - Scaling Flask App Using ReplicaSet

## Objective
- Understand ReplicaSets and Pods
- Scale the Flask app
- Observe pod distribution
- Demonstrate ReplicaSet self-healing

## Application
The Flask Flash Sale application provides:

- `/` - Welcome message and Pod hostname
- `/buy` - Simulates a flash-sale purchase
- `/health` - Health check endpoint

## Docker Image

```bash
docker build -t flashsale:1.0 .
