##Public API Changes in Aspose.Cells 16.12.0
This document describes the changes to the Aspose.Cells API from version 16.11.0 to 16.12.0 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.
## **Added APIs**
### **Filter Objects at Load Time**
Aspose.Cells 16.12.0 has exposed the LoadFilter class along with LoadOptions.LoadFilter property which together can control the type of data to be loaded while initializing an instance of Workbook from a template file.
Here is a simple usage scenario to load only the document properties from a template file.
**Java**
//Create an instance of LoadOptions class
LoadOptions options = new LoadOptions();
//Create an instance of LoadFilter class
//Select to load document properties by passing LoadDataFilterOptions.DocumentProperties to constructor
LoadFilter filter = new LoadFilter(LoadDataFilterOptions.DOCUMENT_PROPERTIES);
//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above
options.setLoadFilter(filter);
//Load a template file by passing file path as well as instance of LoadOptions class
Workbook book = new Workbook(dir + "sample.xlsx", options);
Following snippet loads everything from an existing spreadsheet except for the charts.
**Java**
//Create an instance of LoadOptions class
LoadOptions options = new LoadOptions();
//Create an instance of LoadFilter class
//Select to load document properties by passing parameter to the constructor
LoadFilter filter = new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.CHART);
//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above
options.setLoadFilter(filter);
//Load a template file by passing file path as well as instance of LoadOptions class
Workbook book = new Workbook(dir + "sample.xlsx", options);
Following code loads only the cell data (along with formulas) and formatting from an existing spreadsheet.
**Java**
//Create an instance of LoadOptions class
LoadOptions options = new LoadOptions();
//Create an instance of LoadFilter class
//Select to load document properties by passing parameter to the constructor
LoadFilter filter = new LoadFilter(LoadDataFilterOptions.CELL_DATA);
//Set the LoadFilter property of LoadOptions object to the instance of LoadFilter class created above
options.setLoadFilter(filter);
//Load a template file by passing file path as well as instance of LoadOptions class
Workbook book = new Workbook(dir + "sample.xlsx", options);
### **Added FileFormatType.OTS Enumeration**
Aspose.Cells 16.12.0 has added OTS entry to the FileFormatType enumeration in order to detect the format of OTS files.
The following snippet make use of the FileFormatType.OTS.
**Java**
//Detect the format of the file
FileFormatInfo fileFormatInfo = FileFormatUtil.detectFileFormat(dir + "sample.ots");
//Check if stream is of type OTS
if(fileFormatInfo.getFileFormatType() == FileFormatType.OTS);
{
System.out.println("It is an OTS file");
}
### **Added BuiltInDocumentPropertyCollection.ScaleCrop Property**
Aspose.Cells 16.12.0 has added the ScaleCrop property to the BuiltInDocumentPropertyCollection class. The ScaleCrop indicates the display mode of the document thumbnail. Setting this element to true enables the scaling of the document thumbnail as per display whereas setting it to false enables the cropping of the document thumbnail to show the section that fits the display.
### **Added BuiltInDocumentPropertyCollection.LinksUpToDate Property**
Aspose.Cells 16.12.0 has also exposed the LinksUpToDate property for the BuiltInDocumentPropertyCollection class. The LinksUpToDate property indicates if the hyperlinks in a document are up-to-date.
### **Added Workbook.exportXml Method**
Aspose.Cells 16.12.0 has exposed the Workbook.exportXml method that allows to store the XML map data to specified file path. The Workbook.exportXml method accepts 2 parameters where the first parameter of type string should be the XML map name and second parameter should be the file path location to store the XML data.
### **Added WorksheetCollection.createRange Method**
Aspose.Cells 16.12.0 has added the WorksheetCollection.createRange method that allows to create range based on an address (cell area reference) & Worksheet index.
The following snippet make use of the WorksheetCollection.createRange method to create a range of cells spanning over A1 to A2 in first (default) worksheet.
**Java**
//Create an instance of Workbook
Workbook book = new Workbook();
//Access WorksheetCollection from the Workbook
WorksheetCollection sheets = book.getWorksheets();
//Create a range in first worksheet
Range range = sheets.createRange("A1:A2", 0);
## **Obsoleted APIs**
### **Obsoleted LoadOptions.LoadDataOptions Property**
Please use LoadOptions.LoadFilter property as an alternative.
### **Obsoleted LoadOptions.LoadDataFilterOptions Property**
Please use LoadOptions.LoadFilter property instead.
### **Obsoleted LoadOptions.OnlyLoadDocumentProperties Property**
Please use LoadOptions.LoadFilter property as an alternative.
### **Obsoleted LoadOptions.LoadDataAndFormatting Property**
Please use LoadOptions.LoadFilter property instead.
Code snippets for all the obsoleted APIs have been shared above.
## **Deleted APIs**
### **Deleted DataLabels.Rotation Property**
Please use DataLabels.RotationAngle property instead.
### **Deleted Title.Rotation Property**
Please use Title.RotationAngle property as an alternative.
### **Deleted DataLabels.Background Property**
It is advised to use the DataLabels.BackgroundMode property instead.
### **Deleted DisplayUnitLabel.Rotation Property**
Please consider using DisplayUnitLabel.RotationAngle property to achieve the same goal.
### **Deleted Title.getCharacters Method**
Please use Title.characters method instead.
