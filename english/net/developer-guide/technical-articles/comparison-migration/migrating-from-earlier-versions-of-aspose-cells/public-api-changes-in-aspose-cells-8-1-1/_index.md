---
title: Public API Changes in Aspose.Cells 8.1.1
type: docs
weight: 50
url: /net/public-api-changes-in-aspose-cells-8-1-1/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes changes to the Aspose.Cells API from version 8.1.0 to 8.1.1 that may be of interest to module or application developers. It includes not only new and updated public methods, but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added HtmlSaveOptions.PresentationPreference Property**
The HtmlSaveOptions class has exposed the PresentationPreference property, which can be used to render the results with a better layout when exporting spreadsheets to HTML or MHTML. The default value is false, whereas if set to true, the Aspose.Cells API will export the worksheet contents with better presentation.

{{% alert color="primary" %}} 

Please check the detailed article on [Use PresentationPreference Option for Better Layout](/cells/net/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}}
## **Added Support for Worksheet Scenarios**
A scenario is a named what‑if model that includes variable input cells linked together by one or more formulas accordingly. Aspose.Cells API has exposed Worksheet.Scenarios property along with the following classes in order to facilitate users in creating, manipulating, and removing scenarios from worksheets:

1. Scenario: Represents an individual scenario.  
2. ScenarioCollection: Represents a collection of scenarios.  
3. ScenarioInputCellCollection: Represents a list of input cells for a particular scenario.  
4. ScenarioInputCell: Represents an input cell from the collection of input cells for a particular scenario.

{{% alert color="primary" %}} 

Please check the detailed article on [How to Create, Manipulate or Remove Scenarios from Worksheets](/cells/net/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
