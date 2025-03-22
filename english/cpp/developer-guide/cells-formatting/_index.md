---
title: Format cells with C++
linktitle: Format cells
description: Learn how to format and style cells in Aspose.Cells for C++, including number formatting, date formatting, font styles, and other cell style options. Our guide will help you create attractive and professional-looking spreadsheets.
keywords: Aspose.Cells for C++, cell formatting, styling, number formatting, date formatting, font style, cell style options, spreadsheet, create, professional look, format rows and columns.
type: docs
weight: 120
url: /cpp/cells-formatting/
---

## **Introduction**

{{% alert color="primary" %}}

Aspose.Cells provides the [**GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) and [**SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) methods of the [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class, used to get/set the formatting style of a cell. Aspose.Cells also provides a [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) class.

{{% /alert %}}

## **How to Format Cells using GetStyle and SetStyle Methods**

Apply different kinds of formatting styles on cells to set background or foreground colors, borders, fonts, horizontal and vertical alignments, indentation level, text direction, rotation angle and much more.

### **How to Use the GetStyle and SetStyle Methods**

If developers need to apply different formatting styles to different cells then it's better to get the [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) of the cell using [**Cell.GetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getstyle/) method, specify the style attributes and then apply the formatting using [**Cell.SetStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) method. An example is given below to demonstrate this approach to apply various formatting on a cell.

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

    // Obtaining the reference of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Adding some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Get the style from A1 cell
    Style style = cell.GetStyle();

    // Setting the vertical alignment
    style.SetVerticalAlignment(TextAlignmentType::Center);

    // Setting the horizontal alignment
    style.SetHorizontalAlignment(TextAlignmentType::Center);

    // Setting the font color of the text
    style.GetFont().SetColor(Color::Green());

    // Setting to shrink according to the text contained in it
    style.SetShrinkToFit(true);

    // Setting the bottom border color to red
    style.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Red());

    // Setting the bottom border type to medium
    style.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Medium);

    // Applying the style to A1 cell
    cell.SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **How to Use Style Object to Format Different Cells**

If developers need to apply the Same formatting style to different cells then they can use [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object. Please follow the steps below to use the [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object:

1. Add a [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object by calling the [**CreateStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/createstyle/) method of the [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class
1. Access the newly added [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object
1. Set the desired properties/attributes of the [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object to apply desired formatting settings
1. Assign the configured [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object to your desired cells

This approach can greatly improve the efficiency of your applications and save memory too.

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

    // Create workbook
    Workbook workbook;

    // Adding a new worksheet to the Excel object
    int i = workbook.GetWorksheets().Add();

    // Obtaining the reference of the first worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Accessing the "A1" cell from the worksheet
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Adding some value to the "A1" cell
    cell.PutValue(u"Hello Aspose!");

    // Adding a new Style
    Style style = workbook.CreateStyle();

    // Setting the vertical alignment of the text in the "A1" cell
    style.SetVerticalAlignment(TextAlignmentType::Center);

    // Setting the horizontal alignment of the text in the "A1" cell
    style.SetHorizontalAlignment(TextAlignmentType::Center);

    // Setting the font color of the text in the "A1" cell
    style.GetFont().SetColor(Color::Green());

    // Shrinking the text to fit in the cell
    style.SetShrinkToFit(true);

    // Setting the bottom border color of the cell to red
    style.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Red());

    // Setting the bottom border type of the cell to medium
    style.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Medium);

    // Assigning the Style object to the "A1" cell
    cell.SetStyle(style);

    // Apply the same style to some other cells
    worksheet.GetCells().Get(u"B1").SetStyle(style);
    worksheet.GetCells().Get(u"C1").SetStyle(style);
    worksheet.GetCells().Get(u"D1").SetStyle(style);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Excel file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **How to Use Microsoft Excel 2007 Predefined Styles**

If you need to apply different formatting styles for Microsoft Excel 2007, apply styles using the Aspose.Cells API. An example is given below to demonstrate this approach to apply a predefined style on a cell.

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

    // Path of output excel file
    U16String outputFilePath = outDir + u"book1.out.xlsx";

    // Instantiate a new Workbook
    Workbook workbook;

    // Create a style object
    Style style = workbook.CreateStyle();

    // Input a value to A1 cell
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").PutValue(u"Test");

    // Apply the style to the cell
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").SetStyle(style);

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **How to Format Selected Characters in a Cell**

Dealing with Font Settings explains how to format text in cells, but it only explains how to format all of the cell content. What if you want to format only selected characters?

Aspose.Cells supports this feature too. This topic explains how to we use this feature effectively.

### **How to Format Selected Characters**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains the [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides a [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. Each item in the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class.

The [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class provides the [**Characters**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/characters/) method that takes the following parameters to select a range of characters inside a cell:

- **Start Index**, the index of the character that the selection starts from.
- **Number of Characters**, the number of characters to select.

The [**Characters**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/characters/) method returns an instance of the [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/) class that allows developers to format the characters in the same way as they would a cell as shown below in the code example. In the output file, in the A1 cell, the word 'Visit' will be formatted with the default font but 'Aspose!' is bold and blue.

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

    // Create workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the "A1" cell
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Add value to the cell
    cell.PutValue(u"Visit Aspose!");

    // Set font of selected characters to bold
    Font font = cell.Characters(6, 7).GetFont();
    font.SetIsBold(true);

    // Set font color of selected characters to blue
    font.SetColor(Color::Blue());

    // Save the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

If you are interested in formatting a portion of Rich Text in a cell, consider using the [**Cell.GetCharacters**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcharacters/) & [**Cell.SetCharacters**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/) methods. The [**Cell.GetCharacters**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcharacters/) method is to be used to access the portions of the text and then amendments can be done using the [**Cell.SetCharacters**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/) method whereas the **Get** method returns an array of [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/) objects which can be manipulated to set various properties such as font name, font color, boldness, etc. and **Set** method can be used to apply the changes.

{{% /alert %}}

## **How to Format Rows and Columns**

Sometimes, developers need to apply the same formatting on rows or columns. Applying formatting on cells one by one often takes longer and is not a good solution.
To address this issue, Aspose.Cells provides a simple, fast way discussed in detail in this article.

### **Formatting Rows & Columns**

Aspose.Cells provides a class, the [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides a [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. The [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection provides a [**Rows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/rows/) collection.

### **How to Format a Row**

Each item in the [**Rows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/rows/) collection represents a [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/) object. The [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/) object offers the [**ApplyStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/row/applystyle/) method used to set the row's formatting. To apply the same formatting to a row, use the [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object. The steps below show how to use it.

1. Add a [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object to the [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class by calling its [**CreateStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/createstyle/) method.
1. Set the [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object's properties to apply formatting settings.
1. Make the relevant attributes ON for the [**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/) object.
1. Assign the configured [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object to the [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/) object.

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

    // Obtaining the reference of the first (default) worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Adding a new Style to the styles
    Style style = workbook.CreateStyle();

    // Setting the vertical alignment of the text in the "A1" cell
    style.SetVerticalAlignment(TextAlignmentType::Center);

    // Setting the horizontal alignment of the text in the "A1" cell
    style.SetHorizontalAlignment(TextAlignmentType::Center);

    // Setting the font color of the text in the "A1" cell
    style.GetFont().SetColor(Color::Green());

    // Shrinking the text to fit in the cell
    style.SetShrinkToFit(true);

    // Setting the bottom border color of the cell to red
    style.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Red());

    // Setting the bottom border type of the cell to medium
    style.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Medium);

    // Creating StyleFlag
    StyleFlag styleFlag;
    styleFlag.SetHorizontalAlignment(true);
    styleFlag.SetVerticalAlignment(true);
    styleFlag.SetShrinkToFit(true);
    styleFlag.SetBorders(true);
    styleFlag.SetFontColor(true);

    // Accessing a row from the Rows collection
    Row row = worksheet.GetCells().GetRows().Get(0);

    // Assigning the Style object to the Style property of the row
    row.ApplyStyle(style, styleFlag);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **How to Format a Column**

The [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection also provides a [**Columns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/columns/) collection. Each item in the [**Columns**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/columns/) collection represents a [**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/) object. Similar to a [**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/) object, the [**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/) object also offers the [**ApplyStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/row/applystyle/) method for formatting a column.

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

    // Obtaining the reference of the first (default) worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Adding a new Style to the styles
    Style style = workbook.CreateStyle();

    // Setting the vertical alignment of the text in the "A1" cell
    style.SetVerticalAlignment(TextAlignmentType::Center);

    // Setting the horizontal alignment of the text in the "A1" cell
    style.SetHorizontalAlignment(TextAlignmentType::Center);

    // Setting the font color of the text in the "A1" cell
    style.GetFont().SetColor(Color::Green());

    // Shrinking the text to fit in the cell
    style.SetShrinkToFit(true);

    // Setting the bottom border color of the cell to red
    style.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Red());

    // Setting the bottom border type of the cell to medium
    style.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Medium);

    // Creating StyleFlag
    StyleFlag styleFlag;
    styleFlag.SetHorizontalAlignment(true);
    styleFlag.SetVerticalAlignment(true);
    styleFlag.SetShrinkToFit(true);
    styleFlag.SetBorders(true);
    styleFlag.SetFontColor(true);

    // Accessing a column from the Columns collection
    Column column = worksheet.GetCells().GetColumns().Get(0);

    // Applying the style to the column
    column.ApplyStyle(style, styleFlag);

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Advance topics**
- [Alignment Settings](/cells/cpp/cells-alignment-settings/)
- [Border Settings](/cells/cpp/cells-border-settings/)
- [Set Conditional Formats of Excel and ODS files.](/cells/cpp/conditional-formatting/)
- [Excel Themes and Colors](/cells/cpp/excel-themes-and-colors/)
- [Fill Settings](/cells/cpp/cells-fill-settings/)
- [Font Settings](/cells/cpp/cells-font-settings/)
- [Format Worksheet Cells in a Workbook](/cells/cpp/format-worksheet-cells-in-a-workbook/)
- [Implement 1904 Date System](/cells/cpp/implement-1904-date-system/)
- [Merging and Unmerging Cells](/cells/cpp/merging-and-unmerging-cells/)
- [Number Settings](/cells/cpp/cells-number-settings/)
- [Get and Set Style for cells](/cells/cpp/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)