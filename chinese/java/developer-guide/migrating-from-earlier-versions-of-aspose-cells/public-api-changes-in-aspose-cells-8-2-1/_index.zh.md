---
title: 公共 API Aspose.Cells 8.2.1 的变化
type: docs
weight: 90
url: /zh/java/public-api-changes-in-aspose-cells-8-2-1/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.2.0 到 8.2.1 的更改，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **为 Cell 类添加了 getValidation() 方法**
数据验证是电子表格设计人员用来阻止用户将无效值插入特定单元格的功能之一。在 Aspose.Cells for Java 8.2.1 中，API 公开了一种简单的机制，用于识别是否已对单元格应用数据验证。使用 Cell 类的 getValidation 方法获取任何应用的验证。如果没有验证，该方法返回 null。同样，您可以使用 ValidationCollection 类的 getValidationInCell 方法通过提供其行和列索引来获取应用于任何单元格的验证。

{{% alert color="primary" %}} 

请查看详细文章[在 Cell 上应用验证](https://docs.aspose.com/cells/java/get-validation-applied-on-a-cell/)想要查询更多的信息。

{{% /alert %}}
## **为 Cell 类添加了 getValidationValue() 方法**
除了确定是否已应用验证之外，您还可以验证给定值是否满足特定单元格的数据验证规则。当您想要验证单元格中输入的值是否即时满足数据验证规则时，此功能非常有用。 Aspose.Cells API 暴露了Cell类的getValidationValue方法。如果在单元格中输入的值不满足数据验证规则，则 Cell 类的 getValidationValue 方法返回 false。

{{% alert color="primary" %}} 

请查看详细文章[验证 Cell 值是否满足数据验证规则](/cells/zh/java/verify-that-cell-value-satisfies-data-validation-rules/).

{{% /alert %}}
## **为 WorkbookRender 类添加了重载 toPrinter(PrinterSettings printerSettings) 方法**
您可以使用重载方法通过 PrinterSettings 将工作簿呈现给打印机。
