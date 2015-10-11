# Sync Agent

The tool is intended to simplify configuring dockerized applications running in the cloud.

## Design

Sync Agent is a simple application that exposes access to local folder through simple REST API.
The following setup can be used to let Sync Agent manage configuration of an app running in a sibling container on the same host.

<div align="center">
  <img width="50%" src="https://docs.google.com/drawings/d/1faD_9OxswtuCGWN1bITngL2i_StJ29_yvM2qEBYb304/pub?w=527&h=271">
</div>

## Installation

Sync Agent can be launched locally or on remote machine using this command:

```bash
docker run -d \
  -p 8080:8080 \
  -e SYNC_FOLDER=/opt/host \
  -v /Users/egorpushkin/Temp:/opt/host \
  --name sync-agent \
  glympse/sync-agent:latest
```

## API Endpoints

There API endpoints are exposed by running instance of Sync Agent.

### api/1

```
GET /api/1/list
```

Returns the list of files available at the location where Sync Agent instance is pointed at.

```
GET /api/1/get
  ?name=...
```

Responds with the contents of requested file.

```
POST /api/1/update
  ?name=...
```

Uploads new file with the specified name and contents from request body.

## Integrations

[Docker Cluster](https://github.com/Glympse/docker-cluster) includes a plugin that utilizes Sync Agent API:

<div align="center">
  <img width="60%" src="https://drive.google.com/uc?id=0B9NxURKU5b4SVnd2bk1hLS1Vd1U&export=view">
</div>

## Disclaimer

Keep in mind that Sync Agent exposes API that makes it possible to modify local filesystem within Docker container.
It is highly recommended to use Sync Agent for educational and experimental purposes only.

## License

Code is licensed under the [The MIT License](http://opensource.org/licenses/MIT). <br>
Documentation is licensed under [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
