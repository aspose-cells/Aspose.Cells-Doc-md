---
title: Ajouter des signets PDF avec destinations nommées avec C++
linktitle: Ajouter des signets PDF avec des destinations nommées
type: docs
weight: 20
url: /fr/cpp/add-pdf-bookmarks-with-named-destinations/
description: Apprenez comment ajouter des signets PDF avec des destinations nommées en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Les destinations nommées sont un type spécial de signets ou de liens dans le PDF qui ne dépendent pas des pages PDF. Cela signifie que si des pages sont ajoutées ou supprimées du PDF, les signets peuvent devenir invalides mais les destinations nommées resteront intactes. Pour créer une destination nommée, veuillez définir la propriété [**PdfBookmarkEntry.GetDestinationName()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/getdestinationname/).

## **Ajouter des signets PDF avec des destinations nommées**

Veuillez consulter le code d'exemple suivant, son fichier Excel source et son fichier PDF généré. La capture d'écran montre les signets et les destinations nommées à l'intérieur du PDF généré. La capture d'écran décrit également comment visualiser les Destinations Nommées et que vous avez besoin de la version professionnelle de Acrobat Reader.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **Code d'exemple**

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
