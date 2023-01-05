---
title: 以其他语言实施小计或总计标签
type: docs
weight: 50
url: /zh/net/implement-subtotal-or-grand-total-labels-in-other-languages/
---
## **可能的使用场景**

有时，您想用非英语语言（如中文、日语、阿拉伯语、印地语等）显示小计和总计标签。Aspose.Cells 允许您使用[**全球化设置**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)类和[**工作簿.全球化设置**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/globalizationsettings)财产。请参阅这篇文章了解如何使用[**全球化设置**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)班级

- [使用 GlobalizationSettings 类自定义小计标签和饼图的其他标签](/cells/zh/net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## **以其他语言实施小计或总计标签**

下面的示例代码加载[示例 excel 文件](5115151.xlsx)并以中文实现小计和总计名称。请检查[输出Excel文件](5115152.xlsx)此代码生成供您参考。我们首先创建一个类[**全球化设置**](https://reference.aspose.com/cells/net/aspose.cells/globalizationsettings)然后在我们的代码中使用它。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-GlobalizationSettings.cs" >}}

现在在代码中使用上面创建的类，如下所示：

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-TotalsInOtherLanguages-UsingGlobalizationSettings.cs" >}}
