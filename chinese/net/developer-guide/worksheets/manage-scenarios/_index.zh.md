---
title: 创建、操作或从工作表中移除场景
linktitle: 管理方案
type: docs
weight: 190
url: /zh/net/create-manipulate-or-remove-scenarios-from-worksheets/
description: 在本文中，您将学习如何使用C#库和.NET API以编程方式创建、操作或从Excel工作表中删除场景
keywords: 创建场景工作表c#，删除场景Excel工作表c#，操作场景工作表c#
---

{{% alert color="primary" %}}

 有时需要在电子表格中创建、操作或删除场景。场景是一个命名的'假设'模型，其中包括由一个或多个公式链接的可变输入单元格。在创建场景之前，设计工作表使其至少包含一个依赖于可以插入不同值的单元格的公式。以下示例展示了如何通过Aspose.Cells API在工作簿中的工作表中创建和移除场景。

{{% /alert %}}

Aspose.Cells提供了一些有用的类，例如[**ScenarioCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenariocollection)、[**Scenario**](https://reference.aspose.com/cells/net/aspose.cells/scenario)、[**ScenarioInputCellCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcellcollection)和[**ScenarioInputCell**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcell)类。还提供[**Worksheet.Scenarios**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/scenarios)属性。下面的示例代码打开了一个包含一些场景并移除现有场景的XLSX Excel文件。在保存Excel文件之前，它还向工作表添加了一个新场景。该示例使用了一个非常简单的模板文件，其中包含一个场景。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateManipulateRemoveScenarios-1.cs" >}}
