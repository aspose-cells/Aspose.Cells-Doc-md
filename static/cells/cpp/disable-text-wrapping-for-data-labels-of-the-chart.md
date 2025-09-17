##Disable Text Wrapping for Data Labels of the Chart with C++
Learn how to disable text wrapping for data labels in charts using Aspose.Cells for C++. Our guide will show you how to prevent long labels from overlapping and provide more readable and clear chart displays.
Microsoft Excel 2013 allows users to wrap or unwrap text inside the Data Labels of the Chart. By default, the text inside the Data Labels of the Chart is in the wrapped state.
Aspose.Cells provides a [**DataLabels.IsTextWrapped**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/istextwrapped/) property which you can set True or False to Enable or Disable Text Wrapping of Data Labels respectively.
The below code sample shows how to disable text wrapping for the data labels of the chart.
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
// Path of input Excel file
U16String inputFilePath = srcDir + u"sample.xlsx";
// Path of output Excel file
U16String outputFilePath = outDir + u"Output_out.xlsx";
// Load the sample Excel file inside the workbook object
Workbook workbook(inputFilePath);
// Access the first worksheet
Worksheet worksheet = workbook.GetWorksheets().Get(0);
// Access the first chart inside the worksheet
Chart chart = worksheet.GetCharts().Get(0);
// Disable the Text Wrapping of Data Labels in all Series
chart.GetNSeries().Get(0).GetDataLabels().SetIsTextWrapped(false);
chart.GetNSeries().Get(1).GetDataLabels().SetIsTextWrapped(false);
chart.GetNSeries().Get(2).GetDataLabels().SetIsTextWrapped(false);
// Save the workbook
workbook.Save(outputFilePath);
std::cout << "Text wrapping disabled successfully in data labels!" << std::endl;
Aspose::Cells::Cleanup();
}
```
