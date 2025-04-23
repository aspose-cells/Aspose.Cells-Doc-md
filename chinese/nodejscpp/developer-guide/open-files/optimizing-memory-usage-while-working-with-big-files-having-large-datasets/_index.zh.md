---  
title: 使用 C++ 在 Node.js 中优化大文件大量数据集的内存使用  
linktitle: 在处理拥有大型数据集的大文件时优化内存使用  
type: docs  
weight: 180  
url: /zh/nodejs-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/  
---  

{{% alert color="primary" %}}  

当建立含有大量数据集的工作簿或读取大型 Microsoft Excel 文件时，所用的总 RAM 始终是一个关注点。可以采用一些措施来应对这一挑战。Aspose.Cells for Node.js via C++ 提供了一些相关的选项和 API 调用，以降低、减少和优化内存使用。此外，它还能帮助进程更高效、更快地运行。  

使用[**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/)选项来优化单元格数据的内存使用并降低整体内存成本。在构建大型数据集时，相较于使用默认设置([**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/))，它可以节省一定量的内存。  

{{% /alert %}}  

## **优化内存**  

### **读取大型Excel文件**  

以下示例展示了如何以优化模式读取大型Microsoft Excel文件。  

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

### **写入大型Excel文件**  

以下示例展示了如何以优化模式将大型数据集写入工作表。  

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

## **注意**  

默认选项 [**MemorySetting.Normal**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) 适用于所有版本。在某些情况下，例如为单元格建立包含大量数据的数据集的工作簿时，选项 [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) 可能会优化内存使用并降低应用程序的内存成本。然而，在某些特殊情况下，这个选项可能会影响性能，如下：  

1. **随机多次访问单元格**：访问单元格集合的最高效顺序是逐个单元格访问，然后逐行访问。尤其是，如果通过 [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)，[**RowCollection**](https://reference.aspose.com/cells/nodejs-cpp/rowcollection)，和 [**Row**](https://reference.aspose.com/cells/nodejs-cpp/row) 获取到的枚举器访问行/单元格，性能会达到最大化。  
2. **插入和删除单元格及行**：请注意，如果对单元格/行进行大量插入/删除操作，*MemoryPreference* 模式的性能会明显低于 *Normal* 模式。  
3. **操作不同类型的单元格**：如果大多数单元格包含字符串值或公式，内存成本与 *Normal* 模式相同，但如果存在大量空单元格，或单元格值为数字、布尔值等，则选项 [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/nodejs-cpp/memorysetting/) 会提供更好的性能。  

