---
title: Конвертировать файл Excel в совместимый с PDF/A 1a формат PDF с помощью JavaScript через C++
linktitle: Конвертация Excel файла в формат PDF, совместимый с PDF/A 1a
type: docs
weight: 130
url: /ru/javascript-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: Узнайте, как преобразовать файлы Excel в соответствующие PDF файлы PDF/A с помощью Script Aspose.Cells for Java через C++.
---

## **Возможные сценарии использования**  

PDF/A — это уникальный вариант PDF, предназначенный для долгосрочного хранения документов. PDF/A — это стандартизированная версия формата Portable Document Format (PDF), которая является архивным форматом PDF и встраивает все используемые шрифты внутри файла PDF. PDF/A отличается от PDF запретом на использование таких функций, как связывание шрифтов (в отличие от встраивания шрифтов) и шифрование. Script Aspose.Cells for Java через C++ позволяет сохранять Excel файлы в PDF/A-совместимые PDF файлы (поддерживаются разные стандарты PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab и PDF/A-3u). В этой статье описано, как сохранить рабочую книгу Excel в PDF, совместимый с PDF/A (PDF/A-1a).  

## **Преобразовать файл Excel в формат PDF, совместимый с PDF/A-1a**  

Разработчики могут использовать класс [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) для установки различных атрибутов для преобразования. Установка различных свойств класса [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) дает контроль над настройками печати, шрифтов, безопасности и сжатия для создаваемого PDF. Самым важным свойством является [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#compliance--), позволяющее сохранять файлы Excel в архивные PDF-файлы.  

Следующий пример объясняет, как преобразовать файл Excel в PDF-совместимый с PDF/A-1a. См. его [выходной PDF](outputCompliancePdfA1a.pdf) и скриншот для справки.  

## **Снимок экрана**  

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)  

## **Образец кода**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export to PDF (PDFA-1a) Example</h1>
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
            // Create workbook object
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access cell B5 and add some message inside it
            const cell = ws.cells.get("B5");
            cell.value = "This PDF format is compatible with PDFA-1a.";

            // Create pdf save options and set its compliance to PDFA-1a
            const opts = new AsposeCells.PdfSaveOptions();
            opts.compliance = AsposeCells.PdfCompliance.PdfA1a;

            // Save the output pdf
            const outputData = wb.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCompliancePdfA1a.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
