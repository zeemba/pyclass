# pyclass
Python lessons

*Use the command below to spin up the theia container and pull down your github archive you;d like to work on*

docker run -d -p 8088:8080 --name theia -v volume-name:/home/gopath/src -v /var/run/docker.sock:/var/run/docker.sock --restart unless-stopped redmanh/theia-full
