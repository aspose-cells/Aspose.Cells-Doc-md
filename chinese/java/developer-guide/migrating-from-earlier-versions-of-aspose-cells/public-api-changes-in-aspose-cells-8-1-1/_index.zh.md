---
title: Aspose.Cells 8.1.1中的公共API更改
type: docs
weight: 60
url: /zh/java/public-api-changes-in-aspose-cells-8-1-1/
---

{{% alert color="primary" %}} 

本文描述了从版本 8.1.0 到 8.1.1 中 Aspose.Cells API 的更改，可能对模块和应用程序开发人员感兴趣。它不仅包括[新的和更新的公共方法](/cells/zh/java/public-api-changes-in-aspose-cells-8-1-1/)，还包括对 Aspose.Cells 背后行为的任何[更改的描述](/cells/zh/java/public-api-changes-in-aspose-cells-8-1-1/)。

{{% /alert %}} 
## **已添加的属性和功能**
### **添加了 HtmlSaveOptions.PresentationPreference 属性**
HtmlSaveOptions类暴露了PresentationPreference属性的getter/setter，用于在将电子表格导出为HTML或MHTML时以更好的布局呈现结果。默认值为false。如果设置为true，Aspose.Cells API将以更好的演示方式导出工作表内容。

{{% alert color="primary" %}} 

请查看[使用PresentationPreference选项进行更好布局](/cells/zh/java/excel-to-html-use-presentationpreference-option-for-better-layout/)的详细文章。

{{% /alert %}} 
### **添加了对工作表方案的支持**
场景是一个包含由一个或多个公式连接的变量输入单元格的假设模型。Aspose.Cells已经暴露了Worksheet.Scenarios属性的getter和setter，以及以下类来帮助开发人员创建、操作和删除场景。

1. Scenario: 代表一个独立的方案。
1. ScenarioCollection: 代表一组场景。
1. ScenarioInputCellCollection：表示特定场景的输入单元格列表。
1. ScenarioInputCell：表示特定场景的输入单元格集合中的一个输入单元格。

{{% alert color="primary" %}} 

请查看[如何创建、操作或删除工作表中的场景](/cells/zh/java/create-manipulate-or-remove-scenarios-from-worksheets/)的详细文章。

{{% /alert %}}
## **CellsException行为变更**
在之前的Aspose.Cells for Java API版本中，当在Workbook实例中加载可能损坏的电子表时，API通常会抛出一个通用消息，而不会指出问题可能出在哪里。我们在8.1.1版本中改变了这种行为，使API抛出一个带有有意义消息的异常，明确指出了异常的触发位置(哪个单元格)和导致异常的原因(公式表达式)。
