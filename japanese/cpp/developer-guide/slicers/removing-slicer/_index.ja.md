---
title: C++を使ったスライサーの削除
linktitle: スライサーの削除
type: docs
weight: 30
url: /ja/cpp/removing-slicer/
description: Aspose.Cells for C++を使用してExcelファイル内のスライサーをプログラムで削除する方法を学びます。
---

## **可能な使用シナリオ**

Microsoft Excelでスライサーを削除したい場合、単に選択して*Delete*ボタンを押してください。同様に、Aspose.Cells APIを使ってプログラム的に削除するには[**Worksheet.Slicers.Remove()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercollection/remove/)メソッドを使用します。これにより、ワークシートからスライサーが削除されます。

## **スライサーの削除**

Aspose.Cellsはスライサーの形状のレンダリングをサポートしています。ワークシートを画像に変換したり、ワークブックをPDFやHTML形式で保存したりすると、スライサーが正しくレンダリングされます。

![todo:image_alt_text](removing-slicer_1.png)

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing slicer.
    U16String inputFilePath(u"sampleRemovingSlicer.xlsx");
    Workbook wb(inputFilePath);

    // Access first worksheet.
    WorksheetCollection worksheets = wb.GetWorksheets();
    Worksheet ws = worksheets.Get(0);

    // Access the first slicer inside the slicer collection.
    SlicerCollection slicers = ws.GetSlicers();
    Slicer slicer = slicers.Get(0);

    // Remove slicer.
    slicers.Remove(slicer);

    // Save the workbook in output XLSX format.
    U16String outputFilePath(u"outputRemovingSlicer.xlsx");
    wb.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Slicer removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
