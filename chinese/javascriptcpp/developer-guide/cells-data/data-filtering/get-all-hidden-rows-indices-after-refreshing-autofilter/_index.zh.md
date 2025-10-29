---
title: 在刷新AutoFilter后获取所有隐藏行索引 
type: docs  
weight: 320  
url: /zh/javascript-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/  
description: 了解如何在使用C++ API的Aspose.Cells for JavaScript中，通过刷新AutoFilter后获取所有隐藏行的索引。  
keywords: 通过C++获取AutoFilter刷新后所有隐藏行的索引，使用C++通过JavaScript获取AutoFilter刷新后所有隐藏行的索引，检索AutoFilter刷新后所有隐藏行的索引（JavaScript通过C++）  
---

## **可能的使用场景**  

当你在工作表单元格上应用自动筛选时，一些行会自动隐藏。但也可能有一些行已被Excel最终用户手动隐藏，这些行并不是由自动筛选隐藏的。因此，很难知道哪些行是由自动筛选隐藏的，哪些行是由Excel最终用户手动隐藏的。Aspose.Cells for JavaScript通过C++解决了这个问题，使用`Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#refresh-boolean-)。此方法返回所有由自动筛选隐藏、而不是由Excel最终用户手动隐藏的行的索引。  

## **在刷新自动筛选后获取所有隐藏行索引**  

请查看以下示例代码，加载含有一些由Excel最终用户手动隐藏的行的[示例Excel文件](64716909.xlsx)。此代码应用自动筛选并使用`Array` [**AutoFilter.refresh(hideRows)**](https://reference.aspose.com/cells/javascript-cpp/autofilter/#refresh-boolean-)方法刷新筛选，该方法返回所有由自动筛选隐藏的行的索引。然后，它将隐藏行的索引与单元格名称和数值一同打印到控制台。  

## **示例代码**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Hidden Rows After Refreshing AutoFilter</title>
    </head>
    <body>
        <h1>Get Hidden Rows After Refreshing AutoFilter</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Apply autofilter
            worksheet.autoFilter.addFilter(0, "Orange");

            // True means it will refresh autofilter and return hidden rows.
            const rowIndices = worksheet.autoFilter.refresh(true);

            console.log("Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.");
            console.log("--------------------------");

            let output = '<p>Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.</p><pre>';
            rowIndices.forEach(r => {
                const cell = worksheet.cells.get(r, 0);
                console.log(`${r}\t${cell.name}\t${cell.stringValue}`);
                output += `${r}\t${cell.name}\t${cell.stringValue}\n`;
            });
            output += '</pre>';

            resultDiv.innerHTML = output;
        });
    </script>
</html>
```


## **控制台输出**  

{{< highlight java >}}  

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.  

\--------------------------  

1       A2      Apple  

2       A3      Apple  

3       A4      Apple  

6       A7      Apple  

7       A8      Apple  

11      A12     Pear  

12      A13     Pear  

{{< /highlight >}}
