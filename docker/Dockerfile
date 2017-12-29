FROM centos:latest
RUN yum install -y gcc make git ctags ncurses-devel openssl-devel
RUN mkdir ~/krnl_workspace/
COPY /etc/krnl/kernel-deploy/kernels/linux-4.1.48.tar.xz ~/krnl_workspace/
