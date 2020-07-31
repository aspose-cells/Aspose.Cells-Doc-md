---
title : "Create Manipulate or Remove Scenarios from Worksheets" 
description : "" 
weight : 20440 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/mngworkbooksandworksheets/create+manipulate+or+remove+scenarios+from+worksheets/
---

# Aspose.Cells for .NET : Create, Manipulate or Remove Scenarios from Worksheets


Sometimes, you need to create, manipulate or delete scenarios in spreadsheets. A scenario is a named 'what if?' model that includes variable input cells linked by one or more formulas. Before creating a scenario, design the worksheet so that it contains at least one formula that depends on cells that different values can be inserted into. The following example shows how to create and remove scenarios from a worksheet in a workbook via Aspose.Cells APIs.

Aspose.Cells provides some useful classes, for example, [ScenarioCollection](https://apireference.aspose.com/net/cells/aspose.cells/scenariocollection), [Scenario](https://apireference.aspose.com/net/cells/aspose.cells/scenario), [ScenarioInputCellCollection](https://apireference.aspose.com/net/cells/aspose.cells/scenarioinputcellcollection), and [ScenarioInputCell](https://apireference.aspose.com/net/cells/aspose.cells/scenarioinputcell) classes. It also provides the [Worksheet.Scenarios](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/scenarios) property. The sample code below opens an XLSX Excel file that contains some scenarios and removes an existing scenario. It also adds a new scenario to the worksheet before saving the Excel file. The example uses a very simple template file that contains a scenario.

