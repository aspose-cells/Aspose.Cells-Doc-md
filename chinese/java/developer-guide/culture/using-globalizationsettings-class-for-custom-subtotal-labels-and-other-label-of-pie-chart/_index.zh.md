---
title: 使用全球化设置类自定义饼图的其他标签和其他标签
type: docs
weight: 50
url: /zh/java/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---

## **可能的使用场景**
Aspose.Cells APIs已公开了[GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)类，用于处理用户希望在电子表格中使用自定义标签的情况。 此外，[GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)类还可用于在呈现工作表或图表时修改饼图的**Other**标签。
## **全球化设置类简介**
[GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) 类当前提供以下3个方法，可以在自定义类中进行重写，以获取所需标签用于小计或者渲染**Other**标签的饼图。

1. [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)): 获取函数的总名称。
1. [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)): 获取函数的总计名称。
1. [GlobalizationSettings.getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)): 获取饼图的“Other”标签名称。
### **子总计的自定义标签**
[GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) 类可用于通过重写[GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)) 和[GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)) 方法来自定义小计标签。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


要注入自定义标签，需要将[WorkbookSettings.GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) 属性分配给上面定义的*CustomSettings* 类的实例，然后在将小计添加到工作表之前。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomLabelsforSubtotals-CustomLabelsforSubtotals.java" >}}

{{% alert color="primary" %}} 

[GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) 类仅用于添加新的小计。 如果电子表格已包含小计，则无法修改它们的标签。

{{% /alert %}} 
### **饼图的其他标签的自定义文本**
[GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) 类提供了[getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\))方法，用于为饼图的“Other”标签提供自定义值。 以下代码片段定义了一个自定义类，并重写[getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)) 方法，以根据为JVM设定的默认语言获取自定义标签。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


以下代码片段加载了包含饼图的现有电子表格，并在使用上述创建的*CustomSettings* 类时将图表呈现为图像。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomTextforOtherLabelofPieChart-CustomTextforOtherLabelofPieChart.java" >}}


当机器的区域设置为法国时，以下是生成的图像。 正如您看到的那样，“其他”标签已被翻译为“Autre”，如*CustomSettings* 类中定义。

![todo:image_alt_text](using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart_1.png)
