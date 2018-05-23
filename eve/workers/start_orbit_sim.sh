#!/bin/sh

helm install --name ciutil --wait \
    --set orbit-simulator.AWS_GCP_BACKEND_ACCESS_KEY="$AWS_GCP_BACKEND_ACCESS_KEY" \
    --set orbit-simulator.AWS_GCP_BACKEND_ACCESS_KEY_2="$AWS_GCP_BACKEND_ACCESS_KEY_2" \
    --set orbit-simulator.AWS_GCP_BACKEND_SECRET_KEY="$AWS_GCP_BACKEND_SECRET_KEY" \
    --set orbit-simulator.AWS_GCP_BACKEND_SECRET_KEY_2="$AWS_GCP_BACKEND_SECRET_KEY_2" \
    --set orbit-simulator.AWS_S3_BACKBEAT_ACCESS_KEY="$AWS_S3_BACKBEAT_ACCESS_KEY" \
    --set orbit-simulator.AWS_S3_BACKBEAT_SECRET_KEY="$AWS_S3_BACKBEAT_SECRET_KEY" \
    --set orbit-simulator.AWS_S3_BACKBEAT_BUCKET_NAME="$AWS_S3_BACKBEAT_BUCKET_NAME" \
    --set orbit-simulator.AWS_S3_BACKEND_ACCESS_KEY="$AWS_S3_BACKEND_ACCESS_KEY" \
    --set orbit-simulator.AWS_S3_BACKEND_ACCESS_KEY_2="$AWS_S3_BACKEND_ACCESS_KEY_2" \
    --set orbit-simulator.AWS_S3_BACKEND_SECRET_KEY="$AWS_S3_BACKEND_SECRET_KEY" \
    --set orbit-simulator.AWS_S3_BACKEND_SECRET_KEY_2="$AWS_S3_BACKEND_SECRET_KEY_2" \
    --set orbit-simulator.AWS_S3_BUCKET_NAME="$AWS_S3_BUCKET_NAME" \
    --set orbit-simulator.AWS_S3_BUCKET_NAME_2="$AWS_S3_BUCKET_NAME_2" \
    --set orbit-simulator.AZURE_BACKBEAT_CONTAINER_NAME="$AZURE_BACKBEAT_CONTAINER_NAME" \
    --set orbit-simulator.AZURE_BACKEND_ACCESS_KEY="$AZURE_BACKEND_ACCESS_KEY" \
    --set orbit-simulator.AZURE_BACKEND_ACCESS_KEY_2="$AZURE_BACKEND_ACCESS_KEY_2" \
    --set orbit-simulator.AZURE_BACKEND_ACCOUNT_NAME="$AZURE_BACKEND_ACCOUNT_NAME" \
    --set orbit-simulator.AZURE_BACKEND_ACCOUNT_NAME_2="$AZURE_BACKEND_ACCOUNT_NAME_2" \
    --set orbit-simulator.AZURE_BACKEND_CONTAINER_NAME="$AZURE_BACKEND_CONTAINER_NAME" \
    --set orbit-simulator.AZURE_BACKEND_CONTAINER_NAME_2="$AZURE_BACKEND_CONTAINER_NAME_2" \
    --set orbit-simulator.AZURE_BACKEND_ENDPOINT="$AZURE_BACKEND_ENDPOINT" \
    --set orbit-simulator.AZURE_BACKEND_ENDPOINT_2="$AZURE_BACKEND_ENDPOINT_2" \
    --set orbit-simulator.GCP_BUCKET_NAME="$GCP_BUCKET_NAME" \
    --set orbit-simulator.GCP_BUCKET_NAME_2="$GCP_BUCKET_NAME_2" \
    --set orbit-simulator.GCP_CRR_BUCKET_NAME="$GCP_CRR_BUCKET_NAME" \
    --set orbit-simulator.GCP_CRR_MPU_BUCKET_NAME="$GCP_CRR_MPU_BUCKET_NAME" \
    --set orbit-simulator.GCP_MPU_BUCKET_NAME="$GCP_MPU_BUCKET_NAME" \
    --set orbit-simulator.GCP_MPU_BUCKET_NAME_2="$GCP_MPU_BUCKET_NAME_2" \
    orbit-simulator/orbit-simulator
