##Public API Changes in Aspose.Cells 8.1.1
This document describes changes to the Aspose.Cells API from version 8.1.0 to 8.1.1, that may be of interest to module/application developers. It includes not only new and updated public methods, but also a description of any changes in the behavior behind the scenes in Aspose.Cells.
## **Added HtmlSaveOptions.PresentationPreference Property**
The HtmlSaveOptions class has exposed PresentationPreference property which can be used to render the results with better layout when exporting spreadsheets to HTML or MHTML. The default value is false. whereas if set to true, the Aspose.Cells API will export the worksheet contents with better presentation.
Please check the detailed article on [Use PresentationPreference Option for Better Layout](https://docs.aspose.com/cells/net/excel-to-html-use-presentationpreference-option-for-better-layout/)
## **Added Support for Worksheet Scenarios**
A scenario is named what-if model that includes variable input cells linked together by one or more formulas accordingly. Aspose.Cells API has exposed Worksheet.Scenarios property along with the following classes in order to facilitate the users in creating, manipulating and removing scenarios from worksheets,
1. Scenario: Represents an individual scenario.
1. ScenarioCollection: Represents a collection of scenarios.
1. ScenarioInputCellCollection: Represents a list of input-cells for a particular scenario.
1. ScenarioInputCell: Represents an input-cell from the collection of input-cells for a particular scenario.
Please check the detailed article on [How to Create, Manipulate or Remove Scenarios from Worksheets](https://docs.aspose.com/cells/net/create-manipulate-or-remove-scenarios-from-worksheets/).
