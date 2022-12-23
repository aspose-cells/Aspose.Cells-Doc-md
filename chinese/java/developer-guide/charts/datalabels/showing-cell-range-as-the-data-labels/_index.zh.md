---
title: 显示 Cell 范围作为数据标签
type: docs
weight: 110
url: /zh/java/showing-cell-range-as-the-data-labels/
---
## 在 MS Excel 中将单元格范围显示为数据标签

在 Microsoft Excel 2013 中，您可以为数据标签显示 Cell 范围。您可以按照以下步骤选择此选项

- 选择系列的数据标签，然后右键单击以打开弹出菜单。
- 点击**格式化数据标签...**它会显示**标签选项**.
- 选中或取消选中复选框**标签包含 - 值来自 Cells**.

### **将 Cell 范围显示为数据标签的复选框**

以下屏幕截图突出显示了此选项以供您参考。

![待办事项：图片_替代_文本](showing-cell-range-as-the-data-labels_1.png)

## 使用 Aspose.Cells 将单元格范围显示为数据标签

Aspose.Cells 提供了[**DataLabels.setShowCellRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#ShowCellRange)选中或取消选中复选框的方法**标签包含 - 值来自 Cells**如上面的屏幕截图所示。

## Java 将单元格范围显示为数据标签的代码

下面的示例代码访问图表系列的数据标签，然后设置[**DataLabels.setShowCellRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#ShowCellRange)检查真值的方法**标签包含 - 值来自 Cells**选项。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowCellRangeAsTheDataLabels-ShowCellRangeAsTheDataLabels.java" >}}
