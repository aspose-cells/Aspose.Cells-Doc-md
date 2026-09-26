---
title: Create, Manipulate or Remove Scenarios from Worksheets with Golang via C++
linktitle: Manage Scenarios
type: docs
weight: 190
url: /go-cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: In this article, you will learn how to create, manipulate, or remove scenarios from Excel worksheets programmatically using the Go library with Aspose.Cells API.
keywords: create scenario worksheet c++, remove scenario excel worksheet c++, manipulate scenario worksheet c++
---

{{% alert color="primary" %}}

Sometimes, you need to create, manipulate, or delete scenarios in spreadsheets. A scenario is a named “what‑if?” model that includes variable input cells linked by one or more formulas. Before creating a scenario, design the worksheet so that it contains at least one formula that depends on cells into which different values can be inserted. The following example shows how to create and remove scenarios from a worksheet in a workbook via Aspose.Cells APIs.

{{% /alert %}}

Aspose.Cells provides some useful classes, for example, [**ScenarioCollection**](https://reference.aspose.com/cells/go-cpp/scenariocollection/), [**Scenario**](https://reference.aspose.com/cells/go-cpp/scenario/), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/go-cpp/scenarioinputcellcollection/), and [**ScenarioInputCell**](https://reference.aspose.com/cells/go-cpp/scenarioinputcell/) classes. It also provides the [**Worksheet.GetScenarios()**](https://reference.aspose.com/cells/go-cpp/worksheet/getscenarios/) property. The sample code below opens an XLSX Excel file that contains some scenarios and removes an existing scenario. It also adds a new scenario to the worksheet before saving the Excel file. The example uses a very simple template file that contains a scenario.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManageScenarios.go" >}}
{{< app/cells/assistant language="go" >}}
