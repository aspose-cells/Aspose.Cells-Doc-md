##Add or Insert a Worksheet
This article introduces how to add or insert worksheet in GridDesktop.
In this topic, we will discuss the techniques to add or insert worksheets in an Excel file using Aspose.Cells.GridDesktop. The difference between adding and inserting worksheets is that in addition, a worksheet is simply added at the end of the worksheets collection of the Excel file however insertion means adding a worksheet to a specific position in the worksheets collection.
## **Adding a Worksheet**
To add a worksheet using Aspose.Cells.GridDesktop, please follow the steps below:
1. Add Aspose.Cells.GridDesktop control to a form.
1. Call the Worksheet collection's Add method in the GridDesktop control.
Many overloaded versions of the Add method are available. Using the above overloaded version, for example, a worksheet is added to the Excel file with a default sheet name. Using other overloaded versions of the Add method, it is possible to define the name as shown below in the example.
## **Inserting a Worksheet**
To insert a worksheet using Aspose.Cells.GridDesktop, please follow the steps below:
1. Add the Aspose.Cells.GridDesktop control to a form.
1. Call the Worksheets collection's Insert method in the GridDesktop control.
IMPORTANT: Microsoft Excel (97-2003 XLS) supports Excel sheets with up to 65,536 rows and 256 columns. Aspose.Cells.GridDesktop follows the same standards. In the Aspose.Cells.GridDesktop control, developers can add or insert worksheets with more rows and columns than the standard limit but when they try to save the Grid data to an Excel file, an exception will be thrown. It means that only data contained in the 65,536 rows and 256 columns can be saved to an Excel XLS file using Aspose.Cells.GridDesktop, if you use XLSX (MS Excel 2007/2010) file format, there is no such limitation though.
