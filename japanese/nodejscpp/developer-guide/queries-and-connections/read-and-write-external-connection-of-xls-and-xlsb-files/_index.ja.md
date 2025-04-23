---  
title: Node.js経由でC++を使ってXLSおよびXLSBファイルの外部接続を読み書きする方法  
linktitle: XLSおよびXLSBファイルの外部接続の読み取りと書き込み  
type: docs  
weight: 80  
url: /ja/nodejs-cpp/read-and-write-external-connection-of-xls-and-xlsb-files/  
description: Aspose.Cells for Node.js via C++を使って、XLSおよびXLSBファイルの外部接続を読み書きする方法を学びます。  
---  

## **可能な使用シナリオ**  

Aspose.Cellsは既にXLSXファイルの外部接続の読み書きをサポートしていますが、今度はXLSBおよびXLSファイルもサポートします。コードはすべてのフォーマットタイプで同じです。  

## **XLS/XLSBファイルの外部接続の読み取りと書き込み**  

次のサンプルコードは、サンプルXLSBファイル（XLSもロード可能）をロードし、その最初の外部接続（実際にはMicrosoft AccessのDB接続）を読み取ります。その後、[**DBConnection.getName()**](https://reference.aspose.com/cells/nodejs-cpp/dbconnection/#getName--)プロパティを変更し、出力XLS/XLSBファイルとして保存します。スクリーンショットは、[サンプルXLSBファイル](51740722.xlsb)と[出力XLSBファイル](51740723.xlsb)のコード実行後の効果を示しています。参考のため、以下のサンプルコードのコンソール出力もご覧ください。  

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)  

## **サンプルコード**  

このコードは、適切な拡張子のファイルを読み込んで保存することにより、XLSBおよびXLSファイルの両方で動作します。  

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

## **コンソール出力**  

{{< highlight js >}}  

Connection Name: Cust  

Command: Customer  

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False  

{{< /highlight >}}  

