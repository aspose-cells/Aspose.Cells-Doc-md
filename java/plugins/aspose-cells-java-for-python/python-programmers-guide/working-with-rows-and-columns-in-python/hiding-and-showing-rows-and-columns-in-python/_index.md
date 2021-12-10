---
title: Hiding and Showing Rows and Columns in Python
type: docs
weight: 50
url: /java/hiding-and-showing-rows-and-columns-in-python/
---

## **Aspose.Cells - Controlling the Visibility of Rows & Columns**
### **Hiding Rows and Columns**
Developers can hide a row or column by calling the HideRow and HideColumn methods of the Cells collection respectively. Both methods take the row/column index as a parameter to hide the specific row or column.

**Ruby Code**

{{< highlight ruby >}}

 def hide_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Hiding the 3rd row of the worksheet

cells.hideRow(2)

\# Hiding the 2nd column of the worksheet

cells.hideColumn(1)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Hide Rows And Columns.xls")

print "Hide Rows And Columns Successfully." 

{{< /highlight >}}
### **Showing Rows and Columns**
Developers can unhide any hidden row or column by calling the UnhideRow and UnhideColumn methods of the Cells collection respectively. Both methods take two parameters:

- **Rowor column index** - the index of a row or column that is used to show the specific row or column.
- **Row height or column width** - the row height or column width assigned to the row or column after it's shown.

**Ruby Code**

{{< highlight ruby >}}

 def unhide_rows_columns(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

\# Unhiding the 3rd row and setting its height to 13.5

cells.unhideRow(2,13.5)

\# Unhiding the 2nd column and setting its width to 8.5

cells.unhideColumn(1,8.5)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Unhide Rows And Columns.xls")

print "Unhide Rows And Columns Successfully." 

{{< /highlight >}}
## **Download Running Code**
Download **Controlling the Visibility of Rows & Columns (Aspose.Cells)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
- [CodePlex](https://asposecellsjavapython.codeplex.com/releases/view/620185)
