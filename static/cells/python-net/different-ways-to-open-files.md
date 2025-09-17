##Different Ways to Open Files
This article explains how to open an excel file using Aspose.Cells for Python via .NET API.
With Aspose.Cells for Python via .NET it is simple to open files, for example, to retrieve data, or to use a designer template to speed up the development process.
## **How to Open an Excel File via a Path**
Developers can open a Microsoft Excel file using its file path on the local computer by specifying it in the [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class constructor. Simply pass the path in the constructor as a *string*. Aspose.Cells for Python via .NET will automatically detect the file format type.
## **How to Open an Excel File via a Stream**
It is also simple to open an Excel file as a stream. To do so, use an overloaded version of the constructor that takes the *Stream* object that contains the file.
## **How to Open a File with Data only**
To open a file with data only, use the [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) and [**LoadFilter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter) classes to set the related attribute and options of the classes for the template file to be loaded.
