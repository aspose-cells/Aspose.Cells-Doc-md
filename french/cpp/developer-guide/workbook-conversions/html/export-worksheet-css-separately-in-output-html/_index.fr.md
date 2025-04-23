---
title: Exporter les CSS de la feuille de calcul séparément dans le HTML de sortie avec C++
linktitle: Exporter la feuille de calcul CSS séparément dans le HTML de sortie
type: docs
weight: 80
url: /fr/cpp/export-worksheet-css-separately-in-output/
description: Apprenez comment exporter le CSS de la feuille de calcul séparément lors de la conversion de fichiers Excel en HTML en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Aspose.Cells fournit la fonction d’exportation du CSS de la feuille séparément lors de la conversion de votre fichier Excel en HTML. Veuillez utiliser la propriété [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetcssseparately/) à cette fin et la régler sur **true** lors de l’enregistrement du fichier Excel au format HTML.

## **Exporter la feuille de calcul CSS séparément dans le HTML de sortie**

Le code d'exemple suivant crée un fichier Excel, ajoute du texte dans la cellule **B5** en couleur **rouge**, puis le sauvegarde au format HTML en utilisant la propriété [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexportworksheetcssseparately/). Veuillez consulter le [HTML de sortie](60489766.zip) généré par le code pour référence. Vous y trouverez le fichier **stylesheet.css** comme résultat du code d'exemple.

## **Code d'exemple**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access cell B5 and put value inside it
    Cell cell = ws.GetCells().Get(u"B5");
    cell.PutValue(u"This is some text.");

    // Set the style of the cell - font color is Red
    Style st = cell.GetStyle();
    st.GetFont().SetColor(Color::Red());
    cell.SetStyle(st);

    // Specify html save options - export worksheet css separately
    HtmlSaveOptions opts;
    opts.SetExportWorksheetCSSSeparately(true);

    // Save the workbook in html
    wb.Save(u"outputExportWorksheetCSSSeparately.html", opts);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Exporter un classeur à une seule feuille en HTML**

Lorsqu’un classeur avec plusieurs feuilles est converti en HTML avec Aspose.Cells, il crée un fichier HTML ainsi qu’un dossier contenant du CSS et plusieurs fichiers HTML. Lorsqu’on ouvre ce fichier HTML dans le navigateur, les onglets sont visibles. La même fonction est requise pour un classeur avec une seule feuille lors de la conversion en HTML. Auparavant, aucun dossier séparé n’était créé pour les classeurs à une seule feuille, et seul un fichier HTML était créé. Ce fichier HTML ne montre pas d’onglet lorsqu’il est ouvert dans le navigateur. MS Excel crée également un dossier approprié et un HTML pour une seule feuille, c’est pourquoi le même comportement est implémenté via les APIs d’Aspose.Cells. Le fichier d’exemple peut être téléchargé à partir du lien suivant pour être utilisé dans le code exemple ci-dessous :

[sampleSingleSheet.xlsx](79527937.xlsx)

## **Code d'exemple**

```c++
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
    U16String inputFilePath = srcDir + u"sampleSingleSheet.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"outputSampleSingleSheet.htm";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Specify HTML save options
    HtmlSaveOptions options;

    // Set optional settings
    options.SetEncoding(EncodingType::UTF8);
    options.SetExportImagesAsBase64(true);
    options.SetExportGridLines(true);
    options.SetExportSimilarBorderStyle(true);
    options.SetExportBogusRowData(true);
    options.SetExcludeUnusedStyles(true);
    options.SetExportHiddenWorksheet(true);

    // Save the workbook in HTML format with specified HTML save options
    workbook.Save(outputFilePath, options);

    std::cout << "Workbook saved successfully in HTML format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
