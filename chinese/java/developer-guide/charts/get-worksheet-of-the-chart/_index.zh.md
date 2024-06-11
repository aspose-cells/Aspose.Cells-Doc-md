---
title: 获取图表的工作表
type: docs
weight: 80
url: /zh/java/get-worksheet-of-the-chart/
---

{{% alert color="primary" %}}

有时，您可能希望从图表的引用中访问工作表。Aspose.Cells提供了[**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet)属性，该属性返回包含图表的工作表的引用。

{{% /alert %}}

## 示例

以下示例显示了如何使用[**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet)属性。代码首先打印工作表的名称，然后访问工作表上的第一个图表。然后使用[**Chart.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet)属性再次打印工作表名称。

### 用于访问图表的工作表的Java代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetWorksheetOfChart-GetWorksheetOfChart.java" >}}

### 样本代码生成的控制台输出

以下是示例代码生成的控制台输出结果。如您所见，它两次打印相同的工作表名称。

{{< highlight java >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
