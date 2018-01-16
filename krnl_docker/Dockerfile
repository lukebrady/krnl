FROM centos:latest
RUN yum install -y gcc make git ctags ncurses-devel openssl-devel
RUN mkdir ~/krnl_workspace/
COPY ./kernels/linux-4.1.48.tar.xz /root/krnl_workspace/
RUN tar xzv /root/krnl_workspace/linux-4.1.48.tar.xz
RUN cp ./config-3.10.0-693.11.1.el7.x86_64 ./linux-4.1.48.tar.xz/.configRUN cd ~/krnl_workspace/linux-4.1.48.tar.xz; make
