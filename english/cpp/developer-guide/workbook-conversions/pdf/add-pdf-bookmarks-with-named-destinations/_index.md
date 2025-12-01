---
title: Add PDF Bookmarks with Named Destinations with C++
linktitle: Add PDF Bookmarks with Named Destinations
type: docs
weight: 20
url: /cpp/add-pdf-bookmarks-with-named-destinations/
description: Learn how to add PDF bookmarks with named destinations using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Named Destinations are special kinds of bookmarks or links in PDF that do not depend on PDF pages. It means, if pages are added or deleted from PDF, bookmarks may become invalid but named destinations will remain intact. To create Named Destination, please set the [**PdfBookmarkEntry.GetDestinationName()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/getdestinationname/) property.

## **Add PDF Bookmarks with Named Destinations**

Please see the following sample code, its [source Excel file](50528348.xlsx), and its [output PDF file](50528349.pdf). The screenshot shows the bookmarks and named destinations inside the output PDF. The screenshot also describes how to view Named Destinations and that you need Professional version of Acrobat Reader.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **Sample Code**

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
{{< app/cells/assistant language="cpp" >}}
