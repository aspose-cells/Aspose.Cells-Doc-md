##Formatting Pivot Table
## **Pivot Table Appearance**
[How to Create a Pivot Table](https://docs.aspose.com/cells/java/create-pivot-table/) showed how to create a simple pivot table. This article goes further and discusses how to customize a pivot table's appearance by setting properties.
### **Setting Pivot Table Format Options**
The [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) class lets you set various formatting options for a pivot table.
#### **Setting the AutoFormat and PivotTableStyle Types**
The code example that follows illustrates how to set the auto format type and the pivot table style type using the [**AutoFormatType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#AutoFormatType) and [**PivotTableStyleType**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#PivotTableStyleType) properties.
#### **Setting Format Options**
The code sample that follows illustrates how to set a number of formatting options for a pivot table report, including adding grand totals for rows and columns.
### **Setting PivotFields Format Options**
As well as controlling the formatting of the overall pivot table, Aspose.Cells for Java allows fine-tuned control of the formatting for row fields, column fields and page fields.
#### **Setting Row, Column, and Page Fields Format**
The code example that follows shows how to access row fields, access a particular row, set subtotals, apply automatic sorting, and using the autoShow option.
### **Setting Data Fields Format**
The following lines of code illustrate how to format data fields.
### **Modify a Pivot Table's Quick Style**
The code examples that follow show how to modify the quick style applied to a pivot table.
### **Clearing Pivot Fields**
[**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) has a method named [**clear()**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfieldcollection#clear--) that clears pivot fields. Use it to clear pivot fields in all areas for example, page, column, row or data.
The code sample below shows how to clear all the pivot fields in the data area.
## **Consolidation Function**
### **Applying ConsolidationFunction to Data Fields of Pivot Table**
Aspose.Cells can be used to apply ConsolidationFunction to data fields (or value fields) of the pivot table. In Microsoft Excel, you can right click the value field and then select **Value Field Settings...** option and then select the tab **Summarize Values By**. From there, you can select any ConsolidationFunction of your choice like Sum, Count, Average, Max, Min, Product, Distinct Count etc.
Aspose.Cells provides [**ConsolidationFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) enumeration to support the following consolidation functions.
- [**ConsolidationFunction.AVERAGE**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#AVERAGE)
- [**ConsolidationFunction.COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT)
- [**ConsolidationFunction.COUNT_NUMS**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#COUNT-NUMS)
- [**ConsolidationFunction.DISTINCT_COUNT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#DISTINCT-COUNT)
- [**ConsolidationFunction.MAX**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MAX)
- [**ConsolidationFunction.MIN**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#MIN)
- [**ConsolidationFunction.PRODUCT**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#PRODUCT)
- [**ConsolidationFunction.STD_DEV**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD-DEV)
- [**ConsolidationFunction.STD_DEVP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#STD-DEVP)
- [**ConsolidationFunction.SUM**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#SUM)
- [**ConsolidationFunction.VAR**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VAR)
- [**ConsolidationFunction.VARP**](https://reference.aspose.com/cells/java/com.aspose.cells/consolidationfunction#VARP)
The following code applies **Average** consolidation function to first data field (or value field) and **DistinctCount** consolidation function to second data field (or value field).
DistinctCount consolidation function is supported by Microsoft Excel 2013 only.
