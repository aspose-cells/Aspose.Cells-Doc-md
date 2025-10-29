---
title: Защита листов с помощью JavaScript через C++
linktitle: Защита листов
type: docs
weight: 10
url: /ru/javascript-cpp/protecting-worksheets/
description: узнайте, как защитить листы в Excel с помощью Aspose.Cells for JavaScript через C++, включая защиту строк, колонок и отдельных ячеек.
---

{{% alert color="primary" %}}

Когда лист защищён, действия, доступные пользователю, ограничены. Например, он не может вводить данные, вставлять или удалять строки или столбцы и т.п.

{{% /alert %}}

## **Защита листов**

### **Введение**

Основные параметры защиты в Microsoft Excel:

- Содержимое
- Объекты
- Сценарии

Защита листов не скрывает и не защищает конфиденциальные данные, поэтому это отличается от шифрования файлов. Обычно защита листа подходит для ознакомительных целей. Она предотвращает изменение данных, содержимого и форматирования в листе.

### **Защита листа**

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--), которая позволяет получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet).

Класс [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) предоставляет метод [**protect(ProtectionType)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protect-protectiontype-), который используется для применения защиты на листе. Метод [**protect(ProtectionType)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#protect-protectiontype-) принимает следующие параметры:

- Тип защиты, тип защиты, применяемый к листу. Тип защиты применяется с помощью перечисления [**ProtectionType**](https://reference.aspose.com/cells/javascript-cpp/protectiontype).
- Новый пароль, новый пароль, используемый для защиты листа.
- Старый пароль, старый пароль, если лист уже защищен паролем. Если лист еще не защищен, то просто передайте null.

Перечисление [**ProtectionType**](https://reference.aspose.com/cells/javascript-cpp/protectiontype) содержит следующие предопределённые типы защиты:

|**Типы защиты**|**Описание**|
| :- | :- |
|All|Пользователь не может изменять ничего на этом листе|
|Contents|Пользователь не может вводить данные на этом листе|
|Objects|Пользователь не может изменять рисуночные объекты|
|Scenarios|Пользователь не может изменять сохраненные сценарии|
|Structure|Пользователь не может изменять структуру|
|Windows|Защита применяется к окнам|
|None|Никакая защита не применяется|

Приведенный ниже пример показывает, как защитить лист паролем.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Protect Worksheet Example</title>
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

            // Ensure Aspose.Cells is initialized before proceeding
            await AsposeCells.onReady();

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object with file buffer
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Protecting the worksheet with a password
            worksheet.protect(ProtectionType.All, "aspose", null);

            // Saving the modified Excel file in Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Как только указанный выше код используется для защиты листа, вы можете проверить защиту на листе, открыв его. После открытия файла и попытки добавить данные на лист, вы увидите следующий диалог:

|**Предупреждение о том, что пользователь не может изменять лист**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

Для работы на листе снимите защиту листа, выбрав **Защита**, затем **Снять защиту таблицы** из меню **Инструменты**.

После выбора пункта меню Снять защиту таблицы откроется диалоговое окно, призывающее вас ввести пароль, чтобы вы могли работать на листе, как показано ниже:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **Защита нескольких ячеек на листе c помощью Microsoft Excel**

В некоторых случаях нужно защитить только определённые ячейки в листе. Если вы хотите заблокировать конкретные ячейки, необходимо разблокировать все остальные ячейки в листе. Все ячейки в листе изначально настроены на блокировку; проверьте это, открыв любой файл Excel в MS Excel, выбрав **Формат | Ячейки...**, чтобы открыть диалоговое окно **Формат ячейки**, и перейдя на вкладку **Защита**, где по умолчанию стоит флажок «Заблокировано».

Следующие пункты описывают, как заблокировать ячейки в MS Excel. Этот метод подходит для Microsoft Office Excel 97, 2000, 2002, 2003 и более новых версий.

1. Выберите весь лист, нажав кнопку **Выбрать все** (серый прямоугольник над номером строки для строки 1 и слева от буквы столбца A).
2. Нажмите **Ячейки** в меню **Формат**, перейдите на вкладку **Защита**, и снимите галочку с **Заблокировано**.
   Это разблокирует все ячейки в листе.
   Если команда **Ячейки** недоступна, части листа могут уже быть заблокированы. На меню **Инструменты** наведите указатель на **Защита**, а затем щелкните **Снять защиту листа**.
3. Выберите только те ячейки, которые нужно заблокировать, и повторите шаг 2, но на этот раз выберите флажок **Заблокировано**.
4. В меню **Инструменты** наведите указатель на **Защита**, выберите **Защитить лист** и нажмите **ОК**.
5. В диалоговом окне **Защита листа** у вас есть возможность указать пароль и выбрать элементы, которые пользователи смогут изменять.

### **Защитите несколько ячеек в листе, используя Aspose.Cells**

В этом методе мы используем только API Aspose.Cells для выполнения задачи.

Пример: Следующий пример показывает, как защитить несколько ячеек в листе. Он сначала разблокирует все ячейки листа, затем блокирует 3 ячейки (A1, B1, C1). В конце он защищает лист. Объект [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) содержит свойство типа boolean, [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--). Вы можете установить свойство [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) в true или false и применить метод *Column/Row.applyStyle()* для блокировки или разблокировки строки/столбца с желаемыми атрибутами.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Unlock Columns and Protect Specific Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            await readyPromise;

            // Create a new workbook.
            const wb = new Workbook();

            // Create a worksheet object and obtain the first sheet.
            const sheet = wb.worksheets.get(0);

            // Define the style object.
            let style;

            // Define the styleflag object
            const styleflag = new StyleFlag();

            // Loop through all the columns in the worksheet and unlock them.
            for (let i = 0; i <= 255; i++) {
                style = sheet.cells.columns.get(i).style;
                style.isLocked = false;
                styleflag.locked = true;
                sheet.cells.columns.get(i).applyStyle(style, styleflag);
            }

            // Lock the three cells...i.e. A1, B1, C1.
            style = sheet.cells.get("A1").style;
            style.isLocked = true;
            sheet.cells.get("A1").style = style;

            style = sheet.cells.get("B1").style;
            style.isLocked = true;
            sheet.cells.get("B1").style = style;

            style = sheet.cells.get("C1").style;
            style.isLocked = true;
            sheet.cells.get("C1").style = style;

            // Finally, Protect the sheet now.
            sheet.protect(ProtectionType.All);

            // Save the excel file and provide download link
            const outputData = wb.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Защита строки на листе**

Aspose.Cells позволяет легко блокировать любую строку в листе. Здесь мы можем использовать метод [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-) класса [**Aspose.Cells.Row**](https://reference.aspose.com/cells/javascript-cpp/row), чтобы применить [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) к конкретной строке в листе. Этот метод принимает два аргумента: объект [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) и объект [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag), который содержит все участники, связанные с применением форматирования.

Следующий пример показывает, как защитить строку в листе. Он сначала разблокирует все ячейки листа, затем блокирует первую строку. В конце он защищает лист. Объект [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) содержит свойство типа boolean, [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--). Вы можете установить свойство [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) в true или false, чтобы заблокировать или разблокировать строку/столбец, используя объект [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType, Utils } = AsposeCells;

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
            // Create a new workbook.
            const wb = new Workbook();

            // Create a worksheet object and obtain the first sheet.
            const sheet = wb.worksheets.get(0);

            // Define the style object.
            let style;

            // Define the styleflag object.
            const flag = new StyleFlag();

            // Loop through all the columns in the worksheet and unlock them.
            for (let i = 0; i <= 255; i++) {
                style = sheet.cells.columns.get(i).style;
                style.isLocked = false;
                flag.locked = true;
                sheet.cells.columns.get(i).applyStyle(style, flag);
            }

            // Get the first row style.
            style = sheet.cells.rows.get(0).style;

            // Lock it.
            style.isLocked = true;

            // Set the lock setting.
            flag.locked = true;

            // Apply the style to the first row.
            sheet.cells.applyRowStyle(0, style, flag);

            // Protect the sheet.
            sheet.protect(ProtectionType.All);

            // Save the excel file.
            const outputData = wb.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and protected. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Защита столбца на листе**

Aspose.Cells позволяет легко заблокировать любой столбец в листе. Мы можем использовать метод [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/column/#applyStyle-style-styleflag-) класса [**Aspose.Cells.Column**](https://reference.aspose.com/cells/javascript-cpp/column), чтобы применить [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) к конкретному столбцу. Этот метод принимает два аргумента: объект [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) и объект [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag), который содержит все участники, связанные с применением форматирования.

Следующий пример показывает, как защитить столбец в листе. Он сначала разблокирует все ячейки листа, затем блокирует первый столбец. В конце он защищает лист. Объект [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) содержит свойство типа boolean, [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--). Вы можете установить свойство [**isLocked()**](https://reference.aspose.com/cells/javascript-cpp/style/#isLocked--) в true или false, чтобы заблокировать или разблокировать строку/столбец, используя объект [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Unlock Columns and Protect Sheet</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, ProtectionType } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
                // If no file provided, a new workbook will be created
                document.getElementById('result').innerHTML = '<p style="color: orange;">No file selected. A new workbook will be created and processed.</p>';
            } else {
                document.getElementById('result').innerHTML = '<p>Processing selected file...</p>';
            }

            await readyPromise;

            // Load workbook from file if provided, otherwise create new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Create a worksheet object and obtain the first sheet.
            const sheet = workbook.worksheets.get(0);

            // Define the style object.
            let style;

            // Define the styleflag object.
            const flag = new StyleFlag();

            // Loop through all the columns in the worksheet and unlock them.
            for (let i = 0; i <= 255; i++) {
                style = sheet.cells.columns.get(i).style;
                style.isLocked = false;
                flag.locked = true;
                sheet.cells.columns.get(i).applyStyle(style, flag);
            }

            // Get the first column style.
            style = sheet.cells.columns.get(0).style;

            // Lock it.
            style.isLocked = true;

            // Apply the style to the first column.
            sheet.cells.columns.get(0).applyStyle(style, flag);

            // Protect the sheet.
            sheet.protect(ProtectionType.All);

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Разрешить пользователям редактировать диапазоны**

В следующем примере показано, как разрешить пользователям редактировать диапазон в защищенном листе.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Protect Range</title>
    </head>
    <body>
        <h1>Protect Range Example</h1>
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

            // Instantiate a new or loaded Workbook
            let book;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                book = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                book = new Workbook();
            }

            // Get the first (default) worksheet
            const sheet = book.worksheets.get(0);

            // Get the Allow Edit Ranges
            const allowRanges = sheet.allowEditRanges;

            // Define ProtectedRange
            let protected_range;

            // Create the range
            const idx = allowRanges.add("r2", 1, 1, 3, 3);
            protected_range = allowRanges.get(idx);

            // Specify the password
            protected_range.password = "123";

            // Protect the sheet
            sheet.protect(ProtectionType.All);

            // Save the Excel file
            const outputData = book.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'protectedrange.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Protected Range Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Protected range added and sheet protected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
