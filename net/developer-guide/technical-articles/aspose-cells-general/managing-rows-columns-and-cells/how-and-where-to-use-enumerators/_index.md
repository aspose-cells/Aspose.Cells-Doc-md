---
title: How and Where to Use Enumerators
type: docs
weight: 290
url: /net/how-and-where-to-use-enumerators/
---

{{% alert color="primary" %}}

An enumerator is an object that provides the ability to traverse a container or a collection. Enumerators can be used to read the data in the collection, but they cannot be used to modify the underlying collection, whereas IEnumerable is an interface that defines one method GetEnumerator which returns an IEnumerator interface, this, in turn, allows read-only access to a collection.

Aspose.Cells APIs provide a bunch of enumerators however, this article mainly discusses the three types as listed below.

1. Cells Enumerator
1. Rows Enumerator
1. Columns Enumerator

{{% /alert %}}

## **How to use Enumerators**

### **Cells Enumerator**

There are various ways to access the Cells Enumerator, and one can use any of these methods based on the application requirements. Here are the methods that return the cells enumerator.

1. [**Cells.GetEnumerator**](https://apireference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)
1. [**Row.GetEnumerator**](https://apireference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)
1. [**Range.GetEnumerator**](https://apireference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

All of the above-mentioned methods return the enumerator that allows traversing the collection of cells which have been initialized.

{{% alert color="primary" %}}

While traversing the cells, the collection should not be modified (operations that will cause a new Cell to be instantiated or existing Cell to be deleted). Otherwise, the enumerator may not be able to traverse all cells correctly (some elements may be traversed repeatedly or skipped).

{{% /alert %}}

The following code example demonstrates the implementation of the IEnumerator interface for a Cells collection.

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

### **Rows Enumerator**

The Rows Enumerator can be accessed while using the [**RowCollection.GetEnumerator**](https://apireference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator) method. The following code example demonstrates the implementation of the IEnumerator interface for [**RowCollection**](https://apireference.aspose.com/cells/net/aspose.cells/rowcollection).

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

### **Columns Enumerator**

The Columns Enumerator can be accessed while using the [**ColumnCollection.GetEnumerator**](https://apireference.aspose.com/cells/net/aspose.cells/columncollection) method. The following code example demonstrates the implementation of the IEnumerator interface for [**ColumnCollection**](https://apireference.aspose.com/cells/net/aspose.cells/columncollection).

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

## **Where to use Enumerators**

In order to discuss the advantages of using enumerators, let's take a real time example.

**Scenario**

An application requirement is to traverse all cells in a given [**Worksheet**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet) to read their values. There could be several ways to implement this goal. A few are demonstrated below.

### **Using Display Range**

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

### **Using MaxDataRow & MaxDataColumn**

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

As you can observe that both of the above-mentioned approaches use more or less similar logic, that is; loop over all cells in the collection to read the cell values. This could be problematic for a number of reasons as discussed below.

1. APIs such as [**MaxRow**](https://apireference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow), [**MaxDataRow**](https://apireference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow), [**MaxColumn**](https://apireference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn), [**MaxDataColumn**](https://apireference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) & [**MaxDisplayRange**](https://apireference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) require extra time to gather the corresponding statistics. In case the data matrix (rows x columns) is large, using these APIs could impose a performance penalty.
1. In most of the cases, not all cells in a given range are instantiated. In such situations to check every cell in the matrix is not so efficient as compared to check only the initialized cells.
1. Accessing a cell in a loop as Cells row, column will cause all cell objects in a range to be instantiated, which may eventually cause OutOfMemoryException.

## **Conclusion**

Based on above-mentioned facts, the following are the possible scenarios where enumerators should be used.

1. Read-only access of the cell collection is required, that is; the requirement is to only inspect the cells.
1. A large number of cells are to be traversed.
1. Only initialized cells/rows/columns to be traversed.
