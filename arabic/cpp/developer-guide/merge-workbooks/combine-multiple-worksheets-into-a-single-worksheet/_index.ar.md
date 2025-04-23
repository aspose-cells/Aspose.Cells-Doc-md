---
title: دمج أوراق عمل متعددة إلى ورقة عمل واحدة باستخدام C++
linktitle: دمج الأوراق العمل المتعددة في ورقة عمل واحدة
type: docs
weight: 160
url: /ar/cpp/combine-multiple-worksheets-into-a-single-worksheet/
description: تعلم كيفية دمج عدة أوراق عمل في ورقة عمل واحدة باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}} 

في بعض الأحيان، قد تحتاج إلى دمج أوراق العمل المتعددة في ورقة عمل واحدة. يمكن بسهولة تحقيق ذلك باستخدام واجهة برمجة التطبيقات Aspose.Cells. سيوضح لك هذا المقال مثالًا على الكود الذي يقوم بقراءة دفتر عمل المصدر ويدمج البيانات من جميع أوراق العمل المصدر في ورقة عمل واحدة داخل دفتر عمل الوجهة.

{{% /alert %}} 

يُظهر مقطع الكود التالي لك كيفية دمج أوراق عمل متعددة في ورقة عمل واحدة.

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
