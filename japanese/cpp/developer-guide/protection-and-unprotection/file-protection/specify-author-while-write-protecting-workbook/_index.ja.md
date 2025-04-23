---
title: C++でExcelワークブックの書き込み保護時に作者を指定する
linktitle: ブックを書き込み保護する際に著者を指定する
type: docs
weight: 40
url: /ja/cpp/specify-author-while-write-protecting-workbook/
description: Aspose.Cells for C++を使ってワークブックの書き込み保護時に作者名を指定する方法を学びます。
---

## **可能な使用シナリオ**

Aspose.Cells APIを使用し、ワークブックの書き込み保護時に作者名を指定できます。目的のために[**Workbook.GetAuthor()**](https://reference.aspose.com/cells/cpp/aspose.cells/writeprotection/getauthor/)プロパティを使用してください。

## **ブックを書き込み保護する際に著者を指定する**

以下のサンプルコードでは、[**Workbook.GetAuthor()**](https://reference.aspose.com/cells/cpp/aspose.cells/writeprotection/getauthor/)プロパティの使用方法を説明します。このコードは空のワークブックを作成し、パスワード付きで書き込み保護を行い、作者名を指定し、[出力Excelファイル](67338582.xlsx)として保存します。以下のスクリーンショットは、サンプルコードが出力Excelファイルに及ぼす効果を示しています。

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create empty workbook
    Workbook wb;

    // Write protect workbook with password
    wb.GetSettings().GetWriteProtection().SetPassword(u"1234");

    // Specify author while write protecting workbook
    wb.GetSettings().GetWriteProtection().SetAuthor(u"SimonAspose");

    // Save the workbook in XLSX format
    wb.Save(outDir + u"outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx");

    std::cout << "Workbook write protected with author specified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
