---  
title: Lecture et écriture de connexions externes de fichiers XLS et XLSB avec Node.js via C++  
linktitle: Lire et écrire des connexions externes de fichiers XLS et XLSB  
type: docs  
weight: 80  
url: /fr/nodejs-cpp/read-and-write-external-connection-of-xls-and-xlsb-files/  
description: Apprenez à lire et écrire des connexions externes de fichiers XLS et XLSB en utilisant Aspose.Cells for Node.js via C++.  
---  

## **Scénarios d'utilisation possibles**  

Aspose.Cells supporte déjà la lecture et l’écriture de connexions externes des fichiers XLSX, mais maintenant, cette fonctionnalité est également disponible pour XLSB et XLS. Cependant, le code reste identique pour tous les types de formats.  

## **Lire et écrire des connexions externes de fichiers XLS/XLSB**  

Le code suivant charge le fichier XLSB d’exemple (XLS peut également être chargé) et lit sa première connexion externe, qui est en réalité une connexion à une base de données Microsoft Access. Il modifie ensuite la propriété [**DBConnection.getName()**](https://reference.aspose.com/cells/nodejs-cpp/dbconnection/#getName--) et sauvegarde le fichier XLS/XLSB en sortie. La capture d'écran montre l’effet du code sur [le fichier XLSB d’exemple](51740722.xlsb) et [le fichier XLSB de sortie](51740723.xlsb) après son exécution. Veuillez également consulter la sortie console du code d’exemple ci-dessous pour référence.  

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)  

## **Code d'exemple**  

Le code suivant fonctionnera pour les fichiers XLSB et XLS en chargeant et en enregistrant des fichiers avec l'extension appropriée.  

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

## **Sortie console**  

{{< highlight js >}}  

Connection Name: Cust  

Command: Customer  

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
