---  
title: Bestehende SQL Datenverbindung mit Aspose.Cells for Node.js via C++ ändern  
linktitle: Bereits bestehende SQL Datenverbindung mithilfe von Aspose.Cells ändern  
type: docs  
weight: 20  
url: /de/nodejs-cpp/modify-existing-sql-data-connection-using-aspose-cells/  
description: Erfahren Sie, wie Sie die Eigenschaften bestehender SQL Datenverbindungen mit Aspose.Cells for Node.js via C++ ändern.  
---  

{{% alert color="primary" %}}  
Aspose.Cells unterstützt das Ändern einer bereits bestehenden SQL-Datenverbindung. Der Artikel erläutert, wie Aspose.Cells verwendet wird, um verschiedene Eigenschaften einer SQL-Datenverbindung zu ändern.  
Sie können Datenverbindungen in Microsoft Excel hinzufügen oder anzeigen, indem Sie den Menübefehl **Daten > Verbindungen** befolgen.  
Ähnlich ermöglicht Aspose.Cells den Zugriff auf und die Änderung der Datenverbindungen mithilfe der Sammlung Workbook.dataConnections.  
{{% /alert %}}  

## Ändern einer bestehenden SQL-Datenverbindung mit Aspose.Cells  

Das folgende Beispiel zeigt die Verwendung von Aspose.Cells for Node.js via C++, um die SQL-Datenverbindung des Arbeitsbuchs zu ändern. Sie können die in diesem Code verwendete Quelldatei Excel und die vom Code generierte Ausgabedatei hier herunterladen.  

- [Quelldatei](5112357.xlsx)  
- [Ausgabedatei](5112356.xlsx)  

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
