---
title: Access GridCell in a Worksheet
type: docs
weight: 10
url: /net/aspose-cells-griddesktop/access-cell-in-a-worksheet/
keywords: GridDesktop,GridCell,get cell
description: This article introduces how to get cell object (GridCell) in the Worksheet in GridDesktop.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

We have discussed working with worksheets, rows, and columns so far, but now it's time to go deeper and talk about cells. So, in this topic, we would start our discussion about cells with a basic feature of accessing cells.

{{% /alert %}} 

## **Accessing Cells in a Worksheet**
We can access any cell of a worksheet using the API of Aspose.Cells.GridDesktop. There are three possible ways to access a cell, as follows:

- **Using Cell Name**
- **Using Row & Column Indices**
- **Getting Focused Cell**

Let's discuss all three approaches one by one.

### **Using Cell Name**
All cells in a worksheet have a unique name, for example, A1, A2, B1, B2, etc. Aspose.Cells.GridDesktop allows developers to access any desired cell by using its cell name. All we have to do is simply pass the cell name (as an index) to the **Cells** collection of the **Worksheet**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByName.cs" >}}

**Notice**

Accessing a GridCell using `cells[cellName]` may consume more memory. It will always create a new cell (GridCell) object regardless of whether the cell is null.

### **Using Cell's Row and Column Indices**

**Best Practices**:

If we want to get the cell value or cell style and do not want to perform an update operation, we can use the **CheckCell** method, which will return null if the cell does not exist. This will **save memory**.

```csharp
Worksheet sheet = gridDesktop1.GetActiveWorksheet();
// Accessing a cell using its row and column indices
GridCell cell = sheet.Cells.CheckCell(1, 1);
if (cell != null)
{
    Console.WriteLine(cell.ToString());
}
```

A cell in a worksheet can also be recognized using its location in terms of its row and column indices. All we have to do is simply pass the row and column indices of the cell to the **Cells** collection of the **Worksheet**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByIndices.cs" >}}

**Notice**

Accessing a GridCell using `cells[rowIndex, columnIndex]` may consume more memory. It will always create a new cell (GridCell) object regardless of whether the cell is null.

### **Getting Focused Cell**
If you don't know exactly which cell is to be accessed, Aspose.Cells.GridDesktop also allows you to access the cell that is currently in focus for the user. Using this feature, you can let a user select any cell and then access that cell on the backend. It can simply be achieved by using the **GetFocusedCell** method of the **Worksheet**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessFocusedCell.cs" >}}

**Best Practices**:
### Iterate over the cells
If we want to access all the cells in the worksheet one by one, we can use **iterators** to traverse the existing cells. This will **save memory**.

```csharp
Worksheet sheet = gridDesktop1.GetActiveWorksheet();

GridCells cells = sheet.Cells;
foreach (GridCell c in cells)
{
    Console.WriteLine(c.ToString());
}
```

Compare the code below, which is **bad**; it will create all cell objects regardless of whether they are null, thus causing memory issues, so please **do not** use this approach.

```csharp
Worksheet sheet = gridDesktop1.GetActiveWorksheet();
for (int r = 0; r < sheet.RowsCount; r++)
{
    for (int c = 0; c < sheet.ColumnsCount; c++)
    {
        Console.WriteLine(sheet.Cells[r, c].ToString());
    }
}
```
