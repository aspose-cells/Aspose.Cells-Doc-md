---
title: 禁用图表的数据标签文本换行
type: docs
weight: 60
url: /zh/java/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013允许用户在图表的数据标签内换行或取消换行。默认情况下，数据标签文本是换行的。

{{% /alert %}}

Aspose.Cells提供了[**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)方法。设置为**True**或**False**分别启用或禁用数据标签上的文本换行。

同样，使用[**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)方法来查看数据标签是否已经换行。

此屏幕截图显示了一个包含图表的示例Microsoft Excel文件，其中数据标签的文本已经换行。您可以看到，在Microsoft Excel 2013的Format Datalabels面板的ALIGNMENT部分中，您可以选中或清除**Wrap text in shape**选项。

**数据标签换行**

![todo:image_alt_text](disable-text-wrapping-for-data-labels-of-the-chart_1.png)

以下代码加载示例Microsoft Excel文件，并使用[**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)方法禁用数据标签文本换行。当代码执行时，图表看起来像这样。先前换行的文本现在已经取消换行。

**仅显示单行数据标签**

![todo:image_alt_text](disable-text-wrapping-for-data-labels-of-the-chart_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableTextWrapping-DisableTextWrapping.java" >}}
