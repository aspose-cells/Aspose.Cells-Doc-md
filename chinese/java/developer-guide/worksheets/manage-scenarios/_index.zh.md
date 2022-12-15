---
title: 从工作表中创建、操作或删除场景
linktitle: 管理场景
type: docs
weight: 120
url: /zh/java/create-manipulate-or-remove-scenarios-from-worksheets/
---
{{% alert color="primary" %}}

有时，您需要在电子表格中创建、操作或删除方案。场景是一个命名的假设模型，其中包括通过一个或多个公式链接在一起的变量输入单元格。在创建方案之前，设计一个工作表，使其至少包含一个公式，该公式取决于可以插入不同值的单元格。以下示例显示如何使用 Aspose.Cells API 在工作表中创建和删除方案。

{{% /alert %}}

 Aspose.Cells提供了一些有用的类，例如[**场景集**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioCollection), [**设想**](https://reference.aspose.com/cells/java/com.aspose.cells/Scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCellCollection)和[**场景输入单元格**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCell).它还提供了[**工作表.场景**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Scenarios)财产。下面的示例代码打开一个 XLSX Excel 文件（包含一些场景）并从工作表中删除一个现有场景。它还在保存 Excel 文件之前添加了一个新场景。它使用一个包含场景的非常简单的模板文件。

执行代码后，现有方案将被删除，新方案将添加到工作表中。

**输出文件**

![待办事项：图像_替代_文本](create-manipulate-or-remove-scenarios-from-worksheets_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateScenariosfromWorksheets-CreateScenariosfromWorksheets.java" >}}
