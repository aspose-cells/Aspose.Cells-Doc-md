##Rich Text Custom Data Label of Chart Point with C++
Learn how to add rich text custom data labels to chart points in Aspose.Cells for C++. Our guide will show you how to format the labels with different fonts, colors, and alignment options to enhance the appearance and readability of your charts.
You can use Aspose.Cells to create rich text custom data label of the chart point. Aspose.Cells provides the [DataLabels.Characters()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/characters/) method to return the [FontSetting](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/) object which can be used to set the font properties of the text like its color, boldness, etc.
## Rich Text Custom Data Label of Chart Point
The following code accesses the first chart point of the first series, sets its text and then sets the font of the first 10 characters by setting its color to red and boldness to **true**.
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
// Create a workbook from source Excel file
Workbook workbook(srcDir + u"sample.xlsx");
// Access first worksheet
Worksheet worksheet = workbook.GetWorksheets().Get(0);
// Access the first chart inside the sheet
Chart chart = worksheet.GetCharts().Get(0);
// Access the data label of first series first point
DataLabels dlbls = chart.GetNSeries().Get(0).GetPoints().Get(0).GetDataLabels();
// Set data label text
dlbls.SetText(u"Rich Text Label");
// Set the font setting of the first 10 characters
FontSetting fntSetting = dlbls.Characters(0, 10);
fntSetting.GetFont().SetColor(Color::Red());
fntSetting.GetFont().SetIsBold(true);
// Save the workbook
workbook.Save(srcDir + u"output_out.xlsx");
Aspose::Cells::Cleanup();
}
```
