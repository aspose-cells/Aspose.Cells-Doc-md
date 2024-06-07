---
title: 如何在加载大型电子表格时修复java.lang.OutOfMemoryError
type: docs
weight: 20
url: /zh/java/how-to-fix-the-java-lang-outofmemoryerror-while-loading-large-spreadsheets/
---

{{% alert color="primary" %}} 

在加载大型电子表格时，Workbook构造函数可能会抛出java.lang.OutOfMemoryError异常。该异常表明可用内存不足以完全加载电子表格到内存中，因此必须在启用[内存首选项](/cells/zh/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)的情况下加载电子表格。

{{% /alert %}} 
## **如何解决加载大型电子表格时的java.lang.OutOfMemoryError**
Aspose.Cells API提供内存首选项，以优化加载和处理电子表格时的内存消耗。这些选项还有助于有效地加载包含大量数据集的大型电子表格到Workbook对象中，如下所示。 

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
