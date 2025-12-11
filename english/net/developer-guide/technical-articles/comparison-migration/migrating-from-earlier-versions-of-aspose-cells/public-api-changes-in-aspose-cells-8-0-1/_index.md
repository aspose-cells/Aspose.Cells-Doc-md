---
title: Public API Changes in Aspose.Cells 8.0.1
type: docs
weight: 20
url: /net/public-api-changes-in-aspose-cells-8-0-1/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This page lists public API changes that were introduced in Aspose.Cells 8.0.1. It includes not only new and obsoleted public methods, but also a description of any changes in the behavior behind the scenes in Aspose.Cells that may affect existing code. Any behavior introduced that could be seen as a regression or that modifies existing behavior is especially important and is documented here.

{{% /alert %}} 
## **MemorySetting Property Added to Cells Class**
The Cells class exposes a MemorySetting property that can be used to optimize memory usage for cell data, thereby decreasing overall memory consumption. The following example shows how to write large data to a worksheet in optimized mode.

**C#**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences

book.Settings.MemorySetting = MemorySetting.MemoryPreference;

//To change the memory setting of existing sheets, please change the memory setting for them manually:

Cells cells = book.Worksheets[0].Cells;

cells.MemorySetting = MemorySetting.MemoryPreference;

//Input large dataset into the cells of the worksheet

//Your code goes here

{{< /highlight >}}

The memory settings will not work for the default sheet automatically created by the Workbook object. In order to change the memory settings of existing sheets, please apply the memory setting manually before performing any data manipulation.

{{% alert color="primary" %}} 

Please check the detailed article on [Optimizing Memory while Working with Large Data Sets](/cells/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
