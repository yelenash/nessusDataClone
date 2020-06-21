# nessusDataClone

start elasticsearch docker:
```
   docker pull docker.elastic.co/elasticsearch/elasticsearch:7.5.2 
 ``` 
 ```
   docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.5.2
 ```
 ### execute:
 #### Important: use 64bit version of python. The module ZipFile which is used by vulners module, can't handle large files in 32 bit.
  
 ```
 pip install -r requirements.txt
 ``` 
 
```
 python nessusDataClone.py 
``` 
