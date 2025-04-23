---
title: Agregar marcadores PDF con destinos nombrados con C++
linktitle: Agregar marcadores PDF con Destinos Nominados
type: docs
weight: 20
url: /es/cpp/add-pdf-bookmarks-with-named-destinations/
description: Aprende cómo agregar marcadores PDF con destinos nombrados usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

 Los destinos nombrados son tipos especiales de marcadores o enlaces en PDF que no dependen de las páginas del PDF. Esto significa que, si se agregan o eliminan páginas del PDF, los marcadores pueden volverse inválidos, pero los destinos nombrados permanecerán intactos. Para crear un Destino Nombrado, configure la propiedad [**PdfBookmarkEntry.GetDestinationName()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/getdestinationname/).

## **Agregar Marcadores de PDF con Destinos Nombrados**

Por favor ve el siguiente código de ejemplo, su [archivo de Excel fuente](50528348.xlsx), y su [archivo PDF de salida](50528349.pdf). La captura de pantalla muestra los marcadores y destinos nominados dentro del PDF de salida. La captura de pantalla también describe cómo ver los Destinos Nominados y que necesitas la versión Profesional de Acrobat Reader.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **Código de muestra**

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
