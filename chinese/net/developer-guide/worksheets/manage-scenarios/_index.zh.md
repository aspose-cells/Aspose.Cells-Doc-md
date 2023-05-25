---
title: 从工作表中创建、操作或删除场景
linktitle: 管理场景
type: docs
weight: 190
url: /zh/net/create-manipulate-or-remove-scenarios-from-worksheets/
description: 在本文中，您将学习如何使用 C# 库和 .NET API 以编程方式从 Excel 工作表中创建、操作或删除场景。
keywords: create scenario worksheet c#, remove scenario excel worksheet c#, manipulate scenario worksheet c#
---
{{% alert color="primary" %}}

有时，您需要在电子表格中创建、操作或删除方案。一个场景是一个命名为“如果？”包含由一个或多个公式链接的可变输入单元格的模型。在创建方案之前，设计工作表，使其至少包含一个公式，该公式取决于可以插入不同值的单元格。以下示例显示如何通过 Aspose.Cells API 在工作簿的工作表中创建和删除方案。

{{% /alert %}}

Aspose.Cells提供了一些有用的类，例如，[**场景集**](https://reference.aspose.com/cells/net/aspose.cells/scenariocollection), [**设想**](https://reference.aspose.com/cells/net/aspose.cells/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcellcollection) ， 和[**场景输入单元格**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcell)类。它还提供了[**工作表.场景**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/scenarios)财产。下面的示例代码打开一个 XLSX Excel 文件，其中包含一些方案并删除现有方案。它还会在保存 Excel 文件之前向工作表添加一个新方案。该示例使用一个非常简单的模板文件，其中包含一个场景。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateManipulateRemoveScenarios-1.cs" >}}
