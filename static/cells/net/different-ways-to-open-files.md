##Different Ways to Open Files
This article explains how to open an excel file using Aspose.Cells for .NET API.
With Aspose.Cells it is simple to open files, for example, to retrieve data, or to use a designer template to speed up the development process.
## **How to Open an Excel File via a Path**
Developers can open a Microsoft Excel file using its file path on the local computer by specifying it in the [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class constructor. Simply pass the path in the constructor as a *string*. Aspose.Cells will automatically detect the file format type.
## **How to Open an Excel File via a Stream**
It is also simple to open an Excel file as a stream. To do so, use an overloaded version of the constructor that takes the *Stream* object that contains the file.
## **How to Open a File with Data only**
To open a file with data only, use the [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) and [**LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadfilter) classes to set the related attribute and options of the classes for the template file to be loaded.
## **How to Load Visible Sheets only**
While loading a [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) sometimes you may only need data in visible worksheets in a workbook. Aspose.Cells allows you to skip data in invisible worksheets while loading a workbook. To do this, create a custom function that inherits the [**LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadfilter) class and pass its instance to [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) property.
Here is the implementation of the *CustomnLoad* class referenced in the above snippet.
An exception will be thrown if you try to open non-native Excel files or other file formats (for example PPT/PPTX, DOC/DOCX, etc.) by Aspose.Cells.
There are fair chances that the [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) constructor may throw *System.OutOfMemoryException* while loading large spreadsheets. This exception suggests that the available memory is insufficient to completely load the spreadsheet into the memory therefore the spreadsheet has to be loaded while enabling the Memory Preferences.
