---
title: 用C++合并或取消合并多个工作表成为一个工作表
linktitle: 将多个工作表合并为单个工作表
type: docs
weight: 160
url: /zh/cpp/combine-multiple-worksheets-into-a-single-worksheet/
description: 学习如何用C++和Aspose.Cells将多个工作表合并为一个工作表。
---

{{% alert color="primary" %}} 

有时候，您需要将多个工作表合并成一个工作表。通过使用 Aspose.Cells API，可以轻松实现这一目标。本文将展示一个代码示例，该示例读取源工作簿，并将所有源工作表的数据合并到目标工作簿中的一个工作表中。

{{% /alert %}} 

以下代码片段向您展示了如何将多个工作表合并为单个工作表。

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

{{< app/cells/assistant language="cpp" >}}
