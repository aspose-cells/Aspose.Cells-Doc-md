---
title: 在其他语言中实现小计或总计标签
type: docs
weight: 50
url: /zh/net/implement-subtotal-or-grand-total-labels-in-other-languages/
---

## **可能的使用场景**

有时，您希望在非英语语言（如中文、日语、阿拉伯语、印地语等）中显示小计和总计标签。Aspose.Cells允许您使用[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)类和[**Workbook.GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings)属性实现此目的。请参阅关于如何使用[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)类的文章。

- [使用全球化设置类自定义饼图的其他标签和其他标签](/cells/zh/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **在其他语言中实现小计或总计标签**

以下示例代码加载了[示例Excel文件](5115151.xlsx)并将小计和总计名称实现为中文。请查看此代码生成的[输出Excel文件](5115152.xlsx)作为参考。我们首先创建了一个[**GlobalizationSettings**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)类，然后在我们的代码中使用它。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-GlobalizationSettings.cs" >}}

现在在代码中使用上述创建的类，如下所示：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-UsingGlobalizationSettings.cs" >}}
