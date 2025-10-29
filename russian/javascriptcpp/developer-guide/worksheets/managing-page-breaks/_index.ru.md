---
title: Управление разрывами страниц с помощью JavaScript через C++
linktitle: Управление разрывами страниц
type: docs
weight: 30
url: /ru/javascript-cpp/managing-page-breaks/
description: В этой статье приведен пример кода и объясняется, как добавлять, очищать или удалять конкретные разрывы страниц в листах Excel программно с помощью Aspose.Cells for JavaScript через C++.
keywords: разрывы страниц JavaScript через C++, разрывы страниц Excel JavaScript через C++, очистка разрывов страниц JavaScript через C++, удаление конкретного разрыва страницы JavaScript через C++
---

{{% alert color="primary" %}}

Согласно определению, перерыв страницы - это место в текучем тексте, где заканчивается одна страница, и начинается другая. Microsoft Excel позволяет пользователям добавлять перерывы страницы в любую выбранную ячейку листа.

Местоположение ячейки, в которую добавлен перерыв страницы, страница заканчивается, и оставшиеся данные после перерыва странице печатаются на следующей странице во время печати. Проще говоря, перерывы страницы делят ваш лист на несколько страниц в соответствии с вашими спецификациями. Вы также можете добавлять перерывы страниц в свои листы во время выполнения с использованием Aspose.Cells. Aspose.Cells позволяет разработчикам добавлять два вида перерывов страницы:

- Горизонтальный перерыв страницы
- Вертикальный перерыв страницы

В остальной части обсуждения мы опишем, как вы можете добавить горизонтальные или вертикальные перерывы страниц в свои листы с использованием Aspose.Cells.

{{% /alert %}}

## **Разрывы страниц**

Aspose.Cells for JavaScript через C++ предоставляет класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который представляет файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит коллекцию [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--), позволяющую получать доступ к каждому листу в файле Excel.

Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) предоставляет широкий спектр свойств и методов, используемых для управления листом.

Для добавления перерывов страниц используйте свойства класса [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) и методы [**worksheet.horizontalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#horizontalPageBreaks--) и [**worksheet.verticalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#verticalPageBreaks--).

Свойства [**worksheet.horizontalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#horizontalPageBreaks--) и [**worksheet.verticalPageBreaks**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#verticalPageBreaks--) являются коллекциями, которые могут содержать несколько перерывов страницы. Каждая коллекция содержит несколько методов для управления горизонтальными и вертикальными перерывами страниц.

### **Добавление разрывов страниц**

Чтобы добавить разрыв страницы в лист, вставьте вертикальные и горизонтальные разрывы страниц в указанную ячейку, вызвав методы [**HorizontalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/horizontalpagebreakcollection/#add-number-number-number-) и [**VerticalPageBreakCollection.add(number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/verticalpagebreakcollection/#add-number-number-number-). Каждый метод **add** принимает название ячейки, в которую необходимо вставить разрыв.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Adding Page Breaks Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add a page break at cell Y30
            worksheet.horizontalPageBreaks.add("Y30");
            worksheet.verticalPageBreaks.add("Y30");

            // Save the Excel file (Excel 97-2003 format .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddingPageBreaks_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page breaks added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

В режиме предварительного просмотра разрывов страниц или предварительного просмотра печати можно увидеть, как работают эти разрывы страниц.

{{% /alert %}}

### **Удаление определенного разрыва страницы**

Чтобы удалить конкретный разрыв страницы, вызовите методы [**HorizontalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/javascript-cpp/horizontalpagebreakcollection/#removeAt-number-) и [**VerticalPageBreakCollection.removeAt(number)**](https://reference.aspose.com/cells/javascript-cpp/verticalpagebreakcollection/#removeAt-number-). Каждый метод **removeAt** принимает индекс разрыва страницы, который необходимо удалить.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Remove Specific Page Break Example</title>
    </head>
    <body>
        <h1>Remove Specific Page Break Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            // Removing a specific page break
            worksheet.horizontalPageBreaks.removeAt(0);
            worksheet.verticalPageBreaks.removeAt(0);

            // Saving the Excel file (Excel 97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RemoveSpecificPageBreak_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Page breaks removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Важно знать**

Когда вы устанавливаете свойства **fitToPages** (то есть [**PageSetup.fitToPagesTall**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesTall--) и [**PageSetup.fitToPagesWide**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#fitToPagesWide--)) в настройках разметки страницы, настройки разрывов страниц оказывают влияние, поэтому при печати листа настройки разрывов страниц не учитываются, хотя они все еще установлены.
