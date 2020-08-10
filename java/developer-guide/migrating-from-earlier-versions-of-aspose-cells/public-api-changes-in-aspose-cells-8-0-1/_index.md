---
title: Public API Changes in Aspose.Cells 8.0.1
type: docs
weight: 30
url: /java/public-api-changes-in-aspose-cells-8-0-1/
---

{{% alert color="primary" %}} 

These page list public API changes that were introduced in Aspose.Cells 8.0.1. It includes not only new and obsoleted public methods, but also a description of any changes in the behavior behind the scenes in Aspose.Cells which may affect existing code. Any behavior introduced that could be seen as a regression and modifies existing behavior is especially important and is documented here.

{{% /alert %}} 
### **MemorySetting Property Added to the Cells Class**
Cells class has exposed setMemorySetting & getMemorySetting methods which can be used to optimize the memory usage for cells data, and hence decrease the overall memory cost. The following example shows how to write a large data to a worksheet in optimized mode.

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences

book.getSettings().setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//To change the memory setting of existing sheets, please change memory setting for them manually:

Cells cells = book.getWorksheets().get(0).getCells();

cells.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Input large dataset into the cells of the worksheet.

//Your code goes here

{{< /highlight >}}

{{% alert color="primary" %}} 

The memory settings will not work for the default sheet automatically created by the Workbook. In order to change the memory settings of existing sheets, please apply the memory settings manually before performing any data manipulation. 

{{% /alert %}} {{% alert color="primary" %}} 

Please check the detailed article on [Optimizing Memory while Working with Large Data Sets](/cells/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
