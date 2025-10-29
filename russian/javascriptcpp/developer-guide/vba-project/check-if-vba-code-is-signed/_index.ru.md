---
title: Проверка подписи VBA кода с помощью JavaScript через C++
linktitle: Проверить, подписан ли код VBA
type: docs
weight: 100
url: /ru/javascript-cpp/check-if-vba-code-is-signed/
description: Узнайте, как проверить, подписан ли проект VBA кода с помощью Aspose.Cells for JavaScript через C++. 
---

{{% alert color="primary" %}}

Aspose.Cells позволяет пользователю проверить, подписан ли проект кода VBA или нет. Используйте свойство [**VbaProject.isSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isSigned--) для проверки, подписан ли проект кода VBA или нет.

{{% /alert %}}

Следующий код показывает, как проверить, подписан ли VBA-код с помощью свойства [**VbaProject.isSigned()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isSigned--). Вы можете использовать любой из ваших файлов Excel для тестирования этого кода. Для тестирования можно использовать [этот Excel-файл, использованный в коде](5115032.xlsm).

## **Проверьте, подписан ли VBA-код в JavaScript**

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

## Вывод в консоль

Ниже представлен вывод в консоль вышеупомянутого кода с использованием [образцового файла Excel](5115032.xlsm), предоставленного по ссылке.

{{< highlight java >}}

Is VBA Code Project Signed: True

{{< /highlight >}}
