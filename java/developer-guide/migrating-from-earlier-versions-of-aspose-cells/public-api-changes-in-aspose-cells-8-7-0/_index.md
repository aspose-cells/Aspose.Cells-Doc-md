---
title: Public API Changes in Aspose.Cells 8.7.0
type: docs
weight: 240
url: /java/public-api-changes-in-aspose-cells-8-7-0/
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.6.3 to 8.7.0 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Support for PDF Optimization**
Aspose.Cells APIs already provide the feature of converting spreadsheets to PDF. With this release of the API, users can now [optimize the resultant PDF size](/cells/java/save-excel-into-pdf-with-standard-or-minimum-size/) as well. Aspose.Cells for Java 8.7.0 has exposed the PdfSaveOptions.OptimizationType property along with PdfOptimizationType enumeration in order to facilitate the users to choose the desired optimization algorithm while exporting spreadsheets to PDF format. There are 2 possible values for the PdfSaveOptions.OptimizationType property as detailed below. 

1. PdfOptimizationType.MINIMUM_SIZE: Quality is compromised for the resultant file size.
1. PdfOptimizationType.STANDARD: Quality isn't compromised so the resultant file size will be large.

Following is the simple usage scenario.

**Java**

{{< highlight csharp >}}

 //Create an instance of PdfSaveOptions

PdfSaveOptions pdfSaveOptions = new PdfSaveOptions();

//Set the OptimizationType property to desired value

pdfSaveOptions.setOptimizationType(PdfOptimizationType.MINIMUM_SIZE);

//Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Save the spreadsheet in PDF format while passing the instance of PdfSaveOptions

book.save(outFilePath, pdfSaveOptions);

{{< /highlight >}}
### **Detection of Digitally Signed VBA Project**
Newly exposed VbaProject.isSigned property can be used to in [detect if the VBA project in a Workbook is digitally signed](/cells/java/check-if-vba-code-is-signed/). The VbaProject.isSigned property is of type Boolean, which returns true if the VBA project is digitally signed and vice versa.

Following is the simple usage scenario.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

VbaProject vbaProject = book.getVbaProject();

//Check if VbaProject is digitally signed

if (vbaProject.isSigned())

{

	System.out.println("VbaProject is digitally signed");

}

else

{

	System.out.println("VbaProject is not digitally signed");

}

{{< /highlight >}}
### **Method Protection.verifyPassword Added**
Aspose.Cells APIs have enhanced the Protection class by introducing the verifyPassword method which allows to specify a password as an instance of String and [verifies if same password has been used to protect the Worksheet](/cells/java/verify-password-used-to-protect-the-worksheet/). The Protection.verifyPassword method returns true if the specified password matches with the password used to protect the given worksheet, and false if specified password does not match. Following piece of code uses the Protection.verifyPassword method in conjunction with Protection.isProtectedWithPassword field to detect the password protection, and verifies the password.

Following is the simple usage scenario.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load a spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the protected Worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Check if Worksheet is password protected

if (sheet.getProtection().isProtectedWithPassword())

{

  //Verify the password used to protect the Worksheet

  if (sheet.getProtection().verifyPassword("password"))

  {

	  System.out.println("Specified password has matched");

  }

  else

  {

	  System.out.println("Specified password has not matched");

  }

}

{{< /highlight >}}
### **Property Protection.isProtectedWithPassword Added**
This release of Aspose.Cells for Java has also exposed the Protection.isProtectedWithPassword field that can be useful in [detecting if a Worksheet is password protected or not](/cells/java/detect-if-worksheet-is-password-protected/).

Following is the simple usage scenario.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

Workbook book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

Worksheet sheet = book.getWorksheets().get(0);

//Access Protection module of desired Worksheet

Protection protection = sheet.getProtection();

//Check if Worksheet is password protected

if (protection.isProtectedWithPassword())

{

	System.out.println("Worksheet is password protected");

}

else

{

	System.out.println("Worksheet is not password protected");

}

{{< /highlight >}}
### **Property ColorScale.Is3ColorScale Added**
Aspose.Cells for Java 8.7.0 has exposed the ColorScale.Is3ColorScale property that can be used to [create 2-Color Scale conditional format](/cells/java/adding-2-color-scale-and-3-color-scale-conditional-formattings/). The said property is of type Boolean with default value of true which means that the conditional format will be of 3-Color Scale by default. However, switching the ColorScale.Is3ColorScale property to false will generate a 2-Color Scale conditional format.

Following is the simple usage scenario.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

Workbook book = new Workbook();

//Access the Worksheet to which conditional formatting rule has to be added

Worksheet sheet = book.getWorksheets().get(0);

//Add FormatConditions to the collection

int index = sheet.getConditionalFormattings().add();

//Access newly added formatConditionCollection via its index

FormatConditionCollection formatConditionCollection = sheet.getConditionalFormattings().get(index);

//Create a CellArea on which conditional formatting rule will be applied

CellArea cellArea = CellArea.createCellArea("A1", "A5");

//Add conditional formatted cell range

formatConditionCollection.addArea(cellArea);

//Add format condition of type ColorScale

index = formatConditionCollection.addCondition(FormatConditionType.COLOR_SCALE);

//Access newly added format condition via its index

FormatCondition formatCondition = formatConditionCollection.get(index);

//Set Is3ColorScale to false in order to generate a 2-Color Scale format

formatCondition.getColorScale().setIs3ColorScale(false);

//Set other necessary properties

{{< /highlight >}}
### **Property TxtLoadOptions.HasFormula Added**
Aspose.Cells for Java 8.7.0 has provided support to [identify & parse the formulas while loading CSV/TXT files having delimited plain data](/cells/java/load-or-import-csv-file-with-formulas/). Newly exposed TxtLoadOptions.HasFormula property when set to true directs the API to parse the formulas from the input delimited file and set them to relevant cells without requiring any additional processing.

Following is the simple usage scenario.

**Java**

{{< highlight csharp >}}

 //Create an instance of TxtLoadOptions

TxtLoadOptions options = new TxtLoadOptions();

//Set HasFormula property to true

options.setHasFormula(true);

//Set the Separator property as desired

options.setSeparator(',');

//Load the CSV/TXT file using the instance of TxtLoadOptions

Workbook book = new Workbook(inFilePath, options);

//Calculate formulas in order to get the calculated values of formula in CSV

book.calculateFormula();

//Write result in any of the supported formats

book.save(outFilePath);

{{< /highlight >}}
### **Property DataLabels.ResizeShapeToFitText Added**
Another useful feature that Aspose.Cells for Java 8.7.0 has exposed is the DataLabels.ResizeShapeToFitText property that can enable the [resize shape to fit text](/cells/java/resize-chart-s-data-label-shape-to-fit-text/) feature of Excel application for chart's data labels.

Following is the simple usage scenario.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook containing the Chart

Workbook book = new Workbook(inFilePath);

//Access the Worksheet that contains the Chart

Worksheet sheet = book.getWorksheets().get(0);

//Access the desired Chart via its index or name

Chart chart = sheet.getCharts().get(0);

//Access the DataLabels of desired NSeries

DataLabels labels = chart.getNSeries().get(0).getDataLabels();

//Set ResizeShapeToFitText property to true

labels.setResizeShapeToFitText(true);

//Calculate Chart

chart.calculate();

{{< /highlight >}}
## **Removed APIs**
### **Property Workbook.SaveOptions Removed**
The Workbook.SaveOptions property was marked obsoleted some time back. With this release, it has been completely removed from the public API therefore it is advised to use the Workbook.save(Stream, SaveOptions) or Workbook.save(string, SaveOptions) method as alternative.
