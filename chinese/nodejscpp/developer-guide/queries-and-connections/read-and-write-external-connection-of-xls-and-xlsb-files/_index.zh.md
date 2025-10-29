---  
title: 使用Node.js和C++读写XLS和XLSB文件的外部连接  
linktitle: 读取和写入XLS和XLSB文件的外部连接  
type: docs  
weight: 80  
url: /zh/nodejs-cpp/read-and-write-external-connection-of-xls-and-xlsb-files/  
description: 学习如何使用Aspose.Cells for Node.js via C++读取和写入XLS和XLSB文件的外部连接。  
---  

## **可能的使用场景**  

Aspose.Cells已支持读取和写入XLSX文件的外部连接，现在也支持XLSB和XLS文件。然而，所有格式的代码都是相同的。  

## **读取和写入XLS/XLSB文件的外部连接**  

以下示例加载示例XLSB文件（也可以加载XLS），读取第一个外部连接，实际上是Microsoft Access数据库连接。然后修改[**DBConnection.getName()**](https://reference.aspose.com/cells/nodejs-cpp/dbconnection/#getName--)属性，并将其保存为输出的XLS/XLSB文件。截屏显示代码对[样例XLSB文件](51740722.xlsb)和[输出XLSB文件](51740723.xlsb)的效果。请参考下面的控制台输出。  

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)  

## **示例代码**  

以下代码可以加载和保存具有适当扩展名的XLSB和XLS文件。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExternalConnection_XLSB.xlsb");

// Load the source Excel Xlsb file
const workbook = new AsposeCells.Workbook(filePath);

// Read the first external connection which is actually a DB-Connection
const dbCon = workbook.getDataConnections().get(0);

// Print the Name, Command and Connection Info of the DB-Connection
console.log("Connection Name: " + dbCon.getName());
console.log("Command: " + dbCon.getCommand());
console.log("Connection Info: " + dbCon.getConnectionString());

// Modify the Connection Name
dbCon.setName("NewCust");

// Save the Excel Xlsb file
workbook.save("outputExternalConnection_XLSB.xlsb");
```  

## **控制台输出**  

{{< highlight js >}}  

Connection Name: Cust  

Command: Customer  

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
