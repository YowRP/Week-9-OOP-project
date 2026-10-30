FROM python:3.14-slim

WORKDIR /app

COPY . .

CMD ["python", "inventory_manager.py"]