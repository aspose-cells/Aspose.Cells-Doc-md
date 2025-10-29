---
title: Показать и скрывать листы и вкладки с помощью JavaScript через C++
linktitle: Показывать и скрывать рабочие листы и вкладки
type: docs
weight: 10
url: /ru/javascript-cpp/show-and-hide-worksheets-and-tabs/
description: В этой статье представлен пример кода для использования API JavaScript или библиотеки JavaScript для программного отображения и скрытия листа Excel. Также показано, как отображать и скрывать вкладки рабочей книги Excel.
---

{{% alert color="primary" %}}
Aspose.Cells позволяет пользователю показывать и скрывать элементы книги, включая рабочие листы и вкладки.
{{% /alert %}}

## **Показать и скрыть лист**

Файл Excel может содержать один или более листов. Всякий раз, когда мы создаем файл Excel, мы добавляем листы в файл Excel, в котором работаем. Каждый лист в файле Excel независим от другого листа и имеет свои собственные данные и настройки форматирования и т. д. Иногда разработчики могут захотеть скрыть несколько листов и сделать другие видимыми в файле Excel по своему усмотрению. Таким образом, **Aspose.Cells** позволяет разработчикам контролировать видимость листов в их файлах Excel.

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который представляет файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит коллекцию [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--), для доступа к каждому листу файла Excel.

Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) предоставляет широкий набор свойств и методов для управления листами. Для управления видимостью листа используйте свойство [**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--) класса [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). [**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--) — логическое свойство, которое может хранить только значение **true** или **false**.

### **Сделать лист видимым**

Сделать лист видимым, установив свойство [**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--) класса [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) в **true**.

### **Скрыть лист**

Скрыть лист, установив свойство [**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--) класса [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) в **false**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hide Worksheet Example</title>
    </head>
    <body>
        <h1>Hide Worksheet Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding the first worksheet of the Excel file
            worksheet.isVisible = false;

            // Saving the modified Excel file in Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Показывать и скрывать вкладки**

Если вы внимательно посмотрите внизу файла Microsoft Excel, вы увидите ряд элементов управления. Среди них:

- Вкладки листов.
- Кнопки прокрутки вкладок.

Вкладки представляют листы Excel-файла. Щелкните на любой вкладке, чтобы переключиться на этот лист. Чем больше листов в книге Excel, тем больше вкладок. Если в Excel-файле большое количество листов, вам понадобятся кнопки для перемещения по ним. Поэтому Microsoft Excel предоставляет кнопки прокрутки вкладок для прокрутки по вкладкам.

С помощью Aspose.Cells разработчики могут контролировать видимость вкладок листов и кнопок прокрутки в файле Excel.

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который представляет файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) предлагает широкий набор свойств и методов для управления файлом Excel. Для управления видимостью вкладок в файле Excel разработчики могут использовать свойство [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--) класса [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook). [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--) — логическое свойство, которое может хранить только значение **true** или **false**.

### **Отображение вкладок**

Сделайте вкладки видимыми, установив свойство [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--) класса [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) в **true**.

### **Скрытие вкладок**

Скрыть вкладки в файле Excel, установив свойство [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--) класса [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) в **false**.

Ниже приведен полный пример, который открывает файл Excel (book1.xls), скрывает его вкладки и сохраняет измененный файл как output.xls. После выполнения кода вы увидите, что вкладки книги скрыты.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide Worksheet Tabs Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Hiding the tabs of the Excel file
            workbook.settings.showTabs = false;

            // To show the tabs instead, you could set:
            // workbook.settings.showTabs = true;

            // Saving the modified Excel file (Excel 97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Tabs hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Управление Шириной Панели Вкладок**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Hide Tabs</title>
    </head>
    <body>
        <h1>Hide Tabs Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Hiding the tabs of the Excel file (converted setter to property)
            workbook.settings.showTabs = true;

            // Adjusting the sheet tab bar width (converted setter to property)
            workbook.settings.sheetTabBarWidth = 800;

            // Saving the modified Excel file (SaveFormat.Xls -> SaveFormat.Excel97To2003)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
