---
title: Create, Manipulate or Remove Scenarios from Worksheets
linktitle: Manage Scenarios
type: docs
weight: 190
url: /net/create-manipulate-or-remove-scenarios-from-worksheets/
description: In this article, you will learn how to create, manipulate or remove Scenarios from Excel Worksheets programmatically using C# Library with .NET API.
keywords: create scenario worksheet c#, remove scenario excel worksheet c#, manipulate scenario worksheet c#
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, you need to create, manipulate or delete scenarios in spreadsheets. A scenario is a named 'what if?' model that includes variable input cells linked by one or more formulas. Before creating a scenario, design the worksheet so that it contains at least one formula that depends on cells that different values can be inserted into. The following example shows how to create and remove scenarios from a worksheet in a workbook via Aspose.Cells APIs.

{{% /alert %}}

Aspose.Cells provides some useful classes, for example, [**ScenarioCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenariocollection), [**Scenario**](https://reference.aspose.com/cells/net/aspose.cells/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcellcollection), and [**ScenarioInputCell**](https://reference.aspose.com/cells/net/aspose.cells/scenarioinputcell) classes. It also provides the [**Worksheet.Scenarios**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/scenarios) property. The sample code below opens an XLSX Excel file that contains some scenarios and removes an existing scenario. It also adds a new scenario to the worksheet before saving the Excel file. The example uses a very simple template file that contains a scenario.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateManipulateRemoveScenarios-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
