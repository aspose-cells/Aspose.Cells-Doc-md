---
title: C++でファイルをレスポンスオブジェクトに保存
linktitle: レスポンスオブジェクトへのファイルの保存
type: docs
weight: 50
url: /ja/cpp/saving-file-to-response-object/
description: Aspose.Cells for C++を使用してファイルを動的に保存し、直接クライアントのブラウザに送信する方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すると、ファイルを操作することができます。この記事では、ファイルをレスポンスオブジェクトに保存するさまざまな方法を説明します。

{{% /alert %}}

## **レスポンスオブジェクトへのファイルの保存**

ファイルを動的に生成し、それをクライアントブラウザに直接送信することも可能です。そのためには、次のパラメータを受け入れる[**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)メソッドの特別なオーバーロードバージョンを使用します。

- **HttpResponse**オブジェクト。
- ファイル名。
- [**ContentDisposition**](https://reference.aspose.com/cells/cpp/aspose.cells/contentdisposition/)、出力ファイルのcontent-dispositionタイプ。
- [**SaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/saveoptions/)、ファイル形式タイプ。

[**ContentDisposition**](https://reference.aspose.com/cells/cpp/aspose.cells/contentdisposition/) 列挙型は、ブラウザに送信されるファイルが、ブラウザ内で直接開くか、.xls/.xlsx または他の拡張子に関連付けられたアプリケーションで開くオプションを提供するかを決定します。

列挙型には、以下の事前定義された保存タイプが含まれています:

|**タイプ**|**説明**|
| :- | :- |
|アタッチメント|スプレッドシートをブラウザに送り、.xls/.xlsx や他の拡張子に関連付けられたアプリケーションで添付ファイルとして開きます|
|インライン|ドキュメントをブラウザに送り、スプレッドシートをディスクに保存するかブラウザ内で開くオプションを表示します|

### **XLS ファイル**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Save in Excel2003 XLS format
    U16String outputPath = outDir + u"output.xls";
    XlsSaveOptions saveOptions;
    workbook.Save(outputPath, saveOptions);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **XLSX ファイル**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook
    Workbook workbook;

    // Save in Xlsx format
    OoxmlSaveOptions saveOptions;
    workbook.Save(outputFilePath, saveOptions);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **PDF ファイル**

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

    // Path of output PDF file
    U16String outputPdf = outDir + u"output.pdf";

    // Creating a Workbook object
    Workbook workbook;

    // Save in Pdf format
    PdfSaveOptions saveOptions;
    workbook.Save(outputPdf, saveOptions);

    Aspose::Cells::Cleanup();
}
```

### **注**

NET5 および .Netstandard に含まれていないオブジェクト "System.Web.HttpResponse" により、
この機能は Aspose.Cells .NET5 および .Netstandard バージョンに存在しないため、ファイルをストリームに保存し、ストリームに対して操作を行うために、以下のコードを参照してください。

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Save workbook to memory stream with explicit FileFormatType
    Vector<uint8_t> data = workbook.SaveToStream();

    std::cout << "File size: " << data.GetLength() << std::endl;

    Cleanup();

    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
