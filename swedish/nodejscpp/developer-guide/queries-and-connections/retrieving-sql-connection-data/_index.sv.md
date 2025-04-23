---  
title: Hämta SQL anslutningsdata med Node.js via C++  
linktitle: Hämta SQL anslutningsdata  
type: docs  
weight: 10  
url: /sv/nodejs-cpp/retrieving-sql-connection-data/  
---  

{{% alert color="primary" %}}  

Aspose.Cells kan hjälpa dig att hämta SQL-anslutningsdata. Detta inkluderar all data som krävs för att göra en anslutning till SQL-servern, till exempel **server-URL**, **användarnamn**, **tabellnamn**, **full SQL-fråga**, **frågetyp**, **platsen för tabellen**, och **namnet på namngiven omfattning** som är associerat med den.  

{{% /alert %}}  

I Microsoft Excel, anslut till en databas genom att:  

1. Klicka på menyn **Data** och välj sedan **Från andra källor** följt av **Från SQL Server**.  
1. Välj sedan **Data** följt av **Anslutningar**.  
1. Använd Anslutningar-guiden för att ansluta till databasen och skapa en databasfråga.  

Aspose.Cells for Node.js via C++ tillhandahåller egenskapen `Workbook.dataConnections` för att hämta externa anslutningar. Den returnerar en array av ExternalConnection-objekt i arbetsboken.  

Om ExternalConnection-objektet innehåller SQL-anslutningsdata kan det typecastas till ett DBConnection-objekt och dess egenskaper kan användas för att hämta databaskommando, kommando Typ, anslutningsbeskrivning, anslutningsinformation, autentiseringsuppgifter och så vidare.  

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

