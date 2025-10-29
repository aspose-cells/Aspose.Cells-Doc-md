---
title: Копировать настройки Page Setup из исходного листа в целевой с помощью JavaScript через C++
linktitle: Скопировать настройки страницы из исходного листа в назначенный лист
type: docs
weight: 80
url: /ru/javascript-cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: В этой статье объясняется, как использовать JavaScript API или пример кода библиотеки C++, чтобы программно копировать настройки Page Setup с исходного листа на целевой.
keywords: Копировать настройки Page Setup с помощью JavaScript через C++, копировать настройки в целевой лист с помощью JavaScript через C++
---

## **Возможные сценарии использования**

Когда вы добавляете новый лист в рабочую книгу, он содержит настройки *Page Setup* по умолчанию. Иногда необходимо перенести эти настройки ([**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup)) с одного листа на другой. В этой документации объясняется, как копировать настройки Page Setup с одного листа на другой с помощью API Script Aspose.Cells for Java через C++.

## **Копирование настроек страницы с исходного листа на целевой лист**

Следующий образец кода иллюстрирует, как скопировать *Параметры страницы* с одного листа на другой с использованием метода [**PageSetup.copy(PageSetup, CopyOptions)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#copy-pagesetup-copyoptions-). Обратитесь к следующему образцу кода и его выводу консоли для справки.

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PageSetup Copy</title>
    </head>
    <body>
        <h1>PageSetup Copy Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CopyOptions, PaperSizeType, Utils } = AsposeCells;

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
            // Create workbook
            const wb = new Workbook();

            // Add two test worksheets
            wb.worksheets.add("TestSheet1");
            wb.worksheets.add("TestSheet2");

            // Access both worksheets as TestSheet1 and TestSheet2
            const TestSheet1 = wb.worksheets.get("TestSheet1");
            const TestSheet2 = wb.worksheets.get("TestSheet2");

            // Set the Paper Size of TestSheet1 to PaperA3ExtraTransverse
            TestSheet1.pageSetup.paperSize = PaperSizeType.PaperA3ExtraTransverse;

            // Print the Paper Size of both worksheets (before copy)
            const before1 = TestSheet1.pageSetup.paperSize;
            const before2 = TestSheet2.pageSetup.paperSize;

            // Copy the PageSetup from TestSheet1 to TestSheet2
            TestSheet2.pageSetup.copy(TestSheet1.pageSetup, new CopyOptions());

            // Print the Paper Size of both worksheets (after copy)
            const after1 = TestSheet1.pageSetup.paperSize;
            const after2 = TestSheet2.pageSetup.paperSize;

            // Display results
            document.getElementById('result').innerHTML =
                '<pre>' +
                'Before Paper Size (TestSheet1): ' + before1 + '\n' +
                'Before Paper Size (TestSheet2): ' + before2 + '\n\n' +
                'After Paper Size (TestSheet1): ' + after1 + '\n' +
                'After Paper Size (TestSheet2): ' + after2 +
                '</pre>';

            // Saving the modified Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```

## **Вывод в консоль**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
