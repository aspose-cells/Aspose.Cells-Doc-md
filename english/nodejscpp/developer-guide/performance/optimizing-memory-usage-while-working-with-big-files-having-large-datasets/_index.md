---
title: Optimizing Memory Usage while Working with Big Files having Large Datasets
type: docs
weight: 110
url: /nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

When building a workbook with large data sets, or reading a big Microsoft Excel file, the total amount of RAM the process will take is always a concern. There are measures which can be adapted to cope with the challenge. Aspose.Cells provides some relevant options and API calls to lower, reduce and optimize memory use. Also, it can help the process to work more efficiently and run faster.

Use [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) option to optimize memory used for cells data to decrease the overall memory cost. When building large data set for cells, it can save a certain amount of memory compared to using the default setting [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/).

{{% /alert %}}

## **Optimizing Memory**

The following example shows how to optimize memory usage while working with large data in Aspose.Cells for Node.js via C++.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "OptimizingMemory.js" >}}

## **Caution**

The default option, [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) is applied for all versions. For some situations, such as building a workbook with a large data set for cells, the [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) option may optimize the memory use and decrease the memory cost for the application. However, this option may degrade performance in some special cases such as follow.

1. **Accessing Cells Randomly and Repeatedly**: The most efficient sequence for accessing the cells collection is cell by cell in one row, and then row by row. Especially, if you access rows/cells by the Enumerator acquired from [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells/), [**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection) and [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row), the performance would be maximized with [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/).
1. **Inserting & Deleting Cells & Rows**: Please note that if there are lots of insert/delete operations for Cells/Rows, the performance degradation will be notable for [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) mode as compared to the [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) mode.
1. **Operating on Different Cell Types**: If most of the cells contain string values or formulas, the memory cost will be the same as [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) mode but if there are lots of empty cells, or cell values are numeric, bool and so on, the [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) option will give better performance.

