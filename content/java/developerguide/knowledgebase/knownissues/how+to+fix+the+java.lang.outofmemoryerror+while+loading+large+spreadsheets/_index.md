---
title : "How to Fix the java.lang.OutOfMemoryError while Loading Large Spreadsheets" 
description : "" 
weight : 16583 
toc : false
type: docs
url: /java/developerguide/knowledgebase/knownissues/how+to+fix+the+java.lang.outofmemoryerror+while+loading+large+spreadsheets/
---

# Aspose.Cells for Java : How to Fix the java.lang.OutOfMemoryError while Loading Large Spreadsheets


There are fair chances that the `Workbook` constructor may throw `java.lang.OutOfMemoryError` while loading large spreadsheets. This exception suggests that the available memory is insufficient to completely load the spreadsheet into the memory therefore the spreadsheet has to be loaded while enabling the [Memory Preferences](http://www.aspose.com/docs/display/cellsjava/Optimizing+Memory+Usage+while+Working+with+Big+Files+having+Large+Datasets).

#### How to fix the java.lang.OutOfMemoryError while loading large spreadsheet

Aspose.Cells APIs provide Memory Preferences to optimize the memory consumption while loading & processing spreadsheets. These options are also helpful in efficiently loading the large spreadsheets containing huge data sets in `Workbook` object as demonstrated below.

**Java**

{{< code lang="java" >}}
//Specify the LoadOptions
LoadOptions options = new LoadOptions();
//Set the memory preferences
options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook
//Load the Big Excel file having large Data set in it
Workbook book = new Workbook("sample.xlsx", options);
{{< /code >}}

