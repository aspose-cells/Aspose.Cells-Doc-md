---
title: Optimizing Memory Usage while Working with Big Files having Large Datasets
type: docs
weight: 110
url: /java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

When building a workbook with large data sets, or reading a big Microsoft Excel file, the total amount of RAM the process will take is always a concern. There are measures which can be adapted to cope with the challenge. Aspose.Cells provides some relevant options and API calls to lower, reduce, and optimize memory use. Also, it can help the process to work more efficiently and run faster.

Use the **MemorySetting.MEMORY_PREFERENCE** option to optimize the memory used for cell data, decreasing the overall memory cost. When building a large data set for cells, it can save a certain amount of memory compared to using the default setting **MemorySetting.NORMAL**.

{{% /alert %}}

## **Optimizing Memory**

### **Reading Large Excel Files**

The following example shows how to read a large Microsoft Excel file in optimized mode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadLargeExcelFiles-ReadLargeExcelFiles.java" >}}

### **Writing Large Excel Files**

The following example shows how to write a large dataset to a worksheet in optimized mode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-WritingLargeExcelFiles-WritingLargeExcelFiles.java" >}}

## **Caution**

The default option, **MemorySetting.NORMAL**, is applied for all versions. For some situations, such as building a workbook with a large data set for cells, the **MemorySetting.MEMORY_PREFERENCE** option may optimize memory use and decrease the memory cost for the application. However, this option may degrade performance in some special cases, such as follows.

1. **Accessing Cells Randomly and Repeatedly**: The most efficient sequence for accessing the cells collection is cell by cell within a row, and then row by row. Especially, if you access rows/cells via the enumerator obtained from **Cells**, **RowCollection**, and **Row**, performance is maximized with **MemorySetting.MEMORY_PREFERENCE**.

1. **Inserting & Deleting Cells & Rows**: Please note that if there are many insert/delete operations for cells/rows, performance degradation will be notable for **MemorySetting.MEMORY_PREFERENCE** mode compared to **MemorySetting.NORMAL** mode.

1. **Operating on Different Cell Types**: If most of the cells contain string values or formulas, the memory cost will be the same as **MemorySetting.NORMAL** mode, but if there are many empty cells, or cell values are numeric, boolean, and so on, the **MemorySetting.MEMORY_PREFERENCE** option will give better performance.

{{< app/cells/assistant language="java" >}}
