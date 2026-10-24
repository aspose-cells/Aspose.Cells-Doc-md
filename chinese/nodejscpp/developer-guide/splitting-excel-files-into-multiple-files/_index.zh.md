---
title: 将 Excel 文件拆分为多个文件
linktitle: 将 Excel 文件拆分为多个文件
description: Aspose.Cells 是一个用于处理电子表格文件的 Node.js 库，支持将单个 Excel 文件拆分为多个文件。本文将介绍如何将每个工作表分别复制到单独的工作簿，以及将特定单元格区域复制到其他工作簿，从而拆分 Excel 文件。
keywords: Aspose.Cells, Node.js 库, 电子表格, 拆分 Excel 文件, 复制工作表, 复制区域, 多个工作簿, 另存为独立文件
type: docs
weight: 195
url: /zh/nodejs-cpp/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells 支持将单个 Excel 文件拆分为多个文件。主要有两种方式：(1) 将源工作簿中的每个工作表复制到新工作簿中，并将每个新工作簿另存为单独的文件；(2) 将工作表中的特定单元格区域复制到新工作簿中。当您需要分发数据子集、为不同接收者创建较小的报表，或隔离数据以便单独处理时，这两种方式都很有用。
{{% /alert %}}

## **简介**
在实际场景中，开发者经常需要将单个 Excel 文件拆分为多个较小的文件。例如，一个工作簿可能包含各部门对应的工作表，而每位部门负责人只需要收到本部门的工作表。在其他情况下，您可能希望从工作表中提取特定表格或数据块，并通过电子邮件将其作为独立文件发送，而不暴露工作簿中的其他内容。对于大型合并后的工作簿，也可能需要将其拆分为较小的部分，以便于处理、加快加载速度或供其他系统进行下游处理。
Aspose.Cells 为此任务提供了两种灵活的方式。第一种方式遍历源工作簿中的每个工作表，将其内容复制到全新的 `Workbook` 实例中，并将每个新工作簿分别另存为单独的文件。第二种方式则针对工作表中的特定单元格区域，仅将该区域复制到新工作簿中。在这两种情况下，总体流程相同：使用 `Workbook` 类加载源工作簿，通过 `Worksheet` 和 `Cells` 对象访问相关数据，将内容复制到目标 `Workbook`，然后将目标工作簿保存到磁盘。

## **通过将每个工作表复制到新工作簿来拆分 Excel 文件**

### **方法概述**
在此方法中，只打开一次源工作簿，然后为其 `Worksheets` 集合中的每个 `Worksheet` 创建一个新的目标 `Workbook`。随后，将源工作表的内容复制到目标工作簿的第一个工作表中，并根据源工作表名称生成文件名，将目标工作簿另存为文件。最终，每个工作表对应一个输出文件，每个输出文件仅包含一个源工作表的数据。
当源工作簿中的每个工作表都代表一个逻辑上独立的信息单元（例如部门、地区、月份或产品线），并且您希望单独交付或处理每个单元时，应选择此方法。

### **步骤**
以下步骤说明如何通过将每个工作表复制到新工作簿来拆分 Excel 文件：
1. 实例化一个 `Workbook` 对象并将文件路径传递给其构造函数，以打开源 Excel 文件。
2. 使用 `for` 或 `forEach` 循环遍历 `Workbook.Worksheets` 集合，以处理源文件中的每个 `Worksheet`。
3. 在循环内，为当前工作表创建一个新的目标 `Workbook` 实例（空工作簿）。
4. 将源工作表的内容复制到目标工作表。可以遍历源工作表的 `Cells` 集合中的单元格，并将其值写入目标工作表中的对应单元格；也可以使用 `Cells.copy` 方法一次性复制整个区域。
5. 构建包含源工作表名称的输出文件路径（例如 `dataDir + worksheet.Name + ".xls"`），使每个生成的文件都具有唯一名称。
6. 调用目标 `Workbook.save` 方法将文件写入磁盘。
7. 对下一个工作表重复步骤 3 至 6，直到处理完所有工作表。

### **代码示例**

```javascript
const AsposeCells = require("aspose.cells.node");
const dataDir = "data/";
const workbook = new AsposeCells.Workbook(dataDir + "book1.xls");
for (let i = 0; i < workbook.getWorksheets().getCount(); i++) {
    const sourceSheet = workbook.getWorksheets().get(i);
    const sheetName = sourceSheet.getName();

    const destWorkbook = new AsposeCells.Workbook();
    const destIndex = destWorkbook.getWorksheets().add();
    const destSheet = destWorkbook.getWorksheets().get(destIndex);
    destSheet.setName(sheetName);

    destSheet.copy(sourceSheet);

    const destFile = dataDir + sheetName + ".xls";
    destWorkbook.save(destFile, AsposeCells.SaveFormat.Excel97To2003);
}
```

预期输出是数据目录中的一组新文件，每个工作表对应一个文件。每个文件均以对应的源工作表命名，并包含该源工作表的数据（以及可选的格式）。

## **通过将区域复制到新工作簿来拆分 Excel 文件**

### **方法概述**
有时，需要拆分的数据并不对应整个工作表，而是对应工作表中的特定矩形区域，例如 `A1:D10`，也可能是一个表示特定表格的命名区域。在这种情况下，复制整个工作表会造成不必要的开销，因此需要采用更精确的方法：确定源区域，仅将该区域复制到新工作簿中，然后保存新文件。
当您希望从较大的工作表中提取单个表格、报表块或数据区域，并舍弃所有无关内容时，此方法非常适合。它还适用于将用户选定的工作表区域导出为独立文件。

### **步骤**
以下步骤说明如何通过将特定区域复制到新工作簿来拆分 Excel 文件：
1. 实例化一个 `Workbook` 对象并传入文件路径，以打开源 Excel 文件。
2. 按索引（例如第一个工作表）或名称从 `Worksheets` 集合中获取包含目标区域的工作表。
3. 确定要复制的区域。它可以是硬编码的单元格区域（如 `A1:C10`），也可以是通过 `Worksheet.Cells` 集合获取的命名区域，或通过 `Worksheet.Cells.createRange` 创建的区域。
4. 创建一个新的目标 `Workbook` 实例。
5. 访问目标工作簿的第一个 `Worksheet`（默认工作表）。
6. 将源区域复制到目标工作表，通常从单元格 `A1` 开始。可以使用目标 `Cells` 集合上的 `Cells.copy` 方法复制整个区域，也可以遍历源区域中的单元格，并使用 `putValue` 将其值写入目标单元格。可选的 `CopyOptions` 可用于控制复制内容（仅复制值、值和样式、公式等）。
7. 使用 `Workbook.save` 方法将目标工作簿保存到磁盘上的新文件路径。

### **代码示例**
预期输出是数据目录中的一个新文件，其中仅包含从源工作簿提取的指定区域的值（以及可选的格式）。目标文件与源文件中的任何其他数据均无关系；它仅包含提取的区域，且该区域从目标文件第一个工作表的单元格 `A1` 开始。

## 相关文章
- [在 Aspose.Cells for Node.js via C++ 中向数据透视表添加筛选字段](/cells/zh/nodejs-cpp/add-page-field-in-pivot-table/)
- [在 Aspose.Cells for Node.js via C++ 中对数据透视表应用样式](/cells/zh/nodejs-cpp/apply-style-to-pivot-table/)
- [修改数据透视表中的页面字段布局](/cells/zh/nodejs-cpp/change-page-field-layout/)
- [在 Aspose.Cells for Node.js via C++ 中将迷你图转换为图像和 HTML](/cells/zh/nodejs-cpp/convert-sparkline-to-image-and-html/)
- [将 Excel 转换为 OFD 格式](/cells/zh/nodejs-cpp/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="nodejs-cpp" >}}