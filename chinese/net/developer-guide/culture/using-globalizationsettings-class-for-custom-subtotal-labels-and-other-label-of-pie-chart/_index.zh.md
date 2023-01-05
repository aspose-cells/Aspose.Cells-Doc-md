---
title: 使用 GlobalizationSettings 类自定义小计标签和饼图的其他标签
type: docs
weight: 70
url: /zh/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---
## **可能的使用场景**

 Aspose.Cells API暴露了[**全球化设置**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)类以处理用户希望在电子表格中为小计使用自定义标签的场景。此外，[**全球化设置**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)类也可以用来修改**其他**呈现工作表或图表时饼图的标签。

## **GlobalizationSettings 类简介**

这[**全球化设置**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)类目前提供以下 3 种方法，可以在自定义类中重写这些方法以获得小计所需的标签或呈现自定义文本**其他**饼图的标签。

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname)：获取函数的总名称。
1. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname)：获取函数的总计名称。
1. [**GlobalizationSettings.GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)：获取饼图“其他”标签的名称。

### **小计的自定义标签**

这[**全球化设置**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)类可用于通过覆盖自定义小计标签[**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname) & [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname)前面演示的方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-GlobalizationSettings.cs" >}}

为了注入自定义标签，需要分配[**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings)的一个实例的属性**自定义设置**在将小计添加到工作表之前在上面定义的类。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-UsingGlobalizationSettings.cs" >}}

{{% alert color="primary" %}}

这[**全球化设置**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)类仅适用于添加新的小计。如果电子表格已经包含小计，则无法修改它们的标签。

{{% /alert %}}

### **饼图其他标签的自定义文本**

这[**全球化设置**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)课程优惠[**获取其他名称**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)为饼图的“其他”标签提供自定义值很有用的方法。以下代码段定义了一个自定义类并覆盖了[**获取其他名称**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)根据系统的文化标识符获取自定义标签的方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-GlobalizationSettings.cs" >}}

以下代码片段加载包含饼图的现有电子表格，并在利用**自定义设置**上面创建的类。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-UsingGlobalizationSettings.cs" >}}
