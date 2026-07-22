---
title: 将 Excel 文件拆分为多个文件
linktitle: 将 Excel
description: Aspose.Cells 是一个用于处理电子表格文件的 .NET 库，支持将单个 Excel 文件拆分为多个文件。本文将介绍如何通过将每个工作表复制到单独的工作簿以及将特定的单元格区域复制到其他工作簿来拆分 Excel 文件。
keywords: Aspose.Cells, .NET library, spreadsheet, 拆分 Excel 文件, 复制工作表, 复制区域, 多个工作簿, 另存为单独文件
type: docs
weight: 195
url: /zh/net/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells 支持将单个 Excel 文件拆分为多个文件。主要有两种方法可以做到这一点：（1）通过将源工作簿的每个工作表复制到新的工作簿中并将其另存为单独的文件；（2）将特定的单元格区域从工作表复制到新的工作簿。当您需要分发数据的子集、为不同的收件人创建较小的报告，或隔离数据以进行单独处理时，这两种方法都非常有用。

{{% /alert %}}

## **简介**

在许多实际场景中，开发人员需要将单个 Excel 文件拆分为多个较小的文件。例如，一个工作簿可能每个部门包含一个工作表，每个部门主管只需要接收他们自己的工作表。在其他情况下，您可能希望从工作表中提取特定的表格或数据块，并将其作为独立文件通过电子邮件发送，而不暴露工作簿的其余部分。大型合并的工作簿也可能需要拆分为较小的部分，以便于处理、更快地加载，或供其他系统进行下游处理。

Aspose.Cells 为此任务提供了两种灵活的方法。第一种方法遍历源工作簿中的每个工作表，并将其内容复制到一个全新的 `Workbook` 实例中，然后将每个实例另存为单独的文件。第二种方法专注于工作表中的特定单元格区域，仅将该区域复制到新的工作簿中。在这两种情况下，一般流程是相同的：使用 `Workbook` 类加载源工作簿，通过 `Worksheet` 和 `Cells` 对象访问相关数据，将内容传输到目标 `Workbook`，然后将目标保存到磁盘。

## **通过将每个工作表复制到新工作簿来拆分 Excel 文件**

### **方法概述**

在此方法中，源工作簿被打开一次，然后对于其 `Worksheets` 集合中的每个 `Worksheet`，创建一个新的目标 `Workbook`。然后将源工作表的内容复制到目标工作簿的第一个工作表中，并将目标工作簿保存为文件名源自源工作表名称的文件。结果是每个工作表对应一个输出文件，每个输出文件包含单个源工作表的数据。

当源工作簿中的每个工作表代表一个逻辑上独立的信息单元（例如部门、地区、月份或产品线），并且您希望单独交付或处理每个单元时，此方法是正确的选择。

### **步骤**

以下步骤描述了如何通过将每个工作表复制到新工作簿来拆分 Excel 文件：

1. 通过实例化 `Workbook` 对象并将其文件路径传递给其构造函数来打开源 Excel 文件。
2. 使用 `for` 或 `foreach` 循环遍历 `Workbook.Worksheets` 集合，以便处理源文件中的每个 `Worksheet`。
3. 在循环内部，为当前工作表创建一个新的目标 `Workbook` 实例（一个空工作簿）。
4. 向目标工作簿添加一个新的 `Worksheet`（或使用默认的第一个工作表），并为其分配一个有意义的名称，理想情况下与源工作表的 `Name` 属性相同。
5. 将源工作表的内容复制到目标工作表中。这可以通过遍历源工作表 `Cells` 集合的单元格并将其值写入目标工作表的相应单元格来完成，或者使用 `Cells.Copy` 方法一次性传输整个区域。
6. 构造一个包含源工作表名称的输出文件路径（例如 `dataDir + worksheet.Name + ".xls"`），以便每个生成的文件都有唯一的名称。
7. 调用目标 `Workbook.Save` 方法将文件写入磁盘。
8. 对下一个工作表重复步骤 3 到 7，直到处理完所有工作表。

### **代码示例**

```csharp
using System;
using System.IO;
using Aspose.Cells;

string dataDir = "data/";
Workbook workbook = new Workbook(dataDir + "book1.xls");

for (int i = 0; i < workbook.Worksheets.Count; i++)
{
    Worksheet sourceSheet = workbook.Worksheets[i];
    string sheetName = sourceSheet.Name;
    
    Workbook destWorkbook = new Workbook();
    int destIndex = destWorkbook.Worksheets.Add();
    Worksheet destSheet = destWorkbook.Worksheets[destIndex];
    destSheet.Name = sheetName;
    
    destSheet.Copy(sourceSheet);
    
    string destFile = dataDir + sheetName + ".xls";
    destWorkbook.Save(destFile, SaveFormat.Excel97To2003);
}
```

预期输出是数据目录中的一组新文件，每个源工作表对应一个文件。每个文件以其对应的源工作表命名，文件包含该单个工作表的数据（以及可选的格式）。

## **通过将区域复制到新工作簿来拆分 Excel 文件**

### **方法概述**

有时您需要拆分的数据并不对应于整个工作表，而是工作表中的特定矩形区域，例如 `A1:D10` 或表示特定表格的命名区域。在这些情况下，复制整个工作表是浪费的，需要更精确的方法：识别源区域，仅将该区域复制到新的工作簿中，然后保存新文件。

当您希望从较大的工作表中提取单个表格、报告块或数据区域，同时丢弃所有不相关的内容时，此方法是理想的选择。它对于将用户选择的区域作为独立文件导出也很有用。

### **步骤**

以下步骤描述了如何通过将特定区域复制到新工作簿来拆分 Excel 文件：

1. 通过使用文件路径实例化 `Workbook` 对象来打开源 Excel 文件。
2. 检索包含要复制区域的目标 `Worksheet`，可以通过索引（例如第一个工作表）或通过 `Worksheets` 集合中的名称来获取。
3. 确定要复制的区域。这可以是硬编码的单元格区域，例如 `A1:C10`，也可以是通过 `Worksheet.Cells` 集合获得的命名区域，或者通过 `Worksheet.Cells.CreateRange` 创建的区域。
4. 创建一个新的目标 `Workbook` 实例。
5. 访问目标工作簿的第一个 `Worksheet`（默认工作表）。
6. 将源区域复制到目标工作表中，通常从单元格 `A1` 开始。可以使用目标 `Cells` 集合上的 `Cells.Copy` 方法复制整个区域，或者遍历源区域的单元格并使用 `PutValue` 将其值写入目标单元格。可以提供可选的 `CopyOptions` 来控制传输的内容（仅值、值和样式、公式等）。
7. 使用 `Workbook.Save` 方法将目标工作簿保存到磁盘上的新文件路径。

### **代码示例**

```csharp
using System;
using System.IO;
using Aspose.Cells;

// 定义数据目录和文件路径
string dataDir = "data/";
string sourcePath = dataDir + "book1.xls";
string outputPath = dataDir + "outputrange.xls";

// 打开源 Excel 文件
Workbook sourceWorkbook = new Workbook(sourcePath);

// 从源工作簿中获取第一个工作表
Worksheet sourceWorksheet = sourceWorkbook.Worksheets[0];

// 定义源单元格区域 A1:C10（从第 0 行、第 0 列开始的 10 行 3 列）
var sourceRange = sourceWorksheet.Cells.CreateRange(0, 0, 10, 3);

// 创建一个新的目标工作簿
Workbook destWorkbook = new Workbook();

// 访问目标工作簿中的第一个工作表
Worksheet destWorksheet = destWorkbook.Worksheets[0];

// 在 A1 处创建与源区域尺寸相同的目标区域
var destRange = destWorksheet.Cells.CreateRange(0, 0, 10, 3);

// 将源区域复制到目标区域
destRange.Copy(sourceRange);

// 将目标工作簿保存为新的 .xls 文件
destWorkbook.Save(outputPath, SaveFormat.Excel97To2003);
```

预期输出是数据目录中的单个新文件，其中仅包含从源工作簿中提取的指定区域的值（以及可选的格式）。目标文件与源文件中的任何其他数据没有关系；它仅包含提取的区域，从其第一个工作表的单元格 `A1` 开始。

## **相关文章**

- [复制行和列](/cells/zh/net/copying-rows-and-columns/)
- [合并和取消合并单元格](/cells/zh/net/merging-and-unmerging-cells/)

{{< app/cells/assistant language="csharp" >}}