---
title: 数据验证与C++
linktitle: 数据验证
type: docs
weight: 90
url: /zh/cpp/data-validation/
description: 学习如何通过Aspose.Cells for C++ API添加数据验证。
keywords: 添加数据验证、获取验证值、添加整数数据验证、添加列表数据验证、添加日期数据验证、添加时间数据验证、添加文本长度数据验证、在现有验证中添加单元格区域、检查单元格是否为下拉列表验证、添加自定义验证  
---

{{% alert color="primary" %}}

Microsoft Excel提供了一些快速筛选或验证工作表数据的优秀功能。Aspose.Cells完全支持Microsoft Excel的验证和自动筛选功能。本文介绍如何在Microsoft Excel中使用这些功能以及如何用Aspose.Cells编写相应代码。

{{% /alert %}}

## **数据验证类型和执行**

数据验证是设置有关工作表上输入的数据的规则的能力。例如，使用验证可确保标有日期的列仅包含日期，或者另一列仅包含数字。甚至可以确保标有日期的列仅包含特定范围内的日期。通过数据验证，可以控制输入工作表中单元格的内容。

Microsoft Excel 支持许多不同类型的数据验证。 每种类型用于控制输入到单元格或单元格范围中的数据类型。 下面的代码片段说明了如何验证：

- 数字是整数，即它们没有小数部分。
- 十进制数遵循正确的结构。代码示例定义了一组单元格应具有两个小数位。
- 值受限于值列表。列表验证定义了可应用于单元格或单元格范围的单独值列表。
- 日期在特定范围内。
- 时间在特定范围内。
- 文本在给定的字符长度内。

### **Microsoft Excel中的数据验证**

要使用Microsoft Excel创建验证：

1. 在工作表中，选择要应用验证的单元格。
1. 从**数据**菜单中选择**验证**。将显示验证对话框。
1. 单击**设置**选项卡并输入设置。

### **Aspose.Cells中的数据验证**

数据验证是一项强大的功能，可验证输入工作表的信息。借助数据验证，开发人员可以为用户提供选择列表，限制数据输入为特定类型或大小等功能。
在Aspose.Cells中，每个[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类都有一个[**GetValidations()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getvalidations/)属性，该属性表示一组[**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/)对象。要设置验证，设置一些[**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/)类的属性，如下所示：

- Type – 表示验证类型，可以使用[**ValidationType**](https://reference.aspose.com/cells/cpp/aspose.cells/validationtype/)枚举中预定义的值之一来指定。
- Operator – 表示验证中要使用的运算符，可以通过在 [**OperatorType**](https://reference.aspose.com/cells/cpp/aspose.cells/operatortype/) 枚举中使用预定义的值来指定。
- Formula1 – 表示与数据验证的第一部分关联的值或表达式。
- Formula2 – 表示与数据验证的第二部分关联的值或表达式。

当配置了 [**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/) 对象的属性后，开发人员可以使用 [**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/) 结构来存储有关使用创建的验证进行验证的单元格范围的信息。

#### **数据验证类型**

[**ValidationType**](https://reference.aspose.com/cells/cpp/aspose.cells/validationtype/) 枚举具有以下成员:

|**成员名称**|**描述**|
| :- | :- |
|AnyValue|表示任何类型的值。
|WholeNumber|表示整数的验证类型。
|Decimal|表示十进制数字的验证类型。
|List|表示下拉列表的验证类型。
|Date|表示日期的验证类型。
|Time|表示时间的验证类型。
|TextLength|表示文本长度的验证类型。
|Custom|表示自定义验证类型。

##### **整数数据验证**

使用这种类型的验证，用户只能输入指定范围内的整数到被验证的单元格中。接下来的代码示例展示了如何实现整数验证类型。示例创建了同样的数据验证，用Aspose.Cells来创建，就像我们以上使用Microsoft Excel创建的一样。

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

    // Create a workbook object
    Workbook workbook;

    // Create a worksheet and get the first worksheet
    Worksheet ExcelWorkSheet = workbook.GetWorksheets().Get(0);

    // Accessing the Validations collection of the worksheet
    ValidationCollection validations = workbook.GetWorksheets().Get(0).GetValidations();

    // Create Cell Area
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;

    // Creating a Validation object
    Validation validation = validations.Get(validations.Add(ca));

    // Setting the validation type to whole number
    validation.SetType(ValidationType::WholeNumber);

    // Setting the operator for validation to Between
    validation.SetOperator(OperatorType::Between);

    // Setting the minimum value for the validation
    validation.SetFormula1(u"10");

    // Setting the maximum value for the validation
    validation.SetFormula2(u"1000");

    // Applying the validation to a range of cells from A1 to B2 using the CellArea structure
    CellArea area;
    area.StartRow = 0;
    area.EndRow = 1;
    area.StartColumn = 0;
    area.EndColumn = 1;

    // Adding the cell area to Validation
    validation.AddArea(area);

    // Save the workbook
    workbook.Save(outDir + u"output.out.xls");

    std::cout << "Validation applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **列表数据验证**

这种类型的验证允许用户从下拉列表中输入值。它提供了一个列表：包含数据的一系列行。在示例中，添加了第二个工作表来保存列表源。用户只能从列表中选择值。验证区域是第一个工作表中的单元格范围 A1:A5。

在这里重要的是，将 [**Validation.GetInCellDropDown()**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/getincelldropdown/) 属性设置为 **true**。

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

    // Create a workbook object
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet1 = workbook.GetWorksheets().Get(0);

    // Add a new worksheet and access it
    int i = workbook.GetWorksheets().Add();
    Worksheet worksheet2 = workbook.GetWorksheets().Get(i);

    // Create a range in the second worksheet
    Range range = worksheet2.GetCells().CreateRange(u"E1", u"E4");

    // Name the range
    range.SetName(u"MyRange");

    // Fill different cells with data in the range
    range.Get(0, 0).PutValue(u"Blue");
    range.Get(1, 0).PutValue(u"Red");
    range.Get(2, 0).PutValue(u"Green");
    range.Get(3, 0).PutValue(u"Yellow");

    // Get the validations collection
    ValidationCollection validations = worksheet1.GetValidations();

    // Create Cell Area
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;

    // Create a new validation to the validations list
    Validation validation = validations.Get(validations.Add(ca));

    // Set the validation type
    validation.SetType(ValidationType::List);

    // Set the operator
    validation.SetOperator(OperatorType::None);

    // Set the in cell drop down
    validation.SetInCellDropDown(true);

    // Set the formula1
    validation.SetFormula1(u"=MyRange");

    // Enable it to show error
    validation.SetShowError(true);

    // Set the alert type severity level
    validation.SetAlertStyle(ValidationAlertType::Stop);

    // Set the error title
    validation.SetErrorTitle(u"Error");

    // Set the error message
    validation.SetErrorMessage(u"Please select a color from the list");

    // Specify the validation area
    CellArea area;
    area.StartRow = 0;
    area.EndRow = 4;
    area.StartColumn = 0;
    area.EndColumn = 0;

    // Add the validation area
    validation.AddArea(area);

    // Save the Excel file
    workbook.Save(outDir + u"output.out.xls");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **日期数据验证**

使用此类型的验证，用户可以在验证单元格中输入符合指定范围或特定条件的日期值。在此示例中，用户被限制只能输入1970年至1999年之间的日期。这里，验证区域是B1单元格。

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

    // Create a workbook
    Workbook workbook;

    // Obtain the cells of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Put a string value into the A1 cell
    cells.Get(u"A1").PutValue(u"Please enter Date b/w 1/1/1970 and 12/31/1999");

    // Set row height and column width for the cells
    cells.SetRowHeight(0, 31);
    cells.SetColumnWidth(0, 35);

    // Get the validations collection
    ValidationCollection validations = worksheet.GetValidations();

    // Create Cell Area
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;

    // Add a new validation
    int32_t validationIndex = validations.Add(ca);
    Validation validation = validations.Get(validationIndex);

    // Set the data validation type
    validation.SetType(ValidationType::Date);

    // Set the operator for the data validation
    validation.SetOperator(OperatorType::Between);

    // Set the value or expression associated with the data validation
    validation.SetFormula1(u"1/1/1970");

    // The value or expression associated with the second part of the data validation
    validation.SetFormula2(u"12/31/1999");

    // Enable the error
    validation.SetShowError(true);

    // Set the validation alert style
    validation.SetAlertStyle(ValidationAlertType::Stop);

    // Set the title of the data-validation error dialog box
    validation.SetErrorTitle(u"Date Error");

    // Set the data validation error message
    validation.SetErrorMessage(u"Enter a Valid Date");

    // Set and enable the data validation input message
    validation.SetInputMessage(u"Date Validation Type");
    validation.SetIgnoreBlank(true);
    validation.SetShowInput(true);

    // Set a collection of CellArea which contains the data validation settings
    CellArea cellArea;
    cellArea.StartRow = 0;
    cellArea.EndRow = 0;
    cellArea.StartColumn = 1;
    cellArea.EndColumn = 1;

    // Add the validation area
    validation.AddArea(cellArea);

    // Save the Excel file
    U16String outputPath = outDir + u"output.out.xls";
    workbook.Save(outputPath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **时间数据验证**

使用此类型的验证，用户可以在验证单元格中输入符合指定范围或特定条件的时间值。在此示例中，用户被限制只能输入上午09:00至11:30之间的时间。这里，验证区域是B1单元格。

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

    // Create a workbook
    Workbook workbook;

    // Obtain the cells of the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Put a string value into A1 cell
    cells.Get(u"A1").PutValue(u"Please enter Time b/w 09:00 and 11:30 'o Clock");

    // Set the row height and column width for the cells
    cells.SetRowHeight(0, 31);
    cells.SetColumnWidth(0, 35);

    // Get the validations collection
    ValidationCollection validations = workbook.GetWorksheets().Get(0).GetValidations();

    // Create Cell Area
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;

    // Add a new validation
    Validation validation = validations.Get(validations.Add(ca));

    // Set the data validation type
    validation.SetType(ValidationType::Time);

    // Set the operator for the data validation
    validation.SetOperator(OperatorType::Between);

    // Set the value or expression associated with the data validation
    validation.SetFormula1(u"09:00");

    // The value or expression associated with the second part of the data validation
    validation.SetFormula2(u"11:30");

    // Enable the error
    validation.SetShowError(true);

    // Set the validation alert style
    validation.SetAlertStyle(ValidationAlertType::Information);

    // Set the title of the data-validation error dialog box
    validation.SetErrorTitle(u"Time Error");

    // Set the data validation error message
    validation.SetErrorMessage(u"Enter a Valid Time");

    // Set and enable the data validation input message
    validation.SetInputMessage(u"Time Validation Type");
    validation.SetIgnoreBlank(true);
    validation.SetShowInput(true);

    // Set a collection of CellArea which contains the data validation settings
    CellArea cellArea;
    cellArea.StartRow = 0;
    cellArea.EndRow = 0;
    cellArea.StartColumn = 1;
    cellArea.EndColumn = 1;

    // Add the validation area
    validation.AddArea(cellArea);

    // Save the Excel file
    workbook.Save(outDir + u"output.out.xls");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

##### **文本长度数据验证**

使用此类型的验证，用户可以在验证单元格中输入指定长度的文本值。在此示例中，用户被限制只能输入不超过5个字符的字符串值。验证区域是B1单元格。

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

    // Obtain the cells of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Put a string value into A1 cell
    cells.Get(u"A1").PutValue(u"Please enter a string not more than 5 chars");

    // Set row height and column width for the cell
    cells.SetRowHeight(0, 31);
    cells.SetColumnWidth(0, 35);

    // Get the validations collection
    ValidationCollection validations = worksheet.GetValidations();

    // Create Cell Area
    CellArea ca;
    ca.StartRow = 0;
    ca.EndRow = 0;
    ca.StartColumn = 0;
    ca.EndColumn = 0;

    // Add a new validation
    int32_t validationIndex = validations.Add(ca);
    Validation validation = validations.Get(validationIndex);

    // Set the data validation type
    validation.SetType(ValidationType::TextLength);

    // Set the operator for the data validation
    validation.SetOperator(OperatorType::LessOrEqual);

    // Set the value or expression associated with the data validation
    validation.SetFormula1(u"5");

    // Enable the error
    validation.SetShowError(true);

    // Set the validation alert style
    validation.SetAlertStyle(ValidationAlertType::Warning);

    // Set the title of the data-validation error dialog box
    validation.SetErrorTitle(u"Text Length Error");

    // Set the data validation error message
    validation.SetErrorMessage(u" Enter a Valid String");

    // Set and enable the data validation input message
    validation.SetInputMessage(u"TextLength Validation Type");
    validation.SetIgnoreBlank(true);
    validation.SetShowInput(true);

    // Set a collection of CellArea which contains the data validation settings
    CellArea cellArea;
    cellArea.StartRow = 0;
    cellArea.EndRow = 0;
    cellArea.StartColumn = 1;
    cellArea.EndColumn = 1;

    // Add the validation area
    validation.AddArea(cellArea);

    // Save the Excel file
    U16String outputPath = outDir + u"output.out.xls";
    workbook.Save(outputPath);

    std::cout << "File saved successfully: " << outputPath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **数据验证规则**

当数据验证被实现后，可以通过为单元格分配不同的值来检查验证。[**Cell.GetValidationValue**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidationvalue/)可以用来获取验证结果。以下示例演示了使用不同值的此功能。可以从以下链接下载示例文件进行测试:

[sampleDataValidationRules.xlsx](77496339.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access Cell C1
    // Cell C1 has the Decimal Validation applied on it.
    // It can take only the values Between 10 and 20
    Cell cell = worksheet.GetCells().Get(u"C1");

    // Enter 3 inside this cell
    // Since it is not between 10 and 20, it should fail the validation
    cell.PutValue(3);

    // Check if number 3 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 3 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    // Enter 15 inside this cell
    // Since it is between 10 and 20, it should succeed the validation
    cell.PutValue(15);

    // Check if number 15 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 15 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    // Enter 30 inside this cell
    // Since it is not between 10 and 20, it should fail the validation again
    cell.PutValue(30);

    // Check if number 30 satisfies the Data Validation rule applied on this cell
    std::cout << "Is 30 a Valid Value for this Cell: " << cell.GetValidationValue() << std::endl;

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **检查单元格中的验证是否为下拉列表**

正如我们所见，可以在单元格中实施许多类型的验证。如果要检查验证是否为下拉列表，可以使用[**Validation.GetInCellDropDown()**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/getincelldropdown/)属性来测试。以下示例代码演示了如何使用此属性。测试样本文件可从以下链接下载：

[sampleValidation.xlsx](79527947.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sampleValidation.xlsx";

    // Create workbook
    Workbook book(inputFilePath);

    // Get worksheet
    Worksheet sheet = book.GetWorksheets().Get(u"Sheet1");

    // Get cells collection
    Cells cells = sheet.GetCells();

    // Check validation for cell A2
    Cell a2 = cells.Get(u"A2");
    Validation va2 = a2.GetValidation();
    if (va2.GetInCellDropDown())
    {
        std::cout << "A2 is a dropdown" << std::endl;
    }
    else
    {
        std::cout << "A2 is NOT a dropdown" << std::endl;
    }

    // Check validation for cell B2
    Cell b2 = cells.Get(u"B2");
    Validation vb2 = b2.GetValidation();
    if (vb2.GetInCellDropDown())
    {
        std::cout << "B2 is a dropdown" << std::endl;
    }
    else
    {
        std::cout << "B2 is NOT a dropdown" << std::endl;
    }

    // Check validation for cell C2
    Cell c2 = cells.Get(u"C2");
    Validation vc2 = c2.GetValidation();
    if (vc2.GetInCellDropDown())
    {
        std::cout << "C2 is a dropdown" << std::endl;
    }
    else
    {
        std::cout << "C2 is NOT a dropdown" << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **为现有验证添加CellArea**

可能存在这样的情况，您可能希望通过使用[**Validation.AddArea(CellArea cellArea)**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/addarea/)向现有的[**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/)添加[**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/)。当您使用[**Validation.AddArea(CellArea cellArea)**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/addarea/)添加[**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/)时，Aspose.Cells将检查所有现有区域，以查看新区域是否已经存在。如果文件具有大量验证，这会导致性能下降。为了克服这个问题，API提供了[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/addarea/)方法。*checkIntersection*参数指示是否检查给定区域与现有验证区域的交集。将其设置为**false**将禁用对其他区域的检查。*checkEdge*参数指示是否检查应用区域。如果新区域成为左上角区域，则内部设置将被重新构建。如果您确定新区域不是左上角区域，可以将此参数设置为**false**。

以下代码片段演示了如何使用[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/addarea/)方法向现有的[**Validation**](https://reference.aspose.com/cells/cpp/aspose.cells/validation/)添加新的[**CellArea**](https://reference.aspose.com/cells/cpp/aspose.cells/cellarea/)。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directory paths
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook workbook(srcDir + u"ValidationsSample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing the Validations collection of the worksheet
    Validation validation = worksheet.GetValidations().Get(0);

    // Create cell area
    CellArea cellArea = CellArea::CreateCellArea(u"D5", u"E7");

    // Adding the cell area to Validation
    validation.AddArea(cellArea, false, false);

    // Save the output workbook
    workbook.Save(outDir + u"ValidationsSample_out.xlsx");

    std::cout << "Validation added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

源和输出的Excel文件已附上供参考。

[源文件](96928093.xlsx)

[输出文件](96928220.xlsx)

## **高级主题**
- [获取ODS文件中的单元格验证](/cells/zh/cpp/get-cell-validation-in-ods-files/)
- [获取应用于单元格的验证](/cells/zh/cpp/get-validation-applied-on-a-cell/)
- [验证单元格值是否满足数据验证规则](/cells/zh/cpp/verify-that-cell-value-satisfies-data-validation-rules/)
