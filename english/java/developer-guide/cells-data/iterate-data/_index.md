---
title: How and Where to Use Iterators
linktitle: Iterate Data
type: docs
weight: 640
url: /java/how-and-where-to-use-iterators/
---

{{% alert color="primary" %}} 

An object of an iterator interface can be used to traverse through all elements of a collection. Iterators can be used to inspect the data in a collection but they cannot be used to modify the underlying collection. In general, to use an iterator to cycle through the contents of a collection, following steps have to be taken:

1. Obtain an iterator to the start of the collection by calling the collection's iterator method.
1. Set up a loop that makes a call to hasNext method. Have the loop iterate as long as hasNext method returns true.
1. Within the loop, obtain each element by calling next method.

Aspose.Cells APIs provide a bunch of iterators, however, this article mainly discusses the three types as listed below.

1. Cells Iterator
1. Rows Iterator
1. Columns Iterator

{{% /alert %}} 
## **How to use Iterators**
### **Cells Iterator**
There are various ways to access the cells' iterator, and one can use any of these methods based on the application requirements. Here are the methods that return the cells' iterator.

1. Cells.iterator
1. Row.iterator
1. Range.iterator

All of the above mentioned methods return the iterator that allows to traverse the collection of cells which have been initialized.

{{% alert color="primary" %}} 

While traversing the cells, the collection should not be modified (operations that will cause a new Cell to be instantiated or existing Cell to be deleted). Otherwise the iterator may not be able to traverse all cells correctly (some elements may be traversed repeatedly or skipped).

{{% /alert %}} 

The following code example demonstrates the implementation of the Iterator class for a cells collection.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CellsIterator-CellsIterator.java" >}}




##### **Rows Iterator**
The Rows Iterator can be accessed while using the RowCollection.iterator method. The following code example demonstrates the implementation of the Iterator for RowCollection class.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RowsIterator-RowsIterator.java" >}}




##### **Columns Iterator**
The Columns Iterator can be accessed while using the ColumnCollection.iterator method. The following code example demonstrates the implementation of the Iterator for ColumnCollection class.





{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ColumnsIterator-ColumnsIterator.java" >}}




#### **Where to use Iterators**
In order to discuss the advantages of using iterators, lets take a real time example.
##### **Scenario**
An application requirement is to traverse all cells in a given Worksheet to read their values. There could be several ways to implement this goal. A few are demonstrated below.
###### **Using Display Range**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDisplayRange-UsingDisplayRange.java" >}}




###### **Using MaxDataRow & MaxDataColumn**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingMaxDataRowAndMaxDataColumn-UsingMaxDataRowAndMaxDataColumn.java" >}}





As you can observe that both of the above mentioned approaches use more or less similar logic, that is; loop over all cells in the collection to read the cell values. This could be problematic for a number of reasons as discussed below.

1. The APIs such as MaxRow, MaxDataRow, MaxColumn, MaxDataColumn & MaxDisplayRange require extra time to gather the corresponding statistics. In case the data matrix (rows x columns) is large, using these APIs could impose performance penalty.
1. In most of the cases, not all cells in a given range are instantiated. In such situations to check every cell in the matrix is not so efficient as compared to check only the initialized cells.
1. Accessing a cell in a loop as Cells.get(rowIndex, columnIndex) will cause all cell objects in a range to be instantiated, which may eventually cause OutOfMemoryError.
##### **Conclusion**
Based on above mentioned facts, following are the possible scenarios where iterators should be used.

1. Readonly access of the cell collection is required, that is; requirement is to only inspect the cells.
1. Large number of cells are to be traversed.
1. Only initialized cells/rows/columns are to be traversed.
{{< app/cells/assistant language="java" >}}