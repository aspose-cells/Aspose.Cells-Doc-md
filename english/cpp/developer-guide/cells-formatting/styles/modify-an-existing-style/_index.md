---
title: Modify an Existing Style with C++
description: Aspose.Cells is a C++ library for working with spreadsheet files that allows users to modify existing cell styles. This article will introduce how to modify an existing cell style with the Aspose.Cells library so that users can change the appearance of the cells as they need.
keywords: Modify existing styles, customize the look and feel of your application, guides, tutorials, help documentation, development documentation, API references, sample code, downloads, support.
type: docs
weight: 90
url: /cpp/modify-an-existing-style/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

To apply the same formatting options to cells, create a new formatting style object. A formatting style object is a combination of formatting characteristics, such as font, font size, indentation, number, border, patterns, etc., named and stored as a set. When applied, all of the formatting in that style **is** applied.

You can also use an existing style, save it with the workbook, and use it to format information with the same attributes.

When cells aren't explicitly formatted, the **Normal** style (the workbook's default style) is applied. Microsoft Excel predefines several styles in addition to the Normal style, including Comma, Currency, and Percent.

Aspose.Cells allows modifying any of these styles or any other style that you define with your desired attributes.

{{% /alert %}}

## **Using Microsoft Excel**

To update a style in Microsoft Excel 97‑2003:

1. On the **Format** menu, click **Style**.  
2. Select the style you want to modify from the **Style name** list.  
3. Click **Modify**.  
4. Select the style options that you want using the tabs in the Format Cells dialog.  
5. Click **OK**.  
6. Under **Style includes**, specify the style features you want.  
7. Click **OK** to save the style and apply it to the selected range.

## **Using Aspose.Cells**

The following examples demonstrate how to use the [**Style.Update**](https://reference.aspose.com/cells/cpp/aspose.cells/style/update/) method.

### **Creating and Modifying a Style**

This example creates a [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object, applies it to a range of cells, and modifies the [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object. The modifications are automatically applied to the cell and the range to which the style was applied.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create a workbook.
    Workbook workbook;

    // Create a new style object.
    Style style = workbook.CreateStyle();

    // Set the number format.
    style.SetNumber(14);

    // Set the font color to red.
    style.GetFont().SetColor(Color::Red());

    // Name the style.
    style.SetName(u"Date1");

    // Get the first worksheet cells.
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Specify the style (described above) to the A1 cell.
    cells.Get(u"A1").SetStyle(style);

    // Create a range (B1:D1).
    Range range = cells.CreateRange(u"B1", u"D1");

    // Initialize a StyleFlag object.
    StyleFlag flag;

    // Set all formatting attributes on.
    flag.SetAll(true);

    // Apply the style (described above) to the range.
    range.ApplyStyle(style, flag);

    // Modify the style (described above) and change the font color from red to black.
    style.GetFont().SetColor(Color::Black());

    // Done! Since the named style (described above) has been set to a cell and range,
    // the change will be reflected to the cell (A1) and the range (B1:D1).
    style.Update();

    // Save the Excel file.
    U16String dataDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(dataDir + u"book_styles.out.xls");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Modifying an Existing Style**

This example uses a simple template Excel file in which a style called **Percent** has already been applied to a range. The example:

1. gets the style,  
2. creates a style object, and  
3. modifies the style formatting.

The modifications are automatically applied to the range to which the style was applied.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputPath = srcDir + u"book1.xlsx";

    /*
     * Create a workbook.
     * Open a template file.
     * In the book1.xlsx file, we have applied Microsoft Excel's named style,
     * i.e., "Percent", to the range A1:C8.
    */
    Workbook workbook(inputPath);

    // We get the Percent style and create a style object.
    Style style = workbook.GetNamedStyle(u"Percent");

    // Change the number format to "0.00%".
    style.SetNumber(11);

    // Set the font color.
    Color redColor = Color::Red();
    style.GetFont().SetColor(redColor);

    // Update the style, so the style of range A1:C8 will also be changed.
    style.Update();

    // Save the Excel file.
    U16String outputPath = srcDir + u"book2.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
