---
title: 合并多个工作簿至单个工作簿
linktitle: 工作簿合并
type: docs
weight: 66
url: /zh/net/combine-multiple-workbooks-into-a-single-workbook/
---

{{% alert color="primary" %}}

有时，您需要将内容各异的工作簿（包含图片、图表和数据）合并成一个工作簿。Aspose.Cells支持此功能。本文展示了如何在Visual Studio中创建控制台应用程序，并使用Aspose.Cells的几行简单代码来合并工作簿。

{{% /alert %}}

## **将带有图片和图表的工作簿合并**

示例代码使用Aspose.Cells将两个工作簿合并成一个工作簿。该代码加载源工作簿，使用 [**Workbook.combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine) 方法将它们合并，然后保存输出工作簿。

### **源工作簿**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **输出工作簿**

- [combined.xlsx](5473095.xlsx)

### **截图**

以下是源工作簿和输出工作簿的截图。

{{% alert color="primary" %}}

您可以使用任何源工作簿。这些图片仅供说明目的。

{{% /alert %}}

**图表工作簿的第一个工作表 - 堆叠** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**图表工作簿的第二个工作表 - 直线** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**图片工作簿的第一个工作表 - 图片** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**组合工作簿中的所有三个工作表 - 堆叠，直线，图片** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CombineMultipleWorkbooksSingleWorkbook-1.cs" >}}

## **高级主题**
- [将多个工作表合并为单个工作表](/cells/zh/net/combine-multiple-worksheets-into-a-single-worksheet/)
- [合并文件](/cells/zh/net/merge-files/)
