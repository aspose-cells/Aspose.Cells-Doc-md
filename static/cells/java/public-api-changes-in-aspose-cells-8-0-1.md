##Public API Changes in Aspose.Cells 8.0.1
These page list public API changes that were introduced in Aspose.Cells 8.0.1. It includes not only new and obsoleted public methods, but also a description of any changes in the behavior behind the scenes in Aspose.Cells which may affect existing code. Any behavior introduced that could be seen as a regression and modifies existing behavior is especially important and is documented here.
## **MemorySetting Property Added to the Cells Class**
Cells class has exposed setMemorySetting & getMemorySetting methods which can be used to optimize the memory usage for cells data, and hence decrease the overall memory cost. The following example shows how to write a large data to a worksheet in optimized mode.
**Java**
//Instantiate a new Workbook
Workbook book = new Workbook();
//Set the memory preferences
book.getSettings().setMemorySetting(MemorySetting.MEMORY_PREFERENCE);
//To change the memory setting of existing sheets, please change memory setting for them manually:
Cells cells = book.getWorksheets().get(0).getCells();
cells.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);
//Input large dataset into the cells of the worksheet.
//Your code goes here
The memory settings will not work for the default sheet automatically created by the Workbook. In order to change the memory settings of existing sheets, please apply the memory settings manually before performing any data manipulation.
Please check the detailed article on [Optimizing Memory while Working with Large Data Sets](https://docs.aspose.com/cells/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)
