---
title: Public API Changes in Aspose.Cells 16.12.0
type: docs
weight: 360
url: /net/public-api-changes-in-aspose-cells-16-12-0/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 16.11.0 to 16.12.0 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Filter Objects at Load Time**
Aspose.Cells 16.12.0 has exposed the LoadFilter class along with LoadOptions.LoadFilter property which together can control the type of data to be loaded while initializing an instance of Workbook from a template file.

Here is a simple usage scenario to load only the document properties from a template file.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class

// Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.DocumentProperties);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Following snippet loads everything from an existing spreadsheet except for the charts.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to the constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.All & ~Aspose.Cells.LoadDataFilterOptions.Chart);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



Following code loads only the cell data (along with formulas) and formatting from an existing spreadsheet.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of LoadFilter class with appropriate parameters to constructor

options.LoadFilter = new Aspose.Cells.LoadFilter(Aspose.Cells.LoadDataFilterOptions.CellData);

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}



The LoadFilter class also allows to customize the loading process as per the properties of the Worksheet. In order to customize the loading process as per worksheet, one has to override the LoadFilter.StartSheet method as demonstrated below.

**C#**

{{< highlight csharp >}}

 class CustomFilter : Aspose.Cells.LoadFilter

{

    public override void StartSheet(Worksheet sheet)

    {

        if (sheet.Name == "Sheet1")

        {

            // Load everything

            m_LoadDataFilterOptions = Aspose.Cells.LoadDataFilterOptions.All;

        }

        else

        {

            // Load nothing

            m_LoadDataFilterOptions = Aspose.Cells.LoadDataFilterOptions.None;

        }

    }

}

{{< /highlight >}}



The following snippet make use of the CustomFilter class defined above.

**C#**

{{< highlight csharp >}}

 // Create an instance of LoadOptions class

var options = new Aspose.Cells.LoadOptions();

// Set the LoadFilter property to a new instance of CustomFilter class

options.LoadFilter = new CustomFilter();

// Load a template file by passing file path as well as instance of LoadOptions class

var book = new Aspose.Cells.Workbook(dir + "sample.xlsx", options);

{{< /highlight >}}


### **Added FileFormatType.OTS Enumeration**
Aspose.Cells 16.12.0 has added OTS entry to the FileFormatType enumeration in order to detect the format of OTS files.

The following snippet make use of the FileFormatType.OTS.

**C#**

{{< highlight csharp >}}

 // Load a sample in an instance of FileStream

var stream = File.OpenRead(dir + "sample.ots");

// Detect the format of the stream

var fileFormatInfo = Aspose.Cells.FileFormatUtil.DetectFileFormat(stream);



// Check if stream is of type OTS

Debug.Assert(fileFormatInfo.FileFormatType == FileFormatType.OTS);

{{< /highlight >}}


### **Added FontConfigs.PreferSystemFontSubstitutes Property**
Aspose.Cells 16.12.0 has exposed PreferSystemFontSubstitutes property for the FontConfigs class. The FontConfigs.PreferSystemFontSubstitutes property is of type Boolean, indicating if the API should use the system's font substitution mechanism first, in case a required font is not present and no substitution for the particular font has been defined. The default value of FontConfigs.PreferSystemFontSubstitutes property is false.
### **Added BuiltInDocumentPropertyCollection.ScaleCrop Property**
Aspose.Cells 16.12.0 has added the ScaleCrop property to the BuiltInDocumentPropertyCollection class. The ScaleCrop indicates the display mode of the document thumbnail. Setting this element to true enables the scaling of the document thumbnail as per display whereas setting it to false enables the cropping of the document thumbnail to show the section that fits the display.
### **Added BuiltInDocumentPropertyCollection.LinksUpToDate Property**
Aspose.Cells 16.12.0 has also exposed the LinksUpToDate property for the BuiltInDocumentPropertyCollection class. The LinksUpToDate property indicates if the hyperlinks in a document are up-to-date.
### **Added Workbook.ExportXml Method**
Aspose.Cells 16.12.0 has exposed the Workbook.ExportXml method that allows to store the XML map data to specified file path. The Workbook.ExportXml method accepts 2 parameters where the first parameter of type string should be the XML map name and second parameter should be the file path location to store the XML data.
### **Added WorksheetCollection.CreateRange Method**
Aspose.Cells 16.12.0 has added the WorksheetCollection.CreateRange method that allows to create range based on an address (cell area reference) & Worksheet index.

The following snippet make use of the WorksheetCollection.CreateRange method to create a range of cells spanning over A1 to A2 in first (default) worksheet.

**C#**

{{< highlight csharp >}}

 // Create an instance of Workbook

var book = new Aspose.Cells.Workbook();

// Access WorksheetCollection from the Workbook

var sheets = book.Worksheets;



// Create a range in first worksheet

var range = sheets.CreateRange("A1:A2", 0);

{{< /highlight >}}
## **Obsoleted APIs**
### **Obsoleted LoadOptions.LoadDataOptions Property**
Please use LoadOptions.LoadFilter property as an alternative.
### **Obsoleted LoadOptions.LoadDataFilterOptions Property**
Please use LoadOptions.LoadFilter property instead.
### **Obsoleted LoadOptions.OnlyLoadDocumentProperties Property**
Please use LoadOptions.LoadFilter property as an alternative.
### **Obsoleted LoadOptions.LoadDataAndFormatting Property**
Please use LoadOptions.LoadFilter property instead.

{{% alert color="primary" %}} 

Code snippets for all the obsoleted APIs have been shared above.

{{% /alert %}}
## **Deleted APIs**
### **Deleted DataLabels.Rotation Property**
Please use DataLabels.RotationAngle property instead.
### **Deleted Title.Rotation Property**
Please use Title.RotationAngle property as an alternative.
### **Deleted DataLabels.Background Property**
It is advised to use the DataLabels.BackgroundMode property instead.
### **Deleted DisplayUnitLabel.Rotation Property**
Please consider using DisplayUnitLabel.RotationAngle property to achieve the same goal.
{{< app/cells/assistant language="csharp" >}}
