---
title: 创建、操作或移除工作表中的场景
linktitle: 管理场景
type: docs
weight: 190
url: /zh/net/create-manipulate-or-remove-scenarios-from-worksheets/
description: 在本文中，您将学习如何使用C#库和.NET API以编程方式创建、操作或移除Excel工作表中的方案。
keywords: 创建工作表的方案C#，删除工作表的方案C#，操作工作表的方案C#
---

{{% alert color="primary" %}}

有时，您需要在电子表格中创建、操作或删除方案。方案是一个命名的“假设”模型，其中包含由一个或多个公式链接的可变输入单元格。在创建方案之前，设计工作表，使其至少包含一个依赖于可以插入不同值的单元格的公式。以下示例演示了如何通过Aspose.Cells API在工作簿中的工作表中创建和删除方案。

{{% /alert %}}

Aspose.Cells提供一些有用的类，例如[**ScenarioCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenariocollection)，[**Scenario**](https://reference.aspose.com/cells/net/aspose.cells/scenario)，[**ScenarioInputCellCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcellcollection)和[**ScenarioInputCell**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcell)类。它还提供[**Worksheet.Scenarios**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/scenarios)属性。下面的示例代码打开一个包含一些方案的XLSX Excel文件，然后删除现有的方案。在保存Excel文件之前，它还向工作表添加了一个新的方案。这个示例使用了一个非常简单的包含方案的模板文件。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateManipulateRemoveScenarios-1.cs" >}}
