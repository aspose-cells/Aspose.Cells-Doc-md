---
title: 以其他语言实现小计或总计标签
type: docs
weight: 50
url: /zh/net/implement-subtotal-or-grand-total-labels-in-other-languages/
---

## **可能的使用场景**

有时，您希望在中文、日文、阿拉伯语、印地语等非英语语言中显示小计和总计标签。Aspose.Cells允许您使用[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)类和[**Workbook.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings) 属性来实现这一点。请参阅此文章，了解如何使用[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)类。

- [使用GlobalizationSettings类自定义小计标签和饼图的其他标签](/cells/zh/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **以其他语言实现小计或总计标签**

以下示例代码加载了[样本Excel文件](5115151.xlsx)并在中文语言环境中实现了小计和总计的名称。请检查此代码生成的[output Excel file](5115152.xlsx)以供参考。我们首先创建了[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)类，然后在我们的代码中使用它。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-GlobalizationSettings.cs" >}}

现在在代码中使用上面创建的类，如下所示：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-UsingGlobalizationSettings.cs" >}}
