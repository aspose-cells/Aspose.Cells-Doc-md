---
title: Conserver les séparateurs pour les lignes vides lors de l exportation de feuilles de calcul en format CSV avec C++
linktitle: Conserver les séparateurs pour les lignes vides lors de l exportation de feuilles de calcul au format CSV
type: docs
weight: 160
url: /fr/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: Apprenez comment conserver les séparateurs pour les lignes vides lors de l exportation de feuilles de calcul en format CSV en utilisant Aspose.Cells avec C++.
---

## **Conserver les séparateurs pour les lignes vides lors de l'exportation de feuilles de calcul au format CSV**

Aspose.Cells offre la capacité de conserver les séparateurs de ligne lors de la conversion de feuilles de calcul en format CSV. Pour cela, vous pouvez utiliser la propriété [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) de la classe [**TxtSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/). [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) est une propriété booléenne. Pour conserver les séparateurs pour les lignes vides lors de la conversion du fichier Excel en CSV, définissez la propriété [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) sur **true**.

Le code d'exemple suivant charge le [fichier Excel source](84378743.xlsx). Il définit la propriété [**TxtSaveOptions.GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) à **true** et le sauvegarde en tant que [output.csv](84378744.csv). La capture d'écran montre la comparaison entre le fichier Excel source, la sortie par défaut générée lors de la conversion en CSV, et la sortie générée en définissant [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/getkeepseparatorsforblankrow/) à **true**.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Code d'exemple**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create a Workbook object and opening the file from its path
    Workbook workbook(inputFilePath);

    // Instantiate Text File's Save Options
    TxtSaveOptions options;

    // Set KeepSeparatorsForBlankRow to true to show separators in blank rows
    options.SetKeepSeparatorsForBlankRow(true);

    // Save the file with the options
    workbook.Save(outDir + u"output.csv", options);

    std::cout << "File saved successfully as output.csv!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
