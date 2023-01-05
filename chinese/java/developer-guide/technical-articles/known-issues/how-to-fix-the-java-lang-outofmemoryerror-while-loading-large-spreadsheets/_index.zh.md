---
title: 如何在加载大型电子表格时修复 java.lang.OutOfMemoryError
type: docs
weight: 20
url: /zh/java/how-to-fix-the-java-lang-outofmemoryerror-while-loading-large-spreadsheets/
---
{{% alert color="primary" %}} 

加载大型电子表格时，工作簿构造函数很有可能会抛出 java.lang.OutOfMemoryError。此异常表明可用内存不足以将电子表格完全加载到内存中，因此必须在启用时加载电子表格[内存首选项](/cells/zh/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}} 
## **如何在加载大型电子表格时修复 java.lang.OutOfMemoryError**
Aspose.Cells API 提供内存首选项以优化加载和处理电子表格时的内存消耗。这些选项也有助于有效地加载包含工作簿对象中大量数据集的大型电子表格，如下所示。

**Java**

{{< highlight "csharp" >}}

 //Specify the LoadOptions

LoadOptions options = new LoadOptions();

//Set the memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook

//Load the Big Excel file having large Data set in it

Workbook book = new Workbook("sample.xlsx", options);

{{< /highlight >}}
