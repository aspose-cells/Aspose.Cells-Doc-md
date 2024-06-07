---
title: 获得图表的工作表
type: docs
weight: 80
url: /zh/java/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

有时，您希望从图表的引用中访问工作表。Aspose.Cells提供了[**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet)属性，该属性返回包含该图表的工作表的引用。

{{% /alert %}}

## 示例

下面的示例展示了如何使用[**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet)属性。该代码首先打印出工作表的名称，然后访问工作表上的第一个图表。然后再次通过使用[**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet)属性打印出工作表名称。

### 访问图表的工作表的Java代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetWorksheetOfChart-GetWorksheetOfChart.java" >}}

### 由示例代码生成的控制台输出

以下是示例代码产生的控制台输出。可以看到，它两次都打印相同的工作表名称。

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
