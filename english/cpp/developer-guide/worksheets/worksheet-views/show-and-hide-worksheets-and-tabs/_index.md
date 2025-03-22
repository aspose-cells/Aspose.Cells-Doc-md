---
title: Show and Hide Worksheets and Tabs with C++
linktitle: Show and Hide Worksheets and Tabs
type: docs
weight: 10
url: /cpp/show-and-hide-worksheets-and-tabs/
description: This article provides sample code for using the C++ API or Library to programmatically display and hide an Excel worksheet. Additionally, how to show and hide Excel workbook tabs.
---

{{% alert color="primary" %}}

Aspose.Cells allows the user to show and hide elements of a workbook including worksheets and tabs.

{{% /alert %}}

## **Show and Hide a Worksheet**

An Excel file can have one or more than one worksheets. Whenever we create an Excel file, we add worksheets to the Excel file in which we work. Each worksheet in an Excel file is independent from the other worksheet by having its own data and formatting settings etc. Sometimes, developers may require to make few worksheets hidden and others visible in the Excel file for their own interest. So, **Aspose.Cells** allows developers to control the visibility of the worksheets in their Excel files.

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides a wide range of properties and methods to manage worksheets. To control a worksheet's visibility, use the [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) property of the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) is a Boolean property, which means that it can only store a **true** or **false** value.

### **Making a Worksheet Visible**

Make a worksheet visible by setting the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class' [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) property to **true**.

### **Hiding a Worksheet**

Hide a worksheet by setting the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class' [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) property to **false**.

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

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the first worksheet of the Excel file
    worksheet.SetIsVisible(false);

    // Save the modified Excel file in default (Excel 2003) format
    U16String outputFilePath = outDir + u"output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Worksheet hidden and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Show and Hide Tabs**

If you closely look at the bottom of a Microsoft Excel file, you will see a number of controls. These include:

- Sheet tabs.
- Tab scrolling buttons.

Sheet tabs represent the worksheets in the Excel file. Click any tab to switch to that worksheet. The more worksheets in the workbook, the more sheet tabs there are. If the Excel file has a good number of worksheets you need buttons to navigate through them. So, Microsoft Excel provides tab scrolling buttons for scrolling through the sheet tabs.

Using Aspose.Cells, developers can control the visibility of sheet tabs and tabs scrolling buttons in Excel files.

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class provides a wide range of properties and methods to manage an Excel file. To control the visibility of tabs in an Excel file, developers can use the [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class' [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/showtabs/) property. [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/showtabs/) is a Boolean property, which means that it can only store a **true** or **false** value.

### **Making Tabs Visible**

Make tabs visible with the [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class' [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/showtabs/) property to **true**.

### **Hiding Tabs**

Hide tabs in an Excel file by setting the [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class' [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/showtabs/) property to **false**.

Below is a complete example that opens an Excel file (book1.xls), hides its tabs and saves the modified file as output.xls. After the code execution, you will see that the tabs of the workbook are hidden.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get workbook settings
    WorkbookSettings settings = workbook.GetSettings();

    // Hiding the tabs of the Excel file
    settings.SetShowTabs(false);

    // Shows the tabs of the Excel file
    // settings.SetShowTabs(true);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Controlling the Tab Bar Width**

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get workbook settings
    WorkbookSettings settings = workbook.GetSettings();

    // Show tabs in the Excel file
    settings.SetShowTabs(true);

    // Adjust the sheet tab bar width
    settings.SetSheetTabBarWidth(800);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```