---
title: Exporter Excel en HTML avec les lignes de grille avec C++
linktitle: Exporter Excel en HTML avec les lignes de grille
type: docs
weight: 40
url: /fr/cpp/export-excel-to-html-with-gridlines/
description: Apprenez comment exporter des fichiers Excel en HTML avec des lignes de grille en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}} 

Si vous souhaitez exporter votre fichier Excel en HTML avec des lignes de grille, utilisez la propriété [HtmlSaveOptions.GetExportGridLines()](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportgridlines/) et réglez-la sur **true**.

{{% /alert %}} 

## **Exporter Excel au format HTML avec des lignes de grille**
Le code d’exemple suivant crée un classeur, remplit sa feuille de calcul avec quelques valeurs, puis l’enregistre au format HTML après avoir réglé [HtmlSaveOptions.GetExportGridLines()](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportgridlines/) sur **true**.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Fill worksheet with some integer values
    for (int r = 0; r < 10; r++)
    {
        for (int c = 0; c < 10; c++)
        {
            ws.GetCells().Get(r, c).PutValue(r * 1);
        }
    }

    // Save workbook in HTML format and export gridlines
    HtmlSaveOptions opts;
    opts.SetExportGridLines(true);
    wb.Save(outDir + u"ExportToHTMLWithGridLines_out.html", opts);

    std::cout << "Workbook exported to HTML with gridlines successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
