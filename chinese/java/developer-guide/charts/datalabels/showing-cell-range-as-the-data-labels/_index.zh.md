---
title: 将单元格范围显示为数据标签
type: docs
weight: 110
url: /zh/java/showing-cell-range-as-the-data-labels/
---

## 在MS Excel中将单元格范围显示为数据标签

在Microsoft Excel 2013中，您可以显示单元格范围作为数据标签。您可以通过以下步骤选择此选项

- 选择系列的数据标签, 并右键单击打开弹出菜单。
-单击 **格式化数据标签...**，它将显示 **标签选项**。
-选中或取消选中复选框 **标签包含 - 来自单元格的值**。

### **复选框显示单元格范围作为数据标签**

以下截图突出显示了此选项，供您参考。

![todo:image_alt_text](showing-cell-range-as-the-data-labels_1.png)

## 使用Aspose.Cells显示单元格范围作为数据标签

Aspose.Cells提供了[**DataLabels.setShowCellRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#ShowCellRange)方法，用于选中或取消选中复选框 **标签包含 - 来自单元格的值**，如上面的截图所示。

## 显示单元格范围作为数据标签的Java代码

下面的示例代码访问图表系列的数据标签，然后将[**DataLabels.setShowCellRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#ShowCellRange)方法设置为true，以选中 **标签包含 - 来自单元格的值** 选项。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowCellRangeAsTheDataLabels-ShowCellRangeAsTheDataLabels.java" >}}
