---
title: Блокировать или разблокировать формы с помощью JavaScript через C++
linktitle: Запереть или разблокировать формы
type: docs
weight: 200
url: /ru/javascript-cpp/lock-or-unlock-shapes/
description: В этой статье представлен код, объясняющий, как блокировать или разблокировать формы для их защиты с помощью библиотеки Aspose.Cells для JavaScript через C++.
keywords: Блокировка форм с помощью JavaScript через C++, как блокировать или разблокировать формы с помощью JavaScript через C++, блокировать или разблокировать формы для защиты в JavaScript через C++.
---

## **Возможные сценарии использования**

Иногда вам нужно защитить все формы в определенных листах, чтобы предотвратить их уничтожение нежелательными ситуациями. В этом случае вам нужно запереть все формы на указанном листе. 

Блокировка фигур в таблице или документе может быть полезна по нескольким причинам:
1. Предотвращение случайных изменений: блокировка фигур гарантирует, что их случайно не переместят, не изменят размер или не удалят пользователи. Особенно важно в сложных документах, где фигуры используются для аннотаций, иллюстраций или как часть дизайна документа.
1. Поддержание макета и дизайна: фигуры часто играют важную роль в раскладке и внешнем виде документа. Блокировка сохраняет задуманный внешний вид, делая документ профессиональным и визуально привлекательным.
1. Целостность данных: в таблицах фигуры могут использоваться для выделения важных данных, добавления комментариев или предоставления визуальных объяснений. Блокировка этих фигур обеспечивает сохранение точности и целостности предоставляемой ими контекстной информации.
1. Последовательность в совместных документах: при совместной работе над документами разные пользователи могут обладать разным уровнем опыта. Блокировка фигур помогает поддерживать согласованность документа, предотвращая непреднамеренные изменения.
1. Безопасность: в чувствительных документах блокировка фигур может быть частью общей стратегии защиты информации. Например, в финансовых отчетах или юридических документах заблокированные фигуры используются для защиты конкретных аннотаций или выделений, предоставляющих важный контекст.

Иногда необходимо иметь возможность изменять определенные фигуры в защищенных листах, в таком случае нужно разблокировать эти фигуры. Эта статья подробно расскажет, как блокировать и разблокировать указанные фигуры.

## **Как заблокировать фигуры для их защиты в Excel**

Вот как можно заблокировать ячейки в Microsoft Excel:

1. Откройте файл Excel: Откройте файл Excel, содержащий фигуры, которые вы хотите заблокировать.

1. Выберите фигуру: Щелкните по фигуре, которую хотите заблокировать. Также можно выбрать несколько фигур, зажав клавишу Ctrl и щелкая по каждой фигуре.

1. Откройте панель форматирования фигуры: Щелкните правой кнопкой по выбранной фигуре(ям) и выберите "Размер и свойства". Или перейдите на вкладку "Формат" на ленте и в группе "Размер" нажмите на значок диалогового окна (маленькая стрелка) для открытия панели "Формат фигуры".
1. Заблокируйте фигуру: В панели "Формат фигуры" перейдите на вкладку "Размер и свойства" (значок, похожий на квадрат со стрелками). В разделе "Свойства" установите галочку возле "Заблокировано".
<br>
<img src="1.png" width=60% />
1. Защитите лист: Перейдите на вкладку "Рецензирование" на ленте. Нажмите "Защитить лист." Установите пароль (по желанию) и выберите разрешения, которые хотите разрешить (например, выбор заблокированных ячеек, форматирование ячеек и т.д.). Нажмите "ОК."
<br>
<img src="2.png" width=60% />

## **Как заблокировать все фигуры в определенном листе**

Для защиты всех фигур на указанном листе используйте метод `worksheet.protect(ProtectionType.Objects)`, как показано в следующем примере кода.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Lock Shapes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType } = AsposeCells;

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

            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const text = "This is a test";
            const worksheet = workbook.worksheets.get(0);

            let shape = worksheet.shapes.addTextBox(1, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addRectangle(5, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addButton(9, 0, 1, 0, 30, 100);
            shape.text = text;

            shape = worksheet.shapes.addOval(13, 0, 1, 0, 50, 100);
            shape.text = text;

            // Protect all shapes in the specified worksheet
            shape.worksheet.protect(ProtectionType.Objects);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Locked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Locked.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shapes locked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Как разблокировать указанные фигуры в защищённом листе**

Чтобы разблокировать указанную фигуру на защищённом листе, используйте `shape.isLocked`, как показано в следующем примере кода.

Примечание: `shape.isLocked` имеет смысл только при защищённом листе.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Unlock Shape</title>
    </head>
    <body>
        <h1>Unlock Shape Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get protected worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get the specified shape to be unlocked
            const shape = worksheet.shapes.get("TextBox 1");

            if (!shape) {
                resultDiv.innerHTML = '<p style="color: red;">Shape "TextBox 1" not found.</p>';
                return;
            }

            // Unlock the specified shape
            if (!worksheet.protection.allowEditingObject && shape.isLocked) {
                shape.isLocked = false;
            }

            // Save the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'UnLocked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Shape unlocked successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
