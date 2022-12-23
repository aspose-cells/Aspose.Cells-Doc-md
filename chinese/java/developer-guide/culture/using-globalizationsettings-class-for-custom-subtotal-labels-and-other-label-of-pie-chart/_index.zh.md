---
title: 使用 GlobalizationSettings 类自定义小计标签和饼图的其他标签
type: docs
weight: 50
url: /zh/java/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---
## **可能的使用场景**
 Aspose.Cells API暴露了[全球化设置](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)类以处理用户希望在电子表格中为小计使用自定义标签的场景。此外，[全球化设置](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)类也可以用来修改**其他**呈现工作表或图表时饼图的标签。
## **GlobalizationSettings 类简介**
这[全球化设置](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)类目前提供以下 3 种方法，可以在自定义类中重写这些方法以获得小计所需的标签或呈现自定义文本**其他**饼图的标签。

1. [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)): 获取函数的总名称。
1. [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)): 获取函数的总计名称。
1. [GlobalizationSettings.getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)): 获取饼图“其他”标签的名称。
### **小计的自定义标签**
这[全球化设置](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)类可用于通过覆盖自定义小计标签[GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)) & [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)方法如前所述。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


为了注入自定义标签，需要分配[WorkbookSettings.GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings)的一个实例的属性*自定义设置*在将小计添加到工作表之前在上面定义的类。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomLabelsforSubtotals-CustomLabelsforSubtotals.java" >}}

{{% alert color="primary" %}} 

这[全球化设置](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)类仅适用于添加新的小计。如果电子表格已经包含小计，则无法修改它们的标签。

{{% /alert %}} 
### **饼图其他标签的自定义文本**
这[全球化设置](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)类提供[获取其他名称](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\) 方法，该方法可用于为饼图的“其他”标签提供自定义值。以下代码段定义了一个自定义类并覆盖了[获取其他名称](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)方法获取基于为 JVM 设置的默认语言的自定义标签。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


以下代码片段加载包含饼图的现有电子表格，并在利用*自定义设置*上面创建的类。



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomTextforOtherLabelofPieChart-CustomTextforOtherLabelofPieChart.java" >}}


以下是机器的区域设置为法国时的结果图像。如您所见，标签“Other”已被翻译为“Autre”，如中所定义*自定义设置*班级。

![待办事项：图片_替代_文本](using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart_1.png)
