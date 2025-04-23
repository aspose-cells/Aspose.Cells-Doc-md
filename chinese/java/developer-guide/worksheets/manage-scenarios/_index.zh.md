---
title: 创建、操作或移除工作表中的场景
linktitle: 管理场景
type: docs
weight: 120
url: /zh/java/create-manipulate-or-remove-scenarios-from-worksheets/
---

{{% alert color="primary" %}}

有时，您需要在电子表格中创建、操作或删除场景。场景是一个名为的假设模型，其中包括由一个或多个公式链接在一起的变量输入单元格。在创建场景之前，设计一个包含至少一个依赖于可以插入不同值的单元格的公式的工作表。以下示例演示了如何使用Aspose.Cells API从工作表中创建和移除场景。

{{% /alert %}}

Aspose.Cells提供了一些有用的类，例如 [**ScenarioCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioCollection)、[**Scenario**](https://reference.aspose.com/cells/java/com.aspose.cells/Scenario)、[**ScenarioInputCellCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCellCollection) 和 [**ScenarioInputCell**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCell)。它还提供了 [**Worksheet.Scenarios**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Scenarios) 属性。下面的示例代码打开一个包含一些场景的XLSX Excel文件并从工作表中移除一个现有的场景。然后在保存Excel文件之前添加一个新的场景。它使用了一个非常简单的包含场景的模板文件。

执行代码后，现有场景将被移除，并向工作表添加新的场景。

**输出文件**

![todo:image_alt_text](create-manipulate-or-remove-scenarios-from-worksheets_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateScenariosfromWorksheets-CreateScenariosfromWorksheets.java" >}}
{{< app/cells/assistant language="java" >}}
