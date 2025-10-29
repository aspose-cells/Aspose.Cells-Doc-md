---
title: Проверьте, защищен ли и заблокирован ли проект VBA для просмотра с помощью JavaScript через C++
linktitle: Проверка защищен ли проект VBA и заблокирован для просмотра
type: docs
weight: 30
url: /ru/javascript-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: Узнайте, как проверить, защищен ли и заблокирован ли проект VBA в файле Excel для просмотра с помощью Aspose.Cells for JavaScript через C++. 
---

## Проверка, защищен ли и заблокирован ли проект VBA для просмотра с помощью JavaScript через C++

Aspose.Cells позволяет проверить, защищен ли VBA-проект файла Excel и заблокирован ли для просмотра. Для этого API предоставляет свойство [**VbaProject.islockedForViewing**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#islockedForViewing--). Если он заблокирован для просмотра, то свойство [**VbaProject.islockedForViewing**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#islockedForViewing--) возвращает **true**.

## **Образец кода**

Следующий пример кода загружает [пример файла Excel](43352065.xlsm) и проверяет, защищен ли VBA (Visual Basic for Applications) проект этого файла для просмотра. Также смотрите его вывод в консоли для справки.

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

## **Вывод в консоль**

Это вывод в консоль вышеупомянутого примера кода при выполнении с предоставленным [образцовым файлом Excel](43352065.xlsm).

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
