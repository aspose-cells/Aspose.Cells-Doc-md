---
title: 使用GlobalizationSettings类自定义小计标签和饼状图的其他标签
type: docs
weight: 70
url: /zh/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---

## **可能的使用场景**

Aspose.Cells API已公开[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)类，以处理用户希望在电子表格中使用自定义标签的情形。此外，[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)类也可用于修改饼图渲染时的**其他**标签。

## **GlobalizationSettings类简介**

[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)类目前提供以下3个方法，可以通过自定义类来覆盖以获得所需的小计标签，或者渲染饼图的**其他**标签的自定义文本。

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname)：获取函数的总名称。
1. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname)：获取函数的总计名称。
1. [**GlobalizationSettings.GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)：获取饼图的"其他"标签的名称。

### **自定义小计标签**

[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)类可通过覆盖[**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/gettotalname)和[**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getgrandtotalname)方法来自定义小计标签，如下所示。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-GlobalizationSettings.cs" >}}

为了注入自定义标签，需要将[**WorkbookSettings.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings)属性分配给上面定义的**CustomSettings**类的实例，然后将小计添加到工作表。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomLabelsSubtotals-UsingGlobalizationSettings.cs" >}}

{{% alert color="primary" %}}

[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)类仅适用于添加新的小计。如果电子表格已包含小计，它们的标签将无法修改。

{{% /alert %}}

### **饼状图的其他标签的自定义文本**

[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)类提供[**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)方法，可用于为饼状图的"其他"标签赋予自定义值。以下片段定义了一个自定义类，并覆盖了[**GetOtherName**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings/methods/getothername)方法，以根据系统的区域设置标识符获取自定义标签。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-GlobalizationSettings.cs" >}}

以下片段加载包含饼图的现有电子表格，并在利用上面创建的**CustomSettings**类的同时将图表渲染为图像。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CustomTextForLabels-UsingGlobalizationSettings.cs" >}}
{{< app/cells/assistant language="csharp" >}}
