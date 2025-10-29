---
title: 用C++创建数据透视表和数据透视图
linktitle: 创建数据透视表和数据透视图
type: docs
weight: 20
url: /zh/cpp/create-pivot-tables-and-pivot-charts/
description: 学习如何使用Aspose.Cells结合C++在Excel文件中创建数据透视表和数据透视图。
---

{{% alert color="primary" %}}

数据透视表是一个交互式的记录汇总。例如，你的工作表中可能有数百条发票条目。数据透视表可以按客户、产品或日期汇总发票。使用微软Excel，可以通过拖动按钮快速重新整理数据透视表中的信息。

数据透视图图表是数据透视表中数据的交互式图形表示。数据透视图图表在Excel 2000中引入。使用数据透视图图表使数据更容易理解，因为数据透视表会自动创建小计和总计。

Aspose.Cells支持[数据透视表](/cells/zh/cpp/create-pivot-tables-and-pivot-charts/)和[数据透视图](/cells/zh/cpp/create-pivot-tables-and-pivot-charts/)。

{{% /alert %}}

## **添加数据透视表和数据透视图**

Aspose.Cells 提供了一组特殊的类，用于创建数据透视表。这些类用于创建和设置 PivotTable 对象，作为数据透视表对象的基本构建快：

- **PivotField**，数据透视表中的字段。
- **PivotFields**，所有PivotField对象的集合。
- **PivotTable**，工作表上的数据透视表报告。
- **PivotTables**，工作表上所有数据透视表对象的集合。

### **准备使用Aspose.Cells**

1. 下载并安装 Aspose.Cells：
   1. [下载Aspose.Cells](https://downloads.aspose.com/cells/cpp)。
   1. 在您的开发计算机上安装它。
      所有[Aspose](http://www.aspose.com/)组件安装后都为评估模式，评估模式没有时间限制，只会在生成的文档中加入水印。若要充分使用组件功能，你需要拥有有效的许可证。
1. 创建一个项目：
   1. 启动你的C++集成开发环境（如Visual Studio）。
   1. 创建新的控制台应用程序。
1. 添加引用：
   将Aspose.Cells组件添加为你的项目引用，例如，`...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll`。

### **添加数据透视表**

使用Aspose.Cells创建数据透视表：

1. 使用`Cell`对象的`PutValue`方法向工作表单元格中添加一些数据。你也可以使用已填充数据的模板文件。数据将用作数据透视表的数据源。
1. 通过调用`PivotTables`集合的`Add`方法（封装在`Worksheet`对象中）向工作表添加数据透视表。
1. 通过传递索引从`PivotTables`集合中访问新的`PivotTable`对象。使用任何封装在`PivotTable`对象中的数据透视表对象来管理表格。

下面是代码示例。

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
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Name the sheet
    sheet.SetName(u"Data");

    // Get the cells collection
    Cells cells = sheet.GetCells();

    // Set values to the cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Employee");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Quarter");
    cell = cells.Get(u"C1");
    cell.PutValue(u"Product");
    cell = cells.Get(u"D1");
    cell.PutValue(u"Continent");
    cell = cells.Get(u"E1");
    cell.PutValue(u"Country");
    cell = cells.Get(u"F1");
    cell.PutValue(u"Sale");

    // Fill employee names
    cell = cells.Get(u"A2");
    cell.PutValue(u"David");
    cell = cells.Get(u"A3");
    cell.PutValue(u"David");
    cell = cells.Get(u"A4");
    cell.PutValue(u"David");
    cell = cells.Get(u"A5");
    cell.PutValue(u"David");
    cell = cells.Get(u"A6");
    cell.PutValue(u"James");
    cell = cells.Get(u"A7");
    cell.PutValue(u"James");
    cell = cells.Get(u"A8");
    cell.PutValue(u"James");
    cell = cells.Get(u"A9");
    cell.PutValue(u"James");
    cell = cells.Get(u"A10");
    cell.PutValue(u"James");
    cell = cells.Get(u"A11");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A12");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A13");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A14");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A15");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A16");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A17");
    cell.PutValue(u"Miya");
    cell = cells.Get(u"A18");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A19");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A20");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A21");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A22");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A23");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A24");
    cell.PutValue(u"Elvis");
    cell = cells.Get(u"A25");
    cell.PutValue(u"Jean");
    cell = cells.Get(u"A26");
    cell.PutValue(u"Jean");
    cell = cells.Get(u"A27");
    cell.PutValue(u"Jean");
    cell = cells.Get(u"A28");
    cell.PutValue(u"Ada");
    cell = cells.Get(u"A29");
    cell.PutValue(u"Ada");
    cell = cells.Get(u"A30");
    cell.PutValue(u"Ada");

    // Fill quarters
    cell = cells.Get(u"B2");
    cell.PutValue(1);
    cell = cells.Get(u"B3");
    cell.PutValue(2);
    cell = cells.Get(u"B4");
    cell.PutValue(3);
    cell = cells.Get(u"B5");
    cell.PutValue(4);
    cell = cells.Get(u"B6");
    cell.PutValue(1);
    cell = cells.Get(u"B7");
    cell.PutValue(2);
    cell = cells.Get(u"B8");
    cell.PutValue(3);
    cell = cells.Get(u"B9");
    cell.PutValue(4);
    cell = cells.Get(u"B10");
    cell.PutValue(4);
    cell = cells.Get(u"B11");
    cell.PutValue(1);
    cell = cells.Get(u"B12");
    cell.PutValue(1);
    cell = cells.Get(u"B13");
    cell.PutValue(2);
    cell = cells.Get(u"B14");
    cell.PutValue(2);
    cell = cells.Get(u"B15");
    cell.PutValue(3);
    cell = cells.Get(u"B16");
    cell.PutValue(4);
    cell = cells.Get(u"B17");
    cell.PutValue(4);
    cell = cells.Get(u"B18");
    cell.PutValue(1);
    cell = cells.Get(u"B19");
    cell.PutValue(1);
    cell = cells.Get(u"B20");
    cell.PutValue(2);
    cell = cells.Get(u"B21");
    cell.PutValue(3);
    cell = cells.Get(u"B22");
    cell.PutValue(3);
    cell = cells.Get(u"B23");
    cell.PutValue(4);
    cell = cells.Get(u"B24");
    cell.PutValue(4);
    cell = cells.Get(u"B25");
    cell.PutValue(1);
    cell = cells.Get(u"B26");
    cell.PutValue(2);
    cell = cells.Get(u"B27");
    cell.PutValue(3);
    cell = cells.Get(u"B28");
    cell.PutValue(1);
    cell = cells.Get(u"B29");
    cell.PutValue(2);
    cell = cells.Get(u"B30");
    cell.PutValue(3);

    // Fill products
    cell = cells.Get(u"C2");
    cell.PutValue(u"Maxilaku");
    cell = cells.Get(u"C3");
    cell.PutValue(u"Maxilaku");
    cell = cells.Get(u"C4");
    cell.PutValue(u"Chai");
    cell = cells.Get(u"C5");
    cell.PutValue(u"Maxilaku");
    cell = cells.Get(u"C6");
    cell.PutValue(u"Chang");
    cell = cells.Get(u"C7");
    cell.PutValue(u"Chang");
    cell = cells.Get(u"C8");
    cell.PutValue(u"Chang");
    cell = cells.Get(u"C9");
    cell.PutValue(u"Chang");
    cell = cells.Get(u"C10");
    cell.PutValue(u"Chang");
    cell = cells.Get(u"C11");
    cell.PutValue(u"Geitost");
    cell = cells.Get(u"C12");
    cell.PutValue(u"Chai");
    cell = cells.Get(u"C13");
    cell.PutValue(u"Geitost");
    cell = cells.Get(u"C14");
    cell.PutValue(u"Geitost");
    cell = cells.Get(u"C15");
    cell.PutValue(u"Maxilaku");
    cell = cells.Get(u"C16");
    cell.PutValue(u"Geitost");
    cell = cells.Get(u"C17");
    cell.PutValue(u"Geitost");
    cell = cells.Get(u"C18");
    cell.PutValue(u"Ikuru");
    cell = cells.Get(u"C19");
    cell.PutValue(u"Ikuru");
    cell = cells.Get(u"C20");
    cell.PutValue(u"Ikuru");
    cell = cells.Get(u"C21");
    cell.PutValue(u"Ikuru");
    cell = cells.Get(u"C22");
    cell.PutValue(u"Ipoh Coffee");
    cell = cells.Get(u"C23");
    cell.PutValue(u"Ipoh Coffee");
    cell = cells.Get(u"C24");
    cell.PutValue(u"Ipoh Coffee");
    cell = cells.Get(u"C25");
    cell.PutValue(u"Chocolade");
    cell = cells.Get(u"C26");
    cell.PutValue(u"Chocolade");
    cell = cells.Get(u"C27");
    cell.PutValue(u"Chocolade");
    cell = cells.Get(u"C28");
    cell.PutValue(u"Chocolade");
    cell = cells.Get(u"C29");
    cell.PutValue(u"Chocolade");
    cell = cells.Get(u"C30");
    cell.PutValue(u"Chocolade");

    // Fill continents
    cell = cells.Get(u"D2");
    cell.PutValue(u"Asia");
    cell = cells.Get(u"D3");
    cell.PutValue(u"Asia");
    cell = cells.Get(u"D4");
    cell.PutValue(u"Asia");
    cell = cells.Get(u"D5");
    cell.PutValue(u"Asia");
    cell = cells.Get(u"D6");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D7");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D8");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D9");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D10");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D11");
    cell.PutValue(u"America");
    cell = cells.Get(u"D12");
    cell.PutValue(u"America");
    cell = cells.Get(u"D13");
    cell.PutValue(u"America");
    cell = cells.Get(u"D14");
    cell.PutValue(u"America");
    cell = cells.Get(u"D15");
    cell.PutValue(u"America");
    cell = cells.Get(u"D16");
    cell.PutValue(u"America");
    cell = cells.Get(u"D17");
    cell.PutValue(u"America");
    cell = cells.Get(u"D18");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D19");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D20");
    cell.PutValue(u"Europe");
    cell = cells.Get(u"D21");
    cell.PutValue(u"Oceania");
    cell = cells.Get(u"D22");
    cell.PutValue(u"Oceania");
    cell = cells.Get(u"D23");
    cell.PutValue(u"Oceania");
    cell = cells.Get(u"D24");
    cell.PutValue(u"Oceania");
    cell = cells.Get(u"D25");
    cell.PutValue(u"Africa");
    cell = cells.Get(u"D26");
    cell.PutValue(u"Africa");
    cell = cells.Get(u"D27");
    cell.PutValue(u"Africa");
    cell = cells.Get(u"D28");
    cell.PutValue(u"Africa");
    cell = cells.Get(u"D29");
    cell.PutValue(u"Africa");
    cell = cells.Get(u"D30");
    cell.PutValue(u"Africa");

    // Fill countries
    cell = cells.Get(u"E2");
    cell.PutValue(u"China");
    cell = cells.Get(u"E3");
    cell.PutValue(u"India");
    cell = cells.Get(u"E4");
    cell.PutValue(u"Korea");
    cell = cells.Get(u"E5");
    cell.PutValue(u"India");
    cell = cells.Get(u"E6");
    cell.PutValue(u"France");
    cell = cells.Get(u"E7");
    cell.PutValue(u"France");
    cell = cells.Get(u"E8");
    cell.PutValue(u"Germany");
    cell = cells.Get(u"E9");
    cell.PutValue(u"Italy");
    cell = cells.Get(u"E10");
    cell.PutValue(u"France");
    cell = cells.Get(u"E11");
    cell.PutValue(u"U.S.");
    cell = cells.Get(u"E12");
    cell.PutValue(u"U.S.");
    cell = cells.Get(u"E13");
    cell.PutValue(u"Brazil");
    cell = cells.Get(u"E14");
    cell.PutValue(u"U.S.");
    cell = cells.Get(u"E15");
    cell.PutValue(u"U.S.");
    cell = cells.Get(u"E16");
    cell.PutValue(u"Canada");
    cell = cells.Get(u"E17");
    cell.PutValue(u"U.S.");
    cell = cells.Get(u"E18");
    cell.PutValue(u"Italy");
    cell = cells.Get(u"E19");
    cell.PutValue(u"France");
    cell = cells.Get(u"E20");
    cell.PutValue(u"Italy");
    cell = cells.Get(u"E21");
    cell.PutValue(u"New Zealand");
    cell = cells.Get(u"E22");
    cell.PutValue(u"Australia");
    cell = cells.Get(u"E23");
    cell.PutValue(u"Australia");
    cell = cells.Get(u"E24");
    cell.PutValue(u"New Zealand");
    cell = cells.Get(u"E25");
    cell.PutValue(u"S.Africa");
    cell = cells.Get(u"E26");
    cell.PutValue(u"S.Africa");
    cell = cells.Get(u"E27");
    cell.PutValue(u"S.Africa");
    cell = cells.Get(u"E28");
    cell.PutValue(u"Egypt");
    cell = cells.Get(u"E29");
    cell.PutValue(u"Egypt");
    cell = cells.Get(u"E30");
    cell.PutValue(u"Egypt");

    // Fill sales
    cell = cells.Get(u"F2");
    cell.PutValue(2000);
    cell = cells.Get(u"F3");
    cell.PutValue(500);
    cell = cells.Get(u"F4");
    cell.PutValue(1200);
    cell = cells.Get(u"F5");
    cell.PutValue(1500);
    cell = cells.Get(u"F6");
    cell.PutValue(500);
    cell = cells.Get(u"F7");
    cell.PutValue(1500);
    cell = cells.Get(u"F8");
    cell.PutValue(800);
    cell = cells.Get(u"F9");
    cell.PutValue(900);
    cell = cells.Get(u"F10");
    cell.PutValue(500);
    cell = cells.Get(u"F11");
    cell.PutValue(1600);
    cell = cells.Get(u"F12");
    cell.PutValue(600);
    cell = cells.Get(u"F13");
    cell.PutValue(2000);
    cell = cells.Get(u"F14");
    cell.PutValue(500);
    cell = cells.Get(u"F15");
    cell.PutValue(900);
    cell = cells.Get(u"F16");
    cell.PutValue(700);
    cell = cells.Get(u"F17");
    cell.PutValue(1400);
    cell = cells.Get(u"F18");
    cell.PutValue(1350);
    cell = cells.Get(u"F19");
    cell.PutValue(300);
    cell = cells.Get(u"F20");
    cell.PutValue(500);
    cell = cells.Get(u"F21");
    cell.PutValue(1000);
    cell = cells.Get(u"F22");
    cell.PutValue(1500);
    cell = cells.Get(u"F23");
    cell.PutValue(1500);
    cell = cells.Get(u"F24");
    cell.PutValue(1600);
    cell = cells.Get(u"F25");
    cell.PutValue(1000);
    cell = cells.Get(u"F26");
    cell.PutValue(1200);
    cell = cells.Get(u"F27");
    cell.PutValue(1300);
    cell = cells.Get(u"F28");
    cell.PutValue(1500);
    cell = cells.Get(u"F29");
    cell.PutValue(1400);
    cell = cells.Get(u"F30");
    cell.PutValue(1000);

    // Add a new sheet
    Worksheet sheet2 = workbook.GetWorksheets().Get(workbook.GetWorksheets().Add());
    sheet2.SetName(u"PivotTable");

    // Get the pivot tables collection
    PivotTableCollection pivotTables = sheet2.GetPivotTables();

    // Add a pivot table
    int index = pivotTables.Add(u"=Data!A1:F30", u"B3", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(index);

    // Show grand totals
    pivotTable.SetShowRowGrandTotals(true);
    pivotTable.SetShowColumnGrandTotals(true);

    // Set auto format
    pivotTable.SetIsAutoFormat(true);
    pivotTable.SetAutoFormatType(PivotTableAutoFormatType::Report6);

    // Add fields to row area
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 1);

    // Add fields to column area
    pivotTable.AddFieldToArea(PivotFieldType::Column, 3);

    // Add fields to data area
    pivotTable.AddFieldToArea(PivotFieldType::Data, 5);

    // Set number format for the first data field
    pivotTable.GetDataFields().Get(0).SetNumberFormat(u"$#,##0.00");

    // Save the workbook
    workbook.Save(outDir + u"pivotTable_test.out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **添加数据透视图**

使用Aspose.Cells创建数据透视图：

1. 添加图表。
1. 设置图表的`PivotSource`，指向工作表中的现有数据透视表。
1. 设置其他属性。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"pivotTable_test.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"pivotChart_test_out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Adding a new sheet
    Worksheet sheet3 = workbook.GetWorksheets().Get(workbook.GetWorksheets().Add(SheetType::Chart));

    // Naming the sheet
    sheet3.SetName(u"PivotChart");

    // Adding a column chart
    int index = sheet3.GetCharts().Add(ChartType::Column, 0, 5, 28, 16);

    // Setting the pivot chart data source
    sheet3.GetCharts().Get(index).SetPivotSource(u"PivotTable!PivotTable1");
    sheet3.GetCharts().Get(index).SetHidePivotFieldButtons(false);

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Pivot chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
