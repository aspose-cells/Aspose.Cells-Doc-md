---
title: Public API Changes in Aspose.Cells 8.8.1
type: docs
weight: 280
url: /java/public-api-changes-in-aspose-cells-8-8-1/
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.8.0 to 8.8.1 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Filter the Data for Loading**
Aspose.Cells for Java 8.8.1 has exposed the LoadDataFilterOptions enumeration along with LoadOptions.LoadDataFilterOptions property which can be used to specify the data type that should be loaded when building the workbook from a template file. Filtering loaded data can improve the performance for special purposes, especially when using LightCells APIs.

The LoadDataFilterOptions enumeration provides the following selections.

1. ALL to load everything from the spreadsheet.
1. NONE to load nothing from the spreadsheet.
1. CELL_BLANK loads the cells whose values are blank.
1. CELL_BOOL loads cells whose values are Boolean.
1. CELL_DATA loads cells data including values, formulas and formatting.
1. CELL_ERROR loads cells whose values are error.
1. CELL_NUMERIC loads cells whose values are numeric (including Date & Time).
1. CELL_STRING loads cells whose values are text/string.
1. CELL_VALUE loads only cell values (all types).
1. CHART loads only charts.
1. CONDITIONAL_FORMATTING loads only conditional formatting rules.
1. DATA_VALIDATION loads only data validation rules.
1. DOCUMENT_PROPERTIES loads only document properties.
1. FORMULA loads formulas including defined names.
1. MERGED_AREA loads only merged cells.
1. PIVOT_TABLE loads Pivot Tables.
1. SETTINGS loads only Workbook & Worksheet settings.
1. SHAPE loads only shapes.
1. STYLE loads cells formatting.
1. TABLE loads Excel tables/List Objects.

{{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Filter Data for Loading](http://www.aspose.com/docs/display/cellsjava/Filtering+the+kind+of+data+while+loading+the+workbook+from+template+file).

{{% /alert %}} 

Following is the simple usage scenario.

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadOptions & initialize it with type of template to be loaded

LoadOptions options = new LoadOptions(LoadFormat.XLSX);

//Set LoadDataFilterOptions to load only shapes

options.setLoadDataFilterOptions(LoadDataFilterOptions.SHAPE);

//Create an instance of Workbook from a existing spreadsheet using instance of LoadOptions

Workbook book = new Workbook(filePath, options);

{{< /highlight >}}
### **Directly Convert Chart to PDF**
Aspose.Cells APIs have already provided the facility to render charts to PDF while using the Chart.toPdf method. With this release, the API has exposed another overloaded version of the said method that could accept an instance of OutputStream, allowing the users to save the chart's PDF in an instance of ByteArrayOutputStream.

{{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Converting Charts to PDF](http://www.aspose.com/docs/display/cellsjava/Converting+Chart+to+PDF).

{{% /alert %}} 

Following is the simple usage scenario.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet with a chart

Workbook workbook = new Workbook(filePath);

//Access first worksheet containing a chart

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first chart from the worksheet

Chart chart = worksheet.getCharts().get(0);

//Save the chart to PDF as Stream

ByteArrayOutputStream outStream = new ByteArrayOutputStream();

chart.toPdf(outStream);

{{< /highlight >}}
### **Added WorkbookSettings.PaperSize Property**
Aspose.Cells for Java 8.8.1 has exposed the WorkbookSettings.PaperSize property in order to set the default printing paper size for the whole spreadsheet. The WorkbookSettings.PaperSize property accepts a value from the PaperSizeType enumeration which contains the predefined sizes for most widely used printing paper types.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access WorkbookSettings from the Workbook

WorkbookSettings settings = book.getSettings();

//Set the default printing paper size for the Workbook

settings.setPaperSize(PaperSizeType.PAPER_A_4);

{{< /highlight >}}
### **Added Shape.TextBody Property**
This release of Aspose.Cells for Java API has exposed the Shape.TextBody in order to manipulate the aspects of the text in a shapes. The following snippet uses the said property to set the shadow effect of the text in a TextBox.

{{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Setting Shadow Effect for Text](http://www.aspose.com/docs/display/cellsjava/Setting+Shadow+of+Text+Effects+of+Shape+or+TextBox).

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet of the Workbook

Worksheet sheet = book.getWorksheets().get(0);

//Add a TextBox to the ShapeCollection

int index = sheet.getTextBoxes().add(2, 2, 100, 400);

TextBox textBox = sheet.getTextBoxes().get(index);

//Set the text of the TextBox

textBox.setText("This text has the following settings.\n\nText Effects > Shadow > Offset Bottom");

//Set shadow effect for text

for (int i = 0; i < textBox.getTextBody().getCount(); i++)

{

  textBox.getTextBody().get(i).getShapeFont().getFillFormat().getShadowEffect().setPresetType(PresetShadowType.OFFSET_BOTTOM);

}

{{< /highlight >}}
### **Added Worksheet.calculateFormula(string formula, CalculationOptions opts) Method**
Aspose.Cells for Java 8.8.1 has exposed another overload for the Worksheet.calculateFormula method which provides the ability to calculate a given formula directly with custom options.

{{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Direct Calculation of Custom Function](http://www.aspose.com/docs/display/cellsjava/Direct+calculation+of+custom+function+without+writing+it+in+a+worksheet).

{{% /alert %}} 
### **Added GridCell.createValidation Method**
Aspose.Cells.GridWeb has provided the ability to directly add the validation rule to a single cell while using the GridCell.createValidation method. The said method requires 2 parameters. First one is of type GridValidationType which determines the validation type, whereas the second parameter (isRequied) is of type Boolean.

{{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Create Data Validation for a GridCell](http://www.aspose.com/docs/display/cellsjava/Create+Data+Validation+in+a+GridCell+of+GridWeb).

{{% /alert %}} 

**Java**

{{< highlight csharp >}}

 //Access first worksheet

GridWorksheet sheet = gridweb.getWorkSheets().get(0);

//Access cell B3

GridCell cell = sheet.getCells().get("B3");

//Add validation inside the GridCell

//Any value which is not between 20 and 40 will cause error in a GridCell

GridValidation val = cell.createValidation(GridValidationType.WHOLE_NUMBER, true);

val.setFormula1("=20");

val.setFormula2("=40");

val.setOperator(OperatorType.BETWEEN);

val.setShowError(true);

val.setShowInput(true);

{{< /highlight >}}
### **Added GridCell.removeValidation Method**
Aspose.Cells.GridWeb has also provided the ability to remove the data validation rule from a GridCell while using the GridCell.removeValidation method.
## **Obsoleted APIs**
### **Obsoleted Shape.TextFrame Property**
It is advised to use the Shape.TextBody.TextAlignment property instead.
