---
title: Manage Worksheets
type: docs
weight: 10
url: /pythonjava/manage-worksheets/
---

Managing worksheets using Aspose.Cells for Python via Java is very easy. In this article, we will demonstrate added, accessing, and removing worksheets using the Aspose.Cells API.
## **Adding Worksheets to a New Excel File**
To create a new Workbook, create an object of the [Workbook](https://apireference.aspose.com/cells/python/asposecells.api/Workbook) class. The [Workbook](https://apireference.aspose.com/cells/python/asposecells.api/Workbook) class represents an Excel file. Then by using the [add](https://apireference.aspose.com/cells/python/asposecells.api/worksheetcollection#add\(\)) method of the [WorksheetCollection](https://apireference.aspose.com/cells/python/asposecells.api/worksheetcollection), new worksheets are added to the Excel file. Finally, to save the newly created Excel file, call the [save](https://apireference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String\)) method of the [Workbook](https://apireference.aspose.com/cells/python/asposecells.api/Workbook) class.

The following code snippet demonstrates creating a new Excel file and adding a worksheet to it.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToNewExcelFile.py" >}}
## **Adding Worksheets to a Designer Spreadsheet**
Adding worksheets to a designer spreadsheet is exactly the same as adding the worksheet to a new Excel file. The only difference is that instead of creating a new Excel file, we open an existing file by the [Workbook](https://apireference.aspose.com/cells/python/asposecells.api/Workbook) class.

The following code snippet demonstrates adding a worksheet to a designer spreadsheet.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToDesignerSpreadsheet.py" >}}
## **Accessing Worksheets using Sheet Name**
After loading a workbook, developers can access any worksheet by using its index or name. The following code snippet demonstrates accessing a worksheet by using its name.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AccessingWorksheetsUsingSheetName.py" >}}
## **Removing Worksheets**
There may be times when some sheets meet to be removed from the workbook. For this, the API provides the [WorksheetCollection.removeAt](https://apireference.aspose.com/cells/python/asposecells.api/worksheetcollection#removeAt\(int\)) method. You can pass it sheet index or sheet name of the sheet to be removed. The following examples demonstrate removing worksheets by using the sheet index and sheet name.
### **Removing Worksheets using Sheet Index**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetIndex.py" >}}
### **Removing Worksheets using Sheet Name**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetName.py" >}}
