---
title: Расширенные настройки защиты с Excel XP с помощью JavaScript и C++
linktitle: Расширенные настройки защиты с Excel XP
type: docs
weight: 30
url: /ru/javascript-cpp/advanced-protection-settings-since-excel-xp/
---

{{% alert color="primary" %}}

С момента выпуска Excel 2002 или XP, Microsoft добавила множество расширенных настроек защиты.

{{% /alert %}}


## **Введение**

Эти настройки защиты ограничивают или разрешают пользователям:

- Удалить строки или столбцы.
- Редактировать содержимое, объекты или сценарии.
- Форматировать ячейки, строки или столбцы.
- Вставлять строки, столбцы или гиперссылки.
- Выбирать заблокированные или разблокированные ячейки.
- Использовать сводные таблицы и многое другое.

 Aspose.Cells for JavaScript через C++ поддерживает все расширенные настройки защиты, предлагаемые Excel XP и более поздними версиями.

### **Настройки расширенной защиты с использованием Excel XP и более поздних версий**

Чтобы просмотреть доступные настройки защиты в Excel XP:

1. Из меню **Инструменты** выберите **Защита**, а затем **Защитить лист**. Будет отображено диалоговое окно.

Чтобы просмотреть доступные настройки защиты в Excel 2016:

1. В меню **Файл** выберите **Защита книги**, а затем **Защитить текущий лист**.
1. Выберите **Защитить лист** в меню **Проверка**.

Следующие шаги откроют диалоговое окно, в котором вы можете разрешить или ограничить функции листа или применить пароль к листу.

### ** Расширенные настройки защиты с помощью Aspose.Cells for JavaScript через C++**

 Aspose.Cells for JavaScript через C++ поддерживает все расширенные настройки защиты.

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection), позволяющую получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet).

Класс [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) предоставляет свойство [**protection**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protection--), которое используется для применения этих расширенных настроек защиты. Свойство [**protection**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protection--) является объектом класса [**Protection**](https://reference.aspose.com/cells/javascript-cpp/protection), который инкапсулирует несколько булевых свойств для отключения или включения ограничений.

Ниже приведен небольшой пример приложения. Он открывает файл Excel и использует большинство поддерживаемых Excel XP и более поздних версий настроек защиты.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Worksheet Protection Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const worksheet = workbook.worksheets.get(0);
            const protection = worksheet.protection;

            // Restricting users to delete columns of the worksheet
            protection.allowDeletingColumn = false;

            // Restricting users to delete row of the worksheet
            protection.allowDeletingRow = false;

            // Restricting users to edit contents of the worksheet
            protection.allowEditingContent = false;

            // Restricting users to edit objects of the worksheet
            protection.allowEditingObject = false;

            // Restricting users to edit scenarios of the worksheet
            protection.allowEditingScenario = false;

            // Restricting users to filter
            protection.allowFiltering = false;

            // Allowing users to format cells of the worksheet
            protection.allowFormattingCell = true;

            // Allowing users to format rows of the worksheet
            protection.allowFormattingRow = true;

            // Allowing users to insert columns in the worksheet
            protection.allowFormattingColumn = true;

            // Allowing users to insert hyperlinks in the worksheet
            protection.allowInsertingHyperlink = true;

            // Allowing users to insert rows in the worksheet
            protection.allowInsertingRow = true;

            // Allowing users to select locked cells of the worksheet
            protection.allowSelectingLockedCell = true;

            // Allowing users to select unlocked cells of the worksheet
            protection.allowSelectingUnlockedCell = true;

            // Allowing users to sort
            protection.allowSorting = true;

            // Allowing users to use pivot tables in the worksheet
            protection.allowUsingPivotTable = true;

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protection settings applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Пожалуйста, не вызывайте метод [**protect(ProtectionType)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protect-protectiontype-) класса [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) при использовании свойства [**protection**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protection--). Также сохраните файл в форматах Excel97To2003 или Xlsx, потому что расширенные настройки защиты поддерживаются только в Excel XP и более поздних версиях.

{{% /alert %}}

### **Проблема блокировки ячеек**

Если вы хотите ограничить редактирование ячеек пользователями, ячейки должны быть защищены (заблокированы) перед применением любых настроек защиты. В противном случае, ячейки могут редактироваться даже если лист защищен. В Microsoft Excel XP ячейки можно заблокировать через следующий диалог:

|**Диалог для блокировки ячеек в Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

Также возможно заблокировать ячейки с помощью API Aspose.Cells. Каждая ячейка может иметь формат [**Style**](https://reference.aspose.com/cells/javascript-cpp/style), который содержит логическое свойство [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--). Установите свойство [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) в **true** или **false**, чтобы заблокировать или разблокировать ячейку.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType, Utils } = AsposeCells;

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

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Lock cell A1 by setting the style property
            const cell = worksheet.cells.get("A1");
            cell.style.isLocked = true;

            // Protect the sheet now.
            worksheet.protect(ProtectionType.All);

            // Saving the modified Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
