##Find Type of X and Y Values of Points in Chart Series with C++
Learn how to determine the type of X and Y values in chart series points using Aspose.Cells for C++. Our guide will explain the different types of data values and show you how to access and work with them in your charts.
## **Possible Usage Scenarios**
Sometimes, you want to know the type of X and Y values of chart points in a series. Aspose.Cells provides `ChartPoint::get_XValueType` and `ChartPoint::get_YValueType` methods that can be used for this purpose. Please note, you will have to call `Chart::Calculate()` method before you could use these properties effectively.
## **Find Type of X and Y Values of Points in Chart Series**
The following sample code loads the [sample Excel file](64716905.xlsx) and accesses the first chart inside the first worksheet. It then calls the `Chart::Calculate()` method and finds the type of X and Y values of the first chart point and prints them on the console. Please see the console output shown below for a reference.
## **Sample Code**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
int main()
{
Aspose::Cells::Startup();
// Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
// Load sample Excel file containing chart
Workbook wb(srcDir + u"sampleFindTypeOfXandYValuesOfPointsInChartSeries.xlsx");
// Access first worksheet
Worksheet ws = wb.GetWorksheets().Get(0);
// Access first chart
Chart ch = ws.GetCharts().Get(0);
// Calculate chart data
ch.Calculate();
// Access first chart point in the first series
ChartPoint pnt = ch.GetNSeries().Get(0).GetPoints().Get(0);
// Print the types of X and Y values of chart point
std::cout << "X Value Type: " << static_cast<int>(pnt.GetXValueType()) << std::endl;
std::cout << "Y Value Type: " << static_cast<int>(pnt.GetYValueType()) << std::endl;
Aspose::Cells::Cleanup();
}
```
## **Console Output**
X Value Type: IsString
Y Value Type: IsNumeric
