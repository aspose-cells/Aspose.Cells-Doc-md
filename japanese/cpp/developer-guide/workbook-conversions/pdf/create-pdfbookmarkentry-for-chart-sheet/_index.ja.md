---
title: C++でチャートシートのPdfBookmarkEntryを作成
linktitle: チャートシートの PdfBookmarkEntry を作成
type: docs
weight: 50
url: /ja/cpp/create-pdfbookmarkentry-for-chart-sheet/
description: Aspose.Cells for C++を使用してチャートシート用のPdfBookmarkEntryを作成する方法を学ぶ。
---

## **可能な使用シナリオ**

以前、Aspose.Cellsは通常のシートに対して[**PdfBookmarkEntry**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/)を作成していました。しかし、今ではAspose.Cellsはチャートシートに対しても[**PdfBookmarkEntry**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/)を作成できます。チャートシートにはセルA1以外のセルがないため、A1セルのみに[**PdfBookmarkEntry**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/)を作成します。

## **チャートシートの PdfBookmarkEntry を作成**

次のサンプルコードは、4つのシートを持つ[サンプルExcelファイル](61767756.xlsx)をロードします。そのうち2つは通常のシートで、残りの2つはチャートシートです。以下のように4つのブックマークエントリを作成します。

- ブックマーク-I
- ブックマーク-II-Chart1
- ブックマーク-III
- ブックマーク-IV-Chart2

次のスクリーンショットは、サンプルコードによって生成された[出力PDF](61767757.pdf)を示しています。

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **サンプルコード**

```cpp
#include <iostream>
#include <vector>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file
    U16String inputFilePath = u"sampleCreatePdfBookmarkEntryForChartSheet.xlsx";
    Workbook wb(inputFilePath);

    // Access all four worksheets
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet sheet1 = sheets.Get(0);
    Worksheet sheet2 = sheets.Get(1);
    Worksheet sheet3 = sheets.Get(2);
    Worksheet sheet4 = sheets.Get(3);

    // Create Pdf Bookmark Entry for Sheet1
    PdfBookmarkEntry ent1;
    ent1.SetDestination(sheet1.GetCells().Get(u"A1"));
    ent1.SetText(u"Bookmark-I");

    // Create Pdf Bookmark Entry for Sheet2 - Chart 
    PdfBookmarkEntry ent2;
    ent2.SetDestination(sheet2.GetCells().Get(u"A1"));
    ent2.SetText(u"Bookmark-II-Chart1");

    // Create Pdf Bookmark Entry for Sheet3 
    PdfBookmarkEntry ent3;
    ent3.SetDestination(sheet3.GetCells().Get(u"A1"));
    ent3.SetText(u"Bookmark-III");

    // Create Pdf Bookmark Entry for Sheet4 - Chart 
    PdfBookmarkEntry ent4;
    ent4.SetDestination(sheet4.GetCells().Get(u"A1"));
    ent4.SetText(u"Bookmark-IV-Chart2");

    // Arrange all Bookmark Entries
    std::vector<PdfBookmarkEntry> lst;
    lst.push_back(ent2);
    lst.push_back(ent3);
    lst.push_back(ent4);

    // Create Pdf Save Options with Bookmark Entries
    PdfSaveOptions opts;
    opts.SetBookmark(ent1);

    // Save the output Pdf
    U16String outputFilePath = u"outputCreatePdfBookmarkEntryForChartSheet.pdf";
    wb.Save(outputFilePath, opts);

    std::cout << "PDF with bookmarks created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
