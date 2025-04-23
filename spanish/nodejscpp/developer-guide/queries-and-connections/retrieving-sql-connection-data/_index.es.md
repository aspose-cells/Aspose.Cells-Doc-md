---  
title: Recuperar datos de conexión SQL con Node.js a través de C++  
linktitle: Recuperación de datos de conexión SQL  
type: docs  
weight: 10  
url: /es/nodejs-cpp/retrieving-sql-connection-data/  
---  

{{% alert color="primary" %}}  

Aspose.Cells puede ayudarte a recuperar datos de conexión SQL. Esto incluye cualquier dato necesario para realizar una conexión al servidor SQL, por ejemplo, URL del servidor, nombre de usuario, nombre de la tabla, consulta SQL completa, tipo de consulta, ubicación de la tabla y nombre del rango con nombre asociado.  

{{% /alert %}}  

En Microsoft Excel, conectarse a una base de datos mediante:  

1. Haga clic en el menú **Datos** y seleccione **Desde otras fuentes** seguido de **Desde SQL Server**.  
1. Luego seleccione **Datos** seguido de **Conexiones**.  
1. Utilice el asistente de conexiones para conectarse a la base de datos y crear una consulta de base de datos.  

Aspose.Cells for Node.js via C++ proporciona la propiedad `Workbook.dataConnections` para recuperar conexiones externas. Devuelve un array de objetos ExternalConnection en el libro de trabajo.  

Si el objeto ExternalConnection contiene datos de conexión SQL, se puede convertir al tipo DBConnection y sus propiedades se pueden usar para recuperar el comando de base de datos, tipo de comando, descripción de la conexión, información de la conexión, credenciales, y más.  

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

