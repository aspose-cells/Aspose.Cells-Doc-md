---  
title: Node.js ve C++ kullanarak SQL Bağlantı Verisini Getirme  
linktitle: SQL Bağlantı Verilerini Almak  
type: docs  
weight: 10  
url: /tr/nodejs-cpp/retrieving-sql-connection-data/  
---  

{{% alert color="primary" %}}  

Aspose.Cells, SQL bağlantı verilerini almanıza yardımcı olabilir. Bu, SQL sunucusuna bağlantı kurmak için gereken tüm veriyi içerir; örneğin, **sunucu URL'si**, **kullanıcı adı**, **tablo adı**, **tam SQL sorgusu**, **sorgu türü**, **tablonun yeri** ve onunla ilişkilendirilmiş **adlandırılmış aralığın adı**.  

{{% /alert %}}  

Microsoft Excel'de, bir veritabanına bağlanmak için:  

1. **Veri** menüsünü tıklayın ve **Diğer Kaynaklardan, SQL Server'dan** ardından **Veri Al**'ı seçin.  
1. Ardından **Veri**'yi ve ardından **Bağlantılar**'ı seçin.  
1. Bağlantı sihirbazını kullanarak veritabanına bağlanın ve bir veritabanı sorgusu oluşturun.  

Aspose.Cells for Node.js via C++, çalışma kitabındaki harici bağlantıları almak için `Workbook.dataConnections` özelliğini sağlar. Çalışma kitabında ExternalConnection nesneleri dizisi döner.  

Eğer ExternalConnection nesnesi SQL bağlantı verisi içeriyorsa, bir DBConnection nesnesine tür dönüştürülüp özellikleri kullanılarak veritabanı komutu, komut tipi, bağlantı açıklaması, bağlantı bilgileri, kimlik bilgileri vb. alınabilir.  

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

