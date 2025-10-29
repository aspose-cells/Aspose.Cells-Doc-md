---  
title: 通过 Node.js 加载或导入带有公式的 CSV 文件  
linktitle: 加载或导入具有公式的CSV文件  
type: docs  
weight: 350  
url: /zh/nodejs-cpp/load-or-import-csv-file-with-formulas/  
description: 学习如何使用 Aspose.Cells for Node.js via C++ 加载和导入包含公式的 CSV 文件。  
---  

{{% alert color="primary" %}}  

大多数 CSV 文件包含文本数据，没有包含任何公式。然而，有时 CSV 文件也可能包含公式。这类 CSV 文件应通过设置 [TxtLoadOptions.getHasFormula()](https://reference.aspose.com/cells/nodejs-cpp/txtloadoptions/#getHasFormula--) 为 **true** 来加载。一旦设置为 **true**，Aspose.Cells 不会将公式视为简单文本，而是作为公式处理，Aspose.Cells 的公式引擎会正常计算。

{{% /alert %}}  

以下代码演示了如何加载以及导入带公式的 CSV 文件。你可以使用任何 CSV 文件。为了示例，我们使用包含此数据的【简单 CSV 文件】（5115034.csv），如你所见，它包含一个公式。

{{< highlight javascript >}}  
const fs = require('fs');  
const AsposeCells = require('aspose.cells');  

let loadOptions = new AsposeCells.TxtLoadOptions();  
loadOptions.setHasFormula(true);  

let workbook = new AsposeCells.Workbook();  
workbook.open("path/to/your/file.csv", loadOptions);  
workbook.save("path/to/output.xlsx");  
{{< /highlight >}}  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.csv");

// TxtLoadOptions configuration
const opts = new AsposeCells.TxtLoadOptions();
opts.setSeparator(',');
opts.setHasFormula(true);

// Load your CSV file with formulas in a Workbook object
const workbook = new AsposeCells.Workbook(filePath, opts);

// You can also import your CSV file like this
// The code below is importing CSV file starting from cell D4
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().importCSV(filePath, opts, 3, 3);

// Save your workbook in Xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

代码首先加载CSV文件，然后在单元格D4处重新导入，并最终将工作簿保存为XLSX格式。输出的 XLSX 文件（[链接](5115052.xlsx)）如下所示。你可以看到，单元格C3和F4包含公式，其结果为800。

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|  
| :- |  


{{< app/cells/assistant language="nodejs-cpp" >}}
