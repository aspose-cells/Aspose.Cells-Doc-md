---
title: 公共 API Aspose.Cells 8.1.1 的变化
type: docs
weight: 60
url: /zh/java/public-api-changes-in-aspose-cells-8-1-1/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.1.0 到 8.1.1 的更改，模块和应用程序开发人员可能会感兴趣。它不仅包括[新的和更新的公共方法](/cells/zh/java/public-api-changes-in-aspose-cells-8-1-1/) 也有任何的描述[行为改变](/cells/zh/java/public-api-changes-in-aspose-cells-8-1-1/)在 Aspose.Cells 的幕后。

{{% /alert %}} 
## **添加的属性和功能**
### **添加了 HtmlSaveOptions.PresentationPreference 属性**
HtmlSaveOptions 类公开了 PresentationPreference 属性的 getter/setter，可用于在将电子表格导出为 HTML 或 MHTML 时以更好的布局呈现结果。默认值为假。而如果设置为 true，则 Aspose.Cells API 会以更好的呈现方式导出工作表内容。

{{% alert color="primary" %}} 

请查看详细文章[使用 PresentationPreference 选项以获得更好的布局](/cells/zh/java/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}} 
### **添加了对工作表场景的支持**
情景是一种假设模型，其中包含通过一个或多个公式链接在一起的可变输入单元格。 Aspose.Cells 公开了 Worksheet.Scenarios 属性的 getter 和 setter 以及以下类，以帮助开发人员创建、操作和删除场景。

1. 场景：代表一个单独的场景。
1. ScenarioCollection：表示场景的集合。
1. ScenarioInputCellCollection：表示特定场景的输入单元列表。
1. ScenarioInputCell：表示来自特定场景的输入单元集合的输入单元。

{{% alert color="primary" %}} 

请查看详细文章[如何从工作表中创建、操作或删除场景](/cells/zh/java/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
## **CellsException 的行为变化**
对于 Aspose.Cells for Java API 的先前版本，当在 Workbook 实例中加载可能已损坏的电子表格时，API 往往会抛出一条通用消息，而不会提及问题可能出在哪里。我们已经为 8.1.1 更改了此行为，以便 API 抛出一个异常，其中包含一条有意义的消息，指出在读取模板文件时在哪里（哪个单元格）和什么（公式表达式）导致异常。
