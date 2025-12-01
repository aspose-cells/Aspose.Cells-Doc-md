---
title: Create, Manipulate or Remove Scenarios from Worksheets
linktitle: Manage Scenarios
type: docs
weight: 120
url: /java/create-manipulate-or-remove-scenarios-from-worksheets/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, you need to create, manipulate or delete scenarios in spreadsheets. A scenario is a named what-if model that includes variable input cells linked together by one or more formulas. Before creating a scenario, design a worksheet so that it contains at least one formula that depends on cells into which different values can be inserted. The following example shows how to create and remove scenarios from a worksheet using the Aspose.Cells APIs.

{{% /alert %}}

Aspose.Cells provides some useful classes, for example [**ScenarioCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioCollection), [**Scenario**](https://reference.aspose.com/cells/java/com.aspose.cells/Scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCellCollection) and [**ScenarioInputCell**](https://reference.aspose.com/cells/java/com.aspose.cells/ScenarioInputCell). It also provides the [**Worksheet.Scenarios**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Scenarios) property. The sample code below opens an XLSX Excel file (that contains some scenarios) and removes an existing scenario from the worksheet. It also adds a new scenario before saving the Excel file. It uses a very simple template file that contains a scenario.

After executing the code, an existing scenario is removed and a new scenario is added to the worksheet.

**The output file**

![todo:image_alt_text](create-manipulate-or-remove-scenarios-from-worksheets_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateScenariosfromWorksheets-CreateScenariosfromWorksheets.java" >}}
{{< app/cells/assistant language="java" >}}
