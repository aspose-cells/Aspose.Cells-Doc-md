---
title: C++を使用してXLSおよびXLSBファイルの外部コネクションの読み取りと書き込み
linktitle: XLSおよびXLSBファイルの外部接続の読み取りと書き込み
type: docs
weight: 80
url: /ja/cpp/read-and-write-external-connection-of-xls-and-xlsb-files/
description: Aspose.Cells for C++を使ってXLS/XLSBファイルの外部データベースコネクションを読み取り、変更する方法を学びます。
---

## **可能な使用シナリオ**

Aspose.Cells for C++はXLSXファイルの外部コネクションの読み書きに対応しており、今ではXLSBやXLSフォーマットにも拡張されています。 同じコード構造で全てのサポートされたファイルタイプに対応します。

## **XLS/XLSBファイルの外部接続の読み取りと書き込み**

以下のサンプルコードは、サンプルのXLSBファイル（XLSでも機能します）を読み込み、最初の外部コネクション（通常はMicrosoft Access DBコネクション）を変更します。コードは次の操作を示しています：

1. スプレッドシートファイルをロードする
2. 外部コネクションにアクセスする
3. 接続プロパティを変更する
4. 変更したファイルを保存する

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)

## **サンプルコード**

このコードは入力/出力ファイルの拡張子を調整することで、XLSBとXLSの両方に対応しています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // File paths
    U16String inputFilePath = srcDir + u"sampleExternalConnection_XLSB.xlsb";
    U16String outputFilePath = outDir + u"outputExternalConnection_XLSB.xlsb";

    // Load source workbook
    Workbook workbook(inputFilePath);

    // Get first external connection
    ExternalConnectionCollection connections = workbook.GetDataConnections();
    DBConnection dbCon = connections.Get(0);

    // Print connection details
    std::cout << "Connection Name: " << dbCon.GetName().ToUtf8() << std::endl;
    std::cout << "Command: " << dbCon.GetCommand().ToUtf8() << std::endl;
    std::cout << "Connection Info: " << dbCon.GetConnectionString().ToUtf8() << std::endl;

    // Modify connection name
    dbCon.SetName(u"NewCust");

    // Save modified workbook
    workbook.Save(outputFilePath);

    std::cout << "External connection updated successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

**C++の等価:**

```cpp
#include <iostream>
#include <Aspose.Cells.h>

using namespace Aspose::Cells;
using namespace Aspose::Cells::ExternalConnections;

int main() {
    Aspose::Cells::Startup();
    // Load source workbook
    Workbook workbook(u"source.xlsb");
    // Access first external connection
    DBConnection conn(workbook.GetDataConnections().Get(0));

    // Output original connection details
    std::cout << "Connection Name: " << conn.GetName().ToUtf8() << std::endl;
    std::cout << "Command: " << conn.GetCommand().ToUtf8() << std::endl;
    std::cout << "Connection Info: " << conn.GetConnectionInfo().ToUtf8() << std::endl;

    // Modify connection name
    conn.SetName(u"Cust_Modified");

    // Save updated workbook
    workbook.Save(u"output.xlsb");
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **コンソール出力**

{{< highlight cpp >}}
Connection Name: Cust
Command: Customer
Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False
{{< /highlight >}}
