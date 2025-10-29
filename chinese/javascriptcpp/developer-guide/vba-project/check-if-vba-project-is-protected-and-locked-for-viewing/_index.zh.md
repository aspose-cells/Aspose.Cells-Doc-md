---
title: 用JavaScript通过C++检查VBA项目是否受保护并锁定以供查看
linktitle: 检查VBA项目是否受保护并已锁定以供查看
type: docs
weight: 30
url: /zh/javascript-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: 学习如何使用Aspose.Cells for JavaScript通过C++检查Excel文件中的VBA项目是否受保护并锁定以供查看。
---

## 用JavaScript通过C++检查VBA项目是否已保护并锁定以供查看

Aspose.Cells允许你检测Excel文件的VBA（Visual Basic for Applications）项目是否已受保护且锁定查看。API提供[**VbaProject.islockedForViewing**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#islockedForViewing--)属性，如果被锁定查看，则返回[**VbaProject.islockedForViewing**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#islockedForViewing--)为**true**。

## **示例代码**

以下示例代码加载[示例Excel文件](43352065.xlsm)，并检查Excel文件的VBA（Visual Basic for Applications）项目是否受保护和锁定以供查看。请同时查看其控制台输出以获取参考。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Check VBA Project Protection Example</title>
    </head>
    <body>
        <h1>Check if VBA Project is Protected</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.xlsb,.csv" />
        <button id="runExample">Check VBA Protection</button>
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
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xlsm) to check.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the VBA project of the workbook.
            const vbaProject = workbook.vbaProject;

            // Whether "Lock project for viewing" is true or not.
            const isLocked = vbaProject ? vbaProject.islockedForViewing : null;

            if (isLocked === null) {
                resultDiv.innerHTML = '<p style="color: orange;">The workbook does not contain a VBA project.</p>';
            } else {
                resultDiv.innerHTML = `<p>Is VBA Project Locked for Viewing: <strong>${isLocked}</strong></p>`;
                console.log("Is VBA Project Locked for Viewing: " + isLocked);
            }
        });
    </script>
</html>
```

## **控制台输出**

这是上述示例代码在使用提供的[示例Excel文件](43352065.xlsm)时执行时的控制台输出。

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
