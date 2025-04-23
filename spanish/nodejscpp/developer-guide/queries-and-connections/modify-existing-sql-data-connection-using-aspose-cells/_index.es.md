---  
title: Modificar la conexión de datos SQL existente usando Aspose.Cells for Node.js via C++  
linktitle: Modificar una Conexión de Datos SQL existente utilizando Aspose.Cells  
type: docs  
weight: 20  
url: /es/nodejs-cpp/modify-existing-sql-data-connection-using-aspose-cells/  
description: Aprende cómo modificar las propiedades de la conexión de datos SQL existente usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells permite modificar una Conexión de Datos SQL existente. El artículo explicará cómo usar Aspose.Cells para modificar diferentes propiedades de una Conexión de Datos SQL.  
Puedes añadir o ver Conexiones de Datos dentro de Microsoft Excel siguiendo el comando de menú **Datos > Conexiones**.  
De manera similar, Aspose.Cells proporciona los medios para acceder y modificar las conexiones de datos utilizando la colección Workbook.dataConnections.  
{{% /alert %}}  

## Modificar una conexión de datos SQL existente usando Aspose.Cells  

El siguiente ejemplo ilustra el uso de Aspose.Cells for Node.js via C++ para modificar la conexión de datos SQL del libro de trabajo. Puedes descargar el archivo Excel fuente utilizado en este código y el archivo Excel de salida generado por el código desde los siguientes enlaces.  

- [Archivo de Excel Fuente](5112357.xlsx)  
- [Archivo de Excel de Salida](5112356.xlsx)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "DataConnection.xlsx"));


// Access first Data Connection
const conn = workbook.getDataConnections().get(0);

// Change the Data Connection Name and Odc file
conn.setName("MyConnectionName");
conn.setOdcFile("C:\\Users\\MyDefaulConnection.odc");

// Change the Command Type, Command and Connection String
const dbConn = conn;
dbConn.setCommandType(AsposeCells.OLEDBCommandType.SqlStatement);
dbConn.setCommand("Select * from AdminTable");
dbConn.setConnectionString("Server=myServerAddress;Database=myDataBase;User ID=myUsername;Password=myPassword;Trusted_Connection=False");

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

