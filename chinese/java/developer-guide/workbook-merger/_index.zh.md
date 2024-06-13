---
title: 将多个工作簿合并为单个工作簿
linktitle: 工作簿合并器
type: docs
weight: 50
url: /zh/java/combine-multiple-workbooks-into-a-single-workbook/
description: 通过使用 Java 代码和 Aspose.Cells for Java API，将多个工作簿合并成单个工作簿
keywords: 将多个工作簿合并成一个，将多个工作簿合并成一个java，将多个工作簿与java合并成一个，将多个工作簿与java合并成一个单一工作簿，将多个工作簿与单一工作簿合并成一个java，使用java代码将多个工作簿合并成一个单一工作簿，如何使用java将多个工作簿合并成一个单一工作簿，如何使用java将多个工作簿合并成一个，使用java合并多个工作簿为一个，如何使用java将多个工作簿合并为一个
---

{{% alert color="primary" %}}

有时，您需要将带有不同内容（如图像、图表和数据）的工作簿合并到单个工作簿中。Aspose.Cells支持此功能。本文演示了如何使用Aspose.Cells创建一个简单的应用程序，使用几行简单的代码将工作簿合并成一个。

{{% /alert %}}

## **合并工作簿**

示例代码使用Aspose.Cells for Java将两个工作簿合并为一个工作簿。该代码加载源工作簿，使用[**Workbook.combine()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#combine(com.aspose.cells.Workbook))方法将它们合并，并保存输出工作簿。

### **源工作簿**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **输出工作簿**

- [combined.xlsx](5473095.xlsx)

### **屏幕截图**

以下是源和输出工作簿的屏幕截图。

{{% alert color="primary" %}}

您可以使用任何源工作簿。这些图像仅用于说明目的。

{{% /alert %}}

**图表工作簿的第一个工作表 - 堆叠**

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**图表工作簿的第二个工作表 - 折线**

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**图片工作簿的第一个工作表 - 图片**

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**组合工作簿中的三个工作表 - 堆叠、线条、图片**

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

以下代码片段显示了如何将多个工作簿合并成一个单一工作簿。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CombineMultipleWorkbooks-CombineMultipleWorkbooks.java" >}}

## **其他资源**

{{% alert color="primary" %}}

您可能会发现[将多个工作表合并到单个工作表](/cells/zh/java/combine-multiple-worksheets-into-a-single-worksheet/)一文对您有所帮助。

{{% /alert %}}

## **高级主题**
- [将多个工作表合并到单个工作表](/cells/zh/java/combine-multiple-worksheets-into-a-single-worksheet/)
- [合并文件](/cells/zh/java/merge-files/)

