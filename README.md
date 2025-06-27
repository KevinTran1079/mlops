# mlops

The purpose of the repository is to develop skills needed to deploy machine learning algorithms and models into production.

I will be training various models and exposing the api for prediction or generation.

Statistical models could include Boosting (AdaBoost, GB, XGB),PCA, SVM, Logistic Regression, MLPs (Multi Layer Perceptrons), KNN, K Means Clustering and various other methods learned in my undergraduate education.

Generative Models include Autoencoders, Variational Autoencoders, GANs (condgan, info gan, or pix2pix), Diffusion, LSTM, Transformers, LLMs and more depending on the computational power available to me.

# Technologies

- FastApi
- Docker
- Kubernetes (K8s) for scaling
- CI/CD
- Cloud Platforms (AWS, GCP, Azure)

# Learning Goals

- Practice building APIs with FastAPI
- Gain experience in model serialization and loading
- Containerize ML apps with Docker
- Deploy containerized apps to the cloud
- Manage deployment with Kubernetes
- Set up CI/CD pipelines for automated deployment

# Bank Note Authentication API

This is a containerized FastAPI application that predicts whether a bank note is real or fake using a trained random forest.

# README below here is generated with AI.

## Project Structure

```
.
├── main.py              # FastAPI application
├── clf.pkl              # Trained ML model (scikit-learn)
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker image specification
└── README.md
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/KevinTran1079/mlops.git
cd mlops
```

### 2. Install Dependencies (for local dev)

```bash
pip install -r requirements.txt
```

### 3. Run Locally

```bash
uvicorn main:app --reload
```

Access API docs at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Docker Instructions

### Build the Docker image

```bash
docker build -t banknote-api .
```

### Run the container

```bash
docker run -d -p 8000:8000 banknote-api
```

The API will be accessible at: [http://localhost:8000](http://localhost:8000)

---

## API Usage

### Endpoint: `POST /predict`

**Request JSON body:**

```json
{
  "variance": 2.3,
  "skewness": 1.1,
  "curtosis": -0.4,
  "entropy": 0.9
}
```

**Response:**

```json
{
  "prediction": "Fake note"
}
```

---

## Model Info

The model (`clf.pkl`) is a pre-trained binary classifier built using scikit-learn. It takes four features from bank note data:

- Variance
- Skewness
- Curtosis
- Entropy

---

## TODOs

- [ ] Add model training script
- [ ] Add logging and error handling
- [ ] Add tests with `pytest`
- [ ] Deploy to cloud (e.g., Render, AWS)

---

## 📄 License

MIT License – feel free to use, modify, and share.
