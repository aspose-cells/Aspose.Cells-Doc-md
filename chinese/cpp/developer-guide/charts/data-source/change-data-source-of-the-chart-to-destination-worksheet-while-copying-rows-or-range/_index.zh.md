---  
title: 在复制行或区域时将图表数据源更改为目标工作表，使用C++  
description: 了解在复制行或范围到Aspose.Cells for C++时，如何将图表的数据源更改为目标工作表。我们的指南将向您展示如何更新图表的数据范围并将其链接到目标工作表，确保复制的行或范围在图表中得到准确反映。  
keywords: Aspose.Cells for C++，制图，数据源，目标工作表，行，区域，复制，更新，数据范围，链接。  
type: docs  
weight: 440  
url: /zh/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/  
---  

## **可能的使用场景**

当你复制包含图表的行或区域到新工作表时，图表的数据源不会改变。例如，如果图表的数据源是=Sheet1!$A$1:$B$4，那么复制到新工作表后，数据源仍然是=Sheet1!$A$1:$B$4，仍指向旧的工作表Sheet1。这也是Microsoft Excel中的默认行为。但如果您想让它指向新的目标工作表，请使用[**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/copyoptions/getrefertodestinationsheet/)属性，并在调用[**Cells.CopyRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/copyrows/)方法时设置为**true**。假如目标工作表是DestSheet，那么您的图表数据源将从=Sheet1!$A$1:$B$4变为=DestSheet!$A$1:$B$4。

## **复制行或区域时更改图表的数据源到目标工作表**

以下示例代码解释了在复制包含图表的行或区域到新工作表时使用[**CopyOptions.GetReferToDestinationSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/copyoptions/getrefertodestinationsheet/)属性的方法。代码使用示例Excel文件（5113699.xlsx），并生成输出Excel文件（5113697.xlsx）。

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

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

    // Load sample Excel file
    Workbook wb(srcDir + u"sample.xlsx");

    // Access the first sheet which contains chart
    Worksheet source = wb.GetWorksheets().Get(0);

    // Add another sheet named DestSheet
    Worksheet destination = wb.GetWorksheets().Add(u"DestSheet");

    // Set CopyOptions.ReferToDestinationSheet to true
    CopyOptions options;
    options.SetReferToDestinationSheet(true);

    // Copy all the rows of source worksheet to destination worksheet which includes chart as well
    // The chart data source will now refer to DestSheet
    destination.GetCells().CopyRows(source.GetCells(), 0, 0, source.GetCells().GetMaxDisplayRange().GetRowCount(), options);

    // Save workbook in xlsx format
    wb.Save(srcDir + u"output_out.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
{{< app/cells/assistant language="cpp" >}}
