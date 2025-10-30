---  
title: Läs och skriv externa anslutningar av XLS och XLSB filer med Node.js via C++  
linktitle: Läs och skriv extern anslutning för XLS och XLSB filer  
type: docs  
weight: 80  
url: /sv/nodejs-cpp/read-and-write-external-connection-of-xls-and-xlsb-files/  
description: Lär dig hur man läser och skriver externa anslutningar av XLS och XLSB filer med Aspose.Cells for Node.js via C++.  
---  

## **Möjliga användningsscenario**  

Aspose.Cells stöder redan att läsa och skriva externa anslutningar av XLSX-filer, men nu stödjer den även denna funktion för XLSB- och XLS-filer. Koden är densamma för alla format.  

## **Läs och skriv extern anslutning för XLS/XLSB-fil**  

Följande exempel laddar en exempel XLSB-fil (XLS kan också laddas) och läser dess första externa anslutning, som är en Microsoft Access DB-anslutning. Den modifierar sedan `[**DBConnection.getName()**](https://reference.aspose.com/cells/nodejs-cpp/dbconnection/#getName--)`-egenskapen och sparar den som en output XLS/XLSB-fil. Skärmbilden visar effekten av koden på [exempel XLSB-fil](51740722.xlsb) och [utdata XLSB-fil](51740723.xlsb) efter körning. Se även konsolutmatningen nedan för referens.  

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)  

## **Exempelkod**  

Följande kod ska fungera för både XLSB- och XLS-filer genom att ladda och spara filer med rätt tillägg.  

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

## **Konsoloutput**  

{{< highlight js >}}  

Connection Name: Cust  

Command: Customer  

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
