---
title: How and Where to Use Enumerators
linktitle: Iterate Data
type: docs
weight: 55
url: /net/how-and-where-to-use-enumerators/
description: Learn How and Where to Use Enumerators through the Aspose.Cells for .NET API.
keywords: How to use Enumerators, Cells Enumerator, Rows Enumerator, Columns Enumerator
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

An enumerator is an object that provides the ability to traverse a container or a collection. Enumerators can be used to read the data in the collection, but they cannot be used to modify the underlying collection, whereas **IEnumerable** is an interface that defines one method, **GetEnumerator**, which returns an **IEnumerator** interface; this, in turn, allows read‑only access to a collection.

Aspose.Cells APIs provide a bunch of enumerators; however, this article mainly discusses the three types listed below.

1. Cells Enumerator  
2. Rows Enumerator  
3. Columns Enumerator  

{{% /alert %}}

## **How to use Enumerators**

### **Cells Enumerator**

There are various ways to access the Cells Enumerator, and one can use any of these methods based on the application requirements. Here are the methods that return the cells enumerator.

1. [**Cells.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/getenumerator)  
2. [**Row.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/getenumerator)  
3. [**Range.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/getenumerator)

All of the above‑mentioned methods return an enumerator that allows traversing the collection of cells, which have been initialized.

{{% alert color="primary" %}}

While traversing the cells, the collection should not be modified (operations that will cause a new **Cell** to be instantiated or an existing **Cell** to be deleted). Otherwise, the enumerator may not be able to traverse all cells correctly (some elements may be traversed repeatedly or skipped).

{{% /alert %}}

The following code example demonstrates the implementation of the **IEnumerator** interface for a Cells collection.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-CellsEnumerator.cs" >}}

### **Rows Enumerator**

The Rows Enumerator can be accessed while using the [**RowCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection/methods/getenumerator) method. The following code example demonstrates the implementation of the **IEnumerator** interface for [**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-RowEnumerator.cs" >}}

### **Columns Enumerator**

The Columns Enumerator can be accessed while using the [**ColumnCollection.GetEnumerator**](https://reference.aspose.com/cells/net/aspose.cells/columncollection) method. The following code example demonstrates the implementation of the **IEnumerator** interface for [**ColumnCollection**](https://reference.aspose.com/cells/net/aspose.cells/columncollection).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-ColumnEnumerator.cs" >}}

## **Where to use Enumerators**

In order to discuss the advantages of using enumerators, let's take a real‑time example.

**Scenario**

An application requirement is to traverse all cells in a given [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) to read their values. There could be several ways to implement this goal. A few are demonstrated below.

### **Using Display Range**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingDisplayRange.cs" >}}

### **Using MaxDataRow & MaxDataColumn**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-HowAndWhereToUseEnumerators-UsingMaxDataRowAndMaxDataColumn.cs" >}}

As you can observe, both of the above‑mentioned approaches use more or less similar logic; that is, loop over all cells in the collection to read the cell values. This could be problematic for a number of reasons as discussed below.

1. APIs such as [**MaxRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxrow), [**MaxDataRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatarow), [**MaxColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxcolumn), [**MaxDataColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdatacolumn) & [**MaxDisplayRange**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/maxdisplayrange) require extra time to gather the corresponding statistics. In case the data matrix (rows × columns) is large, using these APIs could impose a performance penalty.  
2. In most cases, not all cells in a given range are instantiated. In such situations, checking every cell in the matrix is not as efficient as checking only the initialized cells.  
3. Accessing a cell in a loop as **Cells[row, column]** will cause all cell objects in a range to be instantiated, which may eventually cause an **OutOfMemoryException**.

## **Conclusion**

Based on the above‑mentioned facts, the following are the possible scenarios where enumerators should be used.

1. Read‑only access to the cell collection is required; that is, the requirement is to only inspect the cells.  
2. A large number of cells are to be traversed.  
3. Only initialized cells/rows/columns should be traversed.

{{< app/cells/assistant language="csharp" >}}
