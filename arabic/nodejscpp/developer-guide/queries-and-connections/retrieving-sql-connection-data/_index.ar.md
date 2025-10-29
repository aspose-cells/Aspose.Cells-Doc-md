---  
title: استرجاع بيانات اتصال SQL باستخدام Node.js عبر C++  
linktitle: إسترداد بيانات اتصال SQL  
type: docs  
weight: 10  
url: /ar/nodejs-cpp/retrieving-sql-connection-data/  
---  

{{% alert color="primary" %}}  

يمكن لـ Aspose.Cells مساعدتك في استرداد بيانات اتصال SQL. يشمل ذلك أي وكل البيانات المطلوبة للاتصال بخادم SQL، على سبيل المثال، **رابط الخادم**, **اسم المستخدم**, **اسم الجدول**, **استعلام SQL كامل**, **نوع الاستعلام**, **موقع الجدول**, و**اسم النطاق المسمى** المرتبط به.  

{{% /alert %}}  

في برنامج Microsoft Excel، الاتصال بقاعدة بيانات عن طريق:  

1. النقر على القائمة **البيانات** واختيار **من مصادر أخرى** تلاها **من خادم SQL**.  
1. ثم اختيار **البيانات** تلاها **اتصالات**.  
1. استخدام معالج الاتصالات للاتصال بقاعدة البيانات وإنشاء استعلام قاعدة البيانات.  

Aspose.Cells for Node.js via C++ يوفر خاصية `Workbook.dataConnections` لاسترجاع الاتصالات الخارجية. وهي تُرجع مصفوفة من كائنات ExternalConnection في المصنف.  

إذا تضمن كائن ExternalConnection بيانات اتصال SQL، يمكن تحويل نوعه إلى كائن DBConnection، ويمكن استخدام خصائصه لاسترداد أمر قاعدة البيانات، نوع الأمر، وصف الاتصال، معلومات الاتصال، بيانات الاعتماد، وغيرها.  

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
