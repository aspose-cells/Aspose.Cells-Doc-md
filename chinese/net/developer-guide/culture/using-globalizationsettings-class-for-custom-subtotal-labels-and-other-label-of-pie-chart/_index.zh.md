---
title: 使用全球化设置类自定义饼图的其他标签和其他标签
type: docs
weight: 70
url: /zh/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---

## **可能的使用场景**

Aspose.Cells API已经公开了[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)类，以处理用户希望在电子表格中使用自定义标签用于小计的场景。此外，在呈现工作表或图表时，[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)类也可用于修改饼图的**其他**标签。

## **全球化设置类简介**

[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)类目前提供以下3个方法，可以在自定义类中进行重写，以获取期望的小计标签或为饼图的**其他**标签呈现自定义文本。

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname)：获取函数的总名称。
1. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname)：获取函数的总名称。
1. [**GlobalizationSettings.GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)：获取饼图的“其他”标签的名称。

### **子总计的自定义标签**

[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)类可以用于通过重写[**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname)和[**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname)方法自定义子总计标签，如前面所示。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-GlobalizationSettings.cs" >}}

为了注入自定义标签，需要在将子总计添加到工作表之前将[**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings)属性分配给上面定义的**CustomSettings**类的实例。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-UsingGlobalizationSettings.cs" >}}

{{% alert color="primary" %}}

[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)类仅用于添加新的子总计。如果电子表格已包含子总计，它们的标签将无法修改。

{{% /alert %}}

### **饼图的其他标签的自定义文本**

[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)类提供[**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)方法，该方法对于为饼图的“其他”标签赋予自定义值非常有用。以下代码片段定义了一个自定义类，并重写了[**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)方法，根据系统的区域设置标识符获取自定义标签。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-GlobalizationSettings.cs" >}}

以下代码片段加载了包含饼图的现有电子表格，并利用上面创建的**CustomSettings**类将图表渲染为图像。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-UsingGlobalizationSettings.cs" >}}
