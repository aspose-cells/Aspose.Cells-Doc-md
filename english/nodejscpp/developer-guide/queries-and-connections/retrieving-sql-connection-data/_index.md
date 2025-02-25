---  
title: Retrieving SQL Connection Data with Node.js via C++  
linktitle: Retrieving SQL Connection Data  
type: docs  
weight: 10  
url: /nodejs-cpp/retrieving-sql-connection-data/  
---  

{{% alert color="primary" %}}  

Aspose.Cells can help you retrieve SQL connection data. This includes any and all data that is required to make a connection to the SQL server, for example, **server URL**, **username**, **table name**, **full SQL query**, **query type**, **location of the table**, and **name of the named range** associated with it.  

{{% /alert %}}  

In Microsoft Excel, connect to a database by:  

1. Clicking the **Data** menu and selecting **From Other Sources** followed by **From SQL Server**.  
1. Then select **Data** followed by **Connections**.  
1. Use the Connections wizard to connect to the database and create a database query.  

Aspose.Cells for Node.js via C++ provides the `Workbook.dataConnections` property for retrieving external connections. It returns an array of ExternalConnection objects in the workbook.  

If the ExternalConnection object contains SQL connection data, it can be type-cast to a DBConnection object and its properties can be used to retrieve database command, command type, connection description, connection information, credentials, and so on.  

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
  