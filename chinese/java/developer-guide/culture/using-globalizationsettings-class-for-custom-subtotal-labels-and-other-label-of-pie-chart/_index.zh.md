---
title: 使用GlobalizationSettings类自定义小计标签和饼状图的其他标签
type: docs
weight: 50
url: /zh/java/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---

## **可能的使用场景**
Aspose.Cells API 中已公开了 [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) 类，以处理用户希望在电子表格中使用自定义标签进行小计的情况。此外，当渲染工作表或图表时，还可以使用 [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) 类修改饼图的 **Other** 标签。
## **GlobalizationSettings类简介**
全局化设置（GlobalizationSettings）类目前提供以下3种方法，可以重写为自定义类，以获取所需的小计标签或为饼图的“其他”标签呈现自定义文本。

1. GlobalizationSettings.getTotalName: 获取函数的总名称。
1. GlobalizationSettings.getGrandTotalName: 获取函数的总计名称。
1. GlobalizationSettings.getOtherName: 获取饼图的“其他”标签的名称。
### **自定义小计标签**
全局化设置（GlobalizationSettings）类可通过重写GlobalizationSettings.getTotalName和GlobalizationSettings.getGrandTotalName方法来自定义小计标签，如以下所示。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


为了注入自定义标签，需要在将小计添加到工作表之前，将WorkbookSettings.GlobalizationSettings属性分配给上面定义的CustomSettings类的实例。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomLabelsforSubtotals-CustomLabelsforSubtotals.java" >}}

{{% alert color="primary" %}} 

全局化设置（GlobalizationSettings）类仅用于添加新的小计。如果电子表格已包含小计，它们的标签就无法修改。

{{% /alert %}} 
### **饼状图的其他标签的自定义文本**
全局化设置（GlobalizationSettings）类提供getOtherName方法，可用于为饼图的“其他”标签提供自定义值。以下代码片段定义一个自定义类，并重写getOtherName方法以根据为JVM设置的默认语言获取自定义标签。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


以下代码片段加载包含饼图的现有电子表格，并在利用上面创建的CustomSettings类的情况下将图表呈现为图像。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomTextforOtherLabelofPieChart-CustomTextforOtherLabelofPieChart.java" >}}


当计算机的区域设置为法国时，以下是生成的图像。正如您所见，“其他”标签已根据CustomSettings类中定义的内容翻译为“Autre”。

![todo:image_alt_text](using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart_1.png)
