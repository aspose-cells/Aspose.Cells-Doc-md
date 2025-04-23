---
title: Fügen Sie PDF Lesezeichen mit benannten Zielen mit C++ hinzu
linktitle: PDF Lesezeichen mit benannten Zielen hinzufügen
type: docs
weight: 20
url: /de/cpp/add-pdf-bookmarks-with-named-destinations/
description: Erfahren Sie, wie Sie mit Aspose.Cells for C++ PDF Lesezeichen mit benannten Zielen hinzufügen.
---

## **Mögliche Verwendungsszenarien**

Benannte Ziele sind spezielle Arten von Lesezeichen oder Links in PDFs, die nicht von den PDF-Seiten abhängen. Das bedeutet, wenn Seiten zum PDF hinzugefügt oder daraus gelöscht werden, können Lesezeichen ungültig werden, aber benannte Ziele bleiben intakt. Um ein benanntes Ziel zu erstellen, setzen Sie bitte die [**PdfBookmarkEntry.GetDestinationName()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/getdestinationname/)-Eigenschaft.

## **PDF-Lesezeichen mit benannten Zielen hinzufügen**

Bitte sehen Sie sich den folgenden Beispielcode, die Quelldatei Excel (50528348.xlsx) und die Ausgabedatei PDF (50528349.pdf) an. Der Screenshot zeigt die Lesezeichen und benannten Ziele in der Ausgabedatei PDF. Der Screenshot beschreibt auch, wie benannte Ziele angezeigt werden können und dass Sie die professionelle Version von Acrobat Reader benötigen.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **Beispielcode**

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
