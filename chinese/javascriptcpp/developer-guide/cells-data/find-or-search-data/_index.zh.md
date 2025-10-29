---
title: 查找或搜索数据
type: docs
weight: 50
url: /zh/javascript-cpp/find-or-search-data/
description: 学习如何使用Aspose.Cells for JavaScript通过C++查找或搜索包含指定数据的单元格。
keywords: 通过 C++ 查找 JavaScript 数据，通过 C++ 搜索 JavaScript 数据，通过 C++ 查找包含公式的单元格 JavaScript，通过 C++ 搜索包含公式的单元格 JavaScript，通过 C++ 使用 FindOptions 查找数据或公式 JavaScript，通过 C++ 使用 FindOptions 搜索数据或公式 JavaScript，通过 C++ 查找或搜索包含指定字符串值或数字的单元格 JavaScript，通过 C++ 查找或搜索包含指定数据的单元格
---

{{% alert color="primary" %}}  
Microsoft Excel 允许用户在工作表中查找包含指定数据的单元格。  
{{% /alert %}}  

## **查找包含指定数据的单元格**  

### **使用Microsoft Excel**  

Microsoft Excel 允许用户在工作表中查找包含指定数据的单元格。如果在 Microsoft Excel 中选择 **查找** 菜单中的 **编辑**，你会看到一个对话框，可以在其中指定搜索值。  

在这里，我们正在查找值"橙子"。 Aspose.Cells 还允许开发人员查找工作表中包含指定值的单元格。  

### **使用 Aspose.Cells for JavaScript 通过 C++**  

Aspose.Cells 提供一个类 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)，代表一个 Microsoft Excel 文件。[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 类包含一个 [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) 集合，用于访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) 类提供一个 [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) 集合，表示工作表中的所有单元格。[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) 集合提供多种方法，用于查找包含用户指定数据的单元格。以下部分更详细地介绍了这些方法中的一些。  

{{% alert color="primary" %}}  
所有查找方法返回包含指定数据的单元格的引用。  
{{% /alert %}}  

## **查找包含公式的单元格**  

开发者可以通过调用 [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) 集合的 [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) 方法，在工作表中查找指定的公式。通常，[**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) 方法接受三个参数：  

-  要搜索的对象。类型应为 int、double、DateTime、string、bool。  
-  具有相同对象的前一个单元格。如果从头开始搜索，可以将此参数设置为 null。  
-  查找所需对象的选项。  

以下示例使用工作表数据来练习查找方法：  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Find Cell Containing Formula</title>
    </head>
    <body>
        <h1>Find Cell Containing Formula</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FindOptions, LookInType } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Instantiate FindOptions Object and set to look in formulas
            const findOptions = new FindOptions();
            findOptions.lookInType = LookInType.Formulas;

            // Finding the cell containing the specified formula
            const cell = worksheet.cells.find("=SUM(A5:A10)", null, findOptions);

            // Displaying the name of the cell found after searching worksheet
            document.getElementById('result').innerHTML = `<p style="color: green;">Name of the cell containing formula: ${cell.name}</p>`;
        });
    </script>
</html>
```  


## **使用 FindOptions 查找数据或公式**  

可以使用 [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) 集合的 [**Cells.find(object, Cell)**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-) 方法，结合各种 [**FindOptions**](https://reference.aspose.com/cells/javascript-cpp/findoptions)，查找指定的值。通常，[**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) 方法接受以下参数：  

- **搜索值**，要搜索的数据或值。  
- **前一个单元格**，上一个包含相同值的单元格。如果从开头开始搜索，可以将此参数设置为null。  
- **查找选项**，查找选项。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Find Using FindOptions</title>
    </head>
    <body>
        <h1>Find Using FindOptions Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, FindOptions, CellArea, LookInType, LookAtType } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Calculate formulas in workbook
            workbook.calculateFormula();

            // Get Cells collection from first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Instantiate FindOptions Object
            const findOptions = new FindOptions();

            // Create a Cells Area
            const ca = new CellArea();
            ca.startRow = 8;
            ca.startColumn = 2;
            ca.endRow = 17;
            ca.endColumn = 13;

            // Set cells area for find options
            findOptions.range = ca;

            // Set searching properties
            findOptions.searchBackward = false;
            findOptions.searchOrderByRows = true;

            // Set the lookintype, you may specify, values, formulas, comments etc.
            findOptions.lookInType = LookInType.Values;

            // Set the lookattype, you may specify Match entire content, endswith, startswith etc.
            findOptions.lookAtType = LookAtType.EntireContent;

            // Find the cell with value
            const cell = cells.find(341, null, findOptions);

            if (cell !== null) {
                document.getElementById('result').innerHTML = `<p>Name of the cell containing the value: ${cell.name}</p>`;
            } else {
                document.getElementById('result').innerHTML = '<p>Record not found</p>';
            }
        });
    </script>
</html>
```  


## **查找包含指定字符串值或数字的单元格**  

也可以调用同在 [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) 集合中的 [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) 方法，结合各种 [**FindOptions**](https://reference.aspose.com/cells/javascript-cpp/findoptions)，查找指定的字符串值。  

指定 [**FindOptions.lookInType**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#lookInType-lookintype-) 和 [**FindOptions.lookAtType**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#lookAtType-lookattype-) 属性。以下示例代码演示了如何使用这些属性查找在单元格字符串的**开头**、**中间**或**结尾**的各种字符串。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Find Examples</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate the workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Cells collection
            const cells = workbook.worksheets.get(0).cells;

            const opts = new AsposeCells.FindOptions();
            opts.lookInType = AsposeCells.LookInType.Values;
            opts.lookAtType = AsposeCells.LookAtType.EntireContent;

            let messages = '';

            // Find the cell with the input integer or double
            let cell1 = cells.find(205, null, opts);

            if (cell1 !== null) {
                messages += '<p>Name of the cell containing the value: ' + cell1.name + '</p>';
            } else {
                messages += '<p>Record not found</p>';
            }

            // Find the cell with the input string
            let cell2 = cells.find("Items A", null, opts);

            if (cell2 !== null) {
                messages += '<p>Name of the cell containing the value: ' + cell2.name + '</p>';
            } else {
                messages += '<p>Record not found</p>';
            }

            // Find the cell containing the input string (partial match)
            opts.lookAtType = AsposeCells.LookAtType.Contains;
            let cell3 = cells.find("Data", null, opts);

            if (cell3 !== null) {
                messages += '<p>Name of the cell containing the value: ' + cell3.name + '</p>';
            } else {
                messages += '<p>Record not found</p>';
            }

            document.getElementById('result').innerHTML = messages;
        });
    </script>
</html>
``` 



## **高级主题**  
- [查找具有特定样式的单元格](/cells/zh/javascript-cpp/find-cells-with-specific-style/)  
- [查找单元格值是否以单引号开始](/cells/zh/javascript-cpp/find-if-the-cell-value-starts-with-single-quote-mark/)  
- [使用原始值搜索数据](/cells/zh/javascript-cpp/search-data-using-original-values/)
