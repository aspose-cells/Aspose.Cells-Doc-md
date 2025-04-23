---
title: 调整行高和列宽
type: docs
weight: 10
url: /zh/go-cpp/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}}

在处理电子表格并添加数据到行或列时，您可能需要更改行的高度或列的宽度。有时，在行或列上应用格式意味着当前的高度或宽度需要更改以显示数据。通常，用户在Microsoft Excel中在所见即所得的环境下调整行高和列宽。但是，使用Aspose.Cells，开发人员可以在运行时执行这些操作。

{{% /alert %}}

## **处理行**

### **调整行高**

Aspose.Cells提供[Workbook](https://reference.aspose.com/cells/go-cpp/workbook/)类，该类代表微软Excel文件。它包含一个[WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/)，可以访问Excel文件中的每个工作表。工作表由[Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/)类表示。 [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/)类提供了[Cells](https://reference.aspose.com/cells/go-cpp/cells/)集合，用于管理工作表中的所有单元格。该[Cells](https://reference.aspose.com/cells/go-cpp/cells/)集合提供多个方法管理行或列。以下将详细介绍部分方法。

#### **设置行的高度**

可以调用[Cells](https://reference.aspose.com/cells/go-cpp/cells/)集合的[SetRowHeight](https://reference.aspose.com/cells/go-cpp/cells/setrowheight/)方法设置单行的高度。[SetRowHeight](https://reference.aspose.com/cells/go-cpp/cells/setrowheight/)方法的参数如下：

- **行索引**，要更改高度的行的索引。
- **行高**，要应用于该行的行高。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-GPP-SettingHeightOfRow.go" >}}

#### **设置工作表中所有行的高度**

如果开发者需要为工作表中的所有行设置相同的行高，可以使用[Cells](https://reference.aspose.com/cells/go-cpp/cells/)集合的[SetStandardHeight](https://reference.aspose.com/cells/go-cpp/cells/setstandardheight/)方法。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingHeightOfAllRowsInWorksheet.go" >}}

## **使用列**

### **设置列的宽度**

通过调用[Cells](https://reference.aspose.com/cells/go-cpp/cells/)集合的[SetColumnWidth](https://reference.aspose.com/cells/go-cpp/cells/setcolumnwidth/)方法设置列宽。[SetColumnWidth](https://reference.aspose.com/cells/go-cpp/cells/setcolumnwidth/)方法的参数如下：

- **列索引**，要更改其宽度的列的索引。
- **列宽度**，所需的列宽度。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingWidthOfColumn.go" >}}

### **设置工作表中所有列的宽度**

若想为工作表中的所有列设置相同的列宽，可以使用[Cells](https://reference.aspose.com/cells/go-cpp/cells/)集合的[SetStandardWidth](https://reference.aspose.com/cells/go-cpp/cells/setstandardwidth/)方法。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingWidthOfAllColumnsInWorksheet.go" >}}
