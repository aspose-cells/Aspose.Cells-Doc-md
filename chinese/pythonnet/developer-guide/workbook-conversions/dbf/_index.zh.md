---
title: 读取和写入 DBF 文件
linktitle: 读取和写入 DBF
description: Aspose.Cells 是一个通过 .NET 为 Python 提供的电子表格文件处理库，支持读取和写入 dBASE III 和 IV (DBF) 文件。本文介绍如何使用 Aspose.Cells 从 DBF 文件导入数据以及将数据导出到 DBF 文件，包括文件格式详细信息、支持的功能以及分步骤的示例。
keywords: Aspose.Cells, Python via .NET 库, DBF, dBASE, 读取 DBF, 写入 DBF, 导入 DBF, 导出 DBF, 文件格式, .dbf
type: docs
weight: 200
url: /zh/python-net/reading-and-writing-dbf-files/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 提供对读取和写入 DBF (dBASE) 文件的全面支持。您可以将现有的 dBASE III 和 dBASE IV 文件加载到 Workbook 对象中，使用丰富的 Aspose.Cells API 操作数据，然后将工作簿保存回 DBF 格式，以便与旧版数据库应用程序配合使用。

{{% /alert %}}

## **简介**

DBF (DataBase File) 是一种旧版数据库文件格式，最早由 dBASE 于 1980 年代初期推出。尽管该格式年代久远，DBF 文件仍广泛用于许多行业以存储结构化数据，尤其是在会计、GIS 和其他专业应用中。Aspose.Cells 允许您将这些旧版文件无缝集成到现代的 Python via .NET 电子表格工作流中。

该库同时支持读取和写入 DBF 文件，使您能够：

- 将现有 DBF 文件中的数据导入到 Aspose.Cells Workbook 对象中，以便进一步处理或转换为其他格式。
- 从头创建新的 DBF 文件，或通过转换其他电子表格格式的数据来生成 DBF 文件。
- 在将数据传入和传出 DBF 格式时，维护字段定义、数据类型和记录结构。

DBF 文件也可以直接在 Microsoft Excel 和其他电子表格应用程序中打开，使其成为旧版系统与现代电子表格工具之间便捷的桥梁。

## **支持的 DBF 版本和功能**

Aspose.Cells 支持以下 DBF 格式版本：

- **dBASE III** — DBF 格式最初且最广泛支持的变体。
- **dBASE IV** — 支持额外数据类型和更大字段大小的扩展版本。

### 支持的功能

该库为以下操作提供全面的支持：

- 将 DBF 数据读取到 Workbook 对象中，保留所有记录和字段定义。
- 将工作簿数据写回 DBF 格式，以便导出到与 dBASE 兼容的应用程序。
- 处理 DBF 文件中常用的数据类型，包括字符型、数值型、日期型和逻辑型字段。
- 在读取/写入操作期间保留字段定义，如字段名称、类型和长度。

### 限制和注意事项

处理 DBF 文件时，请牢记以下限制：

- 每个文件的最大字段数为 **128**。
- 最大记录大小为 **4000 字节**。
- 字段名称限制为 **10 个字符**，必须为大写，且不能包含空格。
- DBF 文件中的日期值以 `YYYYMMDD` 格式存储。
- 字符编码可能因源应用程序而异（通常为 Windows-1252 或 OEM 代码页）。

## **读取 DBF 文件**

Aspose.Cells 使从 DBF 文件加载数据到 Workbook 对象变得简单直接。该库使用 `LoadOptions` 类指定源格式，确保在加载过程中正确解析数据。

### 使用 Aspose.Cells 读取 DBF 文件

要读取 DBF 文件，您需要创建一个 `LoadOptions` 实例，将其 `load_format` 属性设置为 `LoadFormat.DBF`，然后将其与文件路径一起传递给 `Workbook` 构造函数。加载完成后，可以通过 `worksheets` 集合访问数据，在其中可以遍历单元格、提取值或根据需要操作数据。

以下示例演示如何将现有 DBF 文件加载到 Aspose.Cells 中，访问其第一个工作表，并读取单元格值。

```python
import os
import aspose.cells as ac

data_dir = "Data/"
file_path = os.path.join(data_dir, "example.dbf")

load_options = ac.LoadOptions(ac.LoadFormat.DBF)

workbook = ac.Workbook(file_path, load_options)

worksheet = workbook.worksheets[0]

cells = worksheet.cells

lines = []

max_row = cells.max_data_row
max_col = cells.max_data_column

for i in range(max_row + 1):
    line_parts = []
    for j in range(max_col + 1):
        cell = cells[i, j]
        value = cell.string_value
        line_parts.append("|" + value)
    line_parts.append("|")
    lines.append("".join(line_parts))

result = "\n".join(lines) + ("\n" if lines else "")
print(result)

output_path = os.path.join(data_dir, "output.xlsx")
workbook.save(output_path, ac.SaveFormat.XLSX)

print("DBF file loaded successfully. Converted XLSX saved at: " + output_path)
```

{{% alert color="primary" %}}

您可以通过在"打开"对话框中选择 DBF 文件来直接在 Microsoft Excel 中打开它。Excel 会将 DBF 文件视为电子表格，以表格布局显示其记录。这对于在使用 Aspose.Cells 读取或写入数据后快速验证数据非常有用。

{{% /alert %}}

## **写入 DBF 文件**

使用 Aspose.Cells 将数据写入 DBF 文件的模式与保存任何其他电子表格格式类似。您创建或加载一个 Workbook，向工作表填充数据，然后调用 `save` 方法，同时将 `SaveFormat.DBF` 指定为目标格式。

### 使用 Aspose.Cells 写入 DBF 文件

要创建 DBF 文件，请按照以下步骤操作：

1. 创建一个新的 `Workbook` 实例。
2. 从 `worksheets` 集合中访问第一个工作表。
3. 用您的数据填充工作表，包括第一行的表头和后续行的记录。
4. 调用 `Workbook.save` 方法，将文件路径和 `SaveFormat.DBF` 作为参数传入。

以下示例演示如何从头创建新的 DBF 文件。它用一个包含不同数据类型（字符串、数字和日期）的示例数据填充工作表，以说明导出到 DBF 格式时如何处理字段类型。

```python
from datetime import datetime

outputDir = r"C:\Output\\"
filePath = os.path.join(outputDir, "output.dbf")

if not os.path.exists(outputDir):
    os.makedirs(outputDir, exist_ok=True)

workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells

# 列标题
cells[0, 0].put_value("ID")
cells[0, 1].put_value("Name")
cells[0, 2].put_value("Department")
cells[0, 3].put_value("Salary")
cells[0, 4].put_value("HireDate")

# 数据行 1
cells[1, 0].put_value(101)
cells[1, 1].put_value("John Smith")
cells[1, 2].put_value("Engineering")
cells[1, 3].put_value(75000.50)
cells[1, 4].put_value(datetime(2020, 3, 15))

# 数据行 2
cells[2, 0].put_value(102)
cells[2, 1].put_value("Jane Doe")
cells[2, 2].put_value("Marketing")
cells[2, 3].put_value(68000.75)
cells[2, 4].put_value(datetime(2019, 7, 22))

# 数据行 3
cells[3, 0].put_value(103)
cells[3, 1].put_value("Bob Johnson")
cells[3, 2].put_value("Finance")
cells[3, 3].put_value(82000.00)
cells[3, 4].put_value(datetime(2021, 1, 10))

# 数据行 4
cells[4, 0].put_value(104)
cells[4, 1].put_value("Alice Brown")
cells[4, 2].put_value("Human Resources")
cells[4, 3].put_value(71000.25)
cells[4, 4].put_value(datetime(2018, 11, 5))

# 数据行 5
cells[5, 0].put_value(105)
cells[5, 1].put_value("Charlie Wilson")
cells[5, 2].put_value("Operations")
cells[5, 3].put_value(79500.80)
cells[5, 4].put_value(datetime(2022, 5, 30))

# 设置列宽以提高可读性
worksheet.cells.set_column_width(0, 8)
worksheet.cells.set_column_width(1, 20)
worksheet.cells.set_column_width(2, 20)
worksheet.cells.set_column_width(3, 12)
worksheet.cells.set_column_width(4, 14)

workbook.save(filePath, ac.SaveFormat.Dbf)
```

{{% alert color="primary" %}}

将数据写入 DBF 文件时，请确保您的数据符合该格式的限制。字段名称长度不应超过 10 个字符，且不应包含空格。记录总大小超过 4000 字节的将无法正确保存。日期应为可以以 YYYYMMDD 格式表示的有效日期值。

{{% /alert %}}

## **数据类型和格式注意事项**

在 Aspose.Cells 和 DBF 格式之间传输数据时，了解两个系统之间的数据类型映射方式对于确保数据完整性非常重要。

### 单元格类型到 DBF 字段类型

Aspose.Cells 单元格值在保存时会自动转换为相应的 DBF 字段类型：

- **字符串** 映射到字符型 (C) 字段。
- **数值** （整数和小数）映射到数值型 (N) 字段。
- **日期值** 映射到日期型 (D) 字段，格式为 `YYYYMMDD`。
- **布尔值** 映射到逻辑型 (L) 字段。

### 编码

DBF 文件可能使用不同的字符编码，具体取决于创建它们的应用程序。Aspose.Cells 在大多数情况下透明地处理编码，但如果您遇到字符显示问题，可能需要验证源文件的编码。

### 字段命名规则

DBF 字段名称必须遵守以下规则：

- 最大长度为 10 个字符。
- 必须以字母开头。
- 不能包含空格或特殊字符。
- 无论输入使用的大小写如何，均以大写形式存储。

### 验证输出

写入 DBF 文件后，您可以通过在 Microsoft Excel 或任何与 dBASE 兼容的应用程序中打开它来验证结果。数据应以表格布局显示，字段名称作为列标题，并根据您提供的数据填充相应的记录。

## **DBF 与其他格式之间的转换**

使用 Aspose.Cells 读取和写入 DBF 文件最实用的用例之一是在 DBF 格式和现代电子表格格式（如 XLSX、XLS 或 CSV）之间转换数据。由于 Aspose.Cells 支持多种格式，您可以轻松地加载 DBF 文件并将其重新保存为任何其他支持的格式，反之亦然。

例如，您可以读取一个 DBF 文件，使用 Aspose.Cells API 应用格式或计算，然后将结果保存为 XLSX 文件，以便分发给使用现代电子表格应用程序的用户。反之，您也可以从 XLSX 或 CSV 文件中提取数据，并将其导出为 DBF 格式，以便与旧版系统集成。

{{< app/cells/assistant language="python" >}}