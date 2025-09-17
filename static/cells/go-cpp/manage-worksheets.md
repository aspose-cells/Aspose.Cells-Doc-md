##Manage Worksheets
Developers can easily create and manage worksheets in Microsoft Excel files programmatically using Aspose.Cells flexible API. This topic describes approaches for adding and removing worksheets in Microsoft Excel files.
Aspose.Cells provides a class [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) that represents an Excel file. The [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) class contains a [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) collection that allows access to each worksheet in the Excel file.
A worksheet is represented by the [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) class. The [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) class provides a wide range of methods for managing worksheets.
## **Adding Worksheets to a New Excel File**
To create a new Excel file programmatically:
1. Create an object of the [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) class.
1. Call the [Add](https://reference.aspose.com/cells/go-cpp/worksheetcollection/add_string/) method of the [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) collection. An empty worksheet is added to the Excel file automatically. It can be referenced by passing the sheet index of the new worksheet to the [WorksheetCollection](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) collection.
1. Obtain a worksheet reference.
1. Perform work on the worksheets.
1. Save the new Excel file with new worksheets by calling the [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) class [Save](https://reference.aspose.com/cells/go-cpp/workbook/save_string/) method.
## **Accessing Worksheets using Sheet Index**
The following sample code shows how to access or get any worksheet by specifying its index.
## **Removing Worksheets using Sheet Index**
Removing worksheets by name works well when the name of the worksheet is known. If you don't know the worksheet's name, use an overloaded version of the [RemoveAt](https://reference.aspose.com/cells/go-cpp/worksheetcollection/removeat) method that takes the sheet index of the worksheet instead of its sheet name.
