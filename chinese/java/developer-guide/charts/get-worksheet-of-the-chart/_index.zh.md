---
title: 获取图表的工作表
type: docs
weight: 80
url: /zh/java/get-worksheet-of-the-chart/
---
{{% alert color="primary" %}}

有时，您想要从图表的参考访问工作表。 Aspose.Cells 提供了[**图表.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet)返回包含图表的工作表的引用的属性。

{{% /alert %}}

## 例子

下面的例子展示了如何使用[**图表.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet)财产。该代码首先打印工作表的名称，然后访问工作表上的第一个图表。然后它再次打印工作表名称，使用[**图表.getWorksheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/chart#Worksheet)财产。

### Java 访问图表工作表的代码

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetWorksheetOfChart-GetWorksheetOfChart.java" >}}

### 示例代码生成的控制台输出

下面是示例代码生成的控制台输出。如您所见，它两次打印相同的工作表名称。

{{< highlight "java" >}}

Sheet Name: Portfolio

Chart's Sheet Name: Portfolio

{{< /highlight >}}
