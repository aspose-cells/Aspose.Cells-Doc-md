---
title: 使用JavaScript通过C++查明VBA项目是否受保护
linktitle: 查看 VBA 项目是否已受保护
type: docs
weight: 20
url: /zh/javascript-cpp/find-out-if-vba-project-is-protected/
---

## ** 使用JavaScript查明VBA项目是否受保护**

你可以使用[**VbaProject.isProtected()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isProtected--)属性，判断Excel文件中的VBA（Visual Basic for Applications）项目是否被保护。

## **示例代码**

以下示例代码创建一个工作簿，然后检测其VBA项目是否受保护，然后保护此VBA项目，再次检测。请查看控制台输出作为参考。在保护前，[**VbaProject.isProtected()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isProtected--)返回**false**，保护后返回**true**。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Protect VBA Project Example</title>
    </head>
    <body>
        <h1>Protect VBA Project Example</h1>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Access the VBA project of the workbook.
            const vbaProj = workbook.vbaProject;

            // Find out if VBA Project is Protected using isProtected method.
            const beforeProtected = vbaProj.isProtected();
            console.log("IsProtected - Before Protecting VBA Project: " + beforeProtected);

            // Protect the VBA project.
            vbaProj.protect(true, "11");

            // Find out if VBA Project is Protected using isProtected method.
            const afterProtected = vbaProj.isProtected();
            console.log("IsProtected - After Protecting VBA Project: " + afterProtected);

            // Save the modified workbook as XLSM to preserve VBA project
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'vba_protected.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Protected Workbook';

            document.getElementById('result').innerHTML = `
                <p style="color: green;">Operation completed successfully!</p>
                <p>IsProtected before: ${beforeProtected}</p>
                <p>IsProtected after: ${afterProtected}</p>
            `;
        });
    </script>
</html>
```

## **控制台输出**

这是上述示例代码的控制台输出供参考。

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
