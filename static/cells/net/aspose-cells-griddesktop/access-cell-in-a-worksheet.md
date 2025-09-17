##Access GridCell in a Worksheet
This article introduces how to get cell object (GridCell) in the Worksheet in GridDesktop.
We have discussed about working with worksheets, rows and columns so far but this is the time to go more deeper and talk about cells. So, in this topic, we would start our discussion about cells with a basic feature of accessing cells.
## **Accessing Cell in a Worksheet**
We can access any cell of a worksheet using the API of Aspose.Cells.GridDesktop. There could be three possible ways to access cell as follows:
- **Using Cell Name**
- **Using Row & Column Indices**
- **Getting Focused Cell**
Let's discuss all above three approaches one by one.
### **Using Cell Name**
All cells in a worksheet have a unique name. For example, A1, A2, B1, B2 etc. Aspose.Cells.GridDesktop allows developers to access any desired cell by using its cell name. All we have to do is to just pass the cell name (as an index) to the **Cells** collection of the **Worksheet**.
**Notice**
Access GridCell using cells[cellName] may consume more memory.it will always create a new cell (GridCell) object no matter whether the the cell is null.
### **Using Cell's Row and Column Indices**
**Best Practices**:
if we want to get the cell value or cell style and do not want to do the update operation,we can use **CheckCell** method which will return null if the cell does not exist.this will **save memory**.
~~~C#
Worksheet sheet = gridDesktop1.GetActiveWorksheet();
// Accessing a cell using its row and column indices
GridCell cell = sheet.Cells.CheckCell(1, 1);
if(cell!=null)
{
Console.WriteLine(cell.ToString());
}
~~~
A cell in a worksheet can also be recognized using its location in terms of its row and column indices. All we have to do is to just pass the row and column indices of the cell to the **Cells** collection of the **Worksheet**.
**Notice**
Access GridCell using cells[rowIndex, columnIndex] may consume more memory.it will always create a new cell (GridCell) object no matter whether the the cell is null.
### **Getting Focused Cell**
If you don't know accurately that which cell is to be accessed. Then Aspose.Cells.GridDesktop also allows you to access a cell that is currently in the focus of a user. Using this feature, you can allow a user to select any cell and then you can access that cell at the backend. It can simply be achieved by using **GetFocusedCell** method of the **Worksheet**.
**Best Practices**:
### Iterate over the cells
if we want to access all the cells in the worksheet one by one, we can use **iterators** to  traverse the existed cells. this will **save memory**.
~~~C#
Worksheet sheet = gridDesktop1.GetActiveWorksheet();
GridCells cells = sheet.Cells;
foreach (GridCell c in cells)
{
Console.WriteLine(c.ToString());
}
~~~
compare the below code which is **bad**  ,this will create all the cells object no matter whether it is null,thus will cause memory issues,so please **do not** use this way
~~~C#
Worksheet sheet = gridDesktop1.GetActiveWorksheet();
for(int r=0;r< sheet.RowsCount;r++)
{
for(int c=0;c< sheet.ColumnsCount; c++)
{
Console.WriteLine(sheet.Cells[r,c].ToString());
}
}
~~~
