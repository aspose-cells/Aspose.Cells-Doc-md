---
title: How to Fix the java.lang.OutOfMemoryError while Loading Large Spreadsheets
type: docs
weight: 20
url: /java/how-to-fix-the-java-lang-outofmemoryerror-while-loading-large-spreadsheets/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

There is a fair chance that the Workbook constructor may throw `java.lang.OutOfMemoryError` while loading large spreadsheets. This exception suggests that the available memory is insufficient to completely load the spreadsheet into memory; therefore, the spreadsheet must be loaded while enabling the [Memory Preferences](/cells/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}} 

## **How to Fix the java.lang.OutOfMemoryError While Loading Large Spreadsheets**
Aspose.Cells APIs provide Memory Preferences to optimize memory consumption while loading and processing spreadsheets. These options are also helpful in efficiently loading large spreadsheets containing huge data sets into a Workbook object, as demonstrated below. 

**Java**

{{< highlight csharp >}}
 // Specify the LoadOptions
LoadOptions options = new LoadOptions();

// Set the memory preferences
options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

// Instantiate the Workbook and load the large Excel file containing a large data set
Workbook book = new Workbook("sample.xlsx", options);
{{< /highlight >}}

{{< app/cells/assistant language="java" >}}
