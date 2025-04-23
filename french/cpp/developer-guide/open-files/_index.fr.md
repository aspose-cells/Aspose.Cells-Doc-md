---
title: Charger et gérer des fichiers Excel, OpenOffice, Json, Csv et Html avec C++
linktitle: Ouvrir des fichiers
type: docs
weight: 20
url: /fr/cpp/loading-saving-and-managing/
description: Avec Aspose.Cells for C++, il est simple de créer, ouvrir et gérer des fichiers Excel, CSV, TSV, ODS, HTML, Numbers, Json, XML, Pdf, Jpg, Tiff, Image, Mht et XPS.
---

{{% alert color="primary" %}}

Avec Aspose.Cells for C++, il est simple de créer, ouvrir et gérer des fichiers Excel, par exemple pour récupérer des données ou utiliser un modèle de conception pour accélérer le processus de développement.

{{% /alert %}}

## **Création d'un nouveau classeur**
L'exemple suivant crée un nouveau classeur à partir de zéro.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    try
    {
        // Create a License object
        License license;

        // Set the license of Aspose.Cells to avoid the evaluation limitations
        license.SetLicense(srcDir + u"Aspose.Cells.lic");
    }
    catch (const std::exception& ex)
    {
        std::cerr << ex.what() << std::endl;
    }

    // Instantiate a Workbook object that represents Excel file.
    Workbook wb;

    // When you create a new workbook, a default "Sheet1" is added to the workbook.
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Access the "A1" cell in the sheet.
    Cell cell = sheet.GetCells().Get(u"A1");

    // Input the "Hello World!" text into the "A1" cell
    cell.PutValue(u"Hello World!");

    // Save the Excel file.
    wb.Save(srcDir + u"MyBook_out.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Ouvrir et enregistrer un fichier**
Avec Aspose.Cells for C++, il est simple d'ouvrir, sauvegarder et gérer des fichiers Excel.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"dest.xlsx";

    // Create a Workbook object and open an Excel file using its file path
    Workbook workbook1(inputFilePath);

    // Adding new sheet
    WorksheetCollection sheets = workbook1.GetWorksheets();
    Worksheet sheet = sheets.Add(u"MySheet");

    // Setting active sheet
    sheets.SetActiveSheetIndex(1);

    // Setting values
    Cells cells = sheet.GetCells();

    // Setting text
    cells.Get(u"A1").PutValue(u"Hello!");

    // Setting number
    cells.Get(u"A2").PutValue(1000);

    // Setting Date Time
    Cell cell = cells.Get(u"A3");
    Date currentDate;
    currentDate.year = 2023; // Replace with actual current year
    currentDate.month = 10;  // Replace with actual current month
    currentDate.day = 5;     // Replace with actual current day
    currentDate.hour = 12;   // Replace with actual current hour
    currentDate.minute = 30; // Replace with actual current minute
    currentDate.second = 0;  // Replace with actual current second
    cell.PutValue(currentDate);

    // Setting style for date
    Style style = cell.GetStyle();
    style.SetNumber(14);
    cell.SetStyle(style);

    // Setting formula
    cells.Get(u"A4").SetFormula(u"=SUM(A1:A3)");

    // Saving the workbook to disk
    workbook1.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**
- [Différentes façons d'ouvrir des fichiers](/cells/fr/cpp/different-ways-to-open-files/)
- [Filtrer les noms définis lors du chargement du classeur](/cells/fr/cpp/filter-defined-names-while-loading-workbook/)
- [Filtrer les objets lors du chargement du classeur ou de la feuille de calcul](/cells/fr/cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [Filtrer le type de données lors du chargement du classeur à partir d'un fichier modèle](/cells/fr/cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [Obtenir des avertissements lors du chargement du fichier Excel](/cells/fr/cpp/get-warnings-while-loading-excel-file/)
- [Charger le fichier Excel source sans graphiques](/cells/fr/cpp/load-source-excel-file-without-charts/)
- [Charger des feuilles de calcul spécifiques dans un classeur](/cells/fr/cpp/load-specific-worksheets-in-a-workbook/)
- [Charger le classeur avec la taille de papier de l'imprimante spécifiée](/cells/fr/cpp/load-workbook-with-specified-printer-paper-size/)
- [Ouvrir des fichiers de différentes versions de Microsoft Excel](/cells/fr/cpp/opening-different-microsoft-excel-versions-files/)
- [Ouvrir des fichiers avec différents formats](/cells/fr/cpp/opening-files-with-different-formats/)
- [Optimisation de l'utilisation de la mémoire lors de la manipulation de grands fichiers contenant de larges ensembles de données](/cells/fr/cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [Lire la feuille de calcul Numbers développée par Apple Inc. avec Aspose.Cells](/cells/fr/cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Arrêter la conversion ou le chargement en utilisant InterruptMonitor lorsqu'il prend trop de temps](/cells/fr/cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [Utiliser l'API LightCells](/cells/fr/cpp/using-lightcells-api/)
- [Convertir CSV en JSON](/cells/fr/cpp/convert-csv-to-json/)
- [Convertir Excel en JSON](/cells/fr/cpp/convert-excel-to-json/)
- [Convertir JSON en CSV](/cells/fr/cpp/convert-json-to-csv/)
- [Convertir JSON en Excel](/cells/fr/cpp/convert-json-to-excel/)
- [Convertir Excel en Html](/cells/fr/cpp/convert-excel-to-html/)
