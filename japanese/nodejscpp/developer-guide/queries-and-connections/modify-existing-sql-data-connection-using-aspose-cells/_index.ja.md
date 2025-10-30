---  
title: 既存のSQLデータ接続をAspose.Cells for Node.js via C++を使って変更する  
linktitle: 既存のSQLデータ接続をAspose.Cellsを使用して変更する  
type: docs  
weight: 20  
url: /ja/nodejs-cpp/modify-existing-sql-data-connection-using-aspose-cells/  
description: Aspose.Cells for Node.js via C++を使用して、既存のSQLデータ接続のプロパティを変更する方法を学びます。  
---  

{{% alert color="primary" %}}  
Aspose.Cellsは既存のSQLデータ接続を変更する機能をサポートしています。この記事では、Aspose.Cellsを使用してSQLデータ接続のさまざまなプロパティを変更する方法について説明します。  
Microsoft Excel内のデータ接続を追加または参照するには、**データ > 接続** メニューコマンドに従ってください。  
同様に、Aspose.CellsはWorkbook.dataConnectionsコレクションを使用してデータ接続にアクセスし、変更する手段を提供します。  
{{% /alert %}}  

## Aspose.Cellsを使用して既存のSQLデータ接続を変更する  

以下のサンプルは、Aspose.Cells for Node.js via C++を使用してワークブックのSQLデータ接続を変更する例です。このコードで使用したExcelソースファイルと、生成された出力Excelファイルは以下のリンクからダウンロードできます。  

- [元のExcelファイル](5112357.xlsx)  
- [出力Excelファイル](5112356.xlsx)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook(path.join(dataDir, "DataConnection.xlsx"));


// Access first Data Connection
const conn = workbook.getDataConnections().get(0);

// Change the Data Connection Name and Odc file
conn.setName("MyConnectionName");
conn.setOdcFile("C:\\Users\\MyDefaulConnection.odc");

// Change the Command Type, Command and Connection String
const dbConn = conn;
dbConn.setCommandType(AsposeCells.OLEDBCommandType.SqlStatement);
dbConn.setCommand("Select * from AdminTable");
dbConn.setConnectionString("Server=myServerAddress;Database=myDataBase;User ID=myUsername;Password=myPassword;Trusted_Connection=False");

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
