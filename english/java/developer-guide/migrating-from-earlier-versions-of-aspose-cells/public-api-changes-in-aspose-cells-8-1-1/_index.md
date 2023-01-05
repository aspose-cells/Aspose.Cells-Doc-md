---
title: Public API Changes in Aspose.Cells 8.1.1
type: docs
weight: 60
url: /java/public-api-changes-in-aspose-cells-8-1-1/
---

{{% alert color="primary" %}} 

This document describes changes to the Aspose.Cells API from version 8.1.0 to 8.1.1, that may be of interest to module and application developers. It includes not only [new and updated public methods](/cells/java/public-api-changes-in-aspose-cells-8-1-1/), but also a description of any [changes in the behavior](/cells/java/public-api-changes-in-aspose-cells-8-1-1/) behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added Properties and Features**
### **Added the HtmlSaveOptions.PresentationPreference Property**
The HtmlSaveOptions class has exposed getter/setter for PresentationPreference property which can be used to render the results with better layout when exporting spreadsheets to HTML or MHTML. The default value is false. whereas if set to true, the Aspose.Cells API exports the worksheet contents with better presentation.

{{% alert color="primary" %}} 

Please check the detailed article on [Use PresentationPreference Option for Better Layout](/cells/java/excel-to-html-use-presentationpreference-option-for-better-layout/)

{{% /alert %}} 
### **Added Support for Worksheet Scenarios**
A scenario is a what-if model that includes variable input cells linked together by one or more formulas. Aspose.Cells has exposed a getter and setter for the Worksheet.Scenarios property along with the following classes to help developers create, manipulate and remove scenarios.

1. Scenario: Represents an individual scenario.
1. ScenarioCollection: Represents a collection of scenarios.
1. ScenarioInputCellCollection: Represents a list of input cells for a particular scenario.
1. ScenarioInputCell: Represents an input cell from the collection of input-cells for a particular scenario.

{{% alert color="primary" %}} 

Please check the detailed article on [How to Create, Manipulate or Remove Scenarios from Worksheets](/cells/java/create-manipulate-or-remove-scenarios-from-worksheets/).

{{% /alert %}}
## **Change in Behavior for CellsException**
With previous releases of the Aspose.Cells for Java API, when a possibly damaged spreadsheet was loaded in an instance of Workbook, the API tended to throw a generic message without mentioning where the problem could be. We have changed this behavior for 8.1.1 so that the API throws an exception with a meaningful message that points out where (which cell) and what (formula expression) causes the exception when reading the template file.
