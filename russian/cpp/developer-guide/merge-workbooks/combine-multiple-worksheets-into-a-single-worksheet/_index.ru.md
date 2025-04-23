---
title: Объединение нескольких листов в один с помощью C++
linktitle: Совместить несколько листов в один лист
type: docs
weight: 160
url: /ru/cpp/combine-multiple-worksheets-into-a-single-worksheet/
description: Узнайте, как объединять несколько листов в один, используя Aspose.Cells и C++.
---

{{% alert color="primary" %}} 

Иногда вам нужно объединить несколько листов в один. Это легко сделать с помощью API Aspose.Cells. В этой статье будет показан пример кода, который читает исходную книгу и объединяет данные всех исходных листов в один лист внутри целевой книги.

{{% /alert %}} 

В следующем фрагменте кода показано, как объединить несколько листов в один лист.

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
