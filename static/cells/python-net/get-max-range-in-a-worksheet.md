##Get Max Range In A Worksheet
This article describes how to get the max range , max data range, max display range of Excel files with Aspose.Cells for Python via .NET library.
When reading data from the worksheet, we need to know the maximum area.
When copying all data from a worksheet, we need to know the maximum area.
When exporting a specified area to html and pdf, we need to know the maximum area.
Aspose.Cells for Python via .NET contains different ways to find max range in a worksheet.
## **How to Get Max Range**
In Aspose.Cells for Python via .NET ,if the [**row**](https://reference.aspose.com/cells/python-net/aspose.cells/row) and [**column**](https://reference.aspose.com/cells/python-net/aspose.cells/column) objects are initialized, these rows and columns will be counted to the maximum area, even if there is no data in empty rows or columns.
## **How to Get Max Data Range**
In most cases, we only need to obtain all the ranges containing all the data, even if the empty cells outside the range are formatted.
And the settings about shapes, tables and pivottables will be ignored.
## **How to Get Max Display Range**
When we export all data from the worksheet to HTML, PDF, or images, we need to obtain an area containing all visible objects, including data, styles, graphics, tables, and pivot tables.
The following codes show how to render the max diplay range to html:
Here is [source excel file](Book1.xlsx).
