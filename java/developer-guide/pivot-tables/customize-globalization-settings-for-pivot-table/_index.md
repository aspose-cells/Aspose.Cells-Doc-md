---
title: Customize Globalization Settings for Pivot Table
type: docs
weight: 20
url: /java/customize-globalization-settings-for-pivot-table/
---

## **Possible Usage Scenarios**

Sometimes you want to customize the *Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values* text as per your requirements. Aspose.Cells allows you to customize the globalization settings of the pivot table to deal with such scenarios. You can also use this feature to change the labels to other languages like Arabic, Hindi, Polish, etc.

## **Customize Globalization Settings for Pivot Table**

The following sample code explains how to customize globalization settings for the pivot table. It creates a class *CustomPivotTableGlobalizationSettings* derived from a base class [**GlobalizationSettings**](https://apireference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings) and overrides all of its necessary methods. These methods return the customized text for the *Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values*. Then it assigns the object of this class to [**WorkbookSettings.GlobalizationSettings**](https://apireference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) property. The code loads the [source excel file](40468491.xlsx) that contains the pivot table, refreshes and calculate its data and saves it as [output PDF file](40468490.pdf). The following screenshot shows the effect of the sample code on the output PDF. As you can see in the screenshot, different parts of the pivot table have now a customized text returned by the overridden methods of [**GlobalizationSettings**](https://apireference.aspose.com/cells/java/com.aspose.cells/GlobalizationSettings) class.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-CustomizeGlobalizationSettingsforPivotTable-1.java" >}}
