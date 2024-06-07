---
title: Aspose.Cells 8.2.1中的公共API更改
type: docs
weight: 80
url: /zh/net/public-api-changes-in-aspose-cells-8-2-1/
---

{{% alert color="primary" %}} 

此文档描述了从版本8.2.0到8.2.1的Aspose.Cells API的更改，这可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，还包括对Aspose.Cells内部行为的任何更改的描述。

{{% /alert %}} 
## **为Cell Class添加了GetValidation()方法**
数据验证是电子表格设计者用来阻止用户向特定单元格插入无效值的功能之一。通过Aspose.Cells for .NET 8.2.1，API已公开了一个简单的机制，用于识别单元格上是否应用了数据验证。使用Cell类的GetValidation方法获取应用的任何验证。如果没有验证，该方法将返回null。同样，您可以通过提供其行和列索引使用ValidationCollection类的GetValidationInCell方法获取应用于任何单元格的验证。

{{% alert color="primary" %}} 

请查阅有关[获取应用于单元格的验证的详细文章](/cells/zh/net/get-validation-applied-on-a-cell/)以获取更多信息

{{% /alert %}}
## **为Cell类添加了GetValidationValue()方法**
除了确定是否应用了验证外，您还可以验证给定值是否满足特定单元格的数据验证规则。当您想要验证输入单元格中的值是否满足数据验证规则时，此功能很有用。Aspose.Cells API已为Cell类公开了GetValidationValue方法。如果输入单元格中输入的值不满足数据验证规则，则Cell类的GetValidationValue方法返回false。

{{% alert color="primary" %}} 

请查阅有关[验证单元格值是否符合数据验证规则的详细文章](/cells/zh/net/verify-that-cell-value-satisfies-data-validation-rules/)

{{% /alert %}}
## **为WorkbookRender类添加了重载ToPrinter(PrinterSettings printerSettings)方法**
您可以使用重载的方法通过PrinterSettings将工作簿渲染到打印机。
