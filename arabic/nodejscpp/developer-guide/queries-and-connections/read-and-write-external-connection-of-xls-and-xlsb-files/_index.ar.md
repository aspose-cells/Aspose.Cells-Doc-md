---  
title: قراءة وكتابة الاتصال الخارجي لملفات XLS و XLSB باستخدام Node.js عبر C++  
linktitle: قراءة وكتابة اتصال الخارجي لملفات XLS و XLSB  
type: docs  
weight: 80  
url: /ar/nodejs-cpp/read-and-write-external-connection-of-xls-and-xlsb-files/  
description: تعلم كيفية قراءة وكتابة الاتصالات الخارجية لملفات XLS و XLSB باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  

يدعم Aspose.Cells بالفعل قراءة وكتابة الاتصالات الخارجية لملفات XLSX، لكنه يدعم الآن أيضًا هذه الميزة لملفات XLSB و XLS. ومع ذلك، فإن الكود هو نفسه لجميع أنواع الصيغ.  

## **قراءة وكتابة اتصال خارجي لملف XLS/XLSB**  

يحمّل المثال التالي ملف XLSB العينة (يمكن تحميل XLS أيضًا) ويقرأ أول اتصال خارجي لها وهو في الواقع اتصال قاعدة بيانات Microsoft Access. ثم يغير الخاصية [**DBConnection.getName()**](https://reference.aspose.com/cells/nodejs-cpp/dbconnection/#getName--) ويحفظه كملف XLS/XLSB ناتج. يظهر لقطة الشاشة تأثير الكود على ملف [XLSB العينة](51740722.xlsb) وملف [XLSB الناتج](51740723.xlsb) بعد التنفيذ. يرجى أيضًا مراجعة المخرجات من وحدة التحكم بعد الكود للمزيد من المعلومات.  

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)  

## **الكود المثالي**  

الكود التالي سيعمل لكل من ملفات XLSB و XLS عن طريق تحميل وحفظ الملفات بامتداد مناسب.  

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

## **مخرجات الوحدة**  

{{< highlight js >}}  

Connection Name: Cust  

Command: Customer  

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
