---  
title: Ändra befintlig SQL dataanslutning med Aspose.Cells for Node.js via C++  
linktitle: Modifiera befintlig SQL Data Connection med hjälp av Aspose.Cells  
type: docs  
weight: 20  
url: /sv/nodejs-cpp/modify-existing-sql-data-connection-using-aspose-cells/  
description: Lär dig hur du modifierar egenskaper för befintlig SQL dataanslutning med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells stöder att ändra befintlig SQL Data Connection. Artikeln förklarar hur man använder Aspose.Cells för att ändra olika egenskaper hos SQL Data Connection.  
Du kan lägga till eller se dataanslutningar inne i Microsoft Excel genom att följa menyn **Data > Connections**.  
På samma sätt ger Aspose.Cells möjlighet att komma åt och modifiera datakonnectioner med hjälp av Workbook.dataConnections-collectionen.  
{{% /alert %}}  

## Modifiera befintlig SQL Data Connection med hjälp av Aspose.Cells  

Följande exempel visar användningen av Aspose.Cells for Node.js via C++ för att modifiera SQL-dataanslutningen i arbetsboken. Du kan ladda ner källexcelfilen som används i koden och den genererade excelfilen från följande länkar.  

- [Käll-Excel-fil](5112357.xlsx)  
- [Utdata-Excel-fil](5112356.xlsx)  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
