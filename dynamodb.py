import boto3
dynamodb = boto3.resource('dynamodb')
list(dynamodb.tables.all())

#Create Table
table = dynamodb.create_table(
TableName = 'Students',
    KeySchema = [
        {
            'AttributeName':  'StudentID',
            'KeyType': 'HASH'
        },
        {
            'AttributeName':  'Email',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions = [
        {
            'AttributeName':  'StudentID',
            'AttributeType': 'N'
        },
        
        {
            'AttributeName':  'Email',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)

#insert item
table = dynamodb.Table('Students')
table.put_item(
    Item = {
        'StudentID': 1,
        'Name': 'Temitope Ilori',
        'Email': 'temitopeii1234@gmail.com'
    },
)
table.put_item(
    Item = {
        'StudentID': 2,
        'Name': 'Joshua Kevin',
        'Email': 'joshuakevin@gmail.com'
    },
)

# Retrieve a student record 
response = table.get_item(
    Key = {
        'StudentID': 1,
        'Email': 'temitopeii1234@gmail.com'
    }
)

item = response.get('Item')

if item:
    print("Item found:", item)
else:
    print("Item not found.")

#Delete Item
table.delete_item(Key = {
        'StudentID': 1,
        'Email': 'temitopeii1234@gmail.com'})

table.delete_item(Key = {
        'StudentID': 2,
        'Email': 'joshuakevin@gmail.com'})

table.delete()