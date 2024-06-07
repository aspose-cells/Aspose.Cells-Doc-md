---
title: Aspose.Cells 8.1.1中的公共API更改
type: docs
weight: 50
url: /zh/net/public-api-changes-in-aspose-cells-8-1-1/
---

{{% alert color="primary" %}} 

此文档描述了从版本8.1.0到8.1.1的Aspose.Cells API的更改，这可能会引起模块/应用程序开发人员的兴趣。它不仅包括新的和更新的公共方法，还描述了Aspose.Cells背后的行为中的任何更改。

{{% /alert %}} 
## **添加了HtmlSaveOptions.PresentationPreference属性**
HtmlSaveOptions类已公开PresentationPreference属性，该属性可用于在将电子表格导出为HTML或MHTML格式时使用更好的布局呈现结果。默认值为false。如果设置为true，Aspose.Cells API将以更好的演示方式导出工作表内容。

{{% alert color="primary" %}} 

请查阅有关[使用PresentationPreference选项获得更好布局的详细文章](/cells/zh/net/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}}
## **添加了对工作表方案的支持**
方案是包含由一个或多个公式连结在一起的变量输入单元格的假设模型。Aspose.Cells API已公开Worksheet.Scenarios属性以及以下类，以帮助用户创建、操控和从工作表中删除方案。 

1. Scenario: 代表一个独立的方案。
1. ScenarioCollection: 代表一组场景。
1. ScenarioInputCellCollection: 代表特定方案的输入单元格列表。
1. ScenarioInputCell: 代表特定方案的输入单元格集合中的一个输入单元格。

{{% alert color="primary" %}} 

请查阅有关[如何在工作表中创建、操作或移除方案的详细文章](/cells/zh/net/create-manipulate-or-remove-scenarios-from-worksheets/)

{{% /alert %}}
