---
title: Aspose.Cells 8.1.1中的公共API更改
type: docs
weight: 50
url: /zh/net/public-api-changes-in-aspose-cells-8-1-1/
---

{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.1.0 到 8.1.1 的更改，可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，还描述了 Aspose.Cells 在幕后行为的任何更改。

{{% /alert %}} 
## **添加了HtmlSaveOptions.PresentationPreference属性**
HtmlSaveOptions类暴露了PresentationPreference属性，可以在将电子表格导出为HTML或MHTML时用于更好的布局。默认值为false。如果设置为true，Aspose.Cells API将以更好的表现形式导出工作表内容。

{{% alert color="primary" %}} 

请查看有关[使用PresentationPreference选项以获得更好的布局](/cells/zh/net/excel-to-html-use-presentationpreference-option-for-better-layout/)的详细文章

{{% /alert %}}
## **增加了对工作表方案的支持**
方案是指包括由一个或多个公式链接的可变输入单元格组成的“假如”模型。Aspose.Cells API暴露了Worksheet.Scenarios属性以及以下类，以方便用户创建、操纵和删除工作表中的方案: 

1. Scenario：表示单个假设模型。
1. ScenarioCollection：表示假设模型的集合。
1. ScenarioInputCellCollection: 代表特定方案的输入单元格列表。
1. ScenarioInputCell: 代表特定方案的输入单元格。

{{% alert color="primary" %}} 

请查看有关[如何在工作表中创建、操纵或删除方案](/cells/zh/net/create-manipulate-or-remove-scenarios-from-worksheets/)的详细文章。

{{% /alert %}}
