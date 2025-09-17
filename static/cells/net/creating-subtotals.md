##Creating Subtotals
Learn how to create subtotals for any repeating values in a spreadsheet by using the Aspose.Cells for .NET API.
You can automatically create subtotals for any repeating values in a spreadsheet. Aspose.Cells provides API features that help you add subtotals to spreadsheets programmatically.
## **Using Microsoft Excel**
To add subtotals in Microsoft Excel:
1. Create a simple data list in the first worksheet of the workbook (as shown in the figure below) and save the file as Book1.xls.
1. Select any cell within your list.
1. From the **Data** menu, select **Subtotals**. The Subtotals dialog will be displayed. Define what function to use and where to place the subtotals.
## **Using the Aspose.Cells API**
Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file.
A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class. The class provides a wide range of properties and methods for managing worksheets and other objects. Each worksheet consists of a [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) collection. To add subtotals to a worksheet, use the [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) class' [**Subtotal**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/subtotal/index) method. Provide parameter values to the method to specify how the subtotal should be calculated and placed.
In the examples below, we have added subtotals to the first worksheet of the template file (Book1.xls) using the Aspose.Cells API. When the code is executed, a worksheet with subtotals is created.
The code snippets that follow show how to add subtotals to a worksheet with Aspose.Cells for .NET.
## **Advance topics**
- [Applying Subtotal and Changing Direction of Outline Summary Rows below Detail](https://docs.aspose.com/cells/net/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
