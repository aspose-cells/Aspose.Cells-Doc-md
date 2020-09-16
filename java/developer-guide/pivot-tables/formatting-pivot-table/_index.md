---
title: Formatting Pivot Table
type: docs
weight: 60
url: /java/formatting-pivot-table/
---

## **Pivot Table Appearance**

[How to Create a Pivot Table](/cells/java/create-pivot-table/) showed how to create a simple pivot table. This article goes further and discusses how to customize a pivot table's appearance by setting properties.

### **Setting Pivot Table Format Options**

The PivotTable class lets you set various formatting options for a pivot table.

#### **Setting the AutoFormat and PivotTableStyle Types**

The code example that follows illustrates how to set the auto format type and the pivot table style using the AutoFormat and PivotTableStyle properties.

{{< gist "aspose-cells" "87c05ec07dd1a65ac6fcdf2fa896b01e" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetAutoFormatandPivotTableStyleTypes-SetAutoFormatandPivotTableStyleTypes.java" >}}

#### **Setting Format Options**

The code sample that follows illustrates how to set a number of formatting options for a pivot table report, including adding grand totals for rows and columns.

{{< gist "aspose-cells" "87c05ec07dd1a65ac6fcdf2fa896b01e" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingFormatOptions-SettingFormatOptions.java" >}}

### **Setting PivotFields Format Options**

As well as controlling the formatting of the overall pivot table, Aspose.Cells for Java allows fine-tuned control of the formatting for row fields, column fields and page fields.

#### **Setting Row, Column, and Page Fields Format**

The code example that follows shows how to access row fields, access a particular row, set subtotals, apply automatic sorting, and using the autoShow option.

{{< gist "aspose-cells" "87c05ec07dd1a65ac6fcdf2fa896b01e" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SetRowColumnPageFieldsFormat-SetRowColumnPageFieldsFormat.java" >}}

### **Setting Data Fields Format**

The following lines of code illustrate how to format data fields.

{{< gist "aspose-cells" "87c05ec07dd1a65ac6fcdf2fa896b01e" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-SettingDataFieldFormat-SettingDataFieldFormat.java" >}}

### **Modify a Pivot Table's Quick Style**

The code examples that follow show how to modify the quick style applied to a pivot table.

{{< gist "aspose-cells" "87c05ec07dd1a65ac6fcdf2fa896b01e" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ModifyPivotTableQuickStyle-ModifyPivotTableQuickStyle.java" >}}

### **Clearing Pivot Fields**

PivotFieldCollection has a method named clear() that clears pivot fields. Use it to clear pivot fields in all areas for example, page, column, row or data.
The code sample below shows how to clear all the pivot fields in the data area.

{{< gist "aspose-cells" "87c05ec07dd1a65ac6fcdf2fa896b01e" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ClearPivotFields-ClearPivotFields.java" >}}

## **Consolidation Function**

### **Applying ConsolidationFunction to Data Fields of Pivot Table**

Aspose.Cells can be used to apply ConsolidationFunction to data fields (or value fields) of the pivot table. In Microsoft Excel, you can right click the value field and then select **Value Field Settings...** option and then select the tab **Summarize Values By**. From there, you can select any ConsolidationFunction of your choice like Sum, Count, Average, Max, Min, Product, Distinct Count etc.

Aspose.Cells provides ConsolidationFunction enumeration to support the following consolidation functions.

- ConsolidationFunction.AVERAGE
- ConsolidationFunction.COUNT
- ConsolidationFunction.COUNT_NUMS
- ConsolidationFunction.DISTINCT_COUNT
- ConsolidationFunction.MAX
- ConsolidationFunction.MIN
- ConsolidationFunction.PRODUCT
- ConsolidationFunction.STD_DEV
- ConsolidationFunction.STD_DEVP
- ConsolidationFunction.SUM
- ConsolidationFunction.VAR
- ConsolidationFunction.VARP

The following code applies **Average** consolidation function to first data field (or value field) and **DistinctCount** consolidation function to second data field (or value field).

{{% alert color="primary" %}}

DistinctCount consolidation function is supported by Microsoft Excel 2013 only.

{{% /alert %}}

{{< gist "aspose-cells" "87c05ec07dd1a65ac6fcdf2fa896b01e" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-ConsolidationFunctions-ConsolidationFunctions.java" >}}
