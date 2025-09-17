##Grouping and Ungrouping Rows and Columns in Python
Learn how to Group and Ungroup Rows and Columns through the Aspose.Cells for Python Via Java API.
## **Group and Ungroup Management of Rows & Columns in Aspose.Cells for Python via Java**
### **How to Group Rows & Columns in Python**
It is possible to group rows or columns by calling the groupRows and groupColumns methods of the Cells collection. Both methods take the following parameters:
- First row/column index, the first row or column in the group.
- Last row/column index, the last row or column in the group.
- Is hidden, a Boolean parameter that specifies whether to hide rows/columns after grouping or not.
**Python Code**
def group_rows_columns(self):
\# Instantiating a Workbook object by excel file path
workbook = self.Workbook(self.dataDir + 'Book1.xls')
\# Accessing the first worksheet in the Excel file
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
\# Grouping first six rows (from 0 to 5) and making them hidden by passing true
cells.groupRows(0,5,True)
\# Grouping first three columns (from 0 to 2) and making them hidden by passing true
cells.groupColumns(0,2,True)
\# Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(self.dataDir + "Group Rows And Columns.xls")
print "Group Rows And Columns Successfully."
### **How to Ungroup Rows & Columns using Python**
Ungroup grouped rows or columns by calling the Cells collection's UngroupRows and UngroupColumns methods. Both methods take the same parameters:
- First row or column index, the first row/column to be ungrouped.
- Last row or column index, the last row/column to be ungrouped.
**Python Code**
def ungroup_rows_columns(self):
\# Instantiating a Workbook object by excel file path
workbook = self.Workbook(self.dataDir + 'Group Rows And Columns.xls')
\# Accessing the first worksheet in the Excel file
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
\# Ungrouping first six rows (from 0 to 5)
cells.ungroupRows(0,5)
\# Ungrouping first three columns (from 0 to 2)
cells.ungroupColumns(0,2)
\# Saving the modified Excel file in default (that is Excel 2003) format
workbook.save(self.dataDir + "Ungroup Rows And Columns.xls")
print "Ungroup Rows And Columns Successfully."
## **Download Running Code**
Download **Group & Ungroup Rows & Columns (Aspose.Cells)** from any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
