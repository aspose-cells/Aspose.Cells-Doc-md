---
title: Public API Changes in Aspose.Cells 17.1.0
type: docs
weight: 380
url: /java/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 16.12.0 to 17.1.0 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Support for Excel 2016 Charts**
Aspose.Cells APIs have added the support for a few Excel 2016 charts by enhancing the ChartType enumeration. Following new fields have been added with the release of Aspose.Cells 17.1.0.

- ChartType.BOX_WHISKER: The series is laid out as box and whisker.
- ChartType.FUNNEL: The series is laid out as a funnel.
- ChartType.PARETO_LINE: The series is laid out as pareto lines.
- ChartType.SUNBURST: The series is laid out as a sunburst.
- ChartType.TREEMAP: The series is laid out as a treemap.
- ChartType.WATERFALL: The series is laid out as a waterfall.
- ChartType.HISTOGRAM: The series is laid out as a histogram.

{{% alert color="primary" %}} 

Check the detailed article on [Reading Excel 2016 Chart Types](/cells/java/read-and-manipulate-excel-2016-charts/)[](http://docs.asposeptyltd.com/display/cellsjava/Read+and+Manipulate+Excel+2016+Charts)[.](http://docs.asposeptyltd.com/display/cellsjava/Read+and+Manipulate+Excel+2016+Charts)

{{% /alert %}} 
### **Added Setter for LoadFilter.LoadDataFilterOptions Property**
Aspose.Cells 17.1.0 has added setter for the LoadFilter.LoadDataFilterOptions property to replace the m_LoadDataFilterOptions instance variable. Users may change the LoadDataFilterOptions property in their own implementation of LoadFilter class to change the behavior of loading template files.

Here is a simple usage scenario.

{{% alert color="primary" %}} 

Check the detailed article on [Custom Template Filtering](/cells/java/filter-objects-while-loading-workbook-or-worksheet/)[](http://docs.asposeptyltd.com/display/cellsjava/Filter+Objects+while+loading+Workbook+or+Worksheet)[.](http://docs.asposeptyltd.com/display/cellsjava/Filter+Objects+while+loading+Workbook+or+Worksheet)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 class CustomLoadFilter extends LoadFilter {

	public void startSheet(Worksheet sheet) {

		if (sheet.getName().equals("NoCharts")) {

			//Load everything and filter charts

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.CHART);

		}

		if (sheet.getName().equals("NoShapes")) {

			//Load everything and filter shapes

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.SHAPE);

		}

		if (sheet.getName().equals("NoConditionalFormatting")) {

			//Load everything and filter conditional formatting

			this.setLoadDataFilterOptions(LoadDataFilterOptions.ALL& ~LoadDataFilterOptions.CONDITIONAL_FORMATTING);

		}

	}

}

{{< /highlight >}}
### **Added CellsHelper.SignificantDigits Property**
Aspose.Cells 17.1.0 has exposed the SignificantDigits property from the CellsHelper class which allows to get or set the number of significant digits for numeric values in a spreadsheet. The default value of CellsHelper.SignificantDigits property is 17 whereas it is applicable only if the result has to be stored in XLSX file format.

Here is a simple scenario to demonstrate the usage of CellsHelper.SignificantDigits property.

{{% alert color="primary" %}} 

Check the detailed article on [Setting Number of Significant Digits](/cells/java/specifying-significant-digits-to-be-stored-in-excel-file/)[](http://docs.asposeptyltd.com/display/cellsjava/Specifying+Significant+Digits+to+be+Stored+in+Excel+file)[.](http://www.aspose.com/docs/display/cellsjava/Specifying+Significant+Digits+to+be+stored+in+Excel+file)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Specify the number of significant digits

CellsHelper.setSignificantDigits(15);

{{< /highlight >}}
### **Added GlowEffect.Color Property**
Aspose.Cells 17.1.0 has added GlowEffect.Color property which can be used to retrieve the color of the glow effect.

The following snippet make use of the GlowEffect.Color property.

{{% alert color="primary" %}} 

Check the detailed article on [Reading the Shape's Glow Color](/cells/java/read-color-of-the-shape-s-glow-effect/)[](http://docs.asposeptyltd.com/display/cellsjava/Read+Color+of+the+Shape%27s+Glow+Effect)[.](http://www.aspose.com/docs/display/cellsjava/Read+Color+of+the+Glow+Effect+of+Shape)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Read the source Excel file

Workbook book = new Workbook(dir + "sample.xlsx");

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access the first shape

Shape shape = sheet.getShapes().get(0);

//Read the glow effect color

GlowEffect glow = shape.getGlow();

CellsColor color = glow.getColor();

{{< /highlight >}}
### **Added PageSetup.PaperWidth & PaperHeight Properties**
Aspose.Cells 17.1.0 has exposed PaperWidth & PaperHeight properties for the PageSetup class. The PageSetup.PaperWidth & PageSetup.PaperHeight properties are of type double representing the paper width & height in the unit of inches while considering the page orientation.

{{% alert color="primary" %}} 

Check the detailed article on [Retrieving Worksheet's Paper Size](/cells/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)[](http://docs.asposeptyltd.com/display/cellsjava/Get+Paper+Width+and+Height+from+PageSetup+of+Worksheet)[.](http://www.aspose.com/docs/display/cellsjava/Get+Paper+Width+and+Height+of+Page+Setup+of+Worksheet)

{{% /alert %}} 
### **Added WorkbookSettings.CheckCustomNumberFormat Property**
Aspose.Cells 17.1.0 has added the CheckCustomNumberFormat property to the WorkbookSettings class. The CheckCustomNumberFormat is useful in checking if the Style.Custom property has been set properly or not. In case the Style.Custom property has been set improperly, that is; the value does not correspond to valid pattern then the Aspose.Cells APIs will throw CellsException with appropriate message.

{{% alert color="primary" %}} 

Check the detailed article on [Verifying Custom Forma](/cells/java/check-custom-number-format-when-setting-style-custom-property/)[t](http://docs.asposeptyltd.com/display/cellsjava/Check+Custom+Number+Format+when+Setting+Style.Custom+Property)[.](http://www.aspose.com/docs/display/cellsjava/Check+Custom+Number+Format+when+setting+Style.Custom+property)

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Set CheckCustomNumberFormat property to true

book.getSettings().setCheckCustomNumberFormat(true);

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access a cell

Cell cell = sheet.getCells().get("B5");

//Insert a value to the cell

cell.putValue(2347);

//Access cell's style

Style style = cell.getStyle();



//Set Custom property to an invalid pattern

style.setCustom("ggg @ fff");

//Set the modified style to the cell

cell.setStyle(style);

{{< /highlight >}}
### **Added DisplayUnitType.PERCENTAGE Field**
Aspose.Cells 17.1.0 has also exposed the PERCENTAGE field to the DisplayUnitType enumeration. The DisplayUnitType.PERCENTAGE field indicates that the values on the chart shall be divided by 0.01.
## **Removed APIs**
### **Instance Variable m_LoadDataFilterOptions Removed**
This release has removed the m_LoadDataFilterOptions instance variable. It is advised to use the LoadFilter.LoadDataFilterOptions property instead.
