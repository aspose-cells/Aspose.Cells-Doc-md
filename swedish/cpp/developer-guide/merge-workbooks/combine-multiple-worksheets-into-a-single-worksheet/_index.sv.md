---
title: Kombinera flera kalkylblad till ett enda med C++
linktitle: Kombinera flera arkmallar till ett enda ark
type: docs
weight: 160
url: /sv/cpp/combine-multiple-worksheets-into-a-single-worksheet/
description: Lär dig hur du kombinerar flera kalkylblad till ett med Aspose.Cells i C++.
---

{{% alert color="primary" %}} 

Ibland behöver du kombinera flera kalkylblad till ett enda kalkylblad. Detta kan enkelt uppnås med Aspose.Cells API. Den här artikeln visar ett kodexempel som läser in en källbok och kombinerar datan från alla källkalkylblad till ett enda kalkylblad i en målbok.

{{% /alert %}} 

Följande kodsnutt visar hur du kombinerar flera arkmallar till ett enda ark.

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
