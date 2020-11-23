FROM centos:7.6.1810
ENV PATH $PATH:/usr/local/python3/bin/
ENV PYTHONIOENCODING utf-8
RUN set -ex \
        && mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup \
        && curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo \
        && yum makecache \
        && sed -i -e '/mirrors.cloud.aliyuncs.com/d' -e '/mirrors.aliyuncs.com/d' /etc/yum.repos.d/CentOS-Base.repo \
        && yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make wget \
        && yum clean all \
        && mkdir /usr/local/python3 \
        && wget http://npm.taobao.org/mirrors/python/3.6.8/Python-3.6.8.tar.xz \
        && tar -xvJf  Python-3.6.8.tar.xz && rm -f Python-3.6.8.tar.xz \
        && cd Python-3.6.8 \
        && ./configure prefix=/usr/local/python3 \
        && make && make install \
        && cd .. \
        && rm -rf Python-3.6.8 \
        && mv /usr/bin/python /usr/bin/python.bak \
        && ln -s /usr/local/python3/bin/python3.6m /usr/bin/python \
        && ln -s /usr/local/python3/bin/pip3 /usr/bin/pip

COPY service /opt/huangxiancun_demo/service
COPY requirements.txt /opt/huangxiancun_demo/requirements.txt
RUN python -V
RUN pip install --upgrade pip -i https://pypi.douban.com/simple
RUN pip -V
RUN cd /opt/huangxiancun_demo/ && \
    pip install -r requirements.txt -i https://pypi.douban.com/simple

VOLUME /opt/huangxiancun_demo
ENV BASE_PATH=/opt/huangxiancun_dmeo/service
WORKDIR $BASE_PATH

