---
title: 读取和写入 DBF 文件
linktitle: 读取和写入 DBF 文件
description: Aspose.Cells 是一个用于处理电子表格文件的 Python via Java 库，支持读取和写入 dBASE III 和 IV (DBF) 文件。本文介绍如何使用 Aspose.Cells 从 DBF 文件导入数据和将数据导出到 DBF 文件，包括文件格式详细信息、支持的功能以及分步示例。
keywords: Aspose.Cells, Python via Java 库, DBF, dBASE, 读取 DBF, 写入 DBF, 导入 DBF, 导出 DBF, 文件格式, .dbf
type: docs
weight: 200
url: /zh/python-java/reading-and-writing-dbf-files/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 完全支持读取和写入 DBF (dBASE) 文件。您可以将现有的 dBASE III 和 dBASE IV 文件加载到 Workbook 对象中，使用强大的 Aspose.Cells API 处理数据，然后将工作簿保存回 DBF 格式，以便与旧版数据库应用程序配合使用。
{{% /alert %}}

## **简介**
DBF (DataBase File) 是一种旧版数据库文件格式，最初由 dBASE 在 1980 年代初期推出。尽管该格式年代久远，但 DBF 文件仍在许多行业广泛用于存储结构化数据，尤其是在会计、GIS 和其他专业应用中。Aspose.Cells 允许您将这些旧版文件无缝集成到现代 Python via Java 电子表格工作流中。
该库同时支持读取和写入 DBF 文件，使您能够：
- 将现有 DBF 文件中的数据导入到 Aspose.Cells Workbook 对象中，以便进一步处理或转换为其他格式。
- 从头创建新的 DBF 文件，或通过转换其他电子表格格式的数据来生成 DBF 文件。
- 在 DBF 格式的数据导入和导出过程中保持字段定义、数据类型和记录结构。
DBF 文件也可以直接在 Microsoft Excel 和其他电子表格应用程序中打开，使其成为旧版系统与现代电子表格工具之间的便捷桥梁。

## **支持的 DBF 版本和功能**
Aspose.Cells 支持以下 DBF 格式版本：
- **dBASE III** — DBF 格式的原始且应用最广泛的变体。
- **dBASE IV** — 扩展版本，支持更多的数据类型和更大的字段大小。

### 支持的功能
该库对以下操作提供全面支持：
- 将 DBF 数据读取到 Workbook 对象中，同时保留所有记录和字段定义。
- 将工作簿数据写回 DBF 格式，以便导出到与 dBASE 兼容的应用程序。
- 处理 DBF 文件中常用的数据类型，包括字符型、数值型、日期型和逻辑型字段。
- 在读写操作过程中保留字段定义，例如字段名称、类型和长度。

### 限制和注意事项
处理 DBF 文件时，请牢记以下约束：
- 每个文件的最大字段数为 **128**。
- 最大记录大小为 **4000 字节**。
- 字段名称限制为 **10 个字符**，必须为大写且不能包含空格。
- DBF 文件中的日期值以 `YYYYMMDD` 格式存储。
- 字符编码可能因源应用程序而异（通常为 Windows-1252 或 OEM 代码页）。

## **读取 DBF 文件**
Aspose.Cells 使得将数据从 DBF 文件加载到 Workbook 对象变得非常直接。该库使用 `LoadOptions` 类来指定源格式，从而确保在加载过程中正确解析数据。

### 使用 Aspose.Cells 读取 DBF 文件
要读取 DBF 文件，您需要创建一个 `LoadOptions` 实例，将其 `LoadFormat` 属性设置为 `LoadFormat.DBF`，并将其与文件路径一起传递给 `Workbook` 构造函数。加载完成后，就可以通过 `Worksheets` 集合访问数据，您可以遍历单元格、提取值或根据需要处理数据。
以下示例演示了如何将现有的 DBF 文件加载到 Aspose.Cells 中，访问其第一个工作表，并读取单元格的值。

```python
import jpype
import os
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, LoadOptions, LoadFormat, SaveFormat
dataDir = "Data/"
filePath = os.path.join(dataDir, "example.dbf")
loadOptions = LoadOptions(LoadFormat.DBF)
workbook = Workbook(filePath, loadOptions)
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
sb = []
maxRow = cells.getMaxDataRow()
maxCol = cells.getMaxDataColumn()
for i in range(maxRow + 1):
    for j in range(maxCol + 1):
        cell = cells.get(i, j)
        value = cell.getStringValue()
        sb.append("|" + value)
    sb.append("|" + "\n")
print("".join(sb))
outputPath = os.path.join(dataDir, "output.xlsx")
workbook.save(outputPath, SaveFormat.XLSX)
print("DBF file loaded successfully. Converted XLSX saved at: " + outputPath)
jpype.shutdownJVM()
```

{{% alert color="primary" %}}
您可以直接在 Microsoft Excel 中打开 DBF 文件，方法是在"打开"对话框中选择该文件。Excel 会将 DBF 文件视为电子表格，以表格布局显示其记录。这对于在使用 Aspose.Cells 读取或写入数据后快速验证数据非常有用。
{{% /alert %}}

## **写入 DBF 文件**
将数据写入 DBF 文件的流程与使用 Aspose.Cells 保存任何其他电子表格格式类似。您可以创建或加载一个 Workbook，用数据填充工作表，然后调用 `Save` 方法并将 `SaveFormat.DBF` 指定为目标格式。

### 使用 Aspose.Cells 写入 DBF 文件
要创建 DBF 文件，请按照以下步骤操作：
1. 创建一个新的 `Workbook` 实例。
2. 通过 `Worksheets` 集合访问第一个工作表。
3. 用您的数据填充工作表，第一行为标题行，后续行为记录行。
4. 调用 `Workbook.save` 方法，将文件路径和 `SaveFormat.DBF` 作为参数传递。
以下示例演示了如何从头开始创建一个新的 DBF 文件。它向工作表填充包含不同数据类型（字符串、数字和日期）的示例数据，以说明导出到 DBF 格式时如何处理字段类型。

```python
import jpype
import os
import jpype.imports
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, SaveFormat
import java.time as _jt
import java.util as _ju
outputDir = "C:\\Output\\"
filePath = os.path.join(outputDir, "output.dbf")
if not os.path.exists(outputDir):
    os.makedirs(outputDir, exist_ok=True)
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
# 列标题
cells.get(0, 0).putValue("ID")
cells.get(0, 1).putValue("Name")
cells.get(0, 2).putValue("Department")
cells.get(0, 3).putValue("Salary")
cells.get(0, 4).putValue("HireDate")
# 数据行 1
cells.get(1, 0).putValue(101)
cells.get(1, 1).putValue("John Smith")
cells.get(1, 2).putValue("Engineering")
cells.get(1, 3).putValue(75000.50)
cells.get(1, 4).putValue(_jt.LocalDate.of(2020, 3, 15))
# 数据行 2
cells.get(2, 0).putValue(102)
cells.get(2, 1).putValue("Jane Doe")
cells.get(2, 2).putValue("Marketing")
cells.get(2, 3).putValue(68000.75)
cells.get(2, 4).putValue(_jt.LocalDate.of(2019, 7, 22))
# 数据行 3
cells.get(3, 0).putValue(103)
cells.get(3, 1).putValue("Bob Johnson")
cells.get(3, 2).putValue("Finance")
cells.get(3, 3).putValue(82000.00)
cells.get(3, 4).putValue(_jt.LocalDate.of(2021, 1, 10))
# 数据行 4
cells.get(4, 0).putValue(104)
cells.get(4, 1).putValue("Alice Brown")
cells.get(4, 2).putValue("Human Resources")
cells.get(4, 3).putValue(71000.25)
cells.get(4, 4).putValue(_jt.LocalDate.of(2018, 11, 5))
# 数据行 5
cells.get(5, 0).putValue(105)
cells.get(5, 1).putValue("Charlie Wilson")
cells.get(5, 2).putValue("Operations")
cells.get(5, 3).putValue(79500.80)
cells.get(5, 4).putValue(_jt.LocalDate.of(2022, 5, 30))
# 设置列宽以提高可读性
worksheet.getCells().setColumnWidth(0, 8)
worksheet.getCells().setColumnWidth(1, 20)
worksheet.getCells().setColumnWidth(2, 20)
worksheet.getCells().setColumnWidth(3, 12)
worksheet.getCells().setColumnWidth(4, 14)
workbook.save(filePath, SaveFormat.DBF)
jpype.shutdownJVM()
```

{{% alert color="primary" %}}
将数据写入 DBF 文件时，请确保您的数据符合该格式的限制。字段名称不应超过 10 个字符，并且不应包含空格。超过 4000 字节的记录将无法正确保存。日期应为可表示为 YYYYMMDD 格式的有效日期值。
{{% /alert %}}

## **数据类型和格式注意事项**
在 Aspose.Cells 和 DBF 格式之间传输数据时，了解两个系统的数据类型映射方式对于确保数据完整性非常重要。

### 单元格类型到 DBF 字段类型的映射
保存时，Aspose.Cells 单元格值会自动转换为相应的 DBF 字段类型：
- **字符串** 映射到字符 (C) 字段。
- **数值**（整数和小数）映射到数值 (N) 字段。
- **日期值** 映射为 `YYYYMMDD` 格式的日期 (D) 字段。
- **布尔值** 映射到逻辑 (L) 字段。

### 编码
DBF 文件可能使用不同的字符编码，具体取决于创建它们的应用程序。在大多数情况下，Aspose.Cells 会以透明的方式处理编码问题，但如果遇到字符显示问题，则可能需要验证源文件的编码。

### 字段名称规则
DBF 字段名称必须遵守以下规则：
- 最大长度为 10 个字符。
- 必须以字母开头。
- 不能包含空格或特殊字符。
- 无论输入时使用的大小写如何，存储时均转为大写。

### 验证输出
写入 DBF 文件后，您可以通过在 Microsoft Excel 或任何与 dBASE 兼容的应用程序中打开它来验证结果。数据应以表格布局显示，字段名称作为列标题，记录根据您提供的数据填充。

## **DBF 与其他格式之间的转换**
使用 Aspose.Cells 读取和写入 DBF 文件最实用的应用之一是在 DBF 格式和现代电子表格格式（如 XLSX、XLS 或 CSV）之间转换数据。由于 Aspose.Cells 支持多种格式，您可以轻松加载 DBF 文件并将其重新保存为任何其他支持的格式，反之亦然。

{{< app/cells/assistant language="python" >}}