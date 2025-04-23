---
title: C++でスライサーのフォーマット設定
linktitle: スライサーの書式を設定する
type: docs
weight: 20
url: /ja/cpp/formatting-slicer/
description: Aspose.Cellsを使用してMicrosoft Excelのスライサーのフォーマット設定（C++）
---

## **可能な使用シナリオ**

Microsoft Excel内のスライサーを列数やスタイルなどを設定してフォーマットできます。Aspose.Cellsは[**Slicer.GetNumberOfColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/getnumberofcolumns/)や[**Slicer.GetStyleType()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/getstyletype/)のプロパティを使ってこれを行うことも可能です。

## **スライサーの書式設定**

以下のコードを参照してください。これはスライサーを含むサンプルExcelファイルを読み込み、スライサーの列数とスタイルタイプを設定して[出力Excelファイル](67338474.xlsx)として保存します。スクリーンショットは、サンプルコード実行後のスライサーの見た目を示しています。

![todo:image_alt_text](formatting-slicer_1.png)

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file containing slicer.
    Workbook workbook(u"sampleFormattingSlicer.xlsx");

    // Access first worksheet.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first slicer inside the slicer collection.
    Slicer slicer = worksheet.GetSlicers().Get(0);

    // Set the number of columns of the slicer.
    slicer.SetNumberOfColumns(2);

    // Set the type of slicer style.
    slicer.SetStyleType(SlicerStyleType::SlicerStyleLight6);

    // Save the workbook in output XLSX format.
    workbook.Save(u"outputFormattingSlicer.xlsx", SaveFormat::Xlsx);

    std::cout << "Slicer formatted and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
