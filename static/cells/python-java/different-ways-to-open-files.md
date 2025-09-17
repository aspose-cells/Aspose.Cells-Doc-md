##Different Ways to Open Files
With Aspose.Cells it is simple to open files, for example, to retrieve data, or to use a designer template to speed up the development process.
## **Opening a File via a Path**
Developers can open a Microsoft Excel file using its file path on the local computer by specifying it in the [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook) class constructor. Simply pass the path in the constructor as a *string*. Aspose.Cells will automatically detect the file format type.
## **Opening a File via a Stream**
It is also simple to open an Excel file as a stream. To do so, use an overloaded version of the constructor that takes the *BufferStream* object that contains the file.
## **Opening a File with Data only**
To open a file with data only, use the [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) and [**LoadFilter**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadFilter) classes to set the related attribute and options of the classes for the template file to be loaded.
An exception will be thrown if you try to open non-native Excel files or other file formats (for example PPT/PPTX, DOC/DOCX, etc.) by Aspose.Cells.
There are fair chances that the [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook) constructor may throw *System.OutOfMemoryException* while loading large spreadsheets. This exception suggests that the available memory is insufficient to completely load the spreadsheet into the memory therefore the spreadsheet has to be loaded while enabling the Memory Preferences.
