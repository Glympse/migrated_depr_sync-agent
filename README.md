# Docker Sync Agent

The tool is intended to simplify configuring dockerized applications running in the cloud.

## Design

Sync Agent is a simple application that exposes access to local folder through simple REST API. 
The following setup can be used to let Sync Agent manage configuration of an app running in a sibling container on the smae host.

<div align="center">
  <img width="50%" src="https://docs.google.com/drawings/d/1faD_9OxswtuCGWN1bITngL2i_StJ29_yvM2qEBYb304/pub?w=527&h=271">
</div>

## Integrations

[Docker Cluster](https://github.com/Glympse/docker-cluster) includes a plugin build on top Sync Agent API:

<div align="center">
  <img width="80%" src="https://drive.google.com/uc?id=0B9NxURKU5b4SVnd2bk1hLS1Vd1U&export=view">
</div>
