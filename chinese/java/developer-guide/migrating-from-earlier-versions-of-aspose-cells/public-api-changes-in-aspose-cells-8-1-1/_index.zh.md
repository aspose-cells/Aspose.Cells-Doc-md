---
title: Aspose.Cells 8.1.1中的公共API更改
type: docs
weight: 60
url: /zh/java/public-api-changes-in-aspose-cells-8-1-1/
---

{{% alert color="primary" %}} 

本文档描述了Aspose.Cells API从版本8.1.0到8.1.1的更改，可能对模块和应用程序开发者感兴趣。文档不仅包括[新的和更新的公共方法](/cells/zh/java/public-api-changes-in-aspose-cells-8-1-1/)，还包括对Aspose.Cells背后的任何行为更改的描述。

{{% /alert %}} 
## **添加的属性和特性**
### **新增了HtmlSaveOptions.PresentationPreference属性**
HtmlSaveOptions类已公开PresentationPreference属性的getter/setter，用于在将电子表格导出为HTML或MHTML时以更好的布局呈现结果。默认值为false。若设置为true，Aspose.Cells API将以更好的演示文稿导出工作表内容。

{{% alert color="primary" %}} 

请参阅详细文章[使用PresentationPreference选项实现更好的布局](/cells/zh/java/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}} 
### **增加了对工作表方案的支持**
方案是包含由一个或多个公式连接的变量输入单元格的假设模型。Aspose.Cells已公开了Worksheet.Scenarios属性的getter和setter，还包括以下类，以帮助开发人员创建、操作和移除假设模型。

1. Scenario：表示单个假设模型。
1. ScenarioCollection：表示假设模型的集合。
1. ScenarioInputCellCollection：表示特定假设模型的一组输入单元格。
1. ScenarioInputCell：表示特定假设模型的输入单元格集合中的一个输入单元格。

{{% alert color="primary" %}} 

请参阅详细文章[如何从工作表中创建、操作或移除假设模型](/cells/zh/java/create-manipulate-or-remove-scenarios-from-worksheets/)

{{% /alert %}}
## **CellsException的行为变更**
在以前的Aspose.Cells for Java API版本中，当在工作簿的实例中加载可能损坏的电子表格时，API倾向于抛出一个通用消息，而没有提及问题可能出现的地方。我们已经改变了这种行为，以便于8.1.1时API抛出一个带有有意义的消息的异常，指出异常发生的地方（哪个单元格）和原因（公式表达式）。
