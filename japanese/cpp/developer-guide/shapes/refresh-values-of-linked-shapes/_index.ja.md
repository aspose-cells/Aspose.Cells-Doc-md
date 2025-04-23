---
title: C++でリンクされた図形の値を更新する
linktitle: リンクされた形状の値をリフレッシュ
type: docs
weight: 3200
url: /ja/cpp/refresh-values-of-linked-shapes/
description: Aspose.Cells for C++を使用してExcelファイル内のリンクされた図形の値を更新する方法を学びます。
---

{{% alert color="primary" %}}

時々、Excelファイルにはセルにリンクされた形状がある場合があります。Microsoft Excelでは、リンクされたセルの値を変更すると、リンクされた形状の値も変更されます。Aspose.Cellsでも、XLSまたはXLSX形式でワークブックを保存する場合には、この動作が適切に機能します。ただし、ワークブックをPDFやHTML形式で保存する場合には、リンクされた形状の値をリフレッシュするために[**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/updateselectedvalue/)メソッドを呼び出さなければなりません。

{{% /alert %}}

## 例

以下のスクリーンショットは、サンプルコードで使用されているソースExcelファイルを示しています。このファイルには、セルA1からE4にリンクされた画像があります。Aspose.Cellsを使ってセルB4の値を変更し、その後[**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/updateselectedvalue/)メソッドを呼び出して画像の値を更新し、PDF形式で保存します。

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

指定されたリンク済みExcelファイル（[ソースExcelファイル](95584291.xlsx)）と出力PDF（[出力PDF](95584292.pdf)）はリンクからダウンロード可能です。

### C++コードによるリンクされた図形の値の更新

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from source file
    Workbook workbook(srcDir + u"sampleRefreshValueOfLinkedShapes.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Change the value of cell B4
    Cell cell = worksheet.GetCells().Get(u"B4");
    cell.PutValue(100);

    // Update the value of the Linked Picture which is linked to cell B4
    worksheet.GetShapes().UpdateSelectedValue();

    // Save the workbook in PDF format
    workbook.Save(outDir + u"outputRefreshValueOfLinkedShapes.pdf", SaveFormat::Pdf);

    std::cout << "Linked shapes value refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
