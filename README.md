# Wisecow Kubernetes Deployment

This repository contains GitHub Actions workflows to:

1. **Setup cert-manager & ClusterIssuer** for TLS in GKE.
2. **Build, push, and deploy** the Wisecow app on Kubernetes.

---

## Secrets Needed

- `GCP_SA_KEY` – GCP service account key  
- `GKE_CLUSTER_NAME` – GKE cluster name  
- `GKE_CLUSTER_ZONE` – GKE cluster zone  
- `GCP_PROJECT_ID` – GCP project ID  
- `DOCKER_USERNAME` – Docker Hub username  
- `DOCKER_PASSWORD` – Docker Hub password  

---

## Workflows

### 1. Cluster Setup
- Installs cert-manager via Helm  
- Creates ClusterIssuer for TLS  

### 2. CI/CD Pipeline
- Builds Docker image  
- Pushes to Docker Hub  
- Deploys Wisecow app to GKE  
- Applies deployment, service, ingress  
- Verifies pods, services, and ingress  

---

## Kubernetes Files
- `deployment.yml` – App deployment  
- `service.yml` – App service  
- `ingress.yml` – App ingress  
- `clusterissuer.yml` – TLS ClusterIssuer  

---

