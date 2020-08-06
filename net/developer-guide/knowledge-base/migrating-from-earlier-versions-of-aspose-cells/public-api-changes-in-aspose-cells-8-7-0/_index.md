---
title: Public API Changes in Aspose.Cells 8.7.0
type: docs
weight: 230
url: /net/public-api-changes-in-aspose-cells-8-7-0/
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.6.3 to 8.7.0 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Support for VBA Project Digital Signing, Detection & Extraction**
This release of Aspose.Cells for .NET has exposed some new properties and methods to aid the users in tasks such as digitally signing a VBA project, detecting if a VBA project is signed & valid. Moreover, the new API allows to extract the certificate as raw data from digitally signed VBA project in Workbook.
###### **Digitally Sign VBA Project**
Aspose.Cells for .NET 8.7.0 has exposed the VbaProject.Sign method that can be used to [digitally sign the VBA project in a Workbook](http://www.aspose.com/docs/display/cellsnet/Digitally+Sign+a+VBA+Code+Project+with+Certificate). The said method accepts an instance of DigitalSignature class which resides in the Aspose.Cells.DigitalSignatures namespace.

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Sign the VbaProject using the X509Certificate

vbaProject.Sign(new DigitalSignature(new System.Security.Cryptography.X509Certificates.X509Certificate2(cert), "Comments", DateTime.Now));

{{< /highlight >}}


###### **Detection of Digitally Signed VBA Project**
Newly exposed VbaProject.IsSigned property can be used to in [detect if the VBA project in a Workbook is digitally signed](http://www.aspose.com/docs/display/cellsnet/Check+if+VBA+Code+is+Signed). The VbaProject.IsSigned property is of type Boolean, which returns true if the VBA project is digitally signed and vice versa.

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Check if VbaProject is digitally signed

if (vbaProject.IsSigned)

{

    Console.WriteLine("VbaProject is digitally signed");

}

else

{

    Console.WriteLine("VbaProject is not digitally signed");

}

{{< /highlight >}}


###### **Extraction of Digital Signature from VBA Project**
This revision of the API has also exposed the VbaProject.CertRawData property which allows to [extract the digital certificate's raw data from the VBA project](http://www.aspose.com/docs/display/cellsnet/Export+VBA+Certifcate+to+File+or+Stream). The VbaProject.CertRawData property is of type byte array, which will contain the raw certificate data if VBA project is digitally signed, otherwise the said property will be null.

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Extract digital signature in an array of bytes

var cert = vbaProject.CertRawData;

{{< /highlight >}}


###### **Validate the Digital Signature of VBA Project**
Another addition to the public API is the VbaProject.IsValidSigned property which could be useful in [validating the digital signature of the VBA project](http://www.aspose.com/docs/display/cellsnet/Check+if+Digital+Signature+of+VBA+Code+is+Valid). The said property returns true if the digital signature is valid and false if the signature is invalid.

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the VbaProject from the Workbook

var vbaProject = book.VbaProject;

//Check if VbaProject is digitally signed

if (vbaProject.IsSigned)

{

    //Check if signature is valid

    if (vbaProject.IsValidSigned)

    {

        Console.WriteLine("VbaProject is digitally signed & signature is valid");

    }

}

{{< /highlight >}}


### **Method Protection.VerifyPassword Added**
Aspose.Cells for .NET 8.7.0 has exposed the Protection.VerifyPassword method that can be used to [verify the password used to protect the Worksheet](http://www.aspose.com/docs/display/cellsnet/Verify+Password+Used+to+Protect+the+Worksheet). This method accepts an instance of string as parameter and returns true if specified password matches with the password used to protect the Worksheet.

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

var sheet = book.Worksheets[0];

//Access Protection module of desired Worksheet

var protection = sheet.Protection;

//Verify the password for Worksheet

if (protection.VerifyPassword(password))

{

    Console.WriteLine("Password has matched");

}

else

{

    Console.WriteLine("Password did not match");

}

{{< /highlight >}}


### **Property Protection.IsProtectedWithPassword Added**
This release of Aspose.Cells for .NET API has also exposed the Protection.IsProtectedWithPassword property that can be useful in [detecting if a Worksheet is password protected or not](http://www.aspose.com/docs/display/cellsnet/Detect+if+Worksheet+is+Password+Protected).

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook and load an existing spreadsheet

var book = new Workbook(inFilePath);

//Access the desired Worksheet via its index or name

var sheet = book.Worksheets[0];

//Access Protection module of desired Worksheet

var protection = sheet.Protection;

//Check if Worksheet is password protected

if (protection.IsProtectedWithPassword)

{

    Console.WriteLine("Worksheet is password protected");

}

else

{

    Console.WriteLine("Worksheet is not password protected");

}

{{< /highlight >}}


### **Property ColorScale.Is3ColorScale Added**
Aspose.Cells for .NET 8.7.0 has exposed the ColorScale.Is3ColorScale property that can be used to create 2-Color Scale conditional format. The said property is of type Boolean with default value of true which means that the conditional format will be of 3-Color Scale by default. However, switching the ColorScale.Is3ColorScale property to false will [generate a 2-Color Scale conditional format](http://www.aspose.com/docs/display/cellsnet/Adding+2-Color+Scale+and+3-Color+Scale+Conditional+Formattings).

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook();

//Access the Worksheet to which conditional formatting rule has to be added

var sheet = book.Worksheets[0];

//Add FormatConditions to the collection

int index = sheet.ConditionalFormattings.Add();

//Access newly added formatConditionCollection via its index

var formatConditionCollection = sheet.ConditionalFormattings[index];

//Create a CellArea on which conditional formatting rule will be applied

var cellArea = CellArea.CreateCellArea("A1", "A5");

//Add conditional formatted cell range

formatConditionCollection.AddArea(cellArea);

//Add format condition of type ColorScale

index = formatConditionCollection.AddCondition(FormatConditionType.ColorScale);

//Access newly added format condition via its index

var formatCondition = formatConditionCollection[index];

//Set Is3ColorScale to false in order to generate a 2-Color Scale format

formatCondition.ColorScale.Is3ColorScale = false;

//Set other necessary properties

{{< /highlight >}}


### **Property TxtLoadOptions.HasFormula Added**
Aspose.Cells for .NET 8.7.0 has provided support to [identify & parse the formulas while loading CSV/TXT files having delimited plain data](http://www.aspose.com/docs/display/cellsnet/Load+or+Import+CSV+file+with+Formulas). Newly exposed TxtLoadOptions.HasFormula property when set to true directs the API to parse the formulas from the input delimited file and set them to relevant cells without requiring any additional processing.

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 //Create an instance of TxtLoadOptions

var options = new TxtLoadOptions();

//Set HasFormula property to true

options.HasFormula = true;

//Set the Separator property as desired

options.Separator = ',';

//Load the CSV/TXT file using the instance of TxtLoadOptions

var book = new Workbook(inFilePath, options);

//Calculate formulas in order to get the calculated values of formula in CSV

book.CalculateFormula();

//Write result in any of the supported formats

book.Save(outFilePath);

{{< /highlight >}}


### **Property DataLabels.IsResizeShapeToFitText Added**
Another useful feature that Aspose.Cells for .NET 8.7.0 has exposed is the DataLabels.IsResizeShapeToFitText property that can enable the [Resize shape to fit text](http://www.aspose.com/docs/display/cellsnet/Resize+Chart%27s+Data+Label+Shape+To+Fit+Text) feature of Excel application for chart's data labels.

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook containing the Chart

var book = new Workbook(inFilePath);

//Access the Worksheet that contains the Chart

var sheet = book.Worksheets[0];

//Access the desired Chart via its index or name

var chart = sheet.Charts[0];

//Access the DataLabels of desired NSeries

var labels = chart.NSeries[0].DataLabels;

//Set ResizeShapeToFitText property to true

labels.IsResizeShapeToFitText = true;

//Calculate Chart

chart.Calculate();

{{< /highlight >}}


### **Property PdfSaveOptions.OptimizationType Added**
Aspose.Cells for .NET 8.7.0 has exposed the PdfSaveOptions.OptimizationType property along with PdfOptimizationType enumeration in order to facilitate the users to [choose the desired optimization algorithm while exporting spreadsheets to PDF format](http://www.aspose.com/docs/display/cellsnet/Save+Excel+into+PDF+with+Standard+or+Minimum+Size). There are 2 possible values for the PdfSaveOptions.OptimizationType property as detailed below.

1. PdfOptimizationType.MinimumSize: Quality is compromised for the resultant file size.
1. PdfOptimizationType.Standard: Quality isn't compromised so the resultant file size will be large.

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 //Create an instance of PdfSaveOptions

var pdfSaveOptions = new PdfSaveOptions();

//Set the OptimizationType property to desired value

pdfSaveOptions.OptimizationType = PdfOptimizationType.MinimumSize;

//Create an instance of Workbook

//Optionally load an existing spreadsheet

var book = new Workbook(inFilePath);

//Save the spreadsheet in PDF format while passing the instance of PdfSaveOptions

book.Save(outFilePath, pdfSaveOptions);

{{< /highlight >}}
## **Removed APIs**
### **Property Workbook.SaveOptions Removed**
The Workbook.SaveOptions property was marked obsoleted some time back. With this release, it has been completely removed from the public API therefore it is advised to use the Workbook.Save(Stream, SaveOptions) or Workbook.Save(string, SaveOptions) method as alternative.
