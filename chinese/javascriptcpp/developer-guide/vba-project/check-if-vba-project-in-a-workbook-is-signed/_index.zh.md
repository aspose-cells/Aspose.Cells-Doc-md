---
title: 检查工作簿中的VBA项目是否用JavaScript通过C++签名
linktitle: 检查工作簿中的VBA项目是否已签名
type: docs
weight: 70
url: /zh/javascript-cpp/check-if-vba-project-in-a-workbook-is-signed/
description: 学习如何使用Aspose.Cells for JavaScript通过C++检查工作簿中的VBA项目是否已签名。
---

{{% alert color="primary" %}}

您可以通过**工具 > 数字签名...**菜单命令，使用Microsoft Excel来检查您的VBA项目是否已签名。同样，您也可以使用Aspose.Cells的[**Workbook.vbaProject**](https://reference.aspose.com/cells/javascript-cpp/workbook/#vbaProject--)属性以编程方式来检查。

{{% /alert %}}

## **用JavaScript检查工作簿中的VBA项目是否已签名**

以下代码加载工作簿，并使用[**Workbook.vbaProject**](https://reference.aspose.com/cells/javascript-cpp/workbook/#vbaProject--)属性检测其VBA项目是否已签名。若已签名，返回**true**；否则返回**false**。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells VBA Signed Check</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the VBA project and checking if it's signed
            const isSigned = workbook.vbaProject.isSigned;

            console.log("VBA Project is Signed: " + isSigned);
            document.getElementById('result').innerHTML = `<p>VBA Project is Signed: ${isSigned}</p>`;
        });
    </script>
</html>
```
