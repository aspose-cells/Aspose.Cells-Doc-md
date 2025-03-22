---
title: Format and Modify Named Ranges with C++
linktitle: Format and Modify Named Ranges
type: docs
weight: 85
url: /cpp/format-and-modify-named-ranges/
description: Learn how to format, rename, merge, and remove named ranges in Excel files using Aspose.Cells with C++.
---

## **Format Ranges**

### **Setting Background Color and Font Attributes to a Named Range**

To apply formatting, define a [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object to specify the style settings and apply it to the [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) object.

The following example shows how to set the solid fill color (shading color) with font settings to a range.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet WS = workbook.GetWorksheets().Get(0);
    Range range = WS.GetCells().CreateRange(1, 1, 1, 18);

    range.SetName(u"MyRange");

    Style stl = workbook.CreateStyle();

    stl.GetFont().SetName(u"Arial");
    stl.GetFont().SetIsBold(true);
    stl.GetFont().SetColor(Color::Red());
    stl.SetForegroundColor(Color::Yellow());
    stl.SetPattern(BackgroundType::Solid);

    StyleFlag flg;
    flg.SetFont(true);
    flg.SetCellShading(true);

    range.ApplyStyle(stl, flg);

    workbook.Save(outDir + u"rangestyles.out.xls");

    Aspose::Cells::Cleanup();
}
```

### **Adding Borders to a Named Range**

It is possible to add borders to a range of cells instead of just a single cell. The [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) object provides a [**SetOutlineBorder**](https://reference.aspose.com/cells/cpp/aspose.cells/range/setoutlineborder/) method that takes the following parameters to add a border to the range of cells:

- Border type, the type of border, selected from the [**BorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/bordertype/) enumeration.
- Line style, the line style, selected from the [**CellBorderType**](https://reference.aspose.com/cells/cpp/aspose.cells/cellbordertype/) enumeration.
- Color, the line color, selected from the Color enumeration.

The following example shows how to set an outline border to a range.

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

    // Instantiating a Workbook object
    Workbook workbook;

    // Clears the worksheets
    workbook.GetWorksheets().Clear();

    // Adding a new worksheet to the Workbook object
    workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Adding some value to the "A1" cell
    cell.PutValue(u"Hello World From Aspose");

    // Creating a range of cells starting from "A1" cell to 3rd column in a row
    Range range = worksheet.GetCells().CreateRange(0, 0, 1, 3);

    // Adding a thick top border with blue line
    range.SetOutlineBorder(BorderType::TopBorder, CellBorderType::Thick, Color::Blue());

    // Adding a thick bottom border with blue line
    range.SetOutlineBorder(BorderType::BottomBorder, CellBorderType::Thick, Color::Blue());

    // Adding a thick left border with blue line
    range.SetOutlineBorder(BorderType::LeftBorder, CellBorderType::Thick, Color::Blue());

    // Adding a thick right border with blue line
    range.SetOutlineBorder(BorderType::RightBorder, CellBorderType::Thick, Color::Blue());

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

The following example shows how to set borders around each cell in the range.

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

    // Instantiate a new Workbook
    Workbook workbook;

    // Access the cells in the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Create a range of cells
    Range range = cells.CreateRange(u"A6", u"P216");

    // Create the style adding to the style collection
    Style stl = workbook.CreateStyle();

    // Specify the font settings
    stl.GetFont().SetName(u"Arial");
    stl.GetFont().SetIsBold(true);
    stl.GetFont().SetColor(Color::Blue());

    // Set the borders
    stl.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    stl.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Blue());
    stl.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    stl.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Blue());
    stl.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    stl.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Blue());
    stl.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    stl.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Blue());

    // Create StyleFlag object
    StyleFlag flg;

    // Make the corresponding formatting attributes ON
    flg.SetFont(true);
    flg.SetBorders(true);

    // Apply the style with format settings to the range
    range.ApplyStyle(stl, flg);

    // Save the excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Rename a Named Range**

Aspose.Cells allows you to rename a named range for your need. You may get the named range and rename it by using [**Name.Text**](https://reference.aspose.com/cells/cpp/aspose.cells/name/text/) attribute. The following example shows how to rename a named range.

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
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"RenamingRange.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the Cells of the sheet
    Cells cells = sheet.GetCells();

    // Get the named range "TestRange"
    Name name = workbook.GetWorksheets().GetNames().Get(u"TestRange");

    // Rename it
    name.SetText(u"NewRange");

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Range renamed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Union of Ranges**

Aspose.Cells provides [**Range.Union**](https://reference.aspose.com/cells/cpp/aspose.cells/range/union/) method to take the union for ranges, the method returns a [*std::vector*](https://en.cppreference.com/w/cpp/container/vector) object. The following example shows how to take union for ranges.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook workbook(srcDir + u"book1.xls");

    Vector<Range> ranges = workbook.GetWorksheets().GetNamedRanges();

    Style style = workbook.CreateStyle();
    style.SetForegroundColor(Color::Yellow());
    style.SetPattern(BackgroundType::Solid);

    StyleFlag flag;
    flag.SetCellShading(true);

    Vector<Range> unionParams{ ranges[1] };
    UnionRange unionResult = ranges[0].UnionRanges(unionParams);
    Vector<Range> al = unionResult.GetRanges();

    for (int i = 0; i < al.GetLength(); i++)
    {
        Range rng = al[i];
        rng.ApplyStyle(style, flag);
    }

    workbook.Save(outDir + u"rngUnion.out.xls");

    std::cout << "Style applied to union ranges successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Intersection of Ranges**

Aspose.Cells provides the [**Range.Intersect**](https://reference.aspose.com/cells/cpp/aspose.cells/range/intersect/) method to intersect two ranges. The method returns a [**Range**](https://reference.aspose.com/cells/cpp/aspose.cells/range/) object. To check whether a range intersects another range, use the [**Range.Intersect**](https://reference.aspose.com/cells/cpp/aspose.cells/range/intersect/) method that returns a Boolean value. The following example shows how to intersect the ranges.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output excel file
    U16String outputFilePath = outDir + u"rngIntersection.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the named ranges
    Vector<Range> ranges = workbook.GetWorksheets().GetNamedRanges();

    // Check whether the first range intersects the second range
    bool isIntersect = ranges[0].IsIntersect(ranges[1]);

    // Create a style object
    Style style = workbook.CreateStyle();

    // Set the shading color with solid pattern type
    style.SetForegroundColor(Color::Yellow());
    style.SetPattern(BackgroundType::Solid);

    // Create a styleflag object
    StyleFlag flag;

    // Apply the cell shading
    flag.SetCellShading(true);

    // If first range intersects second range
    if (isIntersect)
    {
        // Create a range by getting the intersection
        Range intersection = ranges[0].Intersect(ranges[1]);

        // Name the range
        intersection.SetName(u"Intersection");

        // Apply the style to the range
        intersection.ApplyStyle(style, flag);
    }

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Range intersection processed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Merge Cells in the Named Range**

Aspose.Cells provides [**Range.Merge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/merge/) method to merge the cells in the range. The following example shows how to merge the individual cells of a named range.

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

    // Instantiate a new Workbook
    Workbook wb1;

    // Get the first worksheet in the workbook
    Worksheet worksheet1 = wb1.GetWorksheets().Get(0);

    // Create a range
    Range mrange = worksheet1.GetCells().CreateRange(u"A18", u"J18");

    // Name the range
    mrange.SetName(u"Details");

    // Merge the cells of the range
    mrange.Merge();

    // Get the range by name
    Range range1 = wb1.GetWorksheets().GetRangeByName(u"Details");

    // Define a style object
    Style style = wb1.CreateStyle();

    // Set the alignment
    style.SetHorizontalAlignment(TextAlignmentType::Center);

    // Create a StyleFlag object
    StyleFlag flag;
    // Make the relative style attribute ON
    flag.SetHorizontalAlignment(true);

    // Apply the style to the range
    range1.ApplyStyle(style, flag);

    // Input data into range
    range1.Get(0, 0).PutValue(u"Aspose");

    // Save the excel file
    wb1.Save(outDir + u"mergingrange.out.xls");

    std::cout << "Range merged and styled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Remove a Named Range**

Aspose.Cells provides the [**NameCollection.RemoveAt()**](https://reference.aspose.com/cells/cpp/aspose.cells/namecollection/removeat/) method to erase the name of the range. To clear the contents of the range, use [**Cells.ClearRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/clearrange/) method. The following example shows how to remove a named range with its contents.

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

    // Instantiate a new Workbook
    Workbook workbook;

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first worksheet in the worksheets collection
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create a range of cells
    Range range1 = worksheet.GetCells().CreateRange(u"E12", u"I12");

    // Name the range
    range1.SetName(u"MyRange");

    // Set the outline border to the range
    range1.SetOutlineBorder(BorderType::TopBorder, CellBorderType::Medium, Color::AliceBlue());
    range1.SetOutlineBorder(BorderType::BottomBorder, CellBorderType::Medium, Color::Red());
    range1.SetOutlineBorder(BorderType::LeftBorder, CellBorderType::Medium, Color::AliceBlue());
    range1.SetOutlineBorder(BorderType::RightBorder, CellBorderType::Medium, Color::Red());

    // Input some data with some formattings into a few cells in the range
    range1.Get(0, 0).PutValue(u"Test");
    range1.Get(0, 4).PutValue(u"123");

    // Create another range of cells
    Range range2 = worksheet.GetCells().CreateRange(u"B3", u"F3");

    // Name the range
    range2.SetName(u"testrange");

    // Copy the first range into second range
    range2.Copy(range1);

    // Remove the previous named range (range1) with its contents
    worksheet.GetCells().ClearRange(11, 4, 11, 8);
    worksheets.GetNames().RemoveAt(0);

    // Save the excel file
    workbook.Save(outDir + u"copyranges.out.xls");

    Aspose::Cells::Cleanup();
}
```