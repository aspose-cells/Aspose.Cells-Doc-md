---
title: Analyse des enregistrements de cache de pivot lors du chargement d un fichier Excel avec C++
linktitle: Analyse des enregistrements de cache de pivot
type: docs
weight: 70
url: /fr/cpp/parsing-pivot-cached-records-while-loading-excel-file/
description: Apprenez comment analyser les enregistrements de cache de pivot lors du chargement de fichiers Excel en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Lorsque vous créez un tableau croisé dynamique, Microsoft Excel prend une copie des données sources et les enregistre dans le cache du tableau croisé dynamique. Le cache du tableau croisé dynamique est conservé dans la mémoire de Microsoft Excel. Vous ne pouvez pas le voir, mais ce sont les données auxquelles le tableau croisé dynamique fait référence lorsque vous construisez votre tableau croisé dynamique ou modifiez une sélection de filtre ou déplacez des lignes/colonnes. Cela permet à Microsoft Excel de réagir très rapidement aux modifications du tableau croisé dynamique, mais cela peut également doubler la taille de votre fichier. Après tout, le cache du tableau croisé dynamique est simplement une copie de vos données sources, il est donc logique que la taille de votre fichier puisse être potentiellement doublée.

Lorsque vous chargez votre fichier Excel à l'intérieur de l'objet Workbook, vous pouvez décider si vous souhaitez également charger les enregistrements du cache du tableau croisé dynamique ou non, en utilisant la propriété [**LoadOptions.GetParsingPivotCachedRecords()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getparsingpivotcachedrecords/). La valeur par défaut de cette propriété est false. Si le cache du tableau croisé dynamique est assez volumineux, cela peut améliorer les performances. Mais si vous souhaitez également charger les enregistrements du cache du tableau croisé dynamique, vous devez définir cette propriété sur true.

## **Analyse des enregistrements mis en cache du tableau croisé dynamique lors du chargement du fichier Excel**

Le code d'exemple suivant explique l'utilisation de la propriété [**LoadOptions.GetParsingPivotCachedRecords()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getparsingpivotcachedrecords/). Il charge le [fichier Excel d'exemple](61767773.xlsx) tout en analysant les enregistrements mis en cache du tableau croisé dynamique. Ensuite, il actualise le tableau croisé dynamique et l'enregistre sous le nom de [fichier Excel de sortie](61767774.xlsx).

## **Code d'exemple**

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

    // Create load options
    LoadOptions options;

    // Set ParsingPivotCachedRecords true, default value is false
    options.SetParsingPivotCachedRecords(true);

    // Load the sample Excel file containing pivot table cached records
    U16String inputFilePath = srcDir + u"sampleParsingPivotCachedRecordsWhileLoadingExcelFile.xlsx";
    Workbook wb(inputFilePath, options);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first pivot table
    PivotTable pt = ws.GetPivotTables().Get(0);

    // Set refresh data flag true
    pt.SetRefreshDataFlag(true);

    // Refresh and calculate pivot table
    pt.RefreshData();
    pt.CalculateData();

    // Set refresh data flag false
    pt.SetRefreshDataFlag(false);

    // Save the output Excel file
    U16String outputFilePath = outDir + u"outputParsingPivotCachedRecordsWhileLoadingExcelFile.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Pivot table cached records parsed and refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
