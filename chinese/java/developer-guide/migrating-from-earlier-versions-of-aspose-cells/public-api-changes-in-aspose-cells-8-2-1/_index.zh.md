---
title: Aspose.Cells 8.2.1中的公共API更改
type: docs
weight: 90
url: /zh/java/public-api-changes-in-aspose-cells-8-2-1/
---

{{% alert color="primary" %}} 

本文档描述了从版本8.2.0到8.2.1的Aspose.Cells API的更改，这可能会对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，还描述了Aspose.Cells在幕后行为的任何更改。

{{% /alert %}} 
## **为Cell类添加了getValidation()方法**
数据验证是电子表格设计者用来阻止用户在特定单元格中插入无效值的特性之一。使用Aspose.Cells for Java 8.2.1，API公开了一种简单的机制，用于识别是否在单元格上应用了数据验证。使用Cell类的getValidation方法获取应用的任何验证。如果没有验证，该方法将返回null。同样，您可以使用ValidationCollection类的getValidationInCell方法通过提供其行和列索引来获取应用在任何单元格上的验证。

{{% alert color="primary" %}} 

请查看[获取应用在单元格上的验证](https://docs.aspose.com/cells/java/get-validation-applied-on-a-cell/)的详细文章以获取更多信息。

{{% /alert %}}
## **为Cell类添加了getValidationValue()方法**
除确定是否应用了验证之外，您还可以验证给定值是否满足特定单元格的数据验证规则。此功能在您希望实时验证单元格中输入的值是否满足数据验证规则的情况下非常有用。Aspose.Cells API已经公开了Cell类的getValidationValue方法。如果单元格中输入的值不满足数据验证规则，Cell类的getValidationValue方法会返回false。

{{% alert color="primary" %}} 

请查看关于[验证单元格值是否满足数据验证规则]的详细文章(/cells/zh/java/verify-that-cell-value-satisfies-data-validation-rules/)

{{% /alert %}}
## **为WorkbookRender类的toPrinter(PrinterSettings printerSettings)方法添加了重载**
您可以使用重载的方法将工作簿呈现到打印机，通过PrinterSettings。
{{< app/cells/assistant language="java" >}}
