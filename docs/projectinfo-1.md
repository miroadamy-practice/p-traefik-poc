# Basics

The source is https://docs.traefik.io/v2.0/getting-started/quick-start/


## First run

The file:

```yaml
{% include 'src/compose-1/docker-compose-v1.yml' %}
```

```bash
    ➜  compose-1 git:(master) docker-compose up -d reverse-proxy
    Creating network "compose-1_default" with the default driver
    Pulling reverse-proxy (traefik:v2.0)...
    v2.0: Pulling from library/traefik
    89d9c30c1d48: Pull complete
    275722d2e7f6: Pull complete
    a5605da1bde2: Pull complete
    13c9af667fbf: Pull complete
    Digest: sha256:380d2eee7035e3b88be937e7ddeac869b41034834dcc8a30231311805ed9fd22
    Status: Downloaded newer image for traefik:v2.0
    Creating compose-1_reverse-proxy_1 ... done
    ➜  compose-1 git:(master) docker-compose ps
              Name                         Command               State                     Ports
    ---------------------------------------------------------------------------------------------------------------
    compose-1_reverse-proxy_1   /entrypoint.sh --api.insec ...   Up      0.0.0.0:80->80/tcp, 0.0.0.0:8080->8080/tcp
```

Returns

```bash
    ➜  compose-1 git:(master) curl http://localhost:8080/api/rawdata
    {"routers":{"charming-elion@docker":{"service":"charming-elion","rule":"Host(`charming-elion`)","status":"enabled","using":["http","traefik"]},"reverse-proxy-compose-1@docker":{"service":"reverse-proxy-compose-1","rule":"Host(`reverse-proxy-compose-1`)","status":"enabled","using":["http","traefik"]}},"services":{"charming-elion@docker":{"loadBalancer":{"servers":[{"url":"http://172.17.0.2:4000"}],"passHostHeader":true},"status":"enabled","usedBy":["charming-elion@docker"],"serverStatus":{"http://172.17.0.2:4000":"UP"}},"reverse-proxy-compose-1@docker":{"loadBalancer":{"servers":[{"url":"http://172.18.0.2:80"}],"passHostHeader":true},"status":"enabled","usedBy":["reverse-proxy-compose-1@docker"],"serverStatus":{"http://172.18.0.2:80":"UP"}}}}
```

Pretty-prints as:

```json
    ➜  compose-1 git:(master) curl -s http://localhost:8080/api/rawdata | jq
    {
      "routers": {
        "charming-elion@docker": {
          "service": "charming-elion",
          "rule": "Host(`charming-elion`)",
          "status": "enabled",
          "using": [
            "http",
            "traefik"
          ]
        },
        "reverse-proxy-compose-1@docker": {
          "service": "reverse-proxy-compose-1",
          "rule": "Host(`reverse-proxy-compose-1`)",
          "status": "enabled",
          "using": [
            "http",
            "traefik"
          ]
        }
      },
      "services": {
        "charming-elion@docker": {
          "loadBalancer": {
            "servers": [
              {
                "url": "http://172.17.0.2:4000"
              }
            ],
            "passHostHeader": true
          },
          "status": "enabled",
          "usedBy": [
            "charming-elion@docker"
          ],
          "serverStatus": {
            "http://172.17.0.2:4000": "UP"
          }
        },
        "reverse-proxy-compose-1@docker": {
          "loadBalancer": {
            "servers": [
              {
                "url": "http://172.18.0.2:80"
              }
            ],
            "passHostHeader": true
          },
          "status": "enabled",
          "usedBy": [
            "reverse-proxy-compose-1@docker"
          ],
          "serverStatus": {
            "http://172.18.0.2:80": "UP"
          }
        }
      }
    }
```

## How it detects new services

Add ``whoami`` service

```yaml
{% include 'src/compose-1/docker-compose.yml' %}
```

Run `docker-compose up -d whoami`

```bash
    ➜  compose-1 git:(master) ✗ docker-compose up -d whoami
    Pulling whoami (containous/whoami:)...
    latest: Pulling from containous/whoami
    1ffe3ad36c8e: Pull complete
    0bf848301d61: Pull complete
    a7cb4252f1e9: Pull complete
    Digest: sha256:c0d68a0f9acde95c5214bd057fd3ff1c871b2ef12dae2a9e2d2a3240fdd9214b
    Status: Downloaded newer image for containous/whoami:latest
    Creating compose-1_whoami_1 ... done

    ➜  compose-1 git:(master) ✗ docker-compose ps
              Name                         Command               State                     Ports
    ---------------------------------------------------------------------------------------------------------------
    compose-1_reverse-proxy_1   /entrypoint.sh --api.insec ...   Up      0.0.0.0:80->80/tcp, 0.0.0.0:8080->8080/tcp
    compose-1_whoami_1          /whoami                          Up      80/tcp
```

!!! note
    Traefik has automatically detected the new container and updated its own configuration.


```bash
    ➜  compose-1 git:(master) ✗ curl -s http://localhost:8080/api/rawdata
    {"routers":{"charming-elion@docker":{"service":"charming-elion","rule":"Host(`charming-elion`)","status":"enabled","using":["http","traefik"]},"reverse-proxy-compose-1@docker":{"service":"reverse-proxy-compose-1","rule":"Host(`reverse-proxy-compose-1`)","status":"enabled","using":["http","traefik"]},"whoami@docker":{"service":"whoami-compose-1","rule":"Host(`whoami.docker.localhost`)","status":"enabled","using":["http","traefik"]}},"services":{"charming-elion@docker":{"loadBalancer":{"servers":[{"url":"http://172.17.0.2:4000"}],"passHostHeader":true},"status":"enabled","usedBy":["charming-elion@docker"],"serverStatus":{"http://172.17.0.2:4000":"UP"}},"reverse-proxy-compose-1@docker":{"loadBalancer":{"servers":[{"url":"http://172.18.0.2:80"}],"passHostHeader":true},"status":"enabled","usedBy":["reverse-proxy-compose-1@docker"],"serverStatus":{"http://172.18.0.2:80":"UP"}},"whoami-compose-1@docker":{"loadBalancer":{"servers":[{"url":"http://172.18.0.3:80"}],"passHostHeader":true},"status":"enabled","usedBy":["whoami@docker"],"serverStatus":{"http://172.18.0.3:80":"UP"}}}}
    
    ➜  compose-1 git:(master) ✗ curl -s http://localhost:8080/api/rawdata | jq
    {
      "routers": {
        "charming-elion@docker": {
          "service": "charming-elion",
          "rule": "Host(`charming-elion`)",
          "status": "enabled",
          "using": [
            "http",
            "traefik"
          ]
        },
        "reverse-proxy-compose-1@docker": {
          "service": "reverse-proxy-compose-1",
          "rule": "Host(`reverse-proxy-compose-1`)",
          "status": "enabled",
          "using": [
            "http",
            "traefik"
          ]
        },
        "whoami@docker": {
          "service": "whoami-compose-1",
          "rule": "Host(`whoami.docker.localhost`)",
          "status": "enabled",
          "using": [
            "http",
            "traefik"
          ]
        }
      },
      "services": {
        "charming-elion@docker": {
          "loadBalancer": {
            "servers": [
              {
                "url": "http://172.17.0.2:4000"
              }
            ],
            "passHostHeader": true
          },
          "status": "enabled",
          "usedBy": [
            "charming-elion@docker"
          ],
          "serverStatus": {
            "http://172.17.0.2:4000": "UP"
          }
        },
        "reverse-proxy-compose-1@docker": {
          "loadBalancer": {
            "servers": [
              {
                "url": "http://172.18.0.2:80"
              }
            ],
            "passHostHeader": true
          },
          "status": "enabled",
          "usedBy": [
            "reverse-proxy-compose-1@docker"
          ],
          "serverStatus": {
            "http://172.18.0.2:80": "UP"
          }
        },
        "whoami-compose-1@docker": {
          "loadBalancer": {
            "servers": [
              {
                "url": "http://172.18.0.3:80"
              }
            ],
            "passHostHeader": true
          },
          "status": "enabled",
          "usedBy": [
            "whoami@docker"
          ],
          "serverStatus": {
            "http://172.18.0.3:80": "UP"
          }
        }
      }
    }
```

If a request goes to the host ``whoami.docker.localhost`` it will be redirected:

```bash
    ➜  compose-1 git:(master) ✗ curl -H Host:whoami.docker.localhost http://127.0.0.1
    Hostname: decaf14111eb
    IP: 127.0.0.1
    IP: 172.18.0.3
    RemoteAddr: 172.18.0.2:41454
    GET / HTTP/1.1
    Host: whoami.docker.localhost
    User-Agent: curl/7.54.0
    Accept: */*
    Accept-Encoding: gzip
    X-Forwarded-For: 172.18.0.1
    X-Forwarded-Host: whoami.docker.localhost
    X-Forwarded-Port: 80
    X-Forwarded-Proto: http
    X-Forwarded-Server: 037dda9663f3
    X-Real-Ip: 172.18.0.1
```

## Traefik as loadbalancer

Scale the service

```bash
    ➜  compose-1 git:(master) ✗ docker-compose up -d --scale whoami=2
    compose-1_reverse-proxy_1 is up-to-date
    Starting compose-1_whoami_1 ... done
    Creating compose-1_whoami_2 ... done

    ➜  compose-1 git:(master) ✗ docker-compose ps
              Name                         Command               State                     Ports
    ---------------------------------------------------------------------------------------------------------------
    compose-1_reverse-proxy_1   /entrypoint.sh --api.insec ...   Up      0.0.0.0:80->80/tcp, 0.0.0.0:8080->8080/tcp
    compose-1_whoami_1          /whoami                          Up      80/tcp
    compose-1_whoami_2          /whoami                          Up      80/tcp
```

Check few times - note that host and IP are cycling

```bash
    ➜  compose-1 git:(master) ✗ curl -H Host:whoami.docker.localhost http://127.0.0.1
    Hostname: 2b0dc3490462
    IP: 127.0.0.1
    IP: 172.18.0.4
    RemoteAddr: 172.18.0.2:54568
    GET / HTTP/1.1
    Host: whoami.docker.localhost
    User-Agent: curl/7.54.0
    Accept: */*
    Accept-Encoding: gzip
    X-Forwarded-For: 172.18.0.1
    X-Forwarded-Host: whoami.docker.localhost
    X-Forwarded-Port: 80
    X-Forwarded-Proto: http
    X-Forwarded-Server: 037dda9663f3
    X-Real-Ip: 172.18.0.1

    ➜  compose-1 git:(master) ✗ curl -H Host:whoami.docker.localhost http://127.0.0.1
    Hostname: decaf14111eb
    IP: 127.0.0.1
    IP: 172.18.0.3
    RemoteAddr: 172.18.0.2:41462
    GET / HTTP/1.1
    Host: whoami.docker.localhost
    User-Agent: curl/7.54.0
    Accept: */*
    Accept-Encoding: gzip
    X-Forwarded-For: 172.18.0.1
    X-Forwarded-Host: whoami.docker.localhost
    X-Forwarded-Port: 80
    X-Forwarded-Proto: http
    X-Forwarded-Server: 037dda9663f3
    X-Real-Ip: 172.18.0.1

    ➜  compose-1 git:(master) ✗ curl -H Host:whoami.docker.localhost http://127.0.0.1
    Hostname: 2b0dc3490462
    IP: 127.0.0.1
    IP: 172.18.0.4
    RemoteAddr: 172.18.0.2:54568
    GET / HTTP/1.1
    Host: whoami.docker.localhost
    User-Agent: curl/7.54.0
    Accept: */*
    Accept-Encoding: gzip
    X-Forwarded-For: 172.18.0.1
    X-Forwarded-Host: whoami.docker.localhost
    X-Forwarded-Port: 80
    X-Forwarded-Proto: http
    X-Forwarded-Server: 037dda9663f3
    X-Real-Ip: 172.18.0.1

    ➜  compose-1 git:(master) ✗ curl -H Host:whoami.docker.localhost http://127.0.0.1
    Hostname: decaf14111eb
    IP: 127.0.0.1
    IP: 172.18.0.3
    RemoteAddr: 172.18.0.2:41462
    GET / HTTP/1.1
    Host: whoami.docker.localhost
    User-Agent: curl/7.54.0
    Accept: */*
    Accept-Encoding: gzip
    X-Forwarded-For: 172.18.0.1
    X-Forwarded-Host: whoami.docker.localhost
    X-Forwarded-Port: 80
    X-Forwarded-Proto: http
    X-Forwarded-Server: 037dda9663f3
    X-Real-Ip: 172.18.0.1
```

