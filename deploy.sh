MY_INSTANCE_NAME="gce-lotteryscraper"
ZONE=asia-east1-a

gcloud compute instances create $MY_INSTANCE_NAME \
    --image-family=debian-9 \
    --image-project=debian-cloud \
    --machine-type=g1-small \
    --scopes userinfo-email,cloud-platform \
    --metadata-from-file startup-script=gce.sh \
    --zone $ZONE \
    --tags redd-server