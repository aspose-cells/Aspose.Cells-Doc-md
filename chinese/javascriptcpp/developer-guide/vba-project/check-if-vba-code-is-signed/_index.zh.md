---
title: 用JavaScript通过C++检查VBA代码是否已签名
linktitle: 检查VBA代码是否已签名
type: docs
weight: 100
url: /zh/javascript-cpp/check-if-vba-code-is-signed/
description: 学习如何使用Aspose.Cells for JavaScript通过C++检查VBA代码项目是否已签名。 
---

{{% alert color="primary" %}}

Aspose.Cells允许用户检查VBA代码项目是否已签名。请使用[**VbaProject.isSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isSigned--)属性来检查VBA代码项目是否已签名。

{{% /alert %}}

以下代码说明如何使用[**VbaProject.isSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isSigned--)属性检查VBA代码是否已签名。您可以使用任何Excel文件测试此代码。为了测试，可以使用[此代码中用到的Excel文件](5115032.xlsm)。

## **检查VBA代码是否已签名**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells VBA Signed Check Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the VBA project and checking if it's signed
            const vbaProject = workbook.vbaProject;
            const isSigned = vbaProject.isSigned();

            resultDiv.innerHTML = `<p>Is VBA Code Project Signed: ${isSigned}</p>`;
        });
    </script>
</html>
```

## 控制台输出

以下是上述代码的控制台输出，使用链接提供的[示例Excel文件](5115032.xlsm)。

{{< highlight java >}}

Is VBA Code Project Signed: True

{{< /highlight >}}
