---  
title: Node.js経由でC++を使ってSQL接続データを取得する方法  
linktitle: SQL接続データの取得  
type: docs  
weight: 10  
url: /ja/nodejs-cpp/retrieving-sql-connection-data/  
---  

{{% alert color="primary" %}}  

Aspose.Cellsを使用して、SQL接続データを取得できます。これには、SQLサーバへの接続に必要なすべてのデータが含まれます。たとえば、**サーバーURL**、**ユーザー名**、**テーブル名**、**完全なSQLクエリ**、**クエリの種類**、**テーブルの場所**、およびそれに関連付けられた**名前付き範囲の名前**などです。  

{{% /alert %}}  

Microsoft Excelでは、データベースに接続するには:  

1. **データ**メニューをクリックし、**その他のソース**、その後 **SQL Server** を選択します。  
1. 次に、**データ**、その後 **Connections** を選択します。  
1. Connectionsウィザードを使用してデータベースに接続し、データベースクエリを作成します。  

Aspose.Cells for Node.js via C++は、外部接続を取得するための`Workbook.dataConnections`プロパティを提供します。これは、ワークブック内のExternalConnectionオブジェクトの配列を返します。  

ExternalConnectionオブジェクトにSQL接続データが含まれている場合は、DBConnectionにキャストでき、そのプロパティを使ってデータベースコマンド、コマンドタイプ、接続の説明、接続情報、認証情報などを取得できます。  

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
