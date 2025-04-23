---  
title: C++ kullanarak Node.js ile XLS ve XLSB dosyalarının Harici Bağlantılarını Okuma ve Yazma  
linktitle: XLS ve XLSB dosyalarının Dış Bağlantısını Okuma ve Yazma  
type: docs  
weight: 80  
url: /tr/nodejs-cpp/read-and-write-external-connection-of-xls-and-xlsb-files/  
description: Aspose.Cells for Node.js via C++ kullanarak XLS ve XLSB dosyalarının harici bağlantılarını nasıl okuyup yazacağınızı öğrenin.  
---  

## **Olası Kullanım Senaryoları**  

Aspose.Cells, XLSX dosyalarının harici bağlantılarını okuma ve yazma desteğini zaten sağlar, ancak şimdi XLSB ve XLS dosyaları için de bu özelliği destekler. Ancak, kod tüm format türleri için aynıdır.  

## **XLS/XLSB Dosyasının Dış Bağlantısını Okuma ve Yazma**  

Aşağıdaki örnek kod, örnek XLSB dosyasını yükler (XLS de yüklenebilir) ve aslında bir Microsoft Access DB Bağlantısı olan ilk harici bağlantıyı okur. Daha sonra, [**DBConnection.getName()**](https://reference.aspose.com/cells/nodejs-cpp/dbconnection/#getName--) özelliğini değiştirir ve çıktıyı XLS/XLSB dosyası olarak kaydeder. Ekran görüntüsü, kodun çalışması sonrası [örnek XLSB dosyası](51740722.xlsb) ve [çıkış XLSB dosyası](51740723.xlsb) üzerindeki etkisini gösterir. Lütfen aşağıdaki örnek kodun konsol çıkışını da referans için inceleyin.  

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)  

## **Örnek Kod**  

Aşağıdaki kod, uygun uzantısıyla dosyaların yüklenmesini ve kaydedilmesini sağlayarak hem XLSB hem de XLS dosyaları için çalışacaktır.  

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

## **Konsol Çıktısı**  

{{< highlight js >}}  

Connection Name: Cust  

Command: Customer  

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False  

{{< /highlight >}}  

