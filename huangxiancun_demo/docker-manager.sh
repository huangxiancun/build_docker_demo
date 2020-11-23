#!/bin/bash
version='latest'
docker build -f Dockerfile -t 15861813785/nlp/huangxiancun_demo:${version} .
docker tag 15861813785/nlp/huangxiancun_demo:${version} huangxiancun.com/15861813785/nlp/huangxiancun_demo:${version}
docker push huangxiancun.com/15861813785/nlp/huangxiancun_demo:${version}
if [ $? -eq 0 ]; then
 echo "push Success"
else
 echo "push failed"
fi