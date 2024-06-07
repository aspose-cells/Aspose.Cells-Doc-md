---
title: 禁用图表的数据标签的文本换行
type: docs
weight: 60
url: /zh/java/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013允许用户对图表的数据标签进行换行或取消换行。默认情况下，数据标签文本被包装。

{{% /alert %}}

Aspose.Cells提供了[**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)方法。将**True**或**False**设置以分别启用或禁用数据标签上的文本换行。

同样，使用[**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)方法来查找数据标签是否已经被包装。

此屏幕截图显示了包含图表的示例Microsoft Excel文件。如您所见，您可以在Microsoft Excel 2013的格式数据标签面板的ALIGNMENT部分中检查或清除**Wrap text in shape**选项。

**数据标签换行**

![todo:image_alt_text](disable-text-wrapping-for-data-labels-of-the-chart_1.png)

接下来的示例代码加载了使用Aspose.Cells的示例Microsoft Excel文件，并使用[**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)方法禁用了数据标签文本的换行。执行代码后，图表现在是这个样子。先前被包装的文本现在已经取消包装。

**只显示一行数据标签**

![todo:image_alt_text](disable-text-wrapping-for-data-labels-of-the-chart_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableTextWrapping-DisableTextWrapping.java" >}}
