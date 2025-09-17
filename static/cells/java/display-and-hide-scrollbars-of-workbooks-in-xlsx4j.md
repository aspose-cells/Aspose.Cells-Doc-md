##Display and Hide Scrollbars of Workbooks in xlsx4j
## **Aspose.Cells - Display and Hide Scrollbars of Workbooks**
Aspose.Cells provides a class, **Workbook** that represents an Excel file. **Workbook** class provides a wide range of properties and methods to manage an Excel file. But, to control the visibility of the scroll bars in the Excel file, developers may use **setVScrollBarVisible** & **setHScrollBarVisible** methods of the **Workbook** class.
**Java**
//Instantiating a Excel object by excel file path
Workbook workbook = new Workbook(dataDir + "book1.xls");
//Hiding the vertical scroll bar of the Excel file
workbook.getSettings().setVScrollBarVisible(false);
//Hiding the horizontal scroll bar of the Excel file
workbook.getSettings().setHScrollBarVisible(false);
//Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(dataDir + "AsposeSrollbarsHide.xls");
// ===============================================================
//Displaying the vertical scroll bar of the Excel file
workbook.getSettings().setVScrollBarVisible(true);
//Displaying the horizontal scroll bar of the Excel file
workbook.getSettings().setHScrollBarVisible(true);
//Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(dataDir + "AsposeDisplaySrollbars.xls");
## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/displayandhidescrollbars/AsposeDisplayAndHideScrollbars.java)
