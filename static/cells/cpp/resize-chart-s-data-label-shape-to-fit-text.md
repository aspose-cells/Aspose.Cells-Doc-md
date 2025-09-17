##Resize Chart's Data Label Shape To Fit Text with C++
Learn how to resize the data label shape in a chart to fit the text in Aspose.Cells for C++. Our guide will show you how to adjust the size and shape of the label container to ensure that the text is displayed correctly without any truncation or overlapping.
Excel application provides the **Resize shape to fit text** option for Chart's DataLabels in order to increase the size of the shape so that the text fits inside of it.
## **How to Resize Chart's Data Label Shape To Fit Text in Microsoft Excel**
This option can be accessed on the Excel interface by selecting any of the data labels on the chart. Right-click and select the **Format DataLabels** menu. On **Size & Properties** tab, expand **Alignment** to reveal the related properties including the **Resize shape to fix text** option.
## **How to Resize Chart's Data Label Shape To Fit Text Using Aspose.Cells for C++**
In order to mimic Excel's feature of resizing data label shapes to fit the text, the Aspose.Cells APIs have exposed the Boolean type [**DataLabels.IsResizeShapeToFitText**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/isresizeshapetofittext) property. The following piece of code shows the simple usage scenario of [**DataLabels.IsResizeShapeToFitText**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/isresizeshapetofittext) property.
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
