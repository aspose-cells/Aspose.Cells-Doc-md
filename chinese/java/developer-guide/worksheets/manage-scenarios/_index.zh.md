---
title: 创建、操作或从工作表中移除场景
linktitle: 管理方案
type: docs
weight: 120
url: /zh/java/create-manipulate-or-remove-scenarios-from-worksheets/
---

{{% alert color="primary" %}}

有时，您需要在电子表格中创建、操作或删除方案。方案是一种名为“假设”的模型，其中包括由一个或多个公式链接在一起的变量输入单元格。在创建方案之前，请设计一个工作表，以便其中包含至少一种取决于不同值的单元格的公式。以下示例显示了如何使用Aspose.Cells API在工作表中创建和删除方案。

{{% /alert %}}

Aspose.Cells提供一些有用的类，例如[**ScenarioCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioCollection)，[**Scenario**](https://reference.aspose.com/cells/java/com.aspose.cells/Scenario)，[**ScenarioInputCellCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCellCollection)和[**ScenarioInputCell**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCell)，还提供[**Worksheet.Scenarios**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Scenarios)属性。下面的示例代码打开了一个包含一些方案的XLSX Excel文件（其中包含一些方案），并从工作表中删除了一个现有的方案。在保存Excel文件之前，它添加了一个新方案。它使用一个非常简单的包含方案的模板文件。

执行代码后，一个现有的方案将被删除，并且一个新方案将被添加到工作表中。

**输出文件**

![todo:image_alt_text](create-manipulate-or-remove-scenarios-from-worksheets_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateScenariosfromWorksheets-CreateScenariosfromWorksheets.java" >}}
