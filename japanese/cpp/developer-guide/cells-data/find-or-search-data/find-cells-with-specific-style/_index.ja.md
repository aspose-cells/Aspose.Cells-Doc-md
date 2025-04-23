---
title: 特定のスタイルを持つセルをC++で検索する
linktitle: 特定のスタイルを持つセルを検索
type: docs
weight: 190
url: /ja/cpp/find-cells-with-specific-style/
description: Aspose.Cells for C++ APIを通じて特定のスタイルが適用されたセルの検索や検索方法を学びます。
keywords: 特定のスタイルが適用されたセルを見つける、特定のスタイルが適用されたセルを検索する
---

{{% alert color="primary" %}}

時々、特定のスタイルが適用されたセルを見つける必要があります。共通のスタイルを持つすべてのセルを見つけるためにAspose.Cellsを使用できます。Aspose.Cellsは、スタイルを検索するために使用できる[**FindOptions.GetStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/findoptions/getstyle/)プロパティを提供します。

{{% /alert %}}

この例のコードは、セルA1と同じスタイルのすべてのセルを見つけます。コードが実行された後、A1と同じスタイルのすべてのセルにはテキスト「Found」が含まれます。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String filePath = srcDir + u"TestBook.xlsx";

    Workbook workbook(filePath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Style style = worksheet.GetCells().Get(u"A1").GetStyle();

    FindOptions options;
    options.SetStyle(style);

    Cell nextCell;

    do
    {
        nextCell = worksheet.GetCells().Find(U16String(), nextCell, options);
        if (nextCell.GetRow() == -1)
            break;
        nextCell.PutValue(u"Found");
    } while (true);

    U16String outputPath = outDir + u"output.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
