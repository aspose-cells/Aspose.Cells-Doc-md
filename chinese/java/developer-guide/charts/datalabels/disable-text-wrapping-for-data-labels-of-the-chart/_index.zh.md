---
title: 禁用图表数据标签的文本换行
type: docs
weight: 60
url: /zh/java/disable-text-wrapping-for-data-labels-of-the-chart/
---
{{% alert color="primary" %}}

Microsoft Excel 2013 允许用户在图表的数据标签内环绕或展开文本。默认情况下，数据标签文本是换行的。

{{% /alert %}}

Aspose.Cells 提供了[**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)方法。调成**真的**或者**错误的**分别启用或禁用数据标签上的文本换行。

同样，使用[**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)查明数据标签是否已包装的方法。

此屏幕截图显示了一个示例 Microsoft Excel 文件，其中包含一个图表，其中包含数据标签的文本。如您所见，您可以检查或清除**将文字环绕成形状**Microsoft Excel 2013 中格式数据标签面板的对齐部分中的选项。

**包装数据标签**

![待办事项：图像_替代_文本](disable-text-wrapping-for-data-labels-of-the-chart_1.png)

下面的示例代码使用 Aspose.Cells 加载示例 Microsoft Excel 文件并使用禁用数据标签文本换行[**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)方法。执行代码时，图表如下所示。先前换行的文本现在已展开。

**仅在一行中显示数据标签**

![待办事项：图像_替代_文本](disable-text-wrapping-for-data-labels-of-the-chart_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableTextWrapping-DisableTextWrapping.java" >}}
