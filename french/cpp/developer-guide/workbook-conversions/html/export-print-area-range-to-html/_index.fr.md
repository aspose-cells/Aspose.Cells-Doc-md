---
title: Exporter la plage de la zone d impression en HTML avec C++
linktitle: Exporter la plage de la zone d impression en HTML
type: docs
weight: 60
url: /fr/cpp/export-print-area-range-to/
description: Apprenez comment exporter la plage de la zone d impression en HTML en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

C’est un scénario courant où nous devons exporter uniquement la zone d'impression, c’est-à-dire une plage sélectionnée de cellules, plutôt que la feuille entière en HTML. Cette fonctionnalité est déjà disponible pour le rendu PDF ; cependant, vous pouvez désormais effectuer cette tâche également pour HTML. Tout d’abord, réglez la zone d’impression dans l’objet mise en page de la feuille. Ensuite, utilisez le drapeau [**HtmlSaveOptions.GetExportPrintAreaOnly()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportprintareaonly/) pour exporter uniquement la plage sélectionnée.

## **Code d'exemple**

Le code d’exemple suivant charge un classeur puis exporte la zone d’impression en HTML. Le fichier d'essai pour cette fonction peut être téléchargé à partir du lien suivant :

[sampleInlineCharts.xlsx](79527946.xlsx)

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleInlineCharts.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"outputInlineCharts.html";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the print area
    worksheet.GetPageSetup().SetPrintArea(u"D2:M20");

    // Initialize HtmlSaveOptions
    HtmlSaveOptions options;

    // Set flag to export print area only
    options.SetExportPrintAreaOnly(true);

    // Save to HTML format
    workbook.Save(outputFilePath, options);

    std::cout << "HTML file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
