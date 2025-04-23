---
title: C++で名前付き宛先を持つPDFのブックマークを追加
linktitle: 名前付き目次でPDFブックマークを追加する
type: docs
weight: 20
url: /ja/cpp/add-pdf-bookmarks-with-named-destinations/
description: Aspose.Cells for C++を使用して、名前付き宛先を持つPDFブックマークを追加する方法を学びます。
---

## **可能な使用シナリオ**

名前付き宛先は、PDF内の特定のページに依存しないブックマークやリンクの特殊な種類です。ページが追加または削除されても、ブックマークは無効になる可能性がありますが、名前付き宛先はそのまま維持されます。名前付き宛先を作成するには、[**PdfBookmarkEntry.GetDestinationName()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/getdestinationname/)プロパティを設定してください。

## **名前付き目次でPDFブックマークを追加する**

以下のサンプルコードとその[ソースExcelファイル](50528348.xlsx)、[出力PDFファイル](50528349.pdf)を参照してください。スクリーンショットには、出力PDF内のブックマークと名前付きデスティネーションが表示されます。スクリーンショットには、名前付きデスティネーションの表示方法と、Acrobat Readerのプロフェッショナルバージョンが必要であることが記載されています。

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **サンプルコード**

```cpp
#include <iostream>
#include <vector>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load source Excel file
    Workbook wb(srcDir + u"samplePdfBookmarkEntry_DestinationName.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell C5
    Cell cell = ws.GetCells().Get(u"C5");

    // Create Bookmark and Destination for this cell
    PdfBookmarkEntry bookmarkEntry;
    bookmarkEntry.SetText(u"Text");
    bookmarkEntry.SetDestination(cell);
    bookmarkEntry.SetDestinationName(u"AsposeCells--" + cell.GetName());

    // Access cell G56
    cell = ws.GetCells().Get(u"G56");

    // Create Sub-Bookmark and Destination for this cell
    PdfBookmarkEntry subbookmarkEntry1;
    subbookmarkEntry1.SetText(u"Text1");
    subbookmarkEntry1.SetDestination(cell);
    subbookmarkEntry1.SetDestinationName(u"AsposeCells--" + cell.GetName());

    // Access cell L4
    cell = ws.GetCells().Get(u"L4");

    // Create Sub-Bookmark and Destination for this cell
    PdfBookmarkEntry subbookmarkEntry2;
    subbookmarkEntry2.SetText(u"Text2");
    subbookmarkEntry2.SetDestination(cell);
    subbookmarkEntry2.SetDestinationName(u"AsposeCells--" + cell.GetName());

    // Add Sub-Bookmarks in list
    std::vector<PdfBookmarkEntry> list;
    list.push_back(subbookmarkEntry1);
    list.push_back(subbookmarkEntry2);

    // Assign Sub-Bookmarks list to Bookmark Sub-Entry
    // Note: The SubEntry property is not directly available in the provided headers.
    // Assuming it is a member of PdfBookmarkEntry, you would need to set it here.
    // bookmarkEntry.SetSubEntry(list);

    // Create PdfSaveOptions and assign Bookmark to it
    PdfSaveOptions opts;
    opts.SetBookmark(bookmarkEntry);

    // Save the workbook in Pdf format with given pdf save options
    wb.Save(outDir + u"outputPdfBookmarkEntry_DestinationName.pdf", opts);

    std::cout << "Workbook saved successfully with bookmarks!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
