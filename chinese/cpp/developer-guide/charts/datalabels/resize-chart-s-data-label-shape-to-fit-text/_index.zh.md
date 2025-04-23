---  
title: 用 C++ 调整图表数据标签形状以适应文本  
description: 学习如何在 Aspose.Cells for C++ 中调整图表中数据标签的形状以适应文本。我们的指南将教您如何调节标签容器的大小和形状，确保文本正确显示，不被截断或重叠。  
keywords: Aspose.Cells for C++，图表，数据标签，形状调整，文本适应，截断，重叠。  
type: docs  
weight: 220  
url: /zh/cpp/resize-chart-s-data-label-shape-to-fit-text/  
---  

{{% alert color="primary" %}}  

Excel应用程序提供了**调整形状以适应文本**选项，用于图表的数据标签，以增大形状的尺寸，以使文本适应其中。  

{{% /alert %}}  

## **如何在Microsoft Excel中调整图表数据标签的形状以适应文本**  

此选项可通过在 Excel 界面中选择图表上的任意数据标签，右键点击并选择 **格式数据标签** 菜单，然后在 **大小与属性** 标签下展开 **对齐方式**，以显示相关属性，包括 **调整形状以适应文本** 选项。  

## **如何使用Aspose.Cells for C++调整图表数据标签形状以适应文本**  

为了模仿Excel的调整数据标签形状以适应文本的功能，Aspose.Cells API已暴露布尔类型的[**DataLabels.IsResizeShapeToFitText**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/isresizeshapetofittext)属性。以下代码展示了[**DataLabels.IsResizeShapeToFitText**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/isresizeshapetofittext)属性的简单使用场景。  

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Create an instance of Workbook containing the Chart
    Workbook book(inputFilePath);

    // Access the Worksheet that contains the Chart
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Iterate through each Chart in the Worksheet
    for (int32_t i = 0; i < sheet.GetCharts().GetCount(); i++)
    {
        Chart chart = sheet.GetCharts().Get(i);

        // Iterate through each NSeries in the Chart
        for (int32_t index = 0; index < chart.GetNSeries().GetCount(); index++)
        {
            // Access the DataLabels of indexed NSeries
            DataLabels labels = chart.GetNSeries().Get(index).GetDataLabels();

            // Set ResizeShapeToFitText property to true
            labels.SetIsResizeShapeToFitText(true);
        }

        // Calculate Chart
        chart.Calculate();
    }

    // Save the result
    U16String outputFilePath = srcDir + u"output_out.xlsx";
    book.Save(outputFilePath);

    std::cout << "Chart calculations and modifications completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  

