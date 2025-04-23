---
title: C++でレンダリング用のカスタム用紙サイズを実装
linktitle: レンダリング用のワークシートのカスタム用紙サイズを実装する
type: docs
weight: 70
url: /ja/cpp/implement-custom-paper-size-of-worksheet-for-rendering/
description: この文章は、C++のAPIを使用して、ExcelファイルをPDFにレンダリングする際に任意のワークシートのカスタム用紙サイズを設定する方法を解説します。
keywords: ExcelをPDFにレンダリング中にカスタム用紙サイズを設定する C++
---

## **可能な使用シナリオ**

MS Excelには直接的なカスタム用紙サイズの設定オプションはありませんが、ExcelファイルをPDFにレンダリングする際にワークシートの用紙サイズをカスタムに設定できます。このドキュメントは、Aspose.Cells APIを使ってワークシートのカスタム用紙サイズを設定する方法を示します。

## **レンダリングのためのワークシートのカスタム用紙サイズを実装する**

Aspose.Cellsを使えば、目的の用紙サイズを設定できます。`[**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)`クラスの[**CustomPaperSize**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/custompapersize/)メソッドを使ってカスタムページサイズを指定してください。以下のサンプルコードは、ブック内の最初のワークシートにカスタム用紙サイズを指定する例です。参考用に、次のコードで生成された[出力PDF](45056028.pdf)もご覧ください。

## **スクリーンショット**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Set custom paper size in unit of inches
    ws.GetPageSetup().CustomPaperSize(6, 4);

    // Access cell B4
    Cell b4 = ws.GetCells().Get("B4");

    // Add the message in cell B4
    b4.PutValue(u"Pdf Page Dimensions: 6.00 x 4.00 in");

    // Save the workbook in pdf format
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    wb.Save(outputDir + u"outputCustomPaperSize.pdf");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
