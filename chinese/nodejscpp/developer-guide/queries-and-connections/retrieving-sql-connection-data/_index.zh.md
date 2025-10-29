---  
title: 通过 C++ 在 Node.js 中检索 SQL 连接数据  
linktitle: 检索SQL连接数据  
type: docs  
weight: 10  
url: /zh/nodejs-cpp/retrieving-sql-connection-data/  
---  

{{% alert color="primary" %}}  

Aspose.Cells可以帮助您检索SQL连接数据。这包括建立SQL服务器连接所需的所有数据，例如**服务器URL**，**用户名**，**表名**，**完整SQL查询**，**查询类型**，**表的位置**和与之关联的命名范围的**名称**。  

{{% /alert %}}  

在Microsoft Excel中，通过以下步骤连接数据库：  

1. 单击**数据**菜单，选择**来自其他源**，然后选择**来自SQL Server**。  
2. 然后选择**数据**，然后选择**连接**。  
3.使用连接向导连接到数据库并创建数据库查询。  

Aspose.Cells for Node.js via C++ 提供了 `Workbook.dataConnections` 属性，用于检索外部连接。它返回工作簿中的 ExternalConnection 对象数组。  

如果 ExternalConnection 对象包含 SQL 连接数据，则可以将其类型转换为 DBConnection 对象，并使用其属性检索数据库命令、命令类型、连接描述、连接信息、凭据等。  

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
