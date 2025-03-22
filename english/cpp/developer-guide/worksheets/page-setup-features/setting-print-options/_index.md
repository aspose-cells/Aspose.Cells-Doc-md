---
title: Setting Print Options with C++
linktitle: Setting Print Options
type: docs
weight: 40
url: /cpp/setting-print-options/
description: This article demonstrates how to programmatically set the Print Options of the Excel Worksheet Page Setup feature using the C++ API and Library. You can set the Print Area, Print Titles, and Page Order.
keywords: set excel print area c++, set excel print titles c++, set excel page order c++
---

{{% alert color="primary" %}}

Microsoft Excel's page setup settings provide several print options (also referred to as sheet options) that allow users to control how worksheet pages are printed.

{{% /alert %}}

## **Setting Print Options**

These print options allow users to:

- Select a specific print area on a worksheet.
- Print titles.
- Print gridlines.
- Print row/column headings.
- Achieve draft quality.
- Print comments.
- Print cell errors.
- Define page ordering.

Aspose.Cells supports all the print options offered by Microsoft Excel, and developers can easily configure these options for worksheets using the properties offered by the [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) class. How these properties are used is discussed below in more detail.

### **Set Print Area**

By default, the print area incorporates all areas of the worksheet that contain data. Developers can establish a specific print area of the worksheet.

To select a specific print area, use the [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) class' [**PrintArea**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/printarea/) property. Assign a cell range that defines the print area to this property.

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the PageSetup object of the worksheet
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set the print area to the range A1:T35
    pageSetup.SetPrintArea(u"A1:T35");

    // Save the workbook
    workbook.Save(outDir + u"SetPrintArea_out.xls");

    std::cout << "Print area set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Set Print Titles**

Aspose.Cells allows you to designate row and column headers to repeat on all pages of a printed worksheet. To do so, use the [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) class' [**PrintTitleColumns**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/printtitlecolumns/) and [**PrintTitleRows**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/printtitlerows/) properties.

The rows or columns that will be repeated are defined by passing their row or column numbers. For example, rows are defined as $1:$2 and columns are defined as $A:$B.

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
    U16String outputFilePath = outDir + u"SetPrintTitle_out.xls";

    // Create a new workbook
    Workbook workbook;

    // Obtain the reference of the PageSetup of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Define column numbers A & B as title columns
    pageSetup.SetPrintTitleColumns(u"$A:$B");

    // Define row numbers 1 & 2 as title rows
    pageSetup.SetPrintTitleRows(u"$1:$2");

    // Save the workbook
    workbook.Save(outputFilePath);

    std::cout << "Print titles set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Set Other Print Options**

The [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) class also provides several other properties to set general print options as follows:

- [**PrintGridlines**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/printgridlines/): a Boolean property that defines whether to print gridlines or not.
- [**PrintHeadings**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/printheadings/): a Boolean property that defines whether to print row and column headings or not.
- [**BlackAndWhite**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/blackandwhite/): a Boolean property that defines whether to print the worksheet in black and white mode or not.
- [**PrintComments**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/printcomments/): defines whether to display the print comments on the worksheet or at the end of the worksheet.
- [**PrintDraft**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/printdraft/): a boolean property that defines whether to print the sheet without graphics.
- [**PrintErrors**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/printerrors/): defines whether to print cell errors as displayed, blank, dash, or N/A.

To set the [**PrintComments**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/printcomments/) and [**PrintErrors**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/printerrors/) properties, Aspose.Cells also provides two enumerations, [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) and [**PrintErrorsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printerrorstype/) that contain pre-defined values to be assigned to the [**PrintComments**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/printcomments/) and [**PrintErrors**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/printerrors/) properties respectively.

The pre-defined values in the [**PrintCommentsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printcommentstype/) enumeration are listed below with their descriptions.

|**Print Comments Types**|**Description**|
| :- | :- |
|PrintInPlace|Specifies to print comments as displayed on the worksheet.|
|PrintNoComments|Specifies not to print comments.|
|PrintSheetEnd|Specifies to print comments at the end of the worksheet.|

The pre-defined values of [**PrintErrorsType**](https://reference.aspose.com/cells/cpp/aspose.cells/printerrorstype/) enumeration are listed below with their descriptions.

|**Print Errors Types**|**Description**|
| :- | :- |
|PrintErrorsBlank|Specifies not to print errors.|
|PrintErrorsDash|Specifies to print errors as "--".|
|PrintErrorsDisplayed|Specifies to print errors as displayed.|
|PrintErrorsNA|Specifies to print errors as "#N/A".|

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the PageSetup object of the worksheet
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set print options
    pageSetup.SetPrintGridlines(true);  // Allow printing gridlines
    pageSetup.SetPrintHeadings(true);   // Allow printing row/column headings
    pageSetup.SetBlackAndWhite(true);   // Allow printing in black & white mode
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);  // Print comments as displayed
    pageSetup.SetPrintDraft(true);      // Print with draft quality
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsNA);  // Print cell errors as N/A

    // Save the workbook
    U16String outputPath = outDir + u"OtherPrintOptions_out.xls";
    workbook.Save(outputPath);

    std::cout << "Workbook saved with print options successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Set Page Order**

The [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) class provides the [**Order**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/order/) property that is used to order multiple pages of your worksheet to be printed. There are two possibilities to order the pages as follows.

- **Down then over:** prints all the pages down before printing any pages to the right.
- **Over then down:** prints pages left to right before printing the pages below.

Aspose.Cells provides an enumeration, [**PrintOrderType**](https://reference.aspose.com/cells/cpp/aspose.cells/printordertype/) that contains all pre-defined order types.

The pre-defined values of the [**PrintOrderType**](https://reference.aspose.com/cells/cpp/aspose.cells/printordertype/) enumeration are listed below.

|**Print Order Types**|**Description**|
| :- | :- |
|DownThenOver|Represents printing order as down then over.|
|OverThenDown|Represents printing order as over then down.|

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

    // Create a new workbook
    Workbook workbook;

    // Obtain the reference of the PageSetup of the first worksheet
    PageSetup pageSetup = workbook.GetWorksheets().Get(0).GetPageSetup();

    // Set the printing order of the pages to over then down
    pageSetup.SetOrder(PrintOrderType::OverThenDown);

    // Save the workbook
    workbook.Save(outDir + u"SetPageOrder_out.xls");

    std::cout << "Page order set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```