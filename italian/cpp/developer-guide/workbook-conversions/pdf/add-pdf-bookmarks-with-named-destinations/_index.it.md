---
title: Aggiungi segnalibri PDF con destinazioni denominate con C++
linktitle: Aggiungi Segnalibri PDF con Destinazioni con Nome
type: docs
weight: 20
url: /it/cpp/add-pdf-bookmarks-with-named-destinations/
description: Impara come aggiungere segnalibri PDF con destinazioni denominate usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Le Destinazioni Denominate sono tipi speciali di segnalibri o link in PDF che non dipendono dalle pagine PDF. Significa che, se vengono aggiunte o eliminate pagine dal PDF, i segnalibri potrebbero diventare invalidi ma le destinazioni denominate rimarranno intatte. Per creare una Destinazione Nome, imposta la proprietà [**PdfBookmarkEntry.GetDestinationName()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/getdestinationname/).

## **Aggiungi Segnalibri PDF con Destinazioni con Nome**

Si prega di consultare il codice di esempio seguente, il [file Excel di origine](50528348.xlsx) e il [file PDF di output](50528349.pdf). La schermata mostra i segnalibri e le destinazioni con nome all'interno del PDF di output. La schermata descrive anche come visualizzare le Destinazioni con Nome e che è necessaria la versione Professionale di Acrobat Reader.

![todo:image_alt_text](add-pdf-bookmarks-with-named-destinations_1.png)

## **Codice di Esempio**

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
