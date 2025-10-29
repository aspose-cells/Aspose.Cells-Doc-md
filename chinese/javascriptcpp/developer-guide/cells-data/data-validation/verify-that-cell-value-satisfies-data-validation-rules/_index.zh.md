---
title: 验证单元格值是否满足数据验证规则
type: docs
weight: 210
url: /zh/javascript-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: 了解如何通过C++中的Aspose.Cells for JavaScript验证单元格值是否满足数据验证规则。
keywords: 通过C++中的JavaScript获取单元格验证值，验证单元格的值是否满足所应用的数据验证规则，使用C++中的JavaScript获取单元格验证值
---

{{% alert color="primary" %}} 

Microsoft Excel允许用户为单元格添加数据验证规则。例如，小数验证指定只能输入10到20之间的数字。如果用户输入不同的数字，Excel会显示错误信息并提示他们输入正确范围内的数字。如果复制粘贴一个数字，比如3，Excel不会进行验证检查或显示错误信息。

有时，有必要以编程方式验证一个值是否满足应用于该单元格的数据验证规则。例如，上面的情况下，输入应该是失败的。

{{% /alert %}} 
## **介绍**
C++中的Aspose.Cells for JavaScript提供了[Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--)属性，用于以编程方式验证单元格值。如果单元格中的值不满足应用于该单元格的数据验证规则，则返回**false**，否则返回**true**。

以下示例代码说明了[Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--)属性的工作原理。首先，向C1单元格输入值3。由于此值不满足数据验证规则，属性返回**false**。然后，向C1输入值15。因为此值满足数据验证规则，属性返回**true**。类似地，输入30时也返回**false**。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Validation Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Validation Example</h1>
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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access Cell C1
            // Cell C1 has the Decimal Validation applied on it.
            // It can take only the values Between 10 and 20
            const cell = worksheet.cells.get("C1");

            // Enter 3 inside this cell (not between 10 and 20)
            cell.value = 3;

            // Check if number 3 satisfies the Data Validation rule applied on this cell
            const valid3 = cell.validationValue;
            console.log("Is 3 a Valid Value for this Cell: " + valid3);
            resultDiv.innerHTML += `<p>Is 3 a Valid Value for this Cell: ${valid3}</p>`;

            // Enter 15 inside this cell (between 10 and 20)
            cell.value = 15;

            // Check if number 15 satisfies the Data Validation rule applied on this cell
            const valid15 = cell.validationValue;
            console.log("Is 15 a Valid Value for this Cell: " + valid15);
            resultDiv.innerHTML += `<p>Is 15 a Valid Value for this Cell: ${valid15}</p>`;

            // Enter 30 inside this cell (not between 10 and 20)
            cell.value = 30;

            // Check if number 30 satisfies the Data Validation rule applied on this cell
            const valid30 = cell.validationValue;
            console.log("Is 30 a Valid Value for this Cell: " + valid30);
            resultDiv.innerHTML += `<p>Is 30 a Valid Value for this Cell: ${valid30}</p>`;
        });
    </script>
</html>
```


### **输出**
{{< highlight javascript >}}

 Is 3 a Valid Value for this Cell: false

Is 15 a Valid Value for this Cell: true

Is 30 a Valid Value for this Cell: false

{{< /highlight >}}
