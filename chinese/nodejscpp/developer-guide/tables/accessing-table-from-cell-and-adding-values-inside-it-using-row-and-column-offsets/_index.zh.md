---  
title: 使用行和列偏移，通过Node.js与C++访问单元格中的表并添加值  
linktitle: 从单元格访问表格并使用行和列偏移添加值  
type: docs  
weight: 230  
url: /zh/nodejs-cpp/accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets/  
---  

{{% alert color="primary" %}}  

通常，您可以使用 [**Cell.putValue(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) 方法向表格或列表对象中添加值。但有时，您可能需要使用行和列偏移向表格或列表对象中添加值。  

若要从单元格访问表格或列表对象，使用[**Cell.getTable()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getTable--)方法。利用行列偏移添加值时，使用[**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#putCellValue-number-number-object-)方法。  

{{% /alert %}}  

以下截图展示了代码中的源Excel文件，包含空表格，突出显示了内部位于D5的单元格。我们将通过[**Cell.getTable()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getTable--)方法从D5单元格访问此表格，然后用[**Cell.putValue(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-)和[**ListObject.putCellValue(number, number, object)**](https://reference.aspose.com/cells/nodejs-cpp/listobject/#putCellValue-number-number-object-)方法向其内部添加值。  

## 示例  

### 比较源文件和输出文件的截图  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_1.png)|  
| :- |  

以下截图显示了代码生成的输出Excel文件。您可以看到单元格D5具有一个值，而位于表格偏移2,2的单元格F6也具有一个值。  

|![todo:image_alt_text](accessing-table-from-cell-and-adding-values-inside-it-using-row-and-column-offsets_2.png)|  
| :- |  

### 使用Node.js通过C++访问表格和利用行列偏移添加值的代码示例  

以下示例代码加载了上面截图中显示的源Excel文件，并向表格内添加值，并生成了上面所示的输出Excel文件。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Accessing_Table.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cell D5 which lies inside the table
const cell = worksheet.getCells().get("D5");

// Put value inside the cell D5
cell.putValue("D5 Data");

// Access the Table from this cell
const table = cell.getTable();

// Add some value using Row and Column Offset
table.putCellValue(2, 2, "Offset [2,2]");

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
