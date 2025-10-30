---  
title: Ein und Auslesen externer Verbindungen von XLS und XLSB Dateien mit Node.js über C++  
linktitle: Externe Verbindung von XLS und XLSB Dateien lesen und schreiben  
type: docs  
weight: 80  
url: /de/nodejs-cpp/read-and-write-external-connection-of-xls-and-xlsb-files/  
description: Erfahren Sie, wie Sie mit Aspose.Cells for Node.js via C++ externe Verbindungen von XLS und XLSB Dateien lesen und schreiben.  
---  

## **Mögliche Verwendungsszenarien**  

Aspose.Cells unterstützt bereits das Lesen und Schreiben externer Verbindungen von XLSX-Dateien, jetzt aber auch für XLSB- und XLS-Dateien. Der Code bleibt für alle Formate gleich.  

## **Externe Verbindung von XLS/XLSB-Dateien lesen und schreiben**  

Das folgende Beispiel lädt eine Beispiel-XLSB-Datei (XLS kann ebenfalls geladen werden) und liest ihre erste externe Verbindung, die tatsächlich eine Microsoft Access-Datenbankverbindung ist. Es ändert dann die Eigenschaft [**DBConnection.getName()**](https://reference.aspose.com/cells/nodejs-cpp/dbconnection/#getName--) und speichert die Datei als Ausgabe XLS/XLSB. Das Screenshots zeigt die Wirkung des Codes auf die [Beispiel-XLSB-Datei](51740722.xlsb) und die [Ausgabedatei XLSB](51740723.xlsb) nach der Ausführung. Bitte sehen Sie auch die Konsolenausgabe des Beispiels unten zur Referenz.  

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)  

## **Beispielcode**  

Der folgende Code funktioniert sowohl für XLSB- als auch für XLS-Dateien, indem die Dateien mit der entsprechenden Erweiterung geladen und gespeichert werden.  

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

## **Konsolenausgabe**  

{{< highlight js >}}  

Connection Name: Cust  

Command: Customer  

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
