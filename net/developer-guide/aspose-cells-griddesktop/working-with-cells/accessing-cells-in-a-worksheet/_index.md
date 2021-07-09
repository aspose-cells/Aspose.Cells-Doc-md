---
title: Accessing Cells in a Worksheet
type: docs
weight: 10
url: /net/accessing-cells-in-a-worksheet/
---

{{% alert color="primary" %}} 

We have discussed about working with worksheets, rows and columns so far but this is the time to go more deeper and talk about cells. So, in this topic, we would start our discussion about cells with a basic feature of accessing cells.

{{% /alert %}} 
## **Accessing Cells in a Worksheet**
We can access any cell of a worksheet using the API of Aspose.Cells.GridDesktop. There could be three possible ways to access cells as follows:

- **Using Cell Name**
- **Using Cell's Row & Column Indices**
- **Getting Focused Cell**

Let's discuss all above three approaches one by one.
### **Using Cell Name**
All cells in a worksheet have a unique name. For example, A1, A2, B1, B2 etc. Aspose.Cells.GridDesktop allows developers to access any desired cell by using its cell name. All we have to do is to just pass the cell name (as an index) to the **Cells** collection of the **Worksheet**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByName.cs" >}}
### **Using Cell's Row and Column Indices**
A cell in a worksheet can also be recognized using its location in terms of its row and column indices. All we have to do is to just pass the row and column indices of the cell to the **Cells** collection of the **Worksheet**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessByIndices.cs" >}}
### **Getting Focused Cell**
If you don't know accurately that which cell is to be accessed. Then Aspose.Cells.GridDesktop also allows you to access a cell that is currently in the focus of a user. Using this feature, you can allow a user to select any cell and then you can access that cell at the backend. It can simply be achieved by using **GetFocusedCell** method of the **Worksheet**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessingCells-AccessFocusedCell.cs" >}}
