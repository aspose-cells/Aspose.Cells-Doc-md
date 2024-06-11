---
title: Aspose.Cells 8.2.1中的公共API更改
type: docs
weight: 80
url: /zh/net/public-api-changes-in-aspose-cells-8-2-1/
---

{{% alert color="primary" %}} 

本文档描述了从版本8.2.0到8.2.1的Aspose.Cells API的更改，这可能会对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，还描述了Aspose.Cells在幕后行为的任何更改。

{{% /alert %}} 
## **为 Cell 类添加了 GetValidation() 方法**
数据验证是电子表格设计者用来阻止用户在特定单元格中插入无效值的功能之一。使用Aspose.Cells for .NET 8.2.1，API已经提供了一个简单的机制来确定单元格是否应用了数据验证。使用Cell类的GetValidation方法获取应用的任何验证。如果没有验证，则该方法返回null。类似地，您可以使用ValidationCollection类的GetValidationInCell方法获取应用在任何单元格上的验证，方法是提供其行和列索引。

{{% alert color="primary" %}} 

请查看详细文章 [获取应用在单元格上的验证](/cells/zh/net/get-validation-applied-on-a-cell/) 以获取更多信息。

{{% /alert %}}
## **为 Cell 类添加了 GetValidationValue() 方法**
除了确定是否已应用验证外，还可以验证给定值是否符合特定单元格的数据验证规则。此功能在您希望验证输入的值是否实时满足数据验证规则的场景中非常有用。Aspose.Cells API 公开了 Cell 类的 GetValidationValue 方法。如果输入的单元格值不符合数据验证规则，则 Cell 类的 GetValidationValue 方法返回 false。

{{% alert color="primary" %}} 

请查看详细文章 [验证单元格值是否满足数据验证规则](/cells/zh/net/verify-that-cell-value-satisfies-data-validation-rules/) 以获取更多信息。

{{% /alert %}}
## **为 WorkbookRender 类添加了ToPrinter(PrinterSettings printerSettings)方法的重载**
您可以使用重载的方法将工作簿呈现到打印机，通过PrinterSettings。
