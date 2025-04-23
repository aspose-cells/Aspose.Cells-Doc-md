---
title: C++を使用してExcelをPDFにレンダリングする際にタイムラインを描画する
linktitle: ExcelをPDFにレンダリングする際のタイムラインの描画
type: docs
weight: 60
url: /ja/cpp/draw-timeline-while-rendering-excel-to-pdf/
description: Aspose.Cellsを使用してC++でExcelファイルのタイムラインを管理します。
keywords: Office 2013、Office 2016、Office 2019、Office 365を使用せずに、タイムラインをPDFにレンダリング
---

## **ExcelをPDFにレンダリングする際のタイムラインの描画**
タイムラインが適用されたExcelファイルがある場合、そのExcelをPDFにエクスポートし、タイムラインの設定を保持したまま出力できることをAspose.Cellsはサポートしています。単にタイムライン付きのExcelファイルをPDFにエクスポートすると、生成されたPDFにはタイムラインが表示されます。

以下のサンプルコードは、既存のタイムラインを含む[サンプルExcelファイル](input.xlsx)をロードします。その後、ワークブックを[出力PDFファイル](out.pdf)として保存します。以下のスクリーンショットは、ソースのExcelファイルと生成されたPDFファイルを比較したものです。

<img src="out.png" width="60%">

## **サンプルコード**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file
    U16String inputFilePath(u"input.xlsx");
    std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(inputFilePath);

    // Save file to pdf
    U16String outputFilePath(u"out.pdf");
    wb->Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

```cpp
#include <aspose.cells.h>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();
    // Load the sample Excel file
    Workbook workbook(u"input.xlsx");

    // Save the workbook as a PDF file
    workbook.Save(u"output.pdf", SaveFormat::Pdf);
    Aspose::Cells::Cleanup();
    return 0;

}
```

