##Advanced Protection Settings since Excel XP
Since the release of Excel 2002 or XP, Microsoft has added many advanced protection settings.
## **Introduction**
These protection settings restrict or allow users to:
- Delete rows or columns.
- Edit contents, objects or scenarios.
- Format cells, rows or columns.
- Insert rows, columns or hyperlinks.
- Select locked or unlocked cells.
- Use pivot tables and much more.
Aspose.Cells supports all the advanced protection settings offered by Excel XP or later versions.
### **Advanced Protection Settings Using Excel XP and Later Versions**
To view the protection settings available in Excel XP:
1. From the **Tools** menu, select **Protection** followed by **Protect Sheet**. A dialog will be displayed.
To view the protection settings available in Excel 2016
1. From the **File** menu, select **Protect Workbook** followed by **Protect Current Sheet**.
1. Select the **Protect Sheet** in the **Review** menu.
Following the steps mention above will show a dialog where you can allow or restrict worksheets features or apply a password to the worksheet.
### **Advanced Protection Settings Using Aspose.Cells**
Aspose.Cells supports all of the advanced protection settings.
Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class.
The [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class provides the [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) property that is used to apply these advanced protection settings. The [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) property is in fact an object of the [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection) class that encapsulates several Boolean properties for disabling or enabling restrictions.
Below is a small example application. It opens an Excel file and uses most of the advanced protection settings supported by Excel XP and later versions.
Please don't call the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class' [**Protect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) method when using the [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) property. Also, save the file to Excel97To2003 or Xlsx format because the advanced protection settings are only supported by Excel XP and later versions.
### **Cell Locking Issue**
If you want to restrict users from editing cells the cells must be locked before any protection settings are applied. Otherwise, the cells can be edited even if the worksheet is protected. In Microsoft Excel XP, cells can be locked through the following dialog:
|**Dialog to lock cells in Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|
It is possible to lock cells using the Aspose.Cells API too. Each cell can get [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) formatting that contains a Boolean property, [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked). Set the [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) property to **true** or **false** to lock or unlock the cell.
