---  
title: Чтение и запись внешних подключений XLS и XLSB файлов с Node.js через C++  
linktitle: Чтение и запись внешнего соединения файлов XLS и XLSB  
type: docs  
weight: 80  
url: /ru/nodejs-cpp/read-and-write-external-connection-of-xls-and-xlsb-files/  
description: Узнайте, как читать и записывать внешние подключения XLS и XLSB файлов с помощью Aspose.Cells for Node.js via C++.  
---  

## **Возможные сценарии использования**  

Aspose.Cells уже поддерживает чтение и запись внешних подключений XLSX файлов, а теперь также поддерживает эти функции для XLSB и XLS файлов. Однако код для всех типов форматов одинаков.  

## **Чтение и запись внешнего соединения файлов XLS/XLSB**  

Следующий пример кода загружает пример XLSB файла (также можно загрузить XLS) и читает его первое внешнее подключение, которое фактически является подключением к базе данных Microsoft Access. Затем он изменяет свойство [**DBConnection.getName()**](https://reference.aspose.com/cells/nodejs-cpp/dbconnection/#getName--) и сохраняет его как выходной файл XLS/XLSB. Скриншот показывает эффект работы кода на [примере XLSB файла](51740722.xlsb) и [выходном XLSB файле](51740723.xlsb) после его выполнения. Также смотрите вывод в консоль примера кода, приведённый ниже для справки.  

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)  

## **Образец кода**  

Следующий код будет работать как для файлов XLSB, так и для файлов XLS, загружая и сохраняя файлы с соответствующим расширением.  

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

## **Вывод в консоль**  

{{< highlight js >}}  

Connection Name: Cust  

Command: Customer  

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
