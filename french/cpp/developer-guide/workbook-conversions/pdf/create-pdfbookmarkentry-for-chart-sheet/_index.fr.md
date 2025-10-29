---
title: Créer une entrée PdfBookmarkEntry pour la feuille de graphique avec C++
linktitle: Créer une entrée PdfBookmark pour la feuille de graphique
type: docs
weight: 50
url: /fr/cpp/create-pdfbookmarkentry-for-chart-sheet/
description: Découvrez comment créer une PdfBookmarkEntry pour les feuilles de graphique en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Auparavant, Aspose.Cells créait [**PdfBookmarkEntry**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/) pour un feuillet normal. Mais maintenant, Aspose.Cells peut également créer [**PdfBookmarkEntry**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/) pour un feuillet de graphique. Comme un feuillet de graphique ne contient aucune autre cellule que la cellule A1, il créera [**PdfBookmarkEntry**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfbookmarkentry/) pour la cellule A1 uniquement.

## **Créer une entrée PdfBookmark pour une feuille de graphique**

 Le code d'exemple suivant charge le [fichier Excel d'exemple](61767756.xlsx) qui possède quatre feuilles. Deux d'entre elles sont des feuilles normales et les autres deux sont des feuilles de graphique. Il crée quatre entrées de signet comme suit :

- Signet-I
- Signet-II-Graph1
- Signet-III
- Signet-IV-Graph2

La capture d'écran suivante montre le [PDF de sortie](61767757.pdf) généré par le code d'exemple pour référence.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Code d'exemple**

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
