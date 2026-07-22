---
title: 将 Excel 文件拆分为多个文件
linktitle: 将 Excel
description: Aspose.Cells 是一个 Python via Java 库，用于处理电子表格文件，支持将单个 Excel 文件拆分为多个文件。本文将介绍如何通过将每个工作表复制到单独的工作簿以及将特定单元格区域复制到其他工作簿来拆分 Excel 文件。
keywords: Aspose.Cells, Python via Java 库, 电子表格, 拆分 Excel 文件, 复制工作表, 复制区域, 多个工作簿, 另存为单独文件
type: docs
weight: 195
url: /zh/python-java/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 支持将单个 Excel 文件拆分为多个文件。实现此操作主要有两种方式：(1) 将源工作簿的每个工作表复制到新的工作簿，并将每个工作簿另存为单独的文件；(2) 将工作表中特定的单元格区域复制到新的工作簿。当您需要分发数据子集、为不同接收方创建较小的报告，或将数据隔离以进行单独处理时，这两种方法都非常有用。

{{% /alert %}}

## **简介**

在许多实际场景中，开发人员需要将单个 Excel 文件拆分为几个较小的文件。例如，一个工作簿可能为每个部门包含一个工作表，而每个部门负责人只需要接收自己部门的工作表。在其他情况下，您可能希望从工作表中提取特定的表格或数据块，并通过电子邮件将其作为独立文件发送，而无需公开工作簿的其他内容。大型合并工作簿也可能需要拆分为较小的部分，以便于处理、加快加载速度，或供其他系统进行下游处理。

Aspose.Cells 为此任务提供了两种灵活的方法。第一种方法遍历源工作簿中的每个工作表，并将其内容复制到一个全新的 `Workbook` 实例中，然后将每个实例另存为单独的文件。第二种方法专注于工作表中特定的单元格区域，仅将该区域复制到新的工作簿中。在这两种情况下，总体流程是相同的：使用 `Workbook` 类加载源工作簿，通过 `Worksheet` 和 `Cells` 对象访问相关数据，将内容传输到目标 `Workbook`，然后将目标文件保存到磁盘。

## **通过将每个工作表复制到新工作簿来拆分 Excel 文件**

### **方法概述**

在这种方法中，源工作簿只被打开一次，然后针对其 `Worksheets` 集合中的每个 `Worksheet`，都会创建一个新的目标 `Workbook`。源工作表的内容随后被复制到目标工作簿的第一个工作表中，并将目标工作簿保存为文件名源自源工作表名称的文件。结果是每个工作表对应一个输出文件，每个输出文件包含单个源工作表的数据。

当源工作簿中的每个工作表代表一个逻辑上独立的信息单元（例如部门、地区、月份或产品线），并且您希望单独交付或处理每个单元时，此方法是正确的选择。

### **步骤**

以下步骤描述了如何通过将每个工作表复制到新工作簿来拆分 Excel 文件：

1. 通过实例化 `Workbook` 对象并将文件路径传递给其构造函数来打开源 Excel 文件。
2. 使用 `for` 或 `foreach` 循环遍历 `Workbook.Worksheets` 集合，以便处理源文件中的每个 `Worksheet`。
3. 在循环内部，为当前工作表创建一个新的目标 `Workbook` 实例（一个空工作簿）。
4. 向目标工作簿添加一个新的 `Worksheet`（或使用默认的第一个工作表），并为其分配一个有意义的名称，理想情况下与源工作表的 `Name` 属性相同。
5. 将源工作表的内容复制到目标工作表中。这可以通过遍历源工作表 `Cells` 集合的单元格并将其值写入目标工作表的相应单元格来完成，或者使用 `Cells.copy` 方法一次传输整个区域。
6. 构造一个包含源工作表名称的输出文件路径（例如 `dataDir + worksheet.Name + ".xls"`），以便每个生成的文件具有唯一的名称。
7. 调用目标的 `Workbook.save` 方法将文件写入磁盘。
8. 对下一个工作表重复步骤 3 至 7，直到处理完所有工作表。

### **代码示例**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat

dataDir = "data/"
workbook = Workbook(dataDir + "book1.xls")

for i in range(workbook.getWorksheets().getCount()):
    sourceSheet = workbook.getWorksheets().get(i)
    sheetName = sourceSheet.getName()
    
    destWorkbook = Workbook()
    destIndex = destWorkbook.getWorksheets().add()
    destSheet = destWorkbook.getWorksheets().get(destIndex)
    destSheet.setName(sheetName)
    
    destSheet.copy(sourceSheet)
    
    destFile = dataDir + sheetName + ".xls"
    destWorkbook.save(destFile, SaveFormat.Excel97To2003)

jpype.shutdownJVM()
```

预期输出是数据目录中的一组新文件，每个工作表对应一个文件。每个文件以其对应的源工作表命名，并且该文件包含该单个工作表的数据（以及可选的格式）。

## **通过将区域复制到新工作簿来拆分 Excel 文件**

### **方法概述**

有时您需要拆分的数据并不对应于整个工作表，而是对应于工作表中的特定矩形区域，例如 `A1:D10` 或表示特定表格的命名区域。在这些情况下，复制整个工作表会造成浪费，需要采用更精确的方法：确定源区域，仅将该区域复制到新的工作簿中，然后保存新文件。

当您希望从较大的工作表中提取单个表格、报告块或数据区域，同时丢弃所有不相关的内容时，此方法是理想的选择。它还可用于将用户选择的区域作为独立文件导出。

### **步骤**

以下步骤描述了如何通过将特定区域复制到新工作簿来拆分 Excel 文件：

1. 通过使用文件路径实例化 `Workbook` 对象来打开源 Excel 文件。
2. 通过索引（例如第一个工作表）或从 `Worksheets` 集合按名称检索包含要复制区域的目标 `Worksheet`。
3. 确定要复制的区域。这可以是硬编码的单元格区域（例如 `A1:C10`），也可以是通过 `Worksheet.Cells` 集合获取的命名区域，或者是通过 `Worksheet.Cells.createRange` 创建的区域。
4. 创建一个新的目标 `Workbook` 实例。
5. 访问目标工作簿的第一个 `Worksheet`（默认工作表）。
6. 将源区域复制到目标工作表中，通常从单元格 `A1` 开始。可以使用目标 `Cells` 集合上的 `Cells.copy` 方法复制整个区域，或者遍历源区域的单元格并使用 `putValue` 将其值写入目标单元格。可以提供可选的 `CopyOptions` 来控制传输的内容（仅值、值和样式、公式等）。
7. 使用 `Workbook.save` 方法将目标工作簿保存到磁盘上的新文件路径。

### **代码示例**

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat

# 定义数据目录和文件路径
dataDir = "data/"
sourcePath = dataDir + "book1.xls"
outputPath = dataDir + "outputrange.xls"

# 打开源 Excel 文件
sourceWorkbook = Workbook(sourcePath)

# 从源工作簿中获取第一个工作表
sourceWorksheet = sourceWorkbook.getWorksheets().get(0)

# 定义源单元格范围 A1:C10 (从第 0 行第 0 列开始的 10 行 3 列)
sourceRange = sourceWorksheet.getCells().createRange(0, 0, 10, 3)

# 创建一个新的目标工作簿
destWorkbook = Workbook()

# 访问目标工作簿中的第一个工作表
destWorksheet = destWorkbook.getWorksheets().get(0)

# 在 A1 处创建与源范围尺寸相同的目标范围
destRange = destWorksheet.getCells().createRange(0, 0, 10, 3)

# 将源范围复制到目标范围
destRange.copy(sourceRange)

# 将目标工作簿保存为新的 .xls 文件
destWorkbook.save(outputPath, SaveFormat.Excel97To2003)

jpype.shutdownJVM()
```

预期输出是数据目录中的单个新文件，其中仅包含从源工作簿中提取的指定区域的值（以及可选的格式）。目标文件与源文件中的任何其他数据无关；它仅包含提取的区域，从其第一个工作表的单元格 `A1` 开始。

{{< app/cells/assistant language="python" >}}