---  
title: Recupera i dati di connessione SQL con Node.js tramite C++  
linktitle: Recupero dei Dati di Connessione SQL  
type: docs  
weight: 10  
url: /it/nodejs-cpp/retrieving-sql-connection-data/  
---  

{{% alert color="primary" %}}  

Aspose.Cells può aiutarti a recuperare i dati di connessione SQL. Ciò include tutti i dati necessari per stabilire una connessione con il server SQL, ad esempio, **URL server**, **nome utente**, **nome tabella**, **query SQL completa**, **tipo di query**, **posizione della tabella**, e **nome dell'intervallo con nome** ad esso associato.  

{{% /alert %}}  

In Microsoft Excel, connettersi a un database tramite:  

1. Cliccando sul menu **Dati** e selezionando **Da Altre Origini** seguito da **Da Server SQL**.  
1. Poi selezionare **Dati** seguito da **Connessioni**.  
1. Utilizzare la procedura guidata di connessione per collegarsi al database e creare una query del database.  

Aspose.Cells for Node.js via C++ fornisce la proprietà `Workbook.dataConnections` per recuperare le connessioni esterne. Ritorna un array di oggetti ExternalConnection presenti nel workbook.  

Se l'oggetto ExternalConnection contiene dati di connessione SQL, può essere convertito al tipo DBConnection e le sue proprietà possono essere usate per recuperare comando del database, tipo di comando, descrizione della connessione, informazioni sulla connessione, credenziali, e altro ancora.  

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

