---
title: Fusionner plusieurs feuilles de calcul en une seule avec C++
linktitle: Combiner plusieurs feuilles de calcul en une seule feuille de calcul
type: docs
weight: 160
url: /fr/cpp/combine-multiple-worksheets-into-a-single-worksheet/
description: Apprenez à combiner plusieurs feuilles de calcul en une seule avec Aspose.Cells en C++.
---

{{% alert color="primary" %}} 

Parfois, il est nécessaire de combiner plusieurs feuilles de calcul en une seule. Cela peut être facilement réalisé à l'aide de l'API Aspose.Cells. Cet article vous montrera un exemple de code qui lit un classeur source et combine les données de toutes les feuilles de calcul source en une seule feuille de calcul à l'intérieur d'un classeur de destination.

{{% /alert %}} 

Le code d'exemple suivant vous montre comment combiner plusieurs feuilles de calcul en une seule feuille de calcul.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    //For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    //Path of input excel file
    U16String filePath = srcDir + u"SampleInput.xlsx";

    //Create workbook from the input file
    Workbook workbook(filePath);

    //Create a destination workbook
    Workbook destWorkbook;

    //Get the first worksheet of the destination workbook
    Worksheet destSheet = destWorkbook.GetWorksheets().Get(0);

    //Variable to maintain total row count during copy
    int32_t totalRowCount = 0;

    //Iterate through each worksheet in the source workbook
    for (int32_t i = 0; i < workbook.GetWorksheets().GetCount(); i++)
    {
        Worksheet sourceSheet = workbook.GetWorksheets().Get(i);

        //Get the display range of the source sheet
        Range sourceRange = sourceSheet.GetCells().GetMaxDisplayRange();

        //Create a range in the destination sheet according to the source range
        Range destRange = destSheet.GetCells().CreateRange(sourceRange.GetFirstRow() + totalRowCount, 
            sourceRange.GetFirstColumn(), sourceRange.GetRowCount(), sourceRange.GetColumnCount());

        //Copy data from source range to destination range
        destRange.Copy(sourceRange);

        //Update the total row count for the next iteration
        totalRowCount += sourceRange.GetRowCount();
    }

    //Save the destination workbook to the output path
    U16String outputFilePath = srcDir + u"Output.out.xlsx";
    destWorkbook.Save(outputFilePath);

    std::cout << "Workbook processed and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
