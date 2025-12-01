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

Sorting is an important routine task that we mostly use while processing data. In this topic, we will discuss with the help of a simple example that how can we sort data in a worksheet.

{{% /alert %}} 
## **Sorting Worksheet Data**
To sort data in a worksheet using the API of Aspose.Cells.GridDesktop, please follow the steps below:

- First of all create a global object of **CellRange** so that it can be accessed anywhere in the scope of your class
- Create an event handler for **SelectedCellRangeChanged** event of **GridDesktop**. **SelectedCellRangeChanged** event is triggered every time when a cell range selected by a user is changed. For example, if a user selects cells (containing data to be sorted) then every time his range of selection would change, this event would be triggered.
- The event handler provides **CellRangeEventArgs** argument that further provides the update range of cells (selected by user) in the form of a **CellRange** object. So, in this event handler, we will assign this **CellRange** object (containing updated range of cells) to the global **CellRange** object so that it can also be used in other part of the code. To make sure that we don't lost the range of cells, we will write event handler code inside a condition
- Now we can write some code to sort worskheet data. First of all, access a desired worksheet
- Create a **SortRange** object that will keep the range of cells whose data is to be sorted. In **SortRange** constructor, we can specify the worksheet, indices of start row and column, number of rows and columns to sort, orientation of sorting (like top to bottom or left to right) etc.
- Now we can call **Sort** method of **SortRange** object to perform the sorting of data. In **Sort** method, we can specify the index of column or row to be sorted and sorting order (that can be **Ascending** or **Descending** according to your requirements)
- Finally, we can call **Invalidate** method of **GridDesktop** to redraw cells.

In the example given below, we have demonstrated about how to sort data in a column.

Create a global object of CellRange and **SelectedCellRangeChanged** event of GridDesktop. Now write the code like given below:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-CheckingCellRange.cs" >}}


Now we write method for **Ascending Sort**. You can create a button for **Ascending Sort** and write below code inside its **Click** Event.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-AscendingSort.cs" >}}


Finally, we write some code to achieve **Descending Sort** functionality. Create a **Descending Sort** button and write below code inside its **Click** Event.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-DescendingSort.cs" >}}
