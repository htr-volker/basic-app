 
# Build the images and push them to the local docker registry
cp /home/jenkins/.env /var/lib/jenkins/workspace/implementation2/.env
docker-compose build
docker-compose push
