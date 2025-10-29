---  
title: تعديل اتصال بيانات SQL موجود باستخدام Aspose.Cells for Node.js via C++  
linktitle: تعديل اتصال البيانات الحالي باستخدام Aspose.Cells  
type: docs  
weight: 20  
url: /ar/nodejs-cpp/modify-existing-sql-data-connection-using-aspose-cells/  
description: تعلم كيفية تعديل خصائص اتصال بيانات SQL موجود باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
تدعم Aspose.Cells تعديل اتصالات SQL الحالية. سيشرح المقال كيفية استخدام Aspose.Cells لتعديل خصائص مختلفة لاتصالات SQL البيانات.  
يمكنك إضافة أو رؤية اتصالات البيانات داخل Microsoft Excel باستخدام أمر القائمة الخاص بالبيانات > اتصالات.  
وبالمثل، يوفر Aspose.Cells الوسائل للوصول وتعديل.connections عن طريق مجموعة بيانات المصنف.  
{{% /alert %}}  

## تعديل اتصال البيانات الحالي باستخدام Aspose.Cells  

يوضح المثال التالي استخدام Aspose.Cells for Node.js via C++ لتعديل اتصال SQL الخاص بالمصنف. يمكنك تحميل ملف Excel المصدر المستخدم في هذا الكود وملف Excel الناتج من خلال الروابط التالية.  

- [ملف Excel المصدر](5112357.xlsx)  
- [ملف Excel الناتج](5112356.xlsx)  

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
