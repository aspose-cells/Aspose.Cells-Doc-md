---  
title: Получение данных соединения SQL с Node.js через C++  
linktitle: Получение данных подключения к SQL  
type: docs  
weight: 10  
url: /ru/nodejs-cpp/retrieving-sql-connection-data/  
---  

{{% alert color="primary" %}}  

Aspose.Cells может помочь вам получить данные подключения к SQL. Это включает все данные, необходимые для подключения к серверу SQL, например, **URL сервера**, **имя пользователя**, **имя таблицы**, **полный SQL-запрос**, **тип запроса**, **местоположение таблицы** и **имя именованного диапазона**, связанного с ним.  

{{% /alert %}}  

В Microsoft Excel подключитесь к базе данных, выполнив следующее:  

1. Нажмите меню **Данные** и выберите **Из других источников**, а затем **Из SQL Server**.  
1. Затем выберите **Данные**, а затем **Подключения**.  
1. Используйте мастер подключений для подключения к базе данных и создания запроса к базе данных.  

Aspose.Cells for Node.js via C++ предоставляет свойство `Workbook.dataConnections` для получения внешних подключений. Он возвращает массив объектов ExternalConnection в рабочей книге.  

Если объект ExternalConnection содержит данные соединения SQL, его можно привести к типу DBConnection, и его свойства можно использовать для получения команды базы данных, типа команды, описания соединения, информации о соединении, учётных данных и так далее.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "connection.xlsx");
// Create a workbook object from source file
const workbook = new AsposeCells.Workbook(filePath);

// Access the external collections
const connections = workbook.getDataConnections();
const connectionCount = connections.getCount();

let connection = null;

for (let i = 0; i < connectionCount; i++) {
connection = connections.get(i);

// Check if the Connection is DBConnection, then retrieve its various properties
if (connection.getClassType() === AsposeCells.ExternalConnectionClassType.DBConnection) {

const dbConn = connection;

// Retrieve DB Connection Command
console.log("Command: " + dbConn.getCommand());

// Retrieve DB Connection Command Type
console.log("Command Type: " + dbConn.getCommandType());

// Retrieve DB Connection Description
console.log("Description: " + dbConn.getConnectionDescription());

// Retrieve DB Connection ID
console.log("Id: " + dbConn.getId());

// Retrieve DB Connection Info
console.log("Info: " + dbConn.getConnectionString());

// Retrieve DB Connection Credentials
console.log("Credentials: " + dbConn.getCredentialsMethodType());

// Retrieve DB Connection Name
console.log("Name: " + dbConn.getName());

// Retrieve DB Connection ODC File
console.log("OdcFile: " + dbConn.getOdcFile());

// Retrieve DB Connection Source File
console.log("Source file: " + dbConn.getSourceFile());

// Retrieve DB Connection Type
console.log("Type: " + dbConn.getSourceType());

// Retrieve DB Connection Parameters Collection
const paramCollection = dbConn.getParameters();
const paramCount = paramCollection.getCount();

// Iterate the Parameter Collection
for (let j = 0; j < paramCount; j++) {
const param = paramCollection.get(j);

// Retrieve Parameter Cell Reference
console.log("Cell reference: " + param.getCellReference());

// Retrieve Parameter Name
console.log("Parameter name: " + param.getName());

// Retrieve Parameter Prompt
console.log("Prompt: " + param.getPrompt());

// Retrieve Parameter SQL Type
console.log("SQL Type: " + param.getSqlType());

// Retrieve Parameter Type
console.log("Param Type: " + param.getType());

// Retrieve Parameter Value
console.log("Param Value: " + param.getValue());
} // End for
} // End if
} // End for
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
