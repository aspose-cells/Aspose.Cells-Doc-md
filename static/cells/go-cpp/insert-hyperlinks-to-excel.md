##Insert Hyperlinks into Excel or OpenOffice with Golang via C++
How to insert hyperlinks into Excel file with Aspose.Cells library without MS Excel using C++.
A hyperlink is used to create a link between two entities. Everybody is familiar with the use of hyperlinks, especially on websites.
Using Aspose.Cells, developers can create different kinds of hyperlinks in Microsoft Excel files. This topic discusses what types of hyperlinks are supported by Aspose.Cells and how they can be used in our Excel files.
## **Adding Hyperlinks**
Aspose.Cells allows developers to add hyperlinks to Excel files either using the API or designer spreadsheets (spreadsheets where hyperlinks are created manually and Aspose.Cells is used to import them into other spreadsheets).
Aspose.Cells provides a class, [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) that represents a Microsoft Excel file. The [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) class contains a [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides different methods for adding different hyperlinks to Excel files.
## **Adding Link to a URL**
The [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) class contains a [GetHyperlinks()](https://reference.aspose.com/cells/go-cpp/worksheet/gethyperlinks/) collection. Each item in the [GetHyperlinks()](https://reference.aspose.com/cells/go-cpp/worksheet/gethyperlinks/) collection represents a [Hyperlink](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/). Add hyperlinks to URLs by calling the [Hyperlinks](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/) collection's [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) method. The [Add](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlinkcollection/add/) method takes the following parameters:
- Cell name, the name of the cell the hyperlink will be added to.
- Number of rows, the number of rows in this hyperlink range.
- Number of columns, the number of columns in this hyperlink range.
- URL, the URL address.
In the above example, a hyperlink is added to a URL in an empty cell, **A1**. In such cases, if a cell is empty then the URL address is also added to that empty cell as its value. If the cell is not empty and a hyperlink is added, the value of the cell looks like plain text. To make it look like a hyperlink, apply the appropriate formatting settings on that cell.
## **Adding a Link to a Cell in the Same File**
It is possible to add hyperlinks to cells in the same Excel file by calling the [Hyperlinks](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/) collection's [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) method. The [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) method works for both internal and external hyperlinks. One version of the overloaded method takes the following parameters:
- Cell name, the name of the cell the hyperlink will be added to.
- Number of rows, the number of rows in this hyperlink range.
- Number of columns, the number of columns in this hyperlink range.
- URL, the address of the target cell.
## **Adding a Link to an External File**
It is possible to add hyperlinks to external Excel files by calling the [Hyperlinks](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/) collection's [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) method. The [Add](https://reference.aspose.com/cells/go-cpp/hyperlinkcollection/add/) method takes the following parameters:
- Cell name, the name of the cell the hyperlink will be added to.
- Number of rows, the number of rows in this hyperlink range.
- Number of columns, the number of columns in this hyperlink range.
- URL, the address of the target, external Excel file.
## **Advance topics**
- [Add Image Hyperlinks](https://docs.aspose.com/cells/cpp/add-image-hyperlinks/)
- [Detect Hyperlink Type](https://docs.aspose.com/cells/cpp/detect-hyperlink-type/)
- [Editing Hyperlinks of Worksheet](https://docs.aspose.com/cells/cpp/editing-hyperlinks-of-worksheet/)
- [Get Hyperlinks in Range](https://docs.aspose.com/cells/cpp/get-hyperlinks-in-range/)
