---
title: Supprimer les lignes et colonnes vides en tête lors de l exportation de feuilles de calcul en format CSV avec C++
linktitle: Apprenez comment supprimer les lignes et colonnes vides en tête lors de l exportation de feuilles de calcul en format CSV en utilisant Aspose.Cells avec C++.
type: docs
weight: 100
url: /fr/cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/
description: Découvrez comment couper les lignes et colonnes vides en tête lors de l exportation de feuilles de calcul au format CSV en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Parfois, votre fichier Excel ou CSV comporte des colonnes ou lignes vides en tête. Par exemple, considérez cette ligne :

{{< highlight java >}}

 ,,,data1,data2

{{< /highlight >}}

Ici, les trois premières cellules ou colonnes sont vides. Lorsque vous ouvrez un tel fichier CSV dans Microsoft Excel, Microsoft Excel ignore ces lignes et colonnes vides initiales.

Par défaut, Aspose.Cells ne supprime pas les colonnes et lignes vides de tête lors de l'enregistrement, mais si vous souhaitez les supprimer comme le fait Microsoft Excel, alors Aspose.Cells fournit la propriété [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/). Veuillez la définir sur **true** et ensuite toutes les colonnes et lignes vides de tête seront supprimées lors de l'enregistrement.

{{% alert color="primary" %}}

Avant la sortie de Aspose.Cells for C++ 20.4, la valeur par défaut de [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/) était **false**. Depuis la version 20.4, la valeur par défaut de [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/) est **true.**

{{% /alert %}}

## **Supprimer les lignes et colonnes vides en tête lors de l'exportation de feuilles de calcul au format CSV**

Le code d'exemple suivant charge le [fichier Excel source](sampleTrimBlankColumns.xlsx) qui contient deux premières colonnes vides. Il enregistre d'abord le fichier Excel au format CSV sans aucun changement, puis définit la propriété [**TxtSaveOptions.GetTrimLeadingBlankRowAndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/gettrimleadingblankrowandcolumn/) sur **true** et l'enregistre à nouveau. La capture d'écran montre le [fichier Excel source](sampleTrimBlankColumns.xlsx), le [fichier CSV en sortie sans suppression](outputWithoutTrimBlankColumns.csv) et le [fichier CSV en sortie avec suppression](outputTrimBlankColumns.csv).

![todo:image_alt_text](trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format_1.png)

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleTrimBlankColumns.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Save in csv format without trimming blank columns
    wb.Save(outDir + u"outputWithoutTrimBlankColumns.csv", SaveFormat::Csv);

    // Create TxtSaveOptions and set TrimLeadingBlankRowAndColumn to true
    TxtSaveOptions opts;
    opts.SetTrimLeadingBlankRowAndColumn(true);

    // Save in csv format with trimming blank columns
    wb.Save(outDir + u"outputTrimBlankColumns.csv", opts);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
