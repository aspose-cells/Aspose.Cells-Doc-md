---
title: Aspose.Cellsを使用して既存のSQLデータ接続をC++で変更する方法
linktitle: 既存の SQL データ接続を変更する
type: docs
weight: 20
url: /ja/cpp/modify-existing-sql-data-connection-using-aspose-cells/
description: Aspose.Cellsを使ったExcelファイルの既存SQLデータ接続の変更方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsは既存のSQLデータ接続の変更をサポートします。本記事では、Aspose.Cellsを使ってSQLデータ接続のさまざまなプロパティを変更する方法を解説します。

Microsoft Excel内のデータ接続を追加または参照するには、**データ > 接続** メニューコマンドに従ってください。

同様に、Aspose.Cellsは `Workbook.DataConnections` コレクションを使用してデータコネクションにアクセスし、変更する手段も提供します。

{{% /alert %}}

## Aspose.Cellsを使用して既存のSQLデータ接続を変更する

以下のサンプルでは、Aspose.Cellsを使用してワークブックのSQLデータ接続を変更する方法を示しています。このコードで使用されるソースExcelファイルおよびコードによって生成される出力Excelファイルのダウンロードリンクは、次のリンクからご覧いただけます。

- [元のExcelファイル](5112357.xlsx)
- [出力Excelファイル](5112356.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"DataConnection.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Create workbook object
    Workbook workbook(inputFilePath);

    // Access first Data Connection
    ExternalConnection conn = workbook.GetDataConnections().Get(0);

    // Change the Data Connection Name and Odc file
    conn.SetName(u"MyConnectionName");
    conn.SetOdcFile(u"C:\\Users\\MyDefaulConnection.odc");

    // Change the Command Type, Command and Connection String
    DBConnection dbConn = conn;
    dbConn.SetCommandType(OLEDBCommandType::SqlStatement);
    dbConn.SetCommand(u"Select * from AdminTable");
    dbConn.SetConnectionString(u"Server=myServerAddress;Database=myDataBase;User ID=myUsername;Password=myPassword;Trusted_Connection=False");

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Data connection updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
