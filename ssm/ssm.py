import os
import json
import argparse
import boto3

def get_params(env, arg):
    session = boto3.Session(profile_name=env)
    client = session.client('ssm')

    response = client.get_parameters_by_path(
        Path=f'/{env}/',
        Recursive=True,
        WithDecryption=True
    )

    all_params = response['Parameters']

    while 'NextToken' in response:
        response = client.get_parameters_by_path(
            Path=f'/{env}/',
            Recursive=True,
            WithDecryption=True,
            NextToken=response['NextToken']
        )
        all_params += response['Parameters']

    for p in all_params:
        if arg == None or arg in p['Name']:
            print("%s: [%s]" % (p['Name'], p['Value'])) 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get Parameters from SSM in AWS for Relevant Environment')
    parser.add_argument('-e', help='Environment: dev, qa or prod')
    parser.add_argument('-a', help='Argument to grep for')
    args = parser.parse_args()

    get_params(args.e, args.a)
