---
title: Birden Çok Çalışma Sayfasını Tek Sayfaya Birleştir ile C++
linktitle: Birden Fazla Çalışsayfayı Tek Bir Çalışsayfada Birleştirme
type: docs
weight: 160
url: /tr/cpp/combine-multiple-worksheets-into-a-single-worksheet/
description: Aspose.Cells kullanarak birden fazla çalışma sayfasını nasıl tek bir sayfaya birleştireceğinizi öğrenin.
---

{{% alert color="primary" %}} 

Bazen birden fazla çalışsayfayı tek bir çalışsayfada birleştirmeniz gerekebilir. Bu, Aspose.Cells API'sını kullanarak kolayca gerçekleştirilebilir. Bu makale, bir kaynak çalışma kitabını okuyan ve tüm kaynak çalışsayfaların verilerini bir hedef çalışma kitabının içinde tek bir çalışsayfada birleştiren bir kod örneği gösterecektir.

{{% /alert %}} 

Aşağıdaki kod parçacığı, birden fazla çalışsayfayı tek bir çalışsayfada birleştirmenin nasıl yapılacağını göstermektedir.

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
