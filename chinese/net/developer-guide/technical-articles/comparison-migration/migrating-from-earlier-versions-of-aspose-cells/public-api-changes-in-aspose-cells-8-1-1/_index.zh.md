---
title: 公共 API Aspose.Cells 8.1.1 的变化
type: docs
weight: 50
url: /zh/net/public-api-changes-in-aspose-cells-8-1-1/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.1.0 到 8.1.1 的更改，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **添加了 HtmlSaveOptions.PresentationPreference 属性**
HtmlSaveOptions 类公开了 PresentationPreference 属性，可用于在将电子表格导出为 HTML 或 MHTML 时以更好的布局呈现结果。默认值为假。而如果设置为 true，则 Aspose.Cells API 将以更好的呈现方式导出工作表内容。

{{% alert color="primary" %}} 

请查看详细文章[使用 PresentationPreference 选项以获得更好的布局](/cells/zh/net/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}}
## **添加了对工作表场景的支持**
一个场景被命名为假设模型，其中包括通过一个或多个公式相应地链接在一起的变量输入单元格。 Aspose.Cells API 公开了 Worksheet.Scenarios 属性以及以下类，以方便用户从工作表中创建、操作和删除场景，

1. 场景：代表一个单独的场景。
1. ScenarioCollection：表示场景的集合。
1. ScenarioInputCellCollection：表示特定场景的输入单元列表。
1. ScenarioInputCell：表示来自特定场景的输入单元集合的输入单元。

{{% alert color="primary" %}} 

请查看详细文章[如何从工作表中创建、操作或删除场景](/cells/zh/net/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
