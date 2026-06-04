---
title: 将 Excel 文件拆分为多个文件
description: Aspose.Cells 是一个用于处理电子表格文件的 Java 库，支持将单个 Excel 文件拆分为多个文件。本文将介绍如何通过将每个工作表复制到单独的工作簿以及将特定单元格区域复制到其他工作簿来拆分 Excel 文件。
keywords: Aspose.Cells, Java 库, 电子表格, 拆分 Excel 文件, 复制工作表, 复制区域, 多个工作簿, 另存为单独文件
type: docs
weight: 195
url: /zh/java/splitting-excel-files-into-multiple-files/
---

{{% alert color="primary" %}}

Aspose.Cells 支持将单个 Excel 文件拆分为多个文件。主要有两种方式：(1) 通过将源工作簿的每个工作表复制到一个新的工作簿，并将每个工作簿另存为单独的文件；(2) 通过将工作表中的特定单元格区域复制到新的工作簿。当您需要分发数据子集、为不同收件人生成较小的报告，或者隔离数据以便单独处理时，这两种方法都非常有用。

{{% /alert %}}

## **简介**

在许多实际场景中，开发人员需要将单个 Excel 文件拆分为多个较小的文件。例如，一个工作簿可能为每个部门包含一个工作表，而每个部门负责人只需要接收其自己的工作表。在其他情况下，您可能希望从工作表中提取特定的表格或数据块，并通过电子邮件将其作为独立文件发送，而无需公开工作簿的其余内容。大型合并工作簿也可能需要拆分为较小的部分，以便更轻松地处理、更快地加载或供其他系统进行后续处理。

Aspose.Cells 为此任务提供了两种灵活的方法。第一种方法遍历源工作簿中的每个工作表，并将其内容复制到一个全新的 `Workbook` 实例中，然后将每个实例另存为单独的文件。第二种方法专注于工作表内的特定单元格区域，并仅将该区域复制到新的工作簿中。在这两种情况下，一般流程是相同的：使用 `Workbook` 类加载源工作簿，通过 `Worksheet` 和 `Cells` 对象访问相关数据，将内容传输到目标 `Workbook`，然后将目标保存到磁盘。

## **通过将每个工作表复制到新工作簿来拆分 Excel 文件**

### **方法概述**

在这种方法中，源工作簿被打开一次，然后对于其 `Worksheets` 集合中的每个 `Worksheet`，都会创建一个新的目标 `Workbook`。然后将源工作表的内容复制到目标工作簿的第一个工作表中，并将目标工作簿另存为文件名源自源工作表名称的文件。结果是每个工作表对应一个输出文件，每个输出文件包含单个源工作表的数据。

当源工作簿中的每个工作表代表一个逻辑上独立的信息单元（例如部门、区域、月份或产品线），并且您希望独立交付或处理每个单元时，此方法是正确的选择。

### **步骤**

以下步骤描述了如何通过将每个工作表复制到新工作簿来拆分 Excel 文件：

1. 通过实例化一个 `Workbook` 对象并向其构造函数传递文件路径来打开源 Excel 文件。
2. 使用 `for` 或 `foreach` 循环遍历 `Workbook.Worksheets` 集合，以便处理源文件中的每个 `Worksheet`。
3. 在循环内部，为当前工作表创建一个新的目标 `Workbook` 实例（一个空工作簿）。
4. 向目标工作簿添加一个新的 `Worksheet`（或使用默认的第一个工作表），并为其分配一个有意义的名称，理想情况下与源工作表的 `Name` 属性相同。
5. 将源工作表的内容复制到目标工作表中。这可以通过遍历源工作表 `Cells` 集合的单元格并将其值写入目标工作表的相应单元格来完成，或者使用 `Cells.copy` 方法一次性传输整个区域。
6. 构造一个包含源工作表名称的输出文件路径（例如 `dataDir + worksheet.getName() + ".xls"`），以便每个生成的文件都具有唯一的名称。
7. 调用目标 `Workbook.save` 方法将文件写入磁盘。
8. 对下一个工作表重复步骤 3 至 7，直到所有工作表都被处理完毕。

### **代码示例**

```java
import com.aspose.cells.*;

String dataDir = "data/";
Workbook workbook = new Workbook(dataDir + "book1.xls");

for (int i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    Worksheet sourceSheet = workbook.getWorksheets().get(i);
    String sheetName = sourceSheet.getName();
    
    Workbook destWorkbook = new Workbook();
    int destIndex = destWorkbook.getWorksheets().add();
    Worksheet destSheet = destWorkbook.getWorksheets().get(destIndex);
    destSheet.setName(sheetName);
    
    destSheet.copy(sourceSheet);
    
    String destFile = dataDir + sheetName + ".xls";
    destWorkbook.save(destFile, SaveFormat.EXCEL_97_TO_2003);
}
```

预期输出是数据目录中的一组新文件，每个源工作簿中的工作表对应一个文件。每个文件以其对应的源工作表命名，文件包含该单个工作表的数据（以及可选的格式）。

## **通过将区域复制到新工作簿来拆分 Excel 文件**

### **方法概述**

有时您需要拆分的数据并不对应于整个工作表，而是工作表中的特定矩形区域，例如 `A1:D10` 或表示特定表格的命名区域。在这些情况下，复制整个工作表是浪费的，需要更精确的方法：识别源区域，仅将该区域复制到新的工作簿中，然后保存新文件。

当您希望从较大的工作表中提取单个表格、报告块或数据区域，同时丢弃所有不相关的内容时，这种方法是理想的选择。它对于将用户选择的工作表区域作为独立文件导出也非常有用。

### **步骤**

以下步骤描述了如何通过将特定区域复制到新工作簿来拆分 Excel 文件：

1. 通过使用文件路径实例化 `Workbook` 对象来打开源 Excel 文件。
2. 检索包含要复制区域的目标 `Worksheet`，可以通过索引（例如第一个工作表）或通过 `Worksheets` 集合中的名称来获取。
3. 确定要复制的区域。这可以是硬编码的单元格区域，例如 `A1:C10`，也可以是通过 `Worksheet.Cells` 集合获取的命名区域，或者通过 `Worksheet.Cells.createRange` 创建的区域。
4. 创建一个新的目标 `Workbook` 实例。
5. 访问目标工作簿的第一个 `Worksheet`（默认工作表）。
6. 将源区域复制到目标工作表中，通常从单元格 `A1` 开始。目标 `Cells` 集合上的 `Cells.copy` 方法可用于复制整个区域，或者您可以遍历源区域的单元格并使用 `putValue` 将其值写入目标单元格。可以提供可选的 `CopyOptions` 来控制传输的内容（仅值、值和样式、公式等）。
7. 使用 `Workbook.save` 方法将目标工作簿保存到磁盘上的新文件路径。

### **代码示例**

```java
import com.aspose.cells.*;

// 定义数据目录和文件路径
String dataDir = "data/";
String sourcePath = dataDir + "book1.xls";
String outputPath = dataDir + "outputrange.xls";

// 打开源 Excel 文件
Workbook sourceWorkbook = new Workbook(sourcePath);

// 获取源工作簿中的第一个工作表
Worksheet sourceWorksheet = sourceWorkbook.getWorksheets().get(0);

// 定义源单元格区域 A1:C10（10 行，3 列，从第 0 行第 0 列开始）
Range sourceRange = sourceWorksheet.getCells().createRange(0, 0, 10, 3);

// 创建新的目标工作簿
Workbook destWorkbook = new Workbook();

// 访问目标工作簿中的第一个工作表
Worksheet destWorksheet = destWorkbook.getWorksheets().get(0);

// 在 A1 位置创建与源区域尺寸相同的目标区域
Range destRange = destWorksheet.getCells().createRange(0, 0, 10, 3);

// 将源区域复制到目标区域
destRange.copy(sourceRange);

// 将目标工作簿保存为新的 .xls 文件
destWorkbook.save(outputPath, SaveFormat.EXCEL_97_TO_2003);
```

预期输出是数据目录中的一个新文件，其中仅包含从源工作簿提取的指定区域的值（以及可选的格式）。目标文件与源文件中的任何其他数据没有关系；它仅包含提取的区域，从其第一个工作表的单元格 `A1` 开始。

## **相关文章**

- [复制行和列](/zh/cells/java/copying-rows-and-columns/)
- [合并和取消合并单元格](/zh/cells/java/merging-and-unmerging-cells/)

{{< app/cells/assistant language="java" >}}