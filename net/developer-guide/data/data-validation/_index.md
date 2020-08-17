---
title: Data Validation
type: docs
weight: 90
url: /net/data-validation/
---

{{% alert color="primary" %}} 

Microsoft Excel provides some good features to auto filter or validate worksheet data.Aspose.Cells fully supports Microsoft Excel's data validation and AutoFilter features. This article explains how to use the features in Microsoft Excel, and how to code them using Aspose.Cells.

{{% /alert %}} 
## **Data Validation Types and Execution**
Data validation is the ability to set rules pertaining to data entered on a worksheet. For example, use validation to ensure that a column labeled DATE contains only dates, or that another column contains only numbers. You could even ensure that a column labeled DATE contains only dates within a certain range. With data validation, you can control what is entered into cells in the worksheet.

Microsoft Excel supports a number of different types of data validation. Each type is used to control what type of data is entered into a cell, or cell range. Below, code snippets illustrate how to validate that:

- Numbers are whole, that is, that they don't have a decimal part.
- Decimal numbers follow the right structure. The code example defines that a range of cells should have two decimal spaces.
- Values are restricted to a list of values. List validation defines a separate list of values that can be applied to a cell, or cell range.
- Dates fall within a specific range.
- A time is within a specific range.
- A text is within a given character length.
### **Data Validation with Microsoft Excel**
To create validations using Microsoft Excel:

1. In a worksheet, select the cells to which you want to apply validation.
1. From the **Data** menu, select **Validation**. The validation dialog will be displayed.
1. Click the **Settings** tab and enter settings.
### **Data Validation with Aspose.Cells**
Data validation is a powerful feature for validating the information entered into worksheets. With data validation, developers can provide users with a list of choices, restrict data entries to a specific type or size, etc.
In Aspose.Cells, each [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) class has a [Validations](https://apireference.aspose.com/net/cells/aspose.cells/worksheet/properties/validations) property which represents a collection of [Validation](https://apireference.aspose.com/net/cells/aspose.cells/validation) objects. To set up validation, set some of the [Validation](https://apireference.aspose.com/net/cells/aspose.cells/validation) class' properties as follows:

- Type – represents the validation type, which may be specified by using one of the predefined values in the [ValidationType](https://apireference.aspose.com/net/cells/aspose.cells/validationtype) enumeration.
- Operator – represents the operator to be used in the validation, which may be specified by using one of the predefined values in the [OperatorType](https://apireference.aspose.com/net/cells/aspose.cells/operatortype) enumeration.
- Formula1 – represents the value or expression associated with the first part of the data validation.
- Formula2 – represents the value or expression associated with the second part of the data validation.

When the [Validation](https://apireference.aspose.com/net/cells/aspose.cells/validation) object's properties have been configured, developers can use the [CellArea](https://apireference.aspose.com/net/cells/aspose.cells/cellarea) structure to store information about the cell range that will be validated using the created validation.
#### **Types of Data Validation**
The [ValidationType](https://apireference.aspose.com/net/cells/aspose.cells/validationtype) enumeration has the following members:

|**Member Name**|**Description**|
| :- | :- |
|AnyValue|Denotes a value of any type.|
|WholeNumber|Denotes validation type for whole numbers.|
|Decimal|Denotes validation type for decimal numbers.|
|List|Denotes validation type for drop-down list.|
|Date|Denotes validation type for dates.|
|Time|Denotes validation type for time.|
|TextLength|Denotes validation type for the length of the text.|
|Custom|Denotes custom validation type.|
##### **Whole Number Data Validation**
With this type of validation, users can enter only whole numbers within a specified range into the validated cells. The code examples that follow show how to implement the WholeNumber validation type. The example creates the same data validation using Aspose.Cells that we created using Microsoft Excel above.



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Data-Processing-FilteringAndValidation-WholeNumberDataValidation-1.cs" >}}
##### **List Data Validation**
This type of validation allows the user to enter values from a drop-down list. It provides a list: a series of rows that contain data. In the example, a second worksheet is added to hold the list source. Users can only select values from the list. The validation area is the cell range A1:A5 in the first worksheet.

It is important here that you set the [Validation.InCellDropDown](https://apireference.aspose.com/net/cells/aspose.cells/validation/properties/incelldropdown) property to **true**.



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Data-Processing-FilteringAndValidation-ListDataValidation-1.cs" >}}
##### **Date Data Validation**
With this type of validation, users enter date values within a specified range, or meeting specific criteria, into the validated cells. In the example, the user is restricted to enter dates between 1970 to 1999. Here, the validation area is the B1 cell.



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Data-Processing-FilteringAndValidation-DateDataValidation-1.cs" >}}
##### **Time Data Validation**
With this type of validation, users can enter times within a specified range, or meeting some criteria, into the validated cells. In the example, the user is restricted to enter times between 09:00 to 11:30 AM. Here, the validation area is the B1 cell.



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Data-Processing-FilteringAndValidation-TimeDataValidation-1.cs" >}}
##### **Text Length Data Validation**
With this type of validation, users can enter text values of a specified length into the validated cells. In the example, the user is restricted to enter string values with no more than 5 characters. The validation area is the B1 cell.



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Data-Processing-FilteringAndValidation-TextLengthDataValidation-1.cs" >}}
### **Data Validation Rules**
When data validations are implemented, then validation can be checked by assigning different values in the cells. [Cell.GetValidationValue](https://apireference.aspose.com/net/cells/aspose.cells/cell/methods/getvalidationvalue) can be used to fetch the validation result. The following example demonstrates this feature with different values. The sample file can be downloaded from the following link for testing:

[sampleDataValidationRules.xlsx](77496339.xlsx)



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
## **Check if validation in cell is dropdown**
As we have seen there are many types of validations that can be implemented within a cell. If you want to check whether validation is dropdown or not, [Validation.InCellDropDown](https://apireference.aspose.com/net/cells/aspose.cells/validation/properties/incelldropdown) property can be used to test this. The following sample code demonstrates the usage of this property. A sample file for testing can be downloaded from the following link:

[sampleValidation.xlsx](79527947.xlsx)



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-CheckIfValidationInCellDropDown-1.cs" >}}
## **Add CellArea to existing Validation**
There might be cases where you might want to add [CellArea](https://apireference.aspose.com/net/cells/aspose.cells/cellarea) to existing [Validation](https://apireference.aspose.com/net/cells/aspose.cells/validation). When you add [CellArea](https://apireference.aspose.com/net/cells/aspose.cells/cellarea) using [Validation.AddArea(CellArea cellArea)](https://apireference.aspose.com/net/cells/aspose.cells/validation/methods/addarea), Aspose.Cells checks all existing areas to see if the new area already exists. If the file has a large number of validations, this takes a performance hit. To overcome this, the API provides the [Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://apireference.aspose.com/net/cells/aspose.cells.validation/addarea/methods/1) method. The *checkIntersection* parameter indicates whether to check the intersection of a given area with existing validation areas. Setting it to **false** will disable the checking of other areas. The *checkEdge* parameter indicates whether to check the applied areas. If the new area becomes the top-left area, internal settings are rebuilt. If you are sure that the new area is not the top-left area, you may set this parameter as **false**.

The following code snippet demonstrates the use of the [Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://apireference.aspose.com/net/cells/aspose.cells.validation/addarea/methods/1) method to add new [CellArea](https://apireference.aspose.com/net/cells/aspose.cells/cellarea) to existing [Validation](https://apireference.aspose.com/net/cells/aspose.cells/validation).



{{< gist "aspose-com-gists" "922f990b02cf4e04a328bd6f37029af8" "Examples-CSharp-Data-AddValidationArea-1.cs" >}}

The source and output excel files are attached for reference.

[Source File](attachments/96764769/96928093.xlsx)

[Output File](96928220.xlsx)
