---  
title: Leggi e scrivi la connessione esterna di file XLS e XLSB con Node.js tramite C++  
linktitle: Leggere e Scrivere Connessioni Esterne di file XLS e XLSB  
type: docs  
weight: 80  
url: /it/nodejs-cpp/read-and-write-external-connection-of-xls-and-xlsb-files/  
description: Impara come leggere e scrivere le connessioni esterne di file XLS e XLSB usando Aspose.Cells for Node.js via C++.  
---  

## **Possibili Scenari di Utilizzo**  

Aspose.Cells supporta già la lettura e scrittura delle connessioni esterne di file XLSX, ma ora supporta questa funzionalità anche per XLSB e XLS. Tuttavia, il codice è uguale per tutti i tipi di formato.  

## **Leggere e Scrivere Connessioni Esterne di file XLS/XLSB**  

Il seguente esempio di codice carica il file XLSB di esempio (può essere caricato anche XLS) e legge la prima connessione esterna, effettivamente una Connessione Database di Access Microsoft. Quindi modifica la proprietà [**DBConnection.getName()**](https://reference.aspose.com/cells/nodejs-cpp/dbconnection/#getName--) e la salva come file XLS/XLSB di output. Lo screenshot mostra l'effetto del codice sul [file XLSB di esempio](51740722.xlsb) e sul [file XLSB di output](51740723.xlsb) dopo l'esecuzione. Vedi anche l'output della console del codice di esempio qui sotto come riferimento.  

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)  

## **Codice di Esempio**  

Il seguente codice funzionerà sia per i file XLSB che per i file XLS, caricando e salvando i file con l'estensione appropriata.  

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

## **Output della console**  

{{< highlight js >}}  

Connection Name: Cust  

Command: Customer  

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
