---
title: Public API Changes in Aspose.Cells 8.2.1
type: docs
weight: 90
url: /java/public-api-changes-in-aspose-cells-8-2-1/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes changes to the Aspose.Cells API from version 8.2.0 to 8.2.1 that may be of interest to module/application developers. It includes not only new and updated public methods, but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added getValidation() method for Cell Class**
Data validation is one of the features that spreadsheet designers use to stop users from inserting invalid values into a particular cell. With Aspose.Cells for Java 8.2.1, the API has exposed a simple mechanism that identifies whether data validation has been applied to a cell. Use the getValidation method of the Cell class to acquire any applied validation. If there is no validation, the method returns null. Similarly, you may use the getValidationInCell method of the ValidationCollection class to acquire the validation applied to any cell by providing its row and column indices.

{{% alert color="primary" %}} 

Please check the detailed article on [Get Validation Applied on a Cell](https://docs.aspose.com/cells/java/get-validation-applied-on-a-cell/) for more information.

{{% /alert %}}
## **Added getValidationValue() method for Cell class**
In addition to determining whether validation has been applied, you can also verify if a given value satisfies the data validation rules for a particular cell. This feature is useful in scenarios where you want to verify if the value entered in the cell satisfies the data validation rules on the fly. The Aspose.Cells API has exposed the getValidationValue method for the Cell class. If the value entered in a cell does not satisfy the data validation rules, the getValidationValue method for the Cell class returns false.

{{% alert color="primary" %}} 

Please check the detailed article on [Verify that Cell Value Satisfies Data Validation Rules](/cells/java/verify-that-cell-value-satisfies-data-validation-rules/).

{{% /alert %}}
## **Added overload toPrinter(PrinterSettings printerSettings) method for WorkbookRender class**
You can use the overloaded method to render a workbook to a printer via PrinterSettings.
{{< app/cells/assistant language="java" >}}
