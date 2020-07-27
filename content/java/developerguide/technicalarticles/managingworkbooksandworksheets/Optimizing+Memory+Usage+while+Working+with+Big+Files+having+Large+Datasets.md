+++
title = "Optimizing Memory Usage while Working with Big Files having Large Datasets" 
description = "" 
weight = 16425 
+++

Aspose.Cells for Java : Optimizing Memory Usage while Working with Big Files having Large Datasets  

# Aspose.Cells for Java : Optimizing Memory Usage while Working with Big Files having Large Datasets


When building a workbook with large data sets, or reading a big Microsoft Excel file, the total amount of RAM the process will take is always a concern. There are measures which can be adapted to cope with the challenge. Aspose.Cells provides some relevant options and API calls to lower, reduce and optimize memory use. Also, it can help the process to work more efficiently and run faster.

Use [MemorySetting.MEMORY\_PREFERENCE](https://apireference.aspose.com/java/cells/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) option to optimize memory used for cells data to decrease the overall memory cost. When building large data set for cells, it can save a certain amount of memory compared to using the default setting [MemorySetting.NORMAL](https://apireference.aspose.com/java/cells/com.aspose.cells/memorysetting#NORMAL).

## Optimizing Memory

### Reading Large Excel Files

The following example shows how to read a large Microsoft Excel file in optimized mode.


### Writing Large Excel Files

The following example shows how to write a large dataset to a worksheet in optimized mode.

## Caution

The default option, [MemorySetting.NORMAL](https://apireference.aspose.com/java/cells/com.aspose.cells/memorysetting#NORMAL) is applied for all versions. For some situations, such as building a workbook with a large data set for cells, the [MemorySetting.MEMORY\_PREFERENCE](https://apireference.aspose.com/java/cells/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) option may optimize the memory use and decrease the memory cost for the application. However, this option may degrade performance in some special cases such as follow.

1.  **Accessing Cells Randomly and Repeatedly**: The most efficient sequence for accessing the cells collection is cell by cell in one row, and then row by row. Especially, if you access rows/cells by the Enumerator acquired from [Cells](https://apireference.aspose.com/java/cells/com.aspose.cells/Cells), [RowCollection](https://apireference.aspose.com/java/cells/com.aspose.cells/RowCollection) and [Row](https://apireference.aspose.com/java/cells/com.aspose.cells/Row), the performance would be maximized with [MemorySetting.MEMORY\_PREFERENCE](https://apireference.aspose.com/java/cells/com.aspose.cells/memorysetting#MEMORY_PREFERENCE).
2.  **Inserting & Deleting Cells & Rows**: Please note that if there are lots of insert/delete operations for Cells/Rows, the performance degradation will be notable for [MemorySetting.MEMORY\_PREFERENCE](https://apireference.aspose.com/java/cells/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) mode as compared to the [MemorySetting.NORMAL](https://apireference.aspose.com/java/cells/com.aspose.cells/memorysetting#NORMAL) mode.
3.  **Operating on Different Cell Types**: If most of the cells contain string values or formulas, the memory cost will be the same as [MemorySetting.NORMAL](https://apireference.aspose.com/java/cells/com.aspose.cells/memorysetting#NORMAL) mode but if there are lots of empty cells, or cell values are numeric, bool and so on, the [MemorySetting.MEMORY\_PREFERENCE](https://apireference.aspose.com/java/cells/com.aspose.cells/memorysetting#MEMORY_PREFERENCE) option will give better performance.

