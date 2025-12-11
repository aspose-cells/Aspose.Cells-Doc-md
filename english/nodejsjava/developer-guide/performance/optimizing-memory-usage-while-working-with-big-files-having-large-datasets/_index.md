---
title: Optimizing Memory Usage while Working with Big Files Having Large Datasets
type: docs
weight: 110
url: /nodejs-java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

When building a workbook with large data sets, or reading a big Microsoft Excel file, the total amount of RAM the process will consume is always a concern. There are measures which can be adopted to cope with the challenge. Aspose.Cells provides some relevant options and API calls to lower, reduce, and optimize memory use. It can also help the process work more efficiently and run faster.

Use [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) option to optimize the memory used for cell data to decrease the overall memory cost. When building a large data set for cells, it can save a certain amount of memory compared to using the default setting [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL).

{{% /alert %}}

## **Optimizing Memory**

The following example shows how to optimize memory usage while working with large data in Aspose.Cells for Node.js via Java.

{{< gist "aspose-cells-gists" "eb9faad10b8effdcfe82e35b25d5a3c0" "optimize-memory-usage-while-working-with-large-data.js" >}}

## **Caution**

The default option, [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL) is applied for all versions. For some situations, such as building a workbook with a large data set for cells, the [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) option may optimize memory use and decrease the memory cost for the application. However, this option may degrade performance in some special cases such as follows.

1. **Accessing Cells Randomly and Repeatedly**: The most efficient sequence for accessing the cells collection is cell by cell in one row, and then row by row. Especially, if you access rows/cells by the enumerator acquired from [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), [**RowCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/RowCollection) and [**Row**](https://reference.aspose.com/cells/java/com.aspose.cells/Row), performance is maximized with [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE).
2. **Inserting & Deleting Cells & Rows**: Please note that if there are many insert/delete operations for cells/rows, the performance degradation will be notable for [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) mode as compared to the [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL) mode.
3. **Operating on Different Cell Types**: If most of the cells contain string values or formulas, the memory cost will be the same as [**MemorySetting.NORMAL**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#NORMAL) mode, but if there are many empty cells, or cell values are numeric, boolean, and so on, the [**MemorySetting.MEMORY_PREFERENCE**](https://reference.aspose.com/cells/java/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) option will give better performance.
