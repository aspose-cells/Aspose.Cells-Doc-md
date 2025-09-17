##Smartly Importing JSON into Excel With Smart Markers
## **Why Using Json Data for Smart Markers**
Why Use JSON Data as Original Data for Smart Markers?
JSON (JavaScript Object Notation) is a lightweight, human-readable data interchange format that's ideal for structuring hierarchical data. Here’s why it’s well-suited as original data for smart markers (dynamic placeholders that auto-populate spreadsheets, documents, or dashboards):
1. Structured & Hierarchical Data Support
JSON natively supports nested objects and arrays (e.g., { "user": { "name": "Alice", "orders": [ ... ] } }). Smart markers can traverse this hierarchy (e.g., {{user.orders[0].price}}), making it easy to map complex data to templates.
2. Language and Platform Agnostic
JSON parsers exist in virtually all programming languages (Python, JavaScript, Java, etc.). Tools like Excel Power Query, Google Apps Script, or no-code platforms (e.g., Airtable) seamlessly ingest JSON.
3. API-Friendly
Most modern APIs (e.g., REST, GraphQL) return data in JSON format. Smart markers can directly consume live JSON from web services, enabling real-time data updates (e.g., stock prices, weather).
4. Human-Readable & Debuggable
JSON’s plain-text structure is easy to: Validate (e.g., using JSONLint). Edit manually or via scripts. Debug when mapping data to markers.
5. Scalability & Flexibility
Add/remove fields in JSON without breaking existing smart markers (if optional fields are handled gracefully). Supports diverse data types: strings, numbers, booleans, arrays, and objects.
6. Ecosystem Compatibility
Works with modern data tools: Databases: MongoDB, PostgreSQL (JSONB), etc. Automation tools: Zapier, Integromat. Data pipelines: Apache NiFi, Talend.
## **Using Excel Nested Template with JSON Data**
Aspose.Cells for .NET supports json data in smart markers, json data can be nested hierarchically. Please check [template file](smartmarker.xlsx), [json file](smartmarker.json) and the screenshot of the output excel file generated with the following code.
|**The first worksheet of the smartmarker.xlsx file showing smart markers.**|
| :- |
|![todo:image_alt_text](jsontemplate.png)|
|**The screenshot of the output excel file.**|
| :- |
|![todo:image_alt_text](jsonresult.png)|
Json data as follows:
```json data
{
"EntityCin" : "EntityCin Test",
"EntityName" : "EntityName Test",
"FirstName" : "FirstName Test",
"MiddleName" : "MiddleName Test",
"LastName" : "LastName Test",
"DOB" : "2025-02-08",
"SSN" : "11111111",
"Directors" : [
{
"id" : "director id 1",
"FirstName" : "director first 1",
"MiddleName" : "director middle 1",
"LastName" : "director last 1",
"Reportees" : [
{
"id" : "aaa",
"FirstName" : "first aaa",
"MiddleName" : "middle aaa",
"LastName" : "last aaa",
"Department" : "aaa department",
"City" : "aaa city",
"GST" : "Yes",
"ITR" : "No"
},
{
"id" : "bbb",
"FirstName" : "first bbb",
"MiddleName" : "middle bbb",
"LastName" : "last bbb",
"Department" : "bbb department",
"City" : "bbb city",
"GST" : "Yes",
"ITR" : "Yes"
},
{
"id" : "ccc",
"FirstName" : "first ccc",
"MiddleName" : "middle ccc",
"LastName" : "last ccc",
"Department" : "ccc department",
"City" : "ccc city",
"GST" : "No",
"ITR" : "No"
}
]
},
{
"id" : "director id 2",
"FirstName" : "director first 2",
"MiddleName" : "director middle 2",
"LastName" : "director last 2",
"Reportees" : [
{
"id" : "eee",
"FirstName" : "first eee",
"MiddleName" : "middle eee",
"LastName" : "last eee",
"Department" : "eee department",
"City" : "eee city",
"GST" : "Yes",
"ITR" : "No"
},
{
"id" : "fff",
"FirstName" : "first fff",
"MiddleName" : "middle fff",
"LastName" : "last fff",
"Department" : "fff department",
"City" : "fff city",
"GST" : "No",
"ITR" : "No"
}
]
}
]
}
```
The example that follows shows how this works.
## **Using Excel Subtotal Template with JSON Data**
Aspose.Cells for .NET supports json data in smart markers, json data can be nested hierarchically. Subtotal was used for data statistics in the excel template. Please check [template file](jsonExcelTemplate.xlsx), [json file](jsonData.json) and the screenshot of the output excel file generated with the following code.
|**The first worksheet of the jsonExcelTemplate.xlsx file showing smart markers.**|
| :- |
|![todo:image_alt_text](jsontemplate2.png)|
|**The screenshot of the output excel file.**|
| :- |
|![todo:image_alt_text](jsonresult2.png)|
Json data as follows:
```json data
{
"number": 10,
"test": "test abc",
"date": "2011-10-05T14:48:00.000Z",
"arrayNumber": [1,2,3,4,5],
"arrayWords": ["x1","xy2","yz3","z4"],
"arrayOfObjects": [
{"valNumber":12,"valString": "aa"},
{"valNumber":15,"valString": "bb"},
{"valNumber":1,"valString": "cc"},
{"valNumber":20,"valString": "dd"}
],
"nestedArray": [
{"valNumber":12,"valString": "xy","nestArr": [{"val": 1,"some": "aa"}]},
{"valNumber":15,"valString": "y","nestArr": [{"val": 2,"some": "bb"}]},
{"valNumber":1,"valString": "yz","nestArr": [{"some": "cc"}]},
{"valNumber":20,"valString": "z","nestArr": [{"some": "dd"}]}
],
"Products": [
{ "ProductID": "A101", "ProductName": "Apples", "Units": 5 },
{ "ProductID": "A101", "ProductName": "Apples", "Units": 10 },
{ "ProductID": "B202", "ProductName": "Bananas", "Units": 7 },
{ "ProductID": "B202", "ProductName": "Bananas", "Units": 3 },
{ "ProductID": "C303", "ProductName": "Cherries", "Units": 8 }
]
}
```
The example that follows shows how this works.
