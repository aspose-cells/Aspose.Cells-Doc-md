+++
title = "Formatting Pivot Table" 
description = "" 
weight = 12245 
+++

Aspose.Cells for Java : Formatting Pivot Table  

# Aspose.Cells for Java : Formatting Pivot Table



{{< panel title="Contents Summary" style="primary" >}}
*   1 [Pivot Table Appearance](#FormattingPivotTable-PivotTableAppearance)
    *   1.1 [Setting Pivot Table Format Options](#FormattingPivotTable-SettingPivotTableFormatOptions)
        *   1.1.1 [Setting the AutoFormat and PivotTableStyle Types](#FormattingPivotTable-SettingtheAutoFormatandPivotTableStyleTypes)
        *   1.1.2 [Setting Format Options](#FormattingPivotTable-SettingFormatOptions)
    *   1.2 [Setting PivotFields Format Options](#FormattingPivotTable-SettingPivotFieldsFormatOptions)
        *   1.2.1 [Setting Row, Column, and Page Fields Format](#FormattingPivotTable-SettingRow,Column,andPageFieldsFormat)
    *   1.3 [Setting Data Fields Format](#FormattingPivotTable-SettingDataFieldsFormat)
    *   1.4 [Modify a Pivot Table's Quick Style](#FormattingPivotTable-ModifyaPivotTable'sQuickStyle)
    *   1.5 [Clearing Pivot Fields](#FormattingPivotTable-ClearingPivotFields)
*   2 [Consolidation Function](#FormattingPivotTable-ConsolidationFunction)
    *   2.1 [Applying ConsolidationFunction to Data Fields of Pivot Table](#FormattingPivotTable-ApplyingConsolidationFunctiontoDataFieldsofPivotTable)
{{< /panel >}}
 

 

## Pivot Table Appearance

[How to Create a Pivot Table](/pages/createpage.action?spaceKey=cellsjava&title=How+to+Create+a+Pivot+Table&linkCreation=true&fromPageId=5275912) showed how to create a simple pivot table. This article goes further and discusses how to customize a pivot table's appearance by setting properties.

### Setting Pivot Table Format Options

The `PivotTable` class lets you set various formatting options for a pivot table.

#### Setting the AutoFormat and PivotTableStyle Types

The code example that follows illustrates how to set the auto format type and the pivot table style using the `AutoFormat` and `PivotTableStyle` properties.

#### Setting Format Options

The code sample that follows illustrates how to set a number of formatting options for a pivot table report, including adding grand totals for rows and columns.

### Setting PivotFields Format Options

As well as controlling the formatting of the overall pivot table, Aspose.Cells for Java allows fine-tuned control of the formatting for row fields, column fields and page fields.

#### Setting Row, Column, and Page Fields Format

The code example that follows shows how to access row fields, access a particular row, set subtotals, apply automatic sorting, and using the `autoShow` option.

### Setting Data Fields Format

The following lines of code illustrate how to format data fields.

### Modify a Pivot Table's Quick Style

The code examples that follow show how to modify the quick style applied to a pivot table.

### Clearing Pivot Fields

`PivotFieldCollection` has a method named `clear()` that clears pivot fields. Use it to clear pivot fields in all areas for example, page, column, row or data.  
The code sample below shows how to clear all the pivot fields in the data area.

## Consolidation Function

### Applying ConsolidationFunction to Data Fields of Pivot Table

Aspose.Cells can be used to apply ConsolidationFunction to data fields (or value fields) of the pivot table. In Microsoft Excel, you can right click the value field and then select **Value Field Settings...** option and then select the tab **Summarize Values By**. From there, you can select any ConsolidationFunction of your choice like Sum, Count, Average, Max, Min, Product, Distinct Count etc.

Aspose.Cells provides `ConsolidationFunction` enumeration to support the following consolidation functions.

*   `ConsolidationFunction.AVERAGE`
*   `ConsolidationFunction.COUNT`
*   `ConsolidationFunction.COUNT_NUMS`
*   `ConsolidationFunction.DISTINCT_COUNT`
*   `ConsolidationFunction.MAX`
*   `ConsolidationFunction.MIN`
*   `ConsolidationFunction.PRODUCT`
*   `ConsolidationFunction.STD_DEV`
*   `ConsolidationFunction.STD_DEVP`
*   `ConsolidationFunction.SUM`
*   `ConsolidationFunction.VAR`
*   `ConsolidationFunction.VARP`

The following code applies **Average** consolidation function to first data field (or value field) and **DistinctCount** consolidation function to second data field (or value field).

DistinctCount consolidation function is supported by Microsoft Excel 2013 only.

## Attachments:

![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [How to Create a PivotTable-001.jpg](https://docs2.aspose.com/cells/java/attachments/5275912/5472484.jpg) (image/jpeg)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [How to Create a PivotTable-001.png](https://docs2.aspose.com/cells/java/attachments/5275912/5472482.png) (image/png)  

