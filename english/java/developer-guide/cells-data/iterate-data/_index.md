---
title: How and Where to Use Iterators
linktitle: Iterate Data
type: docs
weight: 640
url: /java/how-and-where-to-use-iterators/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

An object of an iterator interface can be used to traverse through all elements of a collection. Iterators can be used to inspect the data in a collection, but they cannot be used to modify the underlying collection. In general, to use an iterator to cycle through the contents of a collection, the following steps have to be taken:

1. Obtain an iterator to the start of the collection by calling the collection's `iterator` method.  
2. Set up a loop that makes a call to the `hasNext` method. Have the loop iterate as long as the `hasNext` method returns true.  
3. Within the loop, obtain each element by calling the `next` method.  

Aspose.Cells APIs provide a number of iterators; however, this article mainly discusses the three types listed below.

1. Cells Iterator  
1. Rows Iterator  
1. Columns Iterator  

{{% /alert %}} 

## **How to use Iterators**
### **Cells Iterator**
There are various ways to access the cells iterator, and one can use any of these methods based on the application requirements. Here are the methods that return the cells iterator.

1. `Cells.iterator`  
1. `Row.iterator`  
1. `Range.iterator`  

All of the above‑mentioned methods return an iterator that allows traversal of the collection of cells that have been initialized.

{{% alert color="primary" %}} 

While traversing the cells, the collection should not be modified (operations that will cause a new Cell to be instantiated or an existing Cell to be deleted). Otherwise, the iterator may not be able to traverse all cells correctly (some elements may be traversed repeatedly or skipped).

{{% /alert %}} 

The following code example demonstrates the implementation of the Iterator class for a cells collection.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CellsIterator-CellsIterator.java" >}}

##### **Rows Iterator**
The Rows Iterator can be accessed via the `RowCollection.iterator` method. The following code example demonstrates the implementation of the Iterator for the `RowCollection` class.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RowsIterator-RowsIterator.java" >}}

##### **Columns Iterator**
The Columns Iterator can be accessed via the `ColumnCollection.iterator` method. The following code example demonstrates the implementation of the Iterator for the `ColumnCollection` class.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ColumnsIterator-ColumnsIterator.java" >}}

#### **Where to use Iterators**
In order to discuss the advantages of using iterators, **let's** take a real‑time example.

##### **Scenario**
An application requirement is to traverse all cells in a given worksheet to read their values. Several ways can be used to achieve this goal; a few are demonstrated below.

###### **Using Display Range**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingDisplayRange-UsingDisplayRange.java" >}}

###### **Using MaxDataRow & MaxDataColumn**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingMaxDataRowAndMaxDataColumn-UsingMaxDataRowAndMaxDataColumn.java" >}}

As you can observe, both of the above‑mentioned approaches use more or less similar logic, that is, loop over all cells in the collection to read the cell values. This could be problematic for a number of reasons, as discussed below.

1. APIs such as `MaxRow`, `MaxDataRow`, `MaxColumn`, `MaxDataColumn` & `MaxDisplayRange` require extra time to gather the corresponding statistics. In case the data matrix (rows × columns) is large, using these APIs could impose a performance penalty.  
2. In most cases, not all cells in a given range are instantiated. In such situations, checking every cell in the matrix is not as efficient as checking only the initialized cells.  
3. Accessing a cell in a loop as `Cells.get(rowIndex, columnIndex)` will cause all cell objects in a range to be instantiated, which may eventually cause an `OutOfMemoryError`.

##### **Conclusion**
Based on the above‑mentioned facts, the following are possible scenarios where iterators should be used.

1. Read‑only access of the cell collection is required, i.e., the requirement is to only inspect the cells.  
2. A large number of cells are to be traversed.  
3. Only initialized cells/rows/columns are to be traversed.

{{< app/cells/assistant language="java" >}}
