---  
title: Récupération des données de connexion SQL avec Node.js via C++  
linktitle: Récupération des données de connexion SQL  
type: docs  
weight: 10  
url: /fr/nodejs-cpp/retrieving-sql-connection-data/  
---  

{{% alert color="primary" %}}  

Aspose.Cells peut vous aider à récupérer les données de connexion SQL. Cela inclut toutes les données nécessaires pour établir une connexion avec le serveur SQL, par exemple, **URL du serveur**, **nom d'utilisateur**, **nom de la table**, **requête SQL complète**, **type de requête**, **emplacement de la table**, et **nom de la plage nommée** associée.  

{{% /alert %}}  

Dans Microsoft Excel, se connecter à une base de données en :  

1. Cliquant sur le menu **Données** et en sélectionnant **À partir d'autres sources**, puis **Depuis un serveur SQL**.  
1. Ensuite, sélectionnez **Données** suivi de **Connexions**.  
1. Utilisez l'assistant Connexions pour vous connecter à la base de données et créer une requête de base de données.  

Aspose.Cells for Node.js via C++ fournit la propriété `Workbook.dataConnections` pour récupérer les connexions externes. Elle renvoie un tableau d’objets ExternalConnection dans le classeur.  

Si l’objet ExternalConnection contient des données de connexion SQL, il peut être converti en un objet DBConnection dont on peut utiliser les propriétés pour récupérer la commande de la base de données, le type de commande, la description de la connexion, les informations sur la connexion, les identifiants, etc.  

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
