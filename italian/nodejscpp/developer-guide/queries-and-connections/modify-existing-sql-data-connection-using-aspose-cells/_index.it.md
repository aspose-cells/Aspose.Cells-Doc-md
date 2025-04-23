---  
title: Modifica la connessione SQL esistente usando Aspose.Cells for Node.js via C++  
linktitle: Modificare la connessione dati SQL esistente utilizzando Aspose.Cells  
type: docs  
weight: 20  
url: /it/nodejs-cpp/modify-existing-sql-data-connection-using-aspose-cells/  
description: Impara come modificare le proprietà della connessione SQL esistente usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells supporta la modifica di una connessione dati SQL esistente. L'articolo spiegherà come utilizzare Aspose.Cells per modificare diverse proprietà di una connessione dati SQL.  
È possibile aggiungere o visualizzare le connessioni dati all'interno di Microsoft Excel seguendo il comando di menu **Dati > Connessioni**.  
Analogamente, Aspose.Cells offre strumenti per accedere e modificare le connessioni dati utilizzando la collezione Workbook.dataConnections.  
{{% /alert %}}  

## Modificare la connessione dati SQL esistente usando Aspose.Cells  

Il seguente esempio illustra l'uso di Aspose.Cells for Node.js via C++ per modificare la connessione SQL del workbook. Puoi scaricare il file Excel di origine utilizzato in questo codice e il file Excel di output generato dal codice dai link seguenti.  

- [File Excel di Origine](5112357.xlsx)  
- [File Excel di Output](5112356.xlsx)  

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

