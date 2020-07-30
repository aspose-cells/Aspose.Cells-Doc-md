---
title : "Public API Changes in Aspose.Cells 8.2.1" 
description : "" 
weight : 16755 
toc : false
type: docs
url: /net/developerguide/knowledgebase/migratingfromearliervs/public+api+changes+in+aspose.cells+8.2.1/
---

# Aspose.Cells for .NET : Public API Changes in Aspose.Cells 8.2.1


This document describes changes to the Aspose.Cells API from version 8.2.0 to 8.2.1, that may be of interest to module/application developers. It includes not only new and updated public methods, but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

### Added GetValidation() method for Cell Class

Data validation is one of the features that spreadsheet designers use to stop users from inserting invalid values into a particular cell. With Aspose.Cells for .NET 8.2.1, the API has exposed a simple mechanism that identifies if data validation has been applied on a cell. Use the `GetValidation` method of the `Cell` class to acquire any applied validation. If there is no validation, the method returns null. Similarly, you may use the `GetValidationInCell` method of `ValidationCollection` class to acquire the validation applied on any cell by providing its row and column indices.

Please check the detailed article on [Get Validation Applied on a Cell](http://www.aspose.com/docs/display/cellsnet/Get+Validation+applied+on+a+Cell) for more information.

### Added GetValidationValue() method for Cell class

In addition to determining whether validation has been applied, you can also verify if a given value satisfies the data validation rules for a particular cell. This feature is useful in scenarios when you want to verify if the value entered in the cell satisfies the data validation rules on the fly. The Aspose.Cells API has exposed the `GetValidationValue` method for the `Cell` class. If the value entered in a cell does not satisfy the data validation rules, the `GetValidationValue` method for the `Cell` class returns false.

Please check the detailed article on [Verify that Cell Value Satisfies Data Validation Rules](http://www.aspose.com/docs/display/cellsnet/Verify+that+Cell+Value+satisfies+Data+Validation+Rules).

### Added overload ToPrinter(PrinterSettings printerSettings) method for WorkbookRender class

You can use the overloaded method to render workbook to Printer via `PrinterSettings`.

