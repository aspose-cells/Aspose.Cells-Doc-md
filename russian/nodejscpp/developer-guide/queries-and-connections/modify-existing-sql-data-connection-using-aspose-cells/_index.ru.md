---  
title: Изменить существующее соединение SQL данных с помощью Aspose.Cells for Node.js via C++  
linktitle: Изменение существующего SQL соединения с данными с использованием Aspose.Cells  
type: docs  
weight: 20  
url: /ru/nodejs-cpp/modify-existing-sql-data-connection-using-aspose-cells/  
description: Узнайте, как изменить свойства существующего соединения SQL данных с помощью Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Aspose.Cells поддерживает изменение существующего SQL-соединения с данными. В статье будет объяснено, как использовать Aspose.Cells для модификации различных свойств SQL-соединения с данными.  
Вы можете добавить или просмотреть соединения с данными внутри Microsoft Excel, следуя команде меню **Данные > Соединения**.  
Аналогично, Aspose.Cells предоставляет средства для доступа и изменения подключений данных с помощью коллекции Workbook.dataConnections.  
{{% /alert %}}  

## Изменение существующего SQL-соединения с данными с использованием Aspose.Cells  

Следующий пример иллюстрирует использование Aspose.Cells for Node.js via C++ для изменения соединения SQL данных рабочей книги. Вы можете скачать исходный Excel-файл, использованный в этом коде, и выходной файл Excel, созданный кодом, по следующим ссылкам.  

- [Исходный файл Excel](5112357.xlsx)  
- [Выходной файл Excel](5112356.xlsx)  

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
