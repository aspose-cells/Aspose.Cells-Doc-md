+++
title = "Public API Changes in Aspose.Cells 16.11.0" 
description = "" 
weight = 12321 
+++

Aspose.Cells for Java : Public API Changes in Aspose.Cells 16.11.0  

# Aspose.Cells for Java : Public API Changes in Aspose.Cells 16.11.0


This document describes the changes to the Aspose.Cells API from version 16.10.0 to 16.11.0 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

## Added APIs

### Support for Globalization Settings

Aspose.Cells 16.11.0 has exposed the `GlobalizationSettings` class along with `WorkbookSettings.GlobalizationSettings` property in order to enforce the Aspose.Cells APIs to use custom labels for Subtotals. The `GlobalizationSettings` class has the following methods which can be overridden in the custom implementation to give desired names to the labels **Total** & **Grand Total**.

*   `GlobalizationSettings.getTotalName`: Gets the total name of the function.
*   `GlobalizationSettings.getGrandTotalName`: Gets the grand total name of the function.

Here is a simple custom class that extends `GlobalizationSettings` class and overrides its aforementioned methods to return custom labels for the consolidation function Average.

**Java**

{{< code lang="java" >}}
public class CustomSettings extends GlobalizationSettings
{    
    public String getTotalName(int functionType)
    {
    	 switch (functionType)
         {
             case ConsolidationFunction.AVERAGE:
                 return "AVG";
             default:
                return super.getTotalName(functionType);
         }
    }

    public String getGrandTotalName(int functionType)
    {
    	 switch (functionType)
         {
             case ConsolidationFunction.AVERAGE:
                 return "GRAND AVG";
             default:
            	 return super.getGrandTotalName(functionType);
         }
                
    }
}
{{< /code >}}

Following snippet loads an existing spreadsheet and adds the Subtotal of type Average on data already available in the worksheet. The `CustomSettings` class and its `getTotalName` & `getGrandTotalName` methods will be called at the time of adding Subtotal to the worksheet.

**Java**

{{< code lang="java" >}}
//Loads an existing spreadsheet containing some data
Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class
//to the class created in first step
book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains data
//Data resides in the cell range A2:B9
Worksheet sheet = book.getWorksheets().get(0);

//Adds SubTotal of type Average to the worksheet
sheet.getCells().subtotal(CellArea.createCellArea("A2", "B9"), 0, ConsolidationFunction.AVERAGE, new int[] { 0,1 });

//Calculates Formulas
book.calculateFormula();

//Auto fits all columns
sheet.autoFitColumns();

//Saves the workbook on disc
book.save(dir + "output.xlsx");
{{< /code >}}

The `GlobalizationSettings` class also offers the `getOtherName` method which is useful to get the name of "Other" labels for Pie charts. Here is a simple usage scenario of `GlobalizationSettings.getOtherName` method.

**Java**

{{< code lang="java" >}}
public class CustomSettings extends GlobalizationSettings
{ 
	public String getOtherName()
	{
		String language = Locale.getDefault().getLanguage();
		System.out.println(language);
		switch (language)
		{
			case "en":
				return "Other";
			case "fr":
				return "Autre";
			case "de":
				return "Andere";

			//Do other cases

			default:
				return super.getOtherName();
		}
	}
}
{{< /code >}}

The following snippet loads an existing spreadsheet containing a Pie chart, and renders the chart to image while utilizing the `CustomSettings` class created above.

**Java**

{{< code lang="java" >}}
//Loads an existing spreadsheet containing a pie chart
Workbook book = new Workbook(dir + "sample.xlsx");

//Assigns the GlobalizationSettings property of the WorkbookSettings class
//to the class created in first step
book.getSettings().setGlobalizationSettings(new CustomSettings());

//Accesses the 1st worksheet from the collection which contains pie chart
Worksheet sheet = book.getWorksheets().get(0);

//Accesses the 1st chart from the collection
Chart chart = sheet.getCharts().get(0);

//Refreshes the chart
chart.calculate();

//Renders the chart to image
chart.toImage(dir + "output.png", new ImageOrPrintOptions());
{{< /code >}}

### Added CellsFactory Class

Aspose.Cells 16.11.0 has exposed the `CellsFactory` class which currently has one method, that is; `createStyle`. The `CellsFactory.createStyle` method can be used to create an instance of `Style` class without adding it to the pool of workbook styles.

Here is simple usage scenario of `CellsFactory.createStyle` method.

**Java**

{{< code lang="java" >}}
//Initializes the CellsFactory class
CellsFactory factory = new CellsFactory();

//Creates an instance of Style
Style style = factory.createStyle();
{{< /code >}}

### Added Workbook.AbsolutePath Property

Aspose.Cells 16.11.0 has exposed the `Workbook.AbsolutePath` property allows to get or set the absolute workbook path stored in workbook.xml file. This property is useful while updating the external links only.

### Added GridHyperlinkCollection.getHyperlink Method

Aspose.Cells.GridWeb 16.11.0 has exposed `getHyperlink` method to the `GridHyperlinkCollection` class that allows to get the instance of `GridHyperlink` by either passing an instance `GridCell` or a pair of integers corresponding to the row column indices.

In case no hyperlink has been found on the specified cell then the `getHyperlink` method would return null.

Here is simple usage scenario of `getHyperlink` method.

**Java**

{{< code lang="java" >}}
//Gets the active worksheet from the collection
GridWorksheet sheet = gridWeb1.getWorkSheets().get(gridWeb1.getActiveSheetIndex());

//Accesses the GridHyperlinkCollection
GridHyperlinkCollection links = sheet.getHyperlinks();

//Gets hyperlink from cell A1
GridHyperlink link = links.getHyperlink(sheet.getCells().get("A1"));

//Gets hyperlink from cell D1
link = links.getHyperlink(0, 3);
{{< /code >}}

## Obsoleted APIs

### Obsoleted Style Constructor

Please use `cellsFactory.createStyle` method as an alternative.

## Deleted APIs

### Deleted Cell.getConditionalStyle Method

Please use `Cell.getConditionalFormattingResult` method instead.

### Deleted Cells.getMaxDataRowInColumn(int column) Method

Please use `Cells.getLastDataRow(int)` method as an alternative.

### Deleted PageSetup.Draft Property

It is advised to use the `PageSetup.PrintDraft` property instead.

### Deleted AutoFilter.FilterColumnCollection Property

Please consider using `AutoFilter.FilterColumns` property to achieve the same goal.

### Deleted TickLabels.Rotation Property

Please use `TickLabels.RotationAngle` property instead.

