import boto3


def ch1(key, secret):
    client = boto3.client('iam',aws_access_key_id=key,aws_secret_access_key=secret)
    response = client.get_account_summary()
    temp=response.get("SummaryMap")

    
    if((temp.get("AccountMFAEnabled"))==0):
        return {'message': "Success",'flag':"blahblahblah"}
    else:
        return {'message': "Failed"}



if __name__ == "__main__":
    try:
        
        print ("Successful")
        
    finally:
        print("Exiting.....")