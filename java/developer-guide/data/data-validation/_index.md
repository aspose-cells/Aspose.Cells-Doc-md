---
title: Data Validation
type: docs
weight: 70
url: /java/data-validation/
---

{{% alert color="primary" %}} 

Microsoft Excel provides some good features to auto-filter or validate worksheet data.

[Data validation](/cells/java/data-validation-html/) is the ability to set rules pertaining to data entered on a worksheet. For example, use validation to ensure that a column labeled DATE contains only dates, or that another column contains only numbers. You could even ensure that a column labeled DATE contains only dates within a certain range. With data validation, you can control what is entered into cells in the worksheet. Aspose.Cells fully supports Microsoft Excel's data validation and autofilter features. This article explains how to use the features in Microsoft Excel, and how to code them using Aspose.Cells.

{{% /alert %}} 
### **Data Validation Types and Execution**
Microsoft Excel supports a number of different types of data validation. Each type is used to control what type of data is entered into a cell, or cell range. Below, code snippets illustrate how to validate that:

- [Numbers are whole](/cells/java/data-validation-html/), that is, that they don't have a decimal part.
- [Decimal numbers follow the right structure](/cells/java/data-validation-html/). The code example defines that a range of cells should have two decimal spaces.
- [Values are restricted to a list of values](/cells/java/data-validation-html/). List validation defines a separate list of values that can be applied to a cell, or cell range.
- [Dates fall within a specific range](/cells/java/data-validation-html/).
- [Time is within a specific range](/cells/java/data-validation-html/).
- [A text is within a given character length](/cells/java/data-validation-html/).
#### **Data Validation with Microsoft Excel**
To create validations using Microsoft Excel:

1. In a worksheet, select the cells to which you want to apply validation.
1. From the **Data** menu, select **Validation**.
   The validation dialog is displayed.
1. Click the **Settings** tab and enter settings as shown below. 

   **Data validation settings** 

![todo:image_alt_text](data-validation_1.png)
#### **Data Validation with Aspose.Cells**
Data validation is a powerful feature for validating the information entered into worksheets. With data validation, developers can provide users with a list of choices, restrict data entries to a specific type or size, etc.
In Aspose.Cells, each [Worksheet](http://www.aspose.com/api/java/cells/com.aspose.cells/classes/Worksheet) class has a [Validations](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#Validations) object which represents a collection of [Validation](https://apireference.aspose.com/java/cells/com.aspose.cells/Validation) objects. To set up validation, set some of the [Validation](https://apireference.aspose.com/java/cells/com.aspose.cells/Validation) class' properties:

- [Type](https://apireference.aspose.com/java/cells/com.aspose.cells/validation#Type): represents the validation type, which may be specified by using one of the predefined values in the [ValidationType](https://apireference.aspose.com/java/cells/com.aspose.cells/ValidationType) enumeration.
- [Operator](https://apireference.aspose.com/java/cells/com.aspose.cells/validation#Operator): represents the operator to be used in the validation, which may be specified by using one of the predefined values in the [OperatorType](https://apireference.aspose.com/java/cells/com.aspose.cells/OperatorType) enumeration.
- [Formula1](https://apireference.aspose.com/java/cells/com.aspose.cells/validation#Formula1): represents the value or expression associated with the first part of the data validation.
- [Formula2](https://apireference.aspose.com/java/cells/com.aspose.cells/validation#Formula2): represents the value or expression associated with the second part of the data validation.

When the [Validation](https://apireference.aspose.com/java/cells/com.aspose.cells/Validation) object's properties have been configured, developers can use the [CellArea](https://apireference.aspose.com/java/cells/com.aspose.cells/CellArea) structure to store information about the cell range that will be validated using the created validation.
##### **Types of Data Validation**
Data validation allows you to build business rules into each cell so that incorrect entries result in error messages. Business rules are the policies and procedures that govern how a business operates. Aspose.Cells supports all the important types of data validation.

The [ValidationType](https://apireference.aspose.com/java/cells/com.aspose.cells/ValidationType) enumeration has the following members:

|**Member Name**|**Description**|
| :- | :- |
|[ANY_VALUE](https://apireference.aspose.com/java/cells/com.aspose.cells/validationtype#ANY_VALUE)|Denotes a value of any type.|
|[WHOLE_NUMBER](https://apireference.aspose.com/java/cells/com.aspose.cells/validationtype#WHOLE_NUMBER)|Denotes validation type for whole numbers.|
|[DECIMAL](https://apireference.aspose.com/java/cells/com.aspose.cells/validationtype#DECIMAL)|Denotes validation type for decimal numbers.|
|[LIST](https://apireference.aspose.com/java/cells/com.aspose.cells/validationtype#LIST)|Denotes validation type for drop-down list.|
|[DATE](https://apireference.aspose.com/java/cells/com.aspose.cells/validationtype#DATE)|Denotes validation type for dates.|
|[TIME](https://apireference.aspose.com/java/cells/com.aspose.cells/validationtype#TIME)|Denotes validation type for Time.|
|[TEXT_LENGTH](https://apireference.aspose.com/java/cells/com.aspose.cells/validationtype#TEXT_LENGTH)|Denotes validation type for the length of the text.|
|[CUSTOM](https://apireference.aspose.com/java/cells/com.aspose.cells/validationtype#CUSTOM)|Denotes custom validation type.|
##### **Programming Sample: Whole Number Data Validation**
With this type of validation, users can enter only whole numbers within a specified range into the validated cells. The code examples that follow show how to implement the [WHOLE_NUMBER](https://apireference.aspose.com/java/cells/com.aspose.cells/validationtype#WHOLE_NUMBER) validation type. The example creates the same data validation using Aspose.Cells that we created using Microsoft Excel above.

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-data-WholeNumberDataValidation-WholeNumberDataValidation.java" >}}



##### **Programming Sample: Decimal Data Validation**
With this type of validation, the user can enter decimal numbers into the validated cells. In the example, the user is restricted to enter decimal value only and the validation area is A1:A10.

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-data-DecimalDataValidation-DecimalDataValidation.java" >}}



##### **Programming Sample: List Data Validation**
This type of validation allows the user to enter values from a drop-down list. It provides a list: a series of rows that contain data. Users can only select values from the list. The validation area is the cell range A1:A5 in the first worksheet.

It is important here that you set the [Validation.setInCellDropDown](https://apireference.aspose.com/java/cells/com.aspose.cells/validation#InCellDropDown) property to **true**.

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-data-ListDataValidation-ListDataValidation.java" >}}



##### **Programming Sample: Date Data Validation**
With this type of validation, users enter date values within a specified range, or meeting specific criteria, into the validated cells. In the example, the user is restricted to enter dates between 1970 to 1999. Here, the validation area is the B1 cell.

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-data-DateDataValidation-DateDataValidation.java" >}}



##### **Programming Samples: Time Data Validation**
With this type of validation, users can enter times within a specified range, or meeting some criteria, into the validated cells. In the example, the user is restricted to enter times between 09:00 to 11:30 AM. Here, the validation area is the B1 cell.

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-data-TimeDataValidation-TimeDataValidation.java" >}}



##### **Programming Samples: Text Length Data Validation**
With this type of validation, users can enter text values of a specified length into the validated cells. In the example, the user is restricted to enter string values with no more than 5 characters. The validation area is the B1 cell.

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-data-TextLengthDataValidation-TextLengthDataValidation.java" >}}
### **Data Validation Rules**
When data validations are implemented, then validation can be checked by assigning different values in the cells. [Cell.GetValidationValue()](https://apireference.aspose.com/java/cells/com.aspose.cells/cell#getValidationValue\(\)) can be used to fetch the validation result. The following example demonstrates this feature with different values. The sample file can be downloaded from the following link for testing:

[SampleDataValidationRules.xlsx](attachments/5276732/77987849.xlsx)

**Sample Code**

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-AsposeCellsExamples-TechnicalArticles-VerifyCellValueSatisfiesDataValidationRules-1.java" >}}
### **Check if validation in a cell is dropdown**
As we have seen there are many types of validations that can be implemented within a cell. If you want to check whether validation is dropdown or not, [Validation.InCellDropDown](https://apireference.aspose.com/java/cells/com.aspose.cells/validation#InCellDropDown) property can be used to test this. Following sample code demonstrates the usage of this property. The sample file for testing can be downloaded from the following link:

[sampleDataValidationRules.xlsx](attachments/5276732/77987849.xlsx)

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-AsposeCellsExamples-Data-CheckIfValidationInCellDropDown-1.java" >}}
### **Add CellArea to existing Validation**
There might be cases where you might want to add [CellArea](https://apireference.aspose.com/java/cells/com.aspose.cells/CellArea) to existing [Validation](https://apireference.aspose.com/java/cells/com.aspose.cells/Validation). When you add [CellArea](https://apireference.aspose.com/java/cells/com.aspose.cells/CellArea) using [Validation.AddArea(CellArea cellArea)](https://apireference.aspose.com/java/cells/com.aspose.cells/validation#addArea\(com.aspose.cells.CellArea\)), Aspose.Cells checks all existing areas to see if the new area already exists. If the file has a large number of validations, this takes a performance hit. To overcome this, the API provides the [Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://apireference.aspose.com/java/cells/com.aspose.cells/validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)) method. The *checkIntersection* parameter indicates whether to check the intersection of a given area with existing validation areas. Setting it to **false** will disable the checking of other areas. The *checkEdge* parameter indicates whether to check the applied areas. If the new area becomes the top-left area, internal settings are rebuilt. If you are sure that the new area is not the top-left area, you may set this parameter as **false**.

The following code snippet demonstrates the use of the [Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://apireference.aspose.com/java/cells/com.aspose.cells/validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)) method to add new [CellArea](https://apireference.aspose.com/java/cells/com.aspose.cells/CellArea) to existing [Validation](https://apireference.aspose.com/java/cells/com.aspose.cells/Validation).



{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-AsposeCellsExamples-Data-AddValidationArea-1.java" >}}

The source and output excel files are attached for reference.

[Source File](https://docs.aspose.com/download/attachments/96764769/PivotTableHideAndSortSample.xlsx?version=1&modificationDate=1575563265610&api=v2)

[Output File](https://docs.aspose.com/download/attachments/5025054/ValidationsSample_out.xlsx?version=1&modificationDate=1575568801067&api=v2)
