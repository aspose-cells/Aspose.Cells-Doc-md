##Fill Settings with C++
Aspose.Cells is a C++ library for working with spreadsheet files. It supports setting the fill settings of cells, allowing users to customize the background and style of cells. This article will introduce how to use the Aspose.Cells library to set cell fill settings.
## **Colors and Background Patterns**
Microsoft Excel can set the foreground (outline) and background (fill) colors of cells and background patterns.
Aspose.Cells also supports these features in a flexible manner. In this topic, we learn to use these features using Aspose.Cells.
### **Setting Colors and Background Patterns**
Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides a [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. Each item in the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class.
The [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) has the [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) and [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) methods that are used to get and set a cell's formatting. The [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) class provides properties for setting the foreground and background colors of the cells. Aspose.Cells provides a [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/) enumeration that contains a set of pre-defined types of background patterns which are given below.
|**Background Patterns**|**Description**|
| :- | :- |
|DiagonalCrosshatch|Represents diagonal crosshatch pattern|
|DiagonalStripe|Represents diagonal stripe pattern|
|Gray6|Represents 6.25% gray pattern|
|Gray12|Represents 12.5% gray pattern|
|Gray25|Represents 25% gray pattern|
|Gray50|Represents 50% gray pattern|
|Gray75|Represents 75% gray pattern|
|HorizontalStripe|Represents horizontal stripe pattern|
|None|Represents no background|
|ReverseDiagonalStripe|Represents reverse diagonal stripe pattern|
|Solid|Represents solid pattern|
|ThickDiagonalCrosshatch|Represents thick diagonal crosshatch pattern|
|ThinDiagonalCrosshatch|Represents thin diagonal crosshatch pattern|
|ThinDiagonalStripe|Represents thin diagonal stripe pattern|
|ThinHorizontalCrosshatch|Represents thin horizontal crosshatch pattern|
|ThinHorizontalStripe|Represents thin horizontal stripe pattern|
|ThinReverseDiagonalStripe|Represents thin reverse diagonal stripe pattern|
|ThinVerticalStripe|Represents thin vertical stripe pattern|
|VerticalStripe|Represents vertical stripe pattern|
In the example below, the foreground color of the A1 cell is set but A2 is configured to have both foreground and background colors with a vertical stripe background pattern.
```c++
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
// Instantiating a Workbook object
Workbook workbook;
// Adding a new worksheet to the Workbook object
int i = workbook.GetWorksheets().Add();
// Obtaining the reference of the newly added worksheet by passing its sheet index
Worksheet worksheet = workbook.GetWorksheets().Get(i);
// Define a Style and get the A1 cell style
Style style = worksheet.GetCells().Get(u"A1").GetStyle();
// Setting the foreground color to yellow
style.SetForegroundColor(Color::Yellow());
// Setting the background pattern to vertical stripe
style.SetPattern(BackgroundType::VerticalStripe);
// Apply the style to A1 cell
worksheet.GetCells().Get(u"A1").SetStyle(style);
// Get the A2 cell style
style = worksheet.GetCells().Get(u"A2").GetStyle();
// Setting the foreground color to blue
style.SetForegroundColor(Color::Blue());
// Setting the background color to yellow
style.SetBackgroundColor(Color::Yellow());
// Setting the background pattern to vertical stripe
style.SetPattern(BackgroundType::VerticalStripe);
// Apply the style to A2 cell
worksheet.GetCells().Get(u"A2").SetStyle(style);
// Saving the Excel file
workbook.Save(outDir + u"book1.out.xls", SaveFormat::Excel97To2003);
std::cout << "Excel file saved successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
### **Important to Know**
- To set a cell's foreground or background color, use the [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object's [**GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) or [**GetBackgroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getbackgroundcolor/) properties. Both properties will take effect only if the [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object's [**GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) property is configured.
- The [**GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) property sets the cell's shade color.
The [**GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) property specifies the type of background pattern used for the foreground or background color. Aspose.Cells provides an enumeration, [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/). that contains a set of pre-defined types of background patterns.
- If you select *BackgroundType.None* value from the [**BackgroundType**](https://reference.aspose.com/cells/cpp/aspose.cells/backgroundtype/) enumeration, the foreground color is not applied.
Likewise, the background color is not applied if you select the *BackgroundType.None* or *BackgroundType.Solid* values.
- When retrieving cell's shading/fill color, if [**Style.GetPattern()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getpattern/) is *BackgroundType.None*, [**Style.GetForegroundColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundcolor/) will return *Color.Empty*.
### **Applying Gradient Fill Effects**
To apply your desired Gradient Fill Effects to the cell, use the [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object's [**SetTwoColorGradient**](https://reference.aspose.com/cells/cpp/aspose.cells/style/settwocolorgradient/) method accordingly.
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::System;
int main()
{
Aspose::Cells::Startup();
U16String outDir(u"..\\Data\\02_OutputDirectory\\");
Workbook workbook;
Worksheet worksheet = workbook.GetWorksheets().Get(0);
worksheet.GetCells().Get(2, 1).PutValue(u"test");
Cell cell = worksheet.GetCells().Get(u"B3");
Style style = cell.GetStyle();
style.SetIsGradient(true);
style.SetTwoColorGradient(
Color{ 0xFF, 0xFF, 0xFF, 0xFF },
Color{ 0xFF, 0x4F, 0x81, 0xBD },
GradientStyleType::Horizontal,
1
);
style.GetFont().SetColor(Color::Red());
style.SetHorizontalAlignment(TextAlignmentType::Center);
style.SetVerticalAlignment(TextAlignmentType::Center);
cell.SetStyle(style);
worksheet.GetCells().SetRowHeightPixel(2, 53);
worksheet.GetCells().Merge(2, 1, 1, 2);
workbook.Save(outDir + u"output.xlsx");
std::cout << "File saved successfully." << std::endl;
Aspose::Cells::Cleanup();
return 0;
}
```
## **Colors and Palette**
A palette is the number of colors available for use in creating an image. The use of a standardized palette in a presentation allows the user to create a consistent look. Each Microsoft Excel (97-2003) file has a palette of 56 colors that can be applied to cells, fonts, gridlines, graphic objects, fills and lines in a chart.
With Aspose.Cells it is possible not only to use the palette's existing colors but also custom colors. Before using a custom color, add it to the palette first.
This topic discusses how to add custom colors to the palette.
### **Adding Custom Colors to Palette**
Aspose.Cells supports Microsoft Excel's 56 color palette. To use a custom color that is not defined in the palette, add the color to the palette.
Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class provides a [**ChangePalette**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/changepalette/) method that takes the following parameters to add a custom color to modify the palette:
- Custom Color, the custom color to be added.
- Index, the index of the color in the palette that the custom color will replace. Should be between 0-55.
The example below adds a custom color (Orchid) to the palette before applying it on a font.
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
Aspose::Cells::Startup();
// Create a new workbook
Workbook workbook;
// Check if Orchid color is in the palette
std::cout << "Is Orchid in palette: " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;
// Add Orchid color to the palette at index 55
workbook.ChangePalette(Color::Orchid(), 55);
// Verify if Orchid color is now in the palette
std::cout << "Is Orchid in palette after change: " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;
// Add a new worksheet
int i = workbook.GetWorksheets().Add();
// Get the reference to the newly added worksheet
Worksheet worksheet = workbook.GetWorksheets().Get(i);
// Access cell A1
Cell cell = worksheet.GetCells().Get(u"A1");
// Set value in cell A1
cell.PutValue(u"Hello Aspose!");
// Create a new style
Style styleObject = workbook.CreateStyle();
// Set the custom color (Orchid) to the font
styleObject.GetFont().SetColor(workbook.GetColors()[55]);
// Apply the style to the cell
cell.SetStyle(styleObject);
// Save the workbook
workbook.Save(u"out.xlsx");
Aspose::Cells::Cleanup();
return 0;
}
```
The palette only holds 56 colors. When you add a custom color to the palette, the palette is changed and any element in the file formatted with the previous color is changed. So, when you change the palette, please be very careful. Moreover, this is the limitation in XLS (Excel 97 - 2003) file format only as there is no such limitation for XLSX or other advanced MS Excel (2007/2010 or 2013) file formats.
