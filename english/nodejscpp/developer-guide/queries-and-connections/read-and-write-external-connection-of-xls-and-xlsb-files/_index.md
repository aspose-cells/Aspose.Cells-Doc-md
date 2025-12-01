---  
title: Read and Write External Connection of XLS and XLSB files with Node.js via C++  
linktitle: Read and Write External Connection of XLS and XLSB files  
type: docs  
weight: 80  
url: /nodejs-cpp/read-and-write-external-connection-of-xls-and-xlsb-files/  
description: Learn how to read and write external connections of XLS and XLSB files using Aspose.Cells for Node.js via C++.  
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**  

Aspose.Cells already supports reading and writing external connections of XLSX files but now, it also supports this feature for XLSB and XLS files. However, the code is the same for all types of formats.  

## **Read and Write External Connection of XLS/XLSB file**  

The following sample code loads the sample XLSB file (XLS can also be loaded) and reads its first external connection which is actually a Microsoft Access DB Connection. It then modifies the [**DBConnection.getName()**](https://reference.aspose.com/cells/nodejs-cpp/dbconnection/#getName--) property and saves it as output XLS/XLSB file. The screenshot shows the effect of code on [sample XLSB file](51740722.xlsb) and [output XLSB file](51740723.xlsb) after its execution. Please also see the console output of the sample code given below for a reference.  

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)  

## **Sample Code**  

The following code shall work for both XLSB and XLS files by loading and saving files with the appropriate extension.  

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

## **Console Output**  

{{< highlight js >}}  

Connection Name: Cust  

Command: Customer  

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False  

{{< /highlight >}}  
  
{{< app/cells/assistant language="nodejs-cpp" >}}
