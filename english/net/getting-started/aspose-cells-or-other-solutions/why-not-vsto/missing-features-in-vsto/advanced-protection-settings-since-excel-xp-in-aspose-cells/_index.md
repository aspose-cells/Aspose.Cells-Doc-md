---
title: Advanced Protection Settings since Excel XP in Aspose.Cells
type: docs
weight: 20
url: /net/advanced-protection-settings-since-excel-xp-in-aspose-cells/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

- Delete rows or columns.
- Edit contents, objects, or scenarios.
- Insert rows, columns, or hyperlinks.
- Select locked or unlocked cells.
- Use pivot tables and much more.

Aspose.Cells supports all the advanced protection settings offered by Excel XP or later versions.

{{% /alert %}}

## **Advanced Protection Settings Using Excel XP and Later Versions**

To view the protection settings available in Excel XP:

1. From the **Tools** menu, select **Protection** followed by **Protect Sheet**.  
   A dialog is displayed.

   **Dialog to show protection options in Excel XP**

   ![todo:image_alt_text](advanced-protection-settings-since-excel-xp-in-aspose-cells_1.png)

2. Allow or restrict worksheet features or apply a password.

### **Advanced Protection Settings Using Aspose.Cells**

Aspose.Cells supports all of the advanced protection settings.

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) class contains a [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class.

The [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class provides the [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) property that is used to apply these advanced protection settings. The [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection) property is, in fact, an object of the [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection) class that encapsulates several Boolean properties for disabling or enabling restrictions.

Below is a small example application. It opens an Excel file and uses most of the advanced protection settings supported by Excel XP and later versions.

**C#**

{{< highlight csharp >}}
 // Creating a file stream containing the Excel file to be opened
 FileStream fstream = new FileStream("book1.xls", FileMode.Open);

 // Instantiating a Workbook object
 // Opening the Excel file through the file stream
 Workbook excel = new Workbook(fstream);

 // Accessing the first worksheet in the Excel file
 Worksheet worksheet = excel.Worksheets[0];

 // Restrict users from deleting columns in the worksheet
 worksheet.Protection.AllowDeletingColumn = false;

 // Restrict users from deleting rows in the worksheet
 worksheet.Protection.AllowDeletingRow = false;

 // Restrict users from editing contents of the worksheet
 worksheet.Protection.AllowEditingContent = false;

 // Restrict users from editing objects of the worksheet
 worksheet.Protection.AllowEditingObject = false;

 // Restrict users from editing scenarios of the worksheet
 worksheet.Protection.AllowEditingScenario = false;

 // Restrict users from filtering
 worksheet.Protection.AllowFiltering = false;

 // Allow users to format cells in the worksheet
 worksheet.Protection.AllowFormattingCell = true;

 // Allow users to format rows in the worksheet
 worksheet.Protection.AllowFormattingRow = true;

 // Allow users to format columns in the worksheet
 worksheet.Protection.AllowFormattingColumn = true;

 // Allow users to insert hyperlinks in the worksheet
 worksheet.Protection.AllowInsertingHyperlink = true;

 // Allow users to insert rows in the worksheet
 worksheet.Protection.AllowInsertingRow = true;

 // Allow users to select locked cells in the worksheet
 worksheet.Protection.AllowSelectingLockedCell = true;

 // Allow users to select unlocked cells in the worksheet
 worksheet.Protection.AllowSelectingUnlockedCell = true;

 // Allow users to sort
 worksheet.Protection.AllowSorting = true;

 // Allow users to use pivot tables in the worksheet
 worksheet.Protection.AllowUsingPivotTable = true;

 // Saving the modified Excel file
 excel.Save("output.xls", SaveFormat.Excel97To2003);

 // Closing the file stream to free all resources
 fstream.Close();
{{< /highlight >}}

## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Advanced%20Protection%20Settings)

## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
