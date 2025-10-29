---  
title: 使用Aspose.Cells for Node.js via C++修改现有SQL数据连接  
linktitle: 使用Aspose.Cells修改现有的SQL数据连接  
type: docs  
weight: 20  
url: /zh/nodejs-cpp/modify-existing-sql-data-connection-using-aspose-cells/  
description: 学习如何使用Aspose.Cells for Node.js via C++修改现有SQL数据连接属性。  
---  

{{% alert color="primary" %}}  
Aspose.Cells支持修改现有的SQL数据连接。本文将解释如何使用Aspose.Cells修改SQL数据连接的不同属性。  
你可以通过**数据 > 连接**菜单命令在Microsoft Excel中添加或查看数据连接。  
同样，Aspose.Cells提供了访问和修改数据连接的方法，使用Workbook.dataConnections集合。  
{{% /alert %}}  

## 使用Aspose.Cells修改现有的SQL数据连接  

以下示例演示如何使用Aspose.Cells for Node.js via C++修改工作簿的SQL数据连接。你可以从以下链接下载示例中使用的源Excel文件和由代码生成的输出Excel文件。  

- [源Excel文件](5112357.xlsx)  
- [输出Excel文件](5112356.xlsx)  

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
