---  
title: Optimizing Memory Usage while Working with Big Files having Large Datasets with Node.js via C++  
linktitle: Optimizing Memory Usage while Working with Big Files having Large Datasets  
type: docs  
weight: 180  
url: /nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/  
---  

{{% alert color="primary" %}}  

When building a workbook with large data sets, or reading a big Microsoft Excel file, the total amount of RAM the process will take is always a concern. There are measures that can be adapted to cope with the challenge. Aspose.Cells for Node.js via C++ provides some relevant options and API calls to lower, reduce and optimize memory use. Also, it can help the process work more efficiently and run faster.  

Use the [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) option to optimize memory use for cells data and decrease the overall memory cost. When building a large data set for cells, it can save a certain amount of memory compared to using the default setting ([**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)).  

{{% /alert %}}  

## **Optimizing Memory**  

### **Reading Large Excel Files**  

The following example shows how to read a large Microsoft Excel file in optimized mode.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the LoadOptions
const opt = new AsposeCells.LoadOptions();
// Set the memory preferences
opt.setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Instantiate the Workbook
// Load the Big Excel file having large Data set in it
const wb = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"), opt);
```  

### **Writing Large Excel Files**  

The following example shows how to write a large dataset to a worksheet in an optimized mode.  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook();

// Set the memory preferences
wb.getSettings().setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Note: The memory settings also would not work for the default sheet i.e., "Sheet1" etc. automatically created by the Workbook

// To change the memory setting of existing sheets, please change memory setting for them manually:
let cells = wb.getWorksheets().get(0).getCells();
cells.setMemorySetting(AsposeCells.MemorySetting.MemoryPreference);

// Input large dataset into the cells of the worksheet.
// Your code goes here.
// .........

// Get cells of the newly created Worksheet "Sheet2" whose memory setting is same with the one defined in WorkbookSettings:
cells = wb.getWorksheets().add("Sheet2").getCells();
// .........
// Input large dataset into the cells of the worksheet.
// Your code goes here.
// .........
```  

## **Caution**  

The default option, [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) is applied for all versions. For some situations, such as building a workbook with a large data set for cells, the [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) option may optimize the memory use and decrease the memory cost for the application. However, this option may degrade performance in some special cases such as follow.  

1. **Accessing Cells Randomly and Repeatedly**: The most efficient sequence for accessing the cells collection is cell by cell in one row, and then row by row. Especially, if you access rows/cells by the Enumerator acquired from [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells), [**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection), and [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row), the performance would be maximized with [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/).  
2. **Inserting & Deleting Cells & Rows**: Please note that if there are lots of insert/delete operations for Cells/Rows, the performance degradation will be notable for *MemoryPreference* mode as compared to the *Normal* mode.  
3. **Operating on Different Cell Types**: If most of the cells contain string values or formulas, the memory cost will be the same as *Normal* mode but if there are lots of empty cells, or cell values are numeric, bool and so on, the [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) option will give better performance.  
  