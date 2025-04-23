---  
title: Abrufen von SQL Verbindungsdaten mit Node.js über C++  
linktitle: SQL Verbindungsdaten abrufen  
type: docs  
weight: 10  
url: /de/nodejs-cpp/retrieving-sql-connection-data/  
---  

{{% alert color="primary" %}}  

Aspose.Cells kann Ihnen helfen, SQL-Verbindungsdaten abzurufen. Dazu gehören alle Daten, die zum Herstellen einer Verbindung zum SQL-Server erforderlich sind, z. B. **Server-URL**, **Benutzername**, **Tabellenname**, **vollständige SQL-Abfrage**, **Abfragetyp**, **Speicherort der Tabelle** und **Name des benannten Bereichs**, der damit verbunden ist.  

{{% /alert %}}  

In Microsoft Excel eine Datenbankverbindung herstellen, indem Sie:  

1. Zum **Daten**-Menü gehen und **Aus anderen Quellen** gefolgt von **Vom SQL Server** auswählen.  
1. Dann **Daten** gefolgt von **Verbindungen** auswählen.  
1. Verwenden Sie den Verbindungs-Assistenten, um eine Verbindung zur Datenbank herzustellen und eine Datenbankabfrage zu erstellen.  

Aspose.Cells for Node.js via C++ bietet die Eigenschaft `Workbook.dataConnections`, um externe Verbindungen abzurufen. Es gibt ein Array von ExternalConnection-Objekten im Arbeitsbuch zurück.  

Wenn das ExternalConnection-Objekt SQL-Verbindungsdaten enthält, kann es in ein DBConnection-Objekt umgewandelt werden, und seine Eigenschaften können verwendet werden, um Datenbankbefehl, Befehlstyp, Verbindungsbeschreibung, Verbindungsinformationen, Anmeldeinformationen usw. abzurufen.  

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

