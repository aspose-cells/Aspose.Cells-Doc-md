---
title: Crear PdfBookmarkEntry para la hoja de gráficos con C++
linktitle: Crear PdfBookmarkEntry para la hoja de gráficos
type: docs
weight: 50
url: /es/cpp/create-pdfbookmarkentry-for-chart-sheet/
description: Aprende cómo crear PdfBookmarkEntry para hojas de gráficos utilizando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Anteriormente, Aspose.Cells crearía [**PdfBookmarkEntry**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/) para una hoja normal. Pero ahora Aspose.Cells también puede crear [**PdfBookmarkEntry**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/) para la hoja de gráficos. Como la hoja de gráficos no tiene ninguna otra celda excepto la celda A1, creado [**PdfBookmarkEntry**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/) para la celda A1 solamente.

## **Crear entrada de marcador de PDF para hoja de gráfico**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](61767756.xlsx) que tiene cuatro hojas. Dos de ellas son hojas normales y las otras dos son hojas de gráficos. Crea cuatro entradas de marcador como sigue:

- Marca de libro-I
- Marca de libro-II-Gráfico1
- Marca de libro-III
- Marca de libro-IV-Gráfico2

La siguiente captura de pantalla muestra el [PDF de salida](61767757.pdf) generado por el código de muestra como referencia.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Código de muestra**

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
