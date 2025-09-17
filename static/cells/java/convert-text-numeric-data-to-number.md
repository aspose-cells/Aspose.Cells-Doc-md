##Convert Text Numeric Data to Number
Learn how to convert numbers stored as text to numbers by using the Aspose.Cells for Java API.
## **Possible Usage Scenarios**
Sometimes, you want to convert numeric data entered as text to numbers. You can enter numbers as text in Microsoft Excel by putting an apostrophe before a number, for example **'12345**. Excel then treats the number as a string. Aspose.Cells allows you to convert strings to numbers.
## Convert numbers stored as text to numbers in Excel
You can convert numbers stored as text to numbers by following a few simple steps.
1. Select any single cell or range of cells that has an error indicator in the upper-left corner.
1. Next to the selected cell or range of cells, click the error button that appears. On the menu, click Convert to Number.
1. If the alert button is not available, Select a column with this problem. If you don't want to convert the whole column, you can select one or more cells instead. Just be sure the cells you select are in the same column, otherwise this process won't work. The Text to Columns button is typically used for splitting a column, but it can also be used to convert a single column of text to numbers. On the Data tab, click Text to Columns.
1. Click the Finish button in the pop-up box.
1. The numbers stored as text are transformed into numbers.
## Convert numbers stored as text to numbers using Aspose.Cells for JAVA
Aspose.Cells for Java API provides the [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue--) method which can be used to convert all string or text numeric data into numbers.
The following screenshot shows string numbers in cells **A1:A17**. String numbers are aligned to the left.
These string numbers have been converted to numbers using [**Cells.convertStringToNumericValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#convertStringToNumericValue--) in the following screenshot. As you can see, they are now right-aligned.
## Java code to convert string numeric data to actual numbers
The following sample code illustrates how to convert all string numeric data to actual numbers in all worksheets.
