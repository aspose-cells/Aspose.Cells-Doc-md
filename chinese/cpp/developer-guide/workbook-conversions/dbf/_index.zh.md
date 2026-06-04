---
title: 读取和写入 DBF 文件
description: Aspose.Cells 是一个用于处理电子表格文件的 C++ 库，支持读取和写入 dBASE III 和 IV (DBF) 文件。本文介绍如何使用 Aspose.Cells 导入和导出 DBF 文件中的数据，包括文件格式细节、支持的功能以及分步示例。
keywords: Aspose.Cells, C++ 库, DBF, dBASE, 读取 DBF, 写入 DBF, 导入 DBF, 导出 DBF, 文件格式, .dbf
type: docs
weight: 200
url: /zh/cpp/reading-and-writing-dbf-files/
---

{{% alert color="primary" %}}

Aspose.Cells 提供对读取和写入 DBF (dBASE) 文件的全面支持。您可以将现有的 dBASE III 和 dBASE IV 文件加载到 Workbook 对象中，使用强大的 Aspose.Cells API 操作数据，然后将工作簿保存回 DBF 格式，以便与旧版数据库应用程序配合使用。

{{% /alert %}}

## **简介**

DBF（DataBase File）是一种旧版数据库文件格式，最初由 dBASE 在 1980 年代初推出。尽管该格式年代久远，但 DBF 文件仍广泛用于许多行业，用于存储结构化数据，特别是在会计、GIS 和其他专业应用程序中。Aspose.Cells 允许您将这些旧版文件无缝集成到现代 C++ 电子表格工作流中。

该库支持读取和写入 DBF 文件，使您能够：

- 将现有 DBF 文件中的数据导入到 Aspose.Cells Workbook 对象中，以便进一步处理或转换为其他格式。
- 从头创建新的 DBF 文件，或者通过转换其他电子表格格式的数据来创建。
- 在数据传入和传出 DBF 格式时，保持字段定义、数据类型和记录结构。

DBF 文件也可以直接在 Microsoft Excel 和其他电子表格应用程序中打开，使它们成为旧版系统与现代电子表格工具之间的便捷桥梁。

## **支持的 DBF 版本和功能**

Aspose.Cells 支持以下 DBF 格式版本：

- **dBASE III** — DBF 格式的原始且最广泛支持的变体。
- **dBASE IV** — 扩展版本，支持更多的数据类型和更大的字段大小。

### 支持的功能

该库为以下操作提供全面的支持：

- 将 DBF 数据读取到 Workbook 对象中，并保留所有记录和字段定义。
- 将工作簿数据写回 DBF 格式，以便导出到与 dBASE 兼容的应用程序。
- 处理 DBF 文件中使用的常见数据类型，包括字符、数值、日期和逻辑字段。
- 在读写操作期间保留字段定义，如字段名称、类型和长度。

### 限制和注意事项

使用 DBF 文件时，请牢记以下限制：

- 每个文件的最大字段数为 **128**。
- 最大记录大小为 **4000 字节**。
- 字段名称限制为 **10 个字符**，必须为大写，且不能包含空格。
- DBF 文件中的日期值以 `YYYYMMDD` 格式存储。
- 字符编码可能因源应用程序而异（通常为 Windows-1252 或 OEM 代码页）。

## **读取 DBF 文件**

Aspose.Cells 使得将数据从 DBF 文件加载到 Workbook 对象中变得简单明了。该库使用 `LoadOptions` 类来指定源格式，确保在加载过程中正确解析数据。

### 使用 Aspose.Cells 读取 DBF 文件

要读取 DBF 文件，您需要创建一个 `LoadOptions` 实例，将其 `LoadFormat` 属性设置为 `LoadFormat.Dbf`，然后将其与文件路径一起传递给 `Workbook` 构造函数。加载完成后，可通过 `Worksheets` 集合访问数据，您可以在其中遍历单元格、提取值或根据需要操作数据。

以下示例演示了如何将现有 DBF 文件加载到 Aspose.Cells 中，访问其第一个工作表，并读取单元格值。

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "Data/";
    std::string filePath = dataDir + "example.dbf";

    LoadOptions loadOptions(LoadFormat::Dbf);

    Workbook workbook(U16String(filePath.c_str()), loadOptions);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Cells cells = worksheet.GetCells();

    std::string sb = "";

    int maxRow = cells.GetMaxDataRow();
    int maxCol = cells.GetMaxDataColumn();

    for (int i = 0; i <= maxRow; i++) {
        for (int j = 0; j <= maxCol; j++) {
            Cell cell = cells.Get(i, j);
            U16String value = cell.GetStringValue();
            sb += "|";
            sb += value.ToUtf8();
        }
        sb += "|";
        sb += "\n";
    }

    std::cout << sb << std::endl;

    std::string outputPath = dataDir + "output.xlsx";
    workbook.Save(U16String(outputPath.c_str()), SaveFormat::Xlsx);

    std::cout << "DBF file loaded successfully. Converted XLSX saved at: " << outputPath << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

您可以通过在"打开"对话框中选择文件，直接在 Microsoft Excel 中打开 DBF 文件。Excel 会将 DBF 文件视为电子表格，以表格布局显示其记录。这对于在使用 Aspose.Cells 读取或写入数据后快速验证数据非常有用。

{{% /alert %}}

## **写入 DBF 文件**

使用 Aspose.Cells 将数据写入 DBF 文件的模式与保存任何其他电子表格格式的模式类似。您可以创建或加载一个 Workbook，向工作表填充数据，然后调用 `Save` 方法并指定 `SaveFormat.Dbf` 作为目标格式。

### 使用 Aspose.Cells 写入 DBF 文件

要创建 DBF 文件，请按照以下步骤操作：

1. 创建一个新的 `Workbook` 实例。
2. 从 `Worksheets` 集合中访问第一个工作表。
3. 使用您的数据填充工作表，包括第一行的标题和后续行的记录。
4. 调用 `Workbook.Save` 方法，将文件路径和 `SaveFormat.Dbf` 作为参数传递。

以下示例演示了如何从头创建新的 DBF 文件。它使用包含不同数据类型（字符串、数字和日期）的示例数据填充工作表，以说明在导出到 DBF 格式时如何处理字段类型。

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    std::string outputDir = "C:/Output/";
    std::string filePath = outputDir + "output.dbf";

    if (!std::filesystem::exists(outputDir)) {
        std::filesystem::create_directories(outputDir);
    }

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // 列标题
    cells.Get(0, 0).PutValue(u"ID");
    cells.Get(0, 1).PutValue(u"Name");
    cells.Get(0, 2).PutValue(u"Department");
    cells.Get(0, 3).PutValue(u"Salary");
    cells.Get(0, 4).PutValue(u"HireDate");

    // 数据行 1
    cells.Get(1, 0).PutValue(101);
    cells.Get(1, 1).PutValue(u"John Smith");
    cells.Get(1, 2).PutValue(u"Engineering");
    cells.Get(1, 3).PutValue(75000.50);
    Date hireDate1{2020, 3, 15, 0, 0, 0, 0};
    cells.Get(1, 4).PutValue(hireDate1);

    // 数据行 2
    cells.Get(2, 0).PutValue(102);
    cells.Get(2, 1).PutValue(u"Jane Doe");
    cells.Get(2, 2).PutValue(u"Marketing");
    cells.Get(2, 3).PutValue(68000.75);
    Date hireDate2{2019, 7, 22, 0, 0, 0, 0};
    cells.Get(2, 4).PutValue(hireDate2);

    // 数据行 3
    cells.Get(3, 0).PutValue(103);
    cells.Get(3, 1).PutValue(u"Bob Johnson");
    cells.Get(3, 2).PutValue(u"Finance");
    cells.Get(3, 3).PutValue(82000.00);
    Date hireDate3{2021, 1, 10, 0, 0, 0, 0};
    cells.Get(3, 4).PutValue(hireDate3);

    // 数据行 4
    cells.Get(4, 0).PutValue(104);
    cells.Get(4, 1).PutValue(u"Alice Brown");
    cells.Get(4, 2).PutValue(u"Human Resources");
    cells.Get(4, 3).PutValue(71000.25);
    Date hireDate4{2018, 11, 5, 0, 0, 0, 0};
    cells.Get(4, 4).PutValue(hireDate4);

    // 数据行 5
    cells.Get(5, 0).PutValue(105);
    cells.Get(5, 1).PutValue(u"Charlie Wilson");
    cells.Get(5, 2).PutValue(u"Operations");
    cells.Get(5, 3).PutValue(79500.80);
    Date hireDate5{2022, 5, 30, 0, 0, 0, 0};
    cells.Get(5, 4).PutValue(hireDate5);

    // 设置列宽以提高可读性
    worksheet.GetCells().SetColumnWidth(0, 8);
    worksheet.GetCells().SetColumnWidth(1, 20);
    worksheet.GetCells().SetColumnWidth(2, 20);
    worksheet.GetCells().SetColumnWidth(3, 12);
    worksheet.GetCells().SetColumnWidth(4, 14);

    workbook.Save(U16String(filePath.c_str()), SaveFormat::Dbf);

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

将数据写入 DBF 文件时，请确保您的数据符合该格式的限制。字段名称长度不应超过 10 个字符，且不应包含空格。记录总大小超过 4000 字节的将无法正确保存。日期应为有效的日期值，且能够以 YYYYMMDD 格式表示。

{{% /alert %}}

## **数据类型和格式注意事项**

在 Aspose.Cells 和 DBF 格式之间传输数据时，了解两种系统之间的数据类型映射对于确保数据完整性非常重要。

### 单元格类型与 DBF 字段类型

保存时，Aspose.Cells 单元格值会自动转换为适当的 DBF 字段类型：

- **字符串** 映射到字符 (C) 字段。
- **数值**（整数和小数）映射到数值 (N) 字段。
- **日期值** 映射到 `YYYYMMDD` 格式的日期 (D) 字段。
- **布尔值** 映射到逻辑 (L) 字段。

### 编码

DBF 文件可能使用不同的字符编码，具体取决于创建它们的应用程序。Aspose.Cells 在大多数情况下会透明地处理编码，但如果您遇到字符显示问题，可能需要验证源文件的编码。

### 字段命名规则

DBF 字段名称必须遵守以下规则：

- 最大长度为 10 个字符。
- 必须以字母开头。
- 不能包含空格或特殊字符。
- 无论输入时使用何种大小写，存储时都将转换为大写。

### 验证输出

写入 DBF 文件后，您可以通过在 Microsoft Excel 或任何 dBASE 兼容应用程序中打开它来验证结果。数据应以表格布局显示，字段名称作为列标题，并根据您提供的数据填充记录。

## **在 DBF 和其他格式之间进行转换**

使用 Aspose.Cells 读取和写入 DBF 文件最实用的用例之一是在 DBF 格式和现代电子表格格式（如 XLSX、XLS 或 CSV）之间转换数据。由于 Aspose.Cells 支持多种格式，您可以轻松地加载 DBF 文件并将其重新保存为任何其他支持的格式，反之亦然。

例如，您可以读取一个 DBF 文件，使用 Aspose.Cells API 应用格式或计算，然后将其结果保存为 XLSX 文件，以便分发给使用现代电子表格应用程序的用户。反之，您也可以从 XLSX 或 CSV 文件中获取数据并将其导出为 DBF 格式，以便与旧版系统集成。



{{< app/cells/assistant language="cpp" >}}