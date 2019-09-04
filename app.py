#!/usr/bin/env python3

from aws_cdk import core

from hello.hello_stack import MyStack
from my_vpc.my_vpc_stack import MyVpcStack


app = core.App()
MyStack(app, "hello-cdk-1", env={'region': 'us-east-2'})
MyStack(app, "hello-cdk-2", env={'region': 'us-west-2'})
MyVpcStack(app, "vpc-cdk-1", env={'region': 'us-west-2'})

app.synth()
