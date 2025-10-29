---
title: Проверьте, подписан ли проект VBA в рабочей книге с помощью JavaScript через C++
linktitle: Проверка подписан ли проект VBA в книге Excel
type: docs
weight: 70
url: /ru/javascript-cpp/check-if-vba-project-in-a-workbook-is-signed/
description: Узнайте, как проверить, подписан ли проект VBA в рабочей книге с помощью Aspose.Cells for JavaScript через C++. 
---

{{% alert color="primary" %}}

Вы можете проверить подписан ли ваш проект VBA или нет, используя Microsoft Excel через меню **Инструменты > Цифровые подписи...**. Аналогичным образом, вы можете проверить это программным способом с помощью свойства [**Workbook.vbaProject**](https://reference.aspose.com/cells/javascript-cpp/workbook/#vbaProject--) библиотеки Aspose.Cells.

{{% /alert %}}

## **Проверьте, подписан ли проект VBA в рабочей книге с помощью JavaScript**

Следующий код загружает рабочую книгу и проверяет, подписан ли VBA-проект с помощью свойства [**Workbook.vbaProject**](https://reference.aspose.com/cells/javascript-cpp/workbook/#vbaProject--). Свойство вернет **true**, если проект подписан, иначе — **false**.

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
