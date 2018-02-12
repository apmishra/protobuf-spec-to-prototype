#Pre-Requisite Installations 
#1. go is installed
go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway
go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger
go get -u github.com/golang/protobuf/protoc-gen-go
#2. protoc is installed
#3. grpc gateway is installed
#4.swagger-codegen is installed


##Step2 Create Protobuf FIle for Service called Simple

1.Ensure you have a Simple.proto file created having the protobuf spec for your service
#Code 

        syntax = "proto3";
        package Simple;
        
        import "google/api/annotations.proto";
        message SearchParameters {
            StringMessage sm=1;
            Classifier p=2;
        }
        /*Default Return*/
         message StringMessage {
           string key=1;
           string value = 2;
         }
        /*KVPair*/
         message KVPair {
           string key=1;
           string value = 2;
         }
        /*KVPairs*/
         message KVPairs {
             repeated KVPair kv_pairs=1;
         }
        
        /*Classifier*/
        message Classifier {
            string id=1;
            string runtime_url=2;
            string creator=3;
            string classifier_type=4;
            string cluster=5;
            string name_space=6;
            KVPairs kv_pairs=7;
         }
        
        /*Classifier*/
        message Classifiers {
            repeated Classifier classifiers=1;
         }
        
        message Plugin {
            string id=1;
            string creator=2;
            string type=3;
            string name_space=4;
            KVPairs kv_pairs=5;
         }
        message Plugins {
            repeated Plugin plugins=1;
        }
        
        
         service Simple {
          rpc ListAll(SearchParameters) returns (Plugins) {
            option (google.api.http) = {
              get: "/v1/simple/listplugins"
            };
          }
        
          rpc ListClassifier(SearchParameters) returns (Classifiers) {
            option (google.api.http) = {
              get: "/v1/simple/listclassifier"
            };
          }
          rpc CreateClassifier(Classifier) returns (Classifiers) {
            option (google.api.http) = {
              post: "/v2/simple/createclassifier"
              body: "*"
            };
          }
         }

##Step3 run the example against the Service
./runexample.sh