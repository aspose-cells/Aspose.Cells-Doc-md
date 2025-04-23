---
title: Convertir Excel en CSV, TSV et Txt avec C++
linktitle: Enregistrer en CSV, TSV et Txt
type: docs
weight: 40
url: /fr/cpp/convert-excel-to-csv-tsv-and-txt/
description: Convertissez facilement des fichiers Excel en formats CSV, TSV, et TXT en utilisant Aspose.Cells avec C++.
---

{{% alert color="primary" %}}

Aspose.Cells permet de convertir des fichiers Excel, ODS, JSON, et autres formats en CSV, TSV, et TXT.

{{% /alert %}}

## **Enregistrer le classeur au format texte ou CSV**

Parfois, vous souhaitez convertir ou enregistrer un classeur avec plusieurs feuilles de calcul au format texte. Pour les formats texte (par exemple TXT, TabDelim, CSV, etc.), par défaut, à la fois Microsoft Excel et Aspose.Cells enregistrent uniquement le contenu de la feuille de calcul active.

L'exemple de code suivant explique comment enregistrer un classeur entier au format texte. Chargez le classeur source qui peut être n'importe quel fichier de feuille de calcul Microsoft Excel ou OpenOffice (donc XLS, XLSX, XLSM, XLSB, ODS, etc.) avec n'importe quel nombre de feuilles de calcul

Lorsque le code est exécuté, il convertit les données de toutes les feuilles du classeur au format TXT

Vous pouvez modifier le même exemple pour enregistrer votre fichier au format CSV. Par défaut, [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getseparator/) est une virgule, donc ne spécifiez pas de séparateur si vous enregistrez en format CSV.

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/TxtSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Load your source workbook
    Workbook workbook(inputFilePath);

    // Text save options. You can use any type of separator
    TxtSaveOptions opts;
    opts.SetSeparator(u'\t');
    opts.SetExportAllSheets(true);

    // Save entire workbook data into file
    U16String outputFilePath = srcDir + u"out.txt";
    workbook.Save(outputFilePath, opts);

    std::cout << "Workbook saved successfully as text file!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Enregistrement de fichiers texte avec séparateur personnalisé**

Les fichiers texte contiennent des données de feuille de calcul sans mise en forme. Le fichier est un type de fichier texte brut qui peut avoir des délimiteurs personnalisés entre ses données

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/TxtSaveOptions.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xlsx";

    // Create a Workbook object and opening the file from its path
    Workbook workbook(filePath);

    // Instantiate Text File's Save Options
    TxtSaveOptions options;

    // Specify the separator
    options.SetSeparator(u';'); // Using U16String for the char

    // Save the file with the options
    workbook.Save(srcDir + u"output.csv", options);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**
- [Conserver les séparateurs pour les lignes vides lors de l'exportation de feuilles de calcul au format CSV](/cells/fr/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Supprimer les lignes et colonnes vides en tête lors de l'exportation de feuilles de calcul au format CSV](/cells/fr/cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
