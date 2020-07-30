---
title : "How and Where to Use Enumerators" 
description : "" 
weight : 20496 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/mngrowscolumnsandcells/how+and+where+to+use+enumerators/
---

# Aspose.Cells for .NET : How and Where to Use Enumerators


An enumerator is an object that provides the ability to traverse a container or a collection. Enumerators can be used to read the data in the collection, but they cannot be used to modify the underlying collection, whereas `IEnumerable` is an interface that defines one method `GetEnumerator` which returns an `IEnumerator` interface, this, in turn, allows read-only access to a collection.

Aspose.Cells APIs provide a bunch of enumerators however, this article mainly discusses the three types as listed below.

1.  Cells Enumerator
2.  Rows Enumerator
3.  Columns Enumerator

{{< panel title="Contents Summary" style="primary" >}}
*   1 [How to use Enumerators](#how-to-use-enumerators)
    *   1.1 [Cells Enumerator](#cells-enumerator)
    *   1.2 [Rows Enumerator](#rows-enumerator)
    *   1.3 [Columns Enumerator](#columns-enumerator)
*   2 [Where to use Enumerators](#where-to-use-enumerators)
    *   2.1 [Using Display Range](#using-display-range)
    *   2.2 [Using MaxDataRow & MaxDataColumn](#using-maxdatarow-&-maxdatacolumn)
*   3 [Conclusion](#conclusion)
{{< /panel >}}
 

 

# How to use Enumerators

## Cells Enumerator

There are various ways to access the Cells Enumerator, and one can use any of these methods based on the application requirements. Here are the methods that return the cells enumerator.

1.  [Cells.GetEnumerator](https://apireference.aspose.com/net/cells/aspose.cells/cells/methods/getenumerator)
2.  [Row.GetEnumerator](https://apireference.aspose.com/net/cells/aspose.cells/row/methods/getenumerator)
3.  [Range.GetEnumerator](https://apireference.aspose.com/net/cells/aspose.cells/range/methods/getenumerator)

All of the above-mentioned methods return the enumerator that allows traversing the collection of cells which have been initialized.

While traversing the cells, the collection should not be modified (operations that will cause a new Cell to be instantiated or existing Cell to be deleted). Otherwise, the enumerator may not be able to traverse all cells correctly (some elements may be traversed repeatedly or skipped).

The following code example demonstrates the implementation of the `IEnumerator` interface for a Cells collection.

## Rows Enumerator

The Rows Enumerator can be accessed while using the [RowCollection.GetEnumerator](https://apireference.aspose.com/net/cells/aspose.cells/rowcollection/methods/getenumerator) method. The following code example demonstrates the implementation of the `IEnumerator` interface for [RowCollection](https://apireference.aspose.com/net/cells/aspose.cells/rowcollection).

## Columns Enumerator

The Columns Enumerator can be accessed while using the [ColumnCollection.GetEnumerator](https://apireference.aspose.com/net/cells/aspose.cells/columncollection) method. The following code example demonstrates the implementation of the `IEnumerator` interface for [ColumnCollection](https://apireference.aspose.com/net/cells/aspose.cells/columncollection).

# Where to use Enumerators

In order to discuss the advantages of using enumerators, let's take a real time example.

**Scenario**

An application requirement is to traverse all cells in a given [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) to read their values. There could be several ways to implement this goal. A few are demonstrated below.

## Using Display Range

## Using MaxDataRow & MaxDataColumn

As you can observe that both of the above-mentioned approaches use more or less similar logic, that is; loop over all cells in the collection to read the cell values. This could be problematic for a number of reasons as discussed below.

1.  APIs such as [MaxRow](https://apireference.aspose.com/net/cells/aspose.cells/cells/properties/maxrow), [MaxDataRow](https://apireference.aspose.com/net/cells/aspose.cells/cells/properties/maxdatarow), [MaxColumn](https://apireference.aspose.com/net/cells/aspose.cells/cells/properties/maxcolumn), [MaxDataColumn](https://apireference.aspose.com/net/cells/aspose.cells/cells/properties/maxdatacolumn) & [MaxDisplayRange](https://apireference.aspose.com/net/cells/aspose.cells/cells/properties/maxdisplayrange) require extra time to gather the corresponding statistics. In case the data matrix (rows x columns) is large, using these APIs could impose a performance penalty.
2.  In most of the cases, not all cells in a given range are instantiated. In such situations to check every cell in the matrix is not so efficient as compared to check only the initialized cells.
3.  Accessing a cell in a loop as Cells row, column will cause all cell objects in a range to be instantiated, which may eventually cause `OutOfMemoryException`.

# Conclusion

Based on above-mentioned facts, the following are the possible scenarios where enumerators should be used.

1.  Read-only access of the cell collection is required, that is; the requirement is to only inspect the cells.
2.  A large number of cells are to be traversed.
3.  Only initialized cells/rows/columns to be traversed.

