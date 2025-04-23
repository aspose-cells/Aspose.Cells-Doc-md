---
title: 如何修复加载大型电子表格时的java.lang.OutOfMemoryError
type: docs
weight: 20
url: /zh/java/how-to-fix-the-java-lang-outofmemoryerror-while-loading-large-spreadsheets/
---

{{% alert color="primary" %}} 

在加载大型电子表格时，Workbook构造函数有可能抛出java.lang.OutOfMemoryError。此异常表明可用内存不足以完全将电子表格加载到内存中，因此必须在启用 [Memory Preferences](/cells/zh/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/) 的情况下加载电子表格。

{{% /alert %}} 
## **如何修复加载大型电子表格时的java.lang.OutOfMemoryError**
Aspose.Cells APIs提供了内存优化偏好设置，可以优化加载和处理电子表格时的内存消耗。这些选项还可以有效地在Workbook对象中加载包含大量数据集的大型电子表格。 

**Java**

{{< highlight csharp >}}

 //Specify the LoadOptions

LoadOptions options = new LoadOptions();

//Set the memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook

//Load the Big Excel file having large Data set in it

Workbook book = new Workbook("sample.xlsx", options);

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
