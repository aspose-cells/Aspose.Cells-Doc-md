---
title: 用C++加载和管理Excel、OpenOffice、Json、Csv和Html文件
linktitle: 打开文件
type: docs
weight: 20
url: /zh/cpp/loading-saving-and-managing/
description: 使用Aspose.Cells for C++，创建、打开和管理Excel、CSV、TSV、ODS、HTML、Numbers、Json、XML、Pdf、Jpg、Tiff、图片、Mht及XPS文件变得简单。
---

{{% alert color="primary" %}}

使用Aspose.Cells for C++，轻松创建、打开和管理Excel文件，例如检索数据或使用设计模板以加快开发过程。

{{% /alert %}}

## **创建新工作簿**
以下示例从零创建一个新工作簿。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    try
    {
        // Create a License object
        License license;

        // Set the license of Aspose.Cells to avoid the evaluation limitations
        license.SetLicense(srcDir + u"Aspose.Cells.lic");
    }
    catch (const std::exception& ex)
    {
        std::cerr << ex.what() << std::endl;
    }

    // Instantiate a Workbook object that represents Excel file.
    Workbook wb;

    // When you create a new workbook, a default "Sheet1" is added to the workbook.
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Access the "A1" cell in the sheet.
    Cell cell = sheet.GetCells().Get(u"A1");

    // Input the "Hello World!" text into the "A1" cell
    cell.PutValue(u"Hello World!");

    // Save the Excel file.
    wb.Save(srcDir + u"MyBook_out.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **打开和保存文件**
使用Aspose.Cells for C++，简单打开、保存和管理Excel文件。

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"dest.xlsx";

    // Create a Workbook object and open an Excel file using its file path
    Workbook workbook1(inputFilePath);

    // Adding new sheet
    WorksheetCollection sheets = workbook1.GetWorksheets();
    Worksheet sheet = sheets.Add(u"MySheet");

    // Setting active sheet
    sheets.SetActiveSheetIndex(1);

    // Setting values
    Cells cells = sheet.GetCells();

    // Setting text
    cells.Get(u"A1").PutValue(u"Hello!");

    // Setting number
    cells.Get(u"A2").PutValue(1000);

    // Setting Date Time
    Cell cell = cells.Get(u"A3");
    Date currentDate;
    currentDate.year = 2023; // Replace with actual current year
    currentDate.month = 10;  // Replace with actual current month
    currentDate.day = 5;     // Replace with actual current day
    currentDate.hour = 12;   // Replace with actual current hour
    currentDate.minute = 30; // Replace with actual current minute
    currentDate.second = 0;  // Replace with actual current second
    cell.PutValue(currentDate);

    // Setting style for date
    Style style = cell.GetStyle();
    style.SetNumber(14);
    cell.SetStyle(style);

    // Setting formula
    cells.Get(u"A4").SetFormula(u"=SUM(A1:A3)");

    // Saving the workbook to disk
    workbook1.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高级主题**
- [打开文件的不同方式](/cells/zh/cpp/different-ways-to-open-files/)
- [在加载工作簿时过滤定义的名称](/cells/zh/cpp/filter-defined-names-while-loading-workbook/)
- [在加载工作簿或工作表时过滤对象](/cells/zh/cpp/filter-objects-while-loading-workbook-or-worksheet/)
- [在从模板文件加载工作簿时过滤数据类型](/cells/zh/cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/)
- [加载Excel文件时获取警告信息](/cells/zh/cpp/get-warnings-while-loading-excel-file/)
- [在不包含图表的源Excel文件中加载](/cells/zh/cpp/load-source-excel-file-without-charts/)
- [加载工作簿中特定的工作表](/cells/zh/cpp/load-specific-worksheets-in-a-workbook/)
- [使用指定打印纸张大小加载工作簿](/cells/zh/cpp/load-workbook-with-specified-printer-paper-size/)
- [打开不同版本的Microsoft Excel文件](/cells/zh/cpp/opening-different-microsoft-excel-versions-files/)
- [打开具有不同格式的文件](/cells/zh/cpp/opening-files-with-different-formats/)
- [优化处理大数据集大文件的内存使用](/cells/zh/cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
- [使用Aspose.Cells读取由苹果公司开发的Numbers电子表格](/cells/zh/cpp/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [当转换或加载时间过长时，使用InterruptMonitor中断转换或加载流程](/cells/zh/cpp/stop-conversion-or-loading-using-interruptmonitor-when-it-is-taking-too-long/)
- [使用LightCells API](/cells/zh/cpp/using-lightcells-api/)
- [将CSV转换为JSON](/cells/zh/cpp/convert-csv-to-json/)
- [将Excel转换为JSON](/cells/zh/cpp/convert-excel-to-json/)
- [将JSON转换为CSV](/cells/zh/cpp/convert-json-to-csv/)
- [将JSON转换为Excel](/cells/zh/cpp/convert-json-to-excel/)
- [将Excel转换为Html](/cells/zh/cpp/convert-excel-to-html/)
