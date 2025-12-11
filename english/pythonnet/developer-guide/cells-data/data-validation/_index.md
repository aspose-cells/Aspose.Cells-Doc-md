---
title: Data Validation
type: docs
weight: 90
url: /python-net/data-validation/
description: Learn how to add data validation through the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python Add Data Validation, Python Get Validation Value, Python Add Whole Number Data Validation, Python Add List Data Validation, Python Add Date Data Validation, Python Add Time Data Validation, Python Add Text Length Data Validation, Python Add CellArea to existing Validation, Python Check if validation in cell is dropdown, Add Custom Validation  
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Microsoft Excel provides some good features to auto-filter or validate worksheet data. Aspose.Cells for Python via .NET fully supports Microsoft Excel's data validation and AutoFilter features. This article explains how to use the features in Microsoft Excel, and how to code them using Aspose.Cells for Python via .NET.

{{% /alert %}}

## **Data Validation Types and Execution**

Data validation is the ability to set rules pertaining to data entered on a worksheet. For example, use validation to ensure that a column labeled DATE contains only dates, or that another column contains only numbers. You could even ensure that a column labeled DATE contains only dates within a certain range. With data validation, you can control what is entered into cells in the worksheet.

Microsoft Excel supports a number of different types of data validation. Each type is used to control what type of data is entered into a cell, or cell range. Below, code snippets illustrate how to validate that:

- Numbers are whole, that is, that they don't have a decimal part.
- Decimal numbers follow the right structure. The code example defines that a range of cells should have two decimal places.
- Values are restricted to a list of values. List validation defines a separate list of values that can be applied to a cell, or cell range.
- Dates fall within a specific range.
- A time is within a specific range.
- Text is within a given character length.

### **Data Validation with Microsoft Excel**

To create validations using Microsoft Excel:

1. In a worksheet, select the cells to which you want to apply validation.  
1. From the **Data** menu, select **Validation**. The validation dialog will be displayed.  
1. Click the **Settings** tab and enter settings.

### **Data Validation with Aspose.Cells for Python Excel Library**

Data validation is a powerful feature for validating the information entered into worksheets. With data validation, developers can provide users with a list of choices, restrict data entries to a specific type or size, etc.  
In Aspose.Cells for Python via .NET, each [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class has a [**validations**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/validations/) property which represents a collection of [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation) objects. To set up validation, set some of the [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation) class's properties as follows:

- type – represents the validation type, which may be specified by using one of the predefined values in the [**ValidationType**](https://reference.aspose.com/cells/python-net/aspose.cells/validationtype) enumeration.  
- Operator – represents the operator to be used in the validation, which may be specified by using one of the predefined values in the [**OperatorType**](https://reference.aspose.com/cells/python-net/aspose.cells/operatortype) enumeration.  
- formula1 – represents the value or expression associated with the first part of the data validation.  
- formula2 – represents the value or expression associated with the second part of the data validation.

When the [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation) object's properties have been configured, developers can use the [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) structure to store information about the cell range that will be validated using the created validation.

#### **Types of Data Validation**

The [**ValidationType**](https://reference.aspose.com/cells/python-net/aspose.cells/validationtype) enumeration has the following members:

|**Member Name**|**Description**|
| :- | :- |
|ANY_VALUE|Denotes a value of any type.|
|WHOLE_NUMBER|Denotes validation type for whole numbers.|
|DECIMAL|Denotes validation type for decimal numbers.|
|LIST|Denotes validation type for drop-down list.|
|DATE|Denotes validation type for dates.|
|TIME|Denotes validation type for time.|
|TEXT_LENGTH|Denotes validation type for the length of the text.|
|CUSTOM|Denotes custom validation type.|

##### **Whole Number Data Validation**

With this type of validation, users can enter only whole numbers within a specified range into the validated cells. The code examples that follow show how to implement the WholeNumber validation type. The example creates the same data validation using Aspose.Cells for Python via .NET that we created using Microsoft Excel above.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-WholeNumberDataValidation-1.py" >}}

##### **List Data Validation**

This type of validation allows the user to enter values from a drop-down list. It provides a list: a series of rows that contain data. In the example, a second worksheet is added to hold the list source. Users can only select values from the list. The validation area is the cell range A1:A5 in the first worksheet.

It is important here that you set the [**Validation.in_cell_drop_down**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/in_cell_drop_down/) property to **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-ListDataValidation-1.py" >}}

##### **Date Data Validation**

With this type of validation, users enter date values within a specified range, or meeting specific criteria, into the validated cells. In the example, the user is restricted to enter dates between 1970 and 1999. Here, the validation area is the B1 cell.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DateDataValidation-1.py" >}}

##### **Time Data Validation**

With this type of validation, users can enter times within a specified range, or meeting some criteria, into the validated cells. In the example, the user is restricted to enter times between 09:00 and 11:30 AM. Here, the validation area is the B1 cell.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-TimeDataValidation-1.py" >}}

##### **Text Length Data Validation**

With this type of validation, users can enter text values of a specified length into the validated cells. In the example, the user is restricted to enter string values with no more than 5 characters. The validation area is the B1 cell.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-TextLengthDataValidation-1.py" >}}

### **Data Validation Rules**

When data validations are implemented, validation can be checked by assigning different values to the cells. [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) can be used to fetch the validation result. The following example demonstrates this feature with different values. The sample file can be downloaded from the following link for testing:

[sampleDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DataValidationRules-1.py" >}}

## **Check if validation in a cell is a dropdown**

As we have seen, there are many types of validations that can be implemented on a cell. If you want to check whether validation is a dropdown or not, [**Validation.in_cell_drop_down**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/in_cell_drop_down/) property can be used to test this. The following sample code demonstrates the usage of this property. A sample file for testing can be downloaded from the following link:

[sampleValidation.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-CheckIfValidationInCellDropDown-1.py" >}}

## **Add CellArea to existing Validation**

There might be cases where you might want to add [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) to existing [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation). When you add [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) using [**Validation.add_area(cell_area)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea), Aspose.Cells checks all existing areas to see if the new area already exists. If the file has a large number of validations, this takes a performance hit. To overcome this, the API provides the [**Validation.add_area(cell_area, check_intersection, check_edge)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea-bool-bool) method. The *checkIntersection* parameter indicates whether to check the intersection of a given area with existing validation areas. Setting it to **false** will disable the checking of other areas. The *checkEdge* parameter indicates whether to check the applied areas. If the new area becomes the top-left area, internal settings are rebuilt. If you are sure that the new area is not the top-left area, you may set this parameter to **false**.

The following code snippet demonstrates the use of the [**Validation.add_area(cell_area, check_intersection, check_edge)**](https://reference.aspose.com/cells/python-net/aspose.cells/validation/add_area/#aspose.cells.CellArea-bool-bool) method to add new [**CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea) to existing [**Validation**](https://reference.aspose.com/cells/python-net/aspose.cells/validation).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AddValidationArea-1.py" >}}

The source and output excel files are attached for reference.

[Source File](96928093.xlsx)

[Output File](96928220.xlsx)


## **Advanced topics**
- [Get Cell Validation in ODS Files](/cells/python-net/get-cell-validation-in-ods-files/)
- [Get Validation Applied on a Cell](/cells/python-net/get-validation-applied-on-a-cell/)
- [Verify that Cell Value Satisfies Data Validation Rules](/cells/python-net/verify-that-cell-value-satisfies-data-validation-rules/)
{{< app/cells/assistant language="python-net" >}}
