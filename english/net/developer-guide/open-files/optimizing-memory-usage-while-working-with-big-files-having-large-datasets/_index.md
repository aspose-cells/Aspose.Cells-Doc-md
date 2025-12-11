---
title: Optimizing Memory Usage while Working with Big Files having Large Datasets
type: docs
weight: 180
url: /net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

When building a workbook with large data sets, or reading a big Microsoft Excel file, the total amount of RAM the process will take is always a concern. There are measures that can be adapted to cope with the challenge. Aspose.Cells provides some relevant options and API calls to lower, reduce, and optimize memory use. It can also help the process work more efficiently and run faster.

Use the [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) option to optimize memory use for cell data and decrease the overall memory cost. When building a large data set for cells, it can save a certain amount of memory compared to using the default setting ([**MemorySetting.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting)).

{{% /alert %}}

## **Optimizing Memory**

### **Reading Large Excel Files**

The following example shows how to read a large Microsoft Excel file in optimized mode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-ReadingLargeExcelFiles-1.cs" >}}

### **Writing Large Excel Files**

The following example shows how to write a large dataset to a worksheet in an optimized mode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-OptimizingMemoryUsage-WritingLargeExcelFiles-1.cs" >}}

## **Caution**

The default option, [**MemorySetting.Normal**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) is applied for all versions. For some situations, such as building a workbook with a large data set for cells, the [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) option may optimize memory use and decrease the memory cost for the application. However, this option may degrade performance in some special cases, such as the following.

1. **Accessing Cells Randomly and Repeatedly**: The most efficient sequence for accessing the cells collection is cell by cell in one row, and then row by row. Especially, if you access rows/cells by the enumerator acquired from [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells), [**RowCollection**](https://reference.aspose.com/cells/net/aspose.cells/rowcollection) and [**Row**](https://reference.aspose.com/cells/net/aspose.cells/row), performance is maximized with [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting).
2. **Inserting & Deleting Cells & Rows**: Please note that if there are many insert/delete operations for cells/rows, performance degradation will be notable for *MemoryPreference* mode compared to the *Normal* mode.
3. **Operating on Different Cell Types**: If most of the cells contain string values or formulas, the memory cost will be the same as *Normal* mode, but if there are many empty cells or cell values are numeric, boolean, and so on, the [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/net/aspose.cells/memorysetting) option will give better performance.
{{< app/cells/assistant language="csharp" >}}
