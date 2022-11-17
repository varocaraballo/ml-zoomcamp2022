## Notes

### Pickle

`pickle` is a library to dump (save) and load data in python. It can serialize and deserialize tuples, lists, and any kind of objects. 

It is commonly used to save trained models to be loaded and used later in prod environments.

---
> WORK-IN-PROGRESS: This sections needs to be completed these are some ideas to develop later. 

So, from my point of view thinking on CRISP (life-cycle) of a ML task, the first thing to do is to analyze the problem, gather data, make some study of the data to determine correlation between the available features (and target). ROC curves may help here...

After that state some model and tune it and evalutae its performance using cross-validation (KFold).

All the process till here can be done playing/using Jupyter notebooks. Not only can be done it is recommended due to the level of flexibility and customization that Jupyter notebooks offer.

Then you should proceeed to serialize the model to be used later with real/unknown inputs, for example as an API or a service.

This is when pickle enters into scene to serialize the model in your Jupyter notebook and later deserializing it and loading it to be used in a server.

---

### Pipenv

`pipenv` is a tool to create python environments. It is pretty useful to setup the environment into a docker image. This allows 


### Docker


...

### ElasticBeanstalk

First thing to do is to intall `awsebcli` (AWS ElasticBeanstalk CLI) in the pip environment (we don't want to install awsebcli for hte whole system, remember modularization/containerization/isolation to avoid that some project affect anothe one) using:
```bash
pipenv install awsebcli --dev 
```

After that execute `eb --help` to check the set of options for this command.

Create a docker application to be submited to AWS:
```bash
eb init <app-name> -p docker -r <aws-region>
```

This creates a docker application inside `.elasticbeanstalk > config.yml`. For example:
```bash
eb init ml-zoomcamp-deployment-homework -p docker -r eu-west-1 
```
creates: 
```yml
branch-defaults:
  default:
    environment: null
    group_suffix: null
global:
  application_name: ml-zoomcamp-deployment-homework
  branch: null
  default_ec2_keyname: null
  default_platform: Docker
  default_region: eu-west-1
  include_git_submodules: true
  instance_profile: null
  platform_name: null
  platform_version: null
  profile: eb-cli
  repository: null
  sc: null
  workspace_type: Application
```

Then we can test this EB-Aplication executing it locally:
```bash
eb local run --port <port>
```

Create an AWS environment in the cloud with all the required resources to have our system ready and operational (load balancers, EC2 instances, security groups, etc...)

```bash
eb create <env-name>  
```
After running this command a lot of resources are created on AWS on our behalf to have out model ready and operation. This also modifies the previously created `.elasticbeanstalk > config.yml` adding the environment name:

```bash
eb create mlzoomcamp-deployment
```
outputs: 
```yml
branch-defaults:
  default:
    environment: mlzoomcamp-deployment
    group_suffix: null
global:
  application_name: ml-zoomcamp-deployment-homework
  branch: null
  default_ec2_keyname: null
  default_platform: Docker
  default_region: eu-west-1
  include_git_submodules: true
  instance_profile: null
  platform_name: null
  platform_version: null
  profile: eb-cli
  repository: null
  sc: null
  workspace_type: Application
```

Finally, to clean-up the environment alongside the application and every created resource, use:
```bash
eb terminate <env-name> 
```
