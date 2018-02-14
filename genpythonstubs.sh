#!/bin/bash
echo "Use Parameres: $0 $PWD <Name Of Proto file without.proto extension>"
GOARCH="amd64"
GOBIN=""
GOEXE=""
GOHOSTARCH="amd64"
GOHOSTOS="darwin"
GOOS="darwin"
GOPATH="$HOME/go"
GOPATH1="./go"
GORACE=""
GOROOT="/usr/local/go"
GOTOOLDIR="/usr/local/go/pkg/tool/darwin_amd64"
GCCGO="gccgo"
CC="clang"
GOGCCFLAGS="-fPIC -m64 -pthread -fno-caret-diagnostics -Qunused-arguments -fmessage-length=0 -fdebug-prefix-map=/var/folders/f0/3j431hfx0fjfqhg6qgynhkjr0000gn/T/go-build312654531=/tmp/go-build -gno-record-gcc-switches -fno-common"
CXX="clang++"
CGO_ENABLED="1"
CGO_CFLAGS="-g -O2"
CGO_CPPFLAGS=""
CGO_CXXFLAGS="-g -O2"
CGO_FFLAGS="-g -O2"
CGO_LDFLAGS="-g -O2"
PKG_CONFIG="pkg-config"

#/usr/local/bin/protoc -I$1 \
#  -I$GOPATH1/src \
#  -I$GOPATH1/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
#  --python_out=plugins=grpc:. \
#  `pwd`/$2.proto

#/usr/local/bin/protoc -I$1 \
#  -I$GOPATH1/src \
#  -I$GOPATH1/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
#  --grpc-gateway_out=logtostderr=true:. \
#  $2.proto

/usr/local/bin/protoc -I$1 \
  -I$GOPATH1/src \
  -I$GOPATH1/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
  --swagger_out=logtostderr=true:. \
  $2.proto

rm -rf pythonout
/usr/local/bin/swagger-codegen generate -i $2.swagger.json -l python-flask -o $2
#(cd $2;/usr/local/bin/python3 -m swagger_server)
(cd $2;/usr/local/bin/docker build -t simple .;/usr/local/bin/docker run -it -p 9999:8080 Simple)
