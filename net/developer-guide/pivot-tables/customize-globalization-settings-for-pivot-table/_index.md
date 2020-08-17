---
title: Customize Globalization Settings for Pivot Table
type: docs
weight: 50
url: /net/customize-globalization-settings-for-pivot-table/
---

## **Possible Usage Scenarios**
Sometimes you want to customize the *Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values* text as per your requirements. Aspose.Cells allows you to customize the globalization settings of the pivot table to deal with such scenarios. You can also use this feature to change the labels to other languages like Arabic, Hindi, Polish, etc.
## **Customize Globalization Settings for Pivot Table**
The following sample code explains how to customize globalization settings for the pivot table. It creates a class *CustomPivotTableGlobalizationSettings* derived from a base class [GlobalizationSettings](https://apireference.aspose.com/net/cells/aspose.cells/globalizationsettings) and overrides all of its necessary methods. These methods return the customized text for the *Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values*. Then it assigns the object of this class to [WorkbookSettings.GlobalizationSettings](https://apireference.aspose.com/net/cells/aspose.cells/workbooksettings/properties/globalizationsettings) property. The code loads the [source excel file](40468488.xlsx) that contains the pivot table, refreshes and calculate its data and saves it as [output PDF](40468487.pdf) file. The following screenshot shows the effect of the sample code on the output PDF. As you can see in the screenshot, different parts of the pivot table have now a customized text returned by the overridden methods of [GlobalizationSettings](https://apireference.aspose.com/net/cells/aspose.cells/globalizationsettings) class.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)
## **Sample Code**
{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-PivotTableExamples-CustomizePivotTableGlobalSettings.cs" >}}
