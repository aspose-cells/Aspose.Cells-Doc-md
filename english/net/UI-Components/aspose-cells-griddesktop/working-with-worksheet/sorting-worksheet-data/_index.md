---
title: Sorting Worksheet Data
type: docs
weight: 80
url: /net/aspose-cells-griddesktop/sorting-worksheet-data/
keywords: GridDesktop,sort,sorting,sort data,data sorting
description: This article introduces how to sort data in worksheet in GridDesktop.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Sorting is an important routine task that we often use while processing data. In this topic, we will discuss, with the help of a simple example, how we can sort data in a worksheet.

{{% /alert %}} 
## **Sorting Worksheet Data**
To sort data in a worksheet using the API of Aspose.Cells.GridDesktop, please follow the steps below:

- First of all, create a global object of **CellRange** so that it can be accessed anywhere in the scope of your class.
- Create an event handler for **SelectedCellRangeChanged** event of **GridDesktop**. The **SelectedCellRangeChanged** event is triggered every time a cell range selected by a user is changed. For example, if a user selects cells containing data to be sorted, then each time the selection range changes, this event is triggered.
- The event handler provides a **CellRangeEventArgs** argument that further provides the updated range of cells (selected by the user) in the form of a **CellRange** object. In this event handler, we will assign this **CellRange** object (containing the updated range of cells) to the global **CellRange** object so that it can also be used in other parts of the code. To make sure that we don't lose the range of cells, we will write the event handler code inside a condition.
- Now we can write some code to sort worksheet data. First of all, access the desired worksheet.
- Create a **SortRange** object that will keep the range of cells whose data is to be sorted. In the **SortRange** constructor, we can specify the worksheet, indices of start row and column, number of rows and columns to sort, orientation of sorting (like top‑to‑bottom or left‑to‑right), etc.
- Now we can call the **Sort** method of the **SortRange** object to perform the sorting of data. In the **Sort** method, we can specify the index of the column or row to be sorted and the sorting order (which can be **Ascending** or **Descending** according to your requirements).
- Finally, we can call the **Invalidate** method of **GridDesktop** to redraw the cells.

In the example given below, we demonstrate how to sort data in a column.

Create a global object of **CellRange** and handle the **SelectedCellRangeChanged** event of **GridDesktop**. Now write the code as shown below:

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-CheckingCellRange.cs" >}}

Now we write a method for **Ascending Sort**. You can create a button for **Ascending Sort** and write the code below inside its **Click** event:

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-AscendingSort.cs" >}}

Finally, we write some code to achieve **Descending Sort** functionality. Create a **Descending Sort** button and write the code below inside its **Click** event:

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-DescendingSort.cs" >}}
