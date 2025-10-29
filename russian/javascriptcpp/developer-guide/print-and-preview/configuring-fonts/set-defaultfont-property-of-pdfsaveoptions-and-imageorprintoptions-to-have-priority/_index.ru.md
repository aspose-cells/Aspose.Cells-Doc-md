---
title: Задайте приоритет свойству DefaultFont в PdfSaveOptions и ImageOrPrintOptions через JavaScript с помощью C++
linktitle: Установите свойство DefaultFont объектов PdfSaveOptions и ImageOrPrintOptions в приоритетном порядке
type: docs
weight: 30
url: /ru/javascript-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: Узнайте, как установить свойство DefaultFont в PdfSaveOptions и ImageOrPrintOptions с помощью Aspose.Cells for JavaScript через C++. Обеспечьте правильное отображение шрифтов при отсутствии шрифтов.
---

## **Возможные сценарии использования**

При установке свойства **DefaultFont** объекта [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) и [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/), возможно, вы ожидаете, что сохранение в PDF или изображение установит этот DefaultFont для всего текста в книге, у которого отсутствует (не установлен) шрифт.

Обычно при сохранении в PDF или изображение Aspose.Cells for JavaScript через C++ сначала пытается установить шрифт по умолчанию книги (то есть `Workbook.DefaultStyle.Font`). Если шрифт по умолчанию оставить нельзя, тогда Aspose.Cells попытается отрисовать с помощью шрифта, указанного в атрибуте DefaultFont в [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions). 

Чтобы соответствовать вашим ожиданиям, у нас есть логическое свойство с именем "**CheckWorkbookDefaultFont**" в [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/). Вы можете установить его в **false**, чтобы отключить попытку использования шрифта по умолчанию книги или предоставить приоритет настройке **DefaultFont** в [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/).

## **Установите свойство DefaultFont объектов PdfSaveOptions/ImageOrPrintOptions**

 Следующий пример кода открывает файл Excel. Ячейка A1 (в первом листе) содержит текст "Christmas Time Font text". Название шрифта — "Christmas Time Personal Use", который не установлен на машине. Мы устанавливаем атрибут **DefaultFont** в [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) в "Times New Roman". Также устанавливаем свойство **CheckWorkbookDefaultFont** в значение **"false"**, что гарантирует отображение текста ячейки A1 с шрифтом "Times New Roman" и не использует шрифт по умолчанию рабочей книги (в данном случае — "Calibri"). Код рендерит первый рабочий лист в форматы изображений PNG и TIFF, а затем в PDF.

{{% alert color="primary" %}}

 Значение по умолчанию для атрибута **CheckWorkbookDefaultFont** равно **true**.

{{% /alert %}}

Это скриншот [шаблонного файла](49446913.xlsx), используемого в примере кода.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

 Это изображение PNG после установки свойства [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) в "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

 См. изображение [TIFF](48496672.tiff) после установки свойства [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) в "Times New Roman".

 См. файл [PDF](48496673.pdf) после установки свойства [**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--) в "Times New Roman".

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Default Font for Export (PNG, TIFF, PDF)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadPng" style="display: none;">Download PNG</a><br/>
            <a id="downloadTiff" style="display: none;">Download TIFF</a><br/>
            <a id="downloadPdf" style="display: none;">Download PDF</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageOrPrintOptions, ImageType, SheetRender, WorkbookRender, PdfSaveOptions } = AsposeCells;

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
            const resultEl = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Rendering to PNG while setting checkWorkbookDefaultFont = false and defaultFont to Times New Roman
            const imgOpt = new ImageOrPrintOptions();
            imgOpt.imageType = ImageType.Png;
            imgOpt.checkWorkbookDefaultFont = false;
            imgOpt.defaultFont = "Times New Roman";

            const sr = new SheetRender(workbook.worksheets.get(0), imgOpt);
            const pngData = sr.toImage(0);
            const pngBlob = new Blob([pngData], { type: 'image/png' });
            const downloadPng = document.getElementById('downloadPng');
            downloadPng.href = URL.createObjectURL(pngBlob);
            downloadPng.download = 'out1_imagePNG.png';
            downloadPng.style.display = 'inline-block';
            downloadPng.textContent = 'Download PNG';

            // Rendering to TIFF while setting checkWorkbookDefaultFont = false and defaultFont to Times New Roman
            imgOpt.imageType = ImageType.Tiff;
            const wr = new WorkbookRender(workbook, imgOpt);
            const tiffData = wr.toImage();
            const tiffBlob = new Blob([tiffData], { type: 'image/tiff' });
            const downloadTiff = document.getElementById('downloadTiff');
            downloadTiff.href = URL.createObjectURL(tiffBlob);
            downloadTiff.download = 'out1_imageTIFF.tiff';
            downloadTiff.style.display = 'inline-block';
            downloadTiff.textContent = 'Download TIFF';

            // Rendering to PDF while setting the default font and checkWorkbookDefaultFont
            const saveOptions = new PdfSaveOptions();
            saveOptions.defaultFont = "Times New Roman";
            saveOptions.checkWorkbookDefaultFont = false;
            const pdfData = workbook.save(SaveFormat.Pdf, saveOptions);
            const pdfBlob = new Blob([pdfData], { type: 'application/pdf' });
            const downloadPdf = document.getElementById('downloadPdf');
            downloadPdf.href = URL.createObjectURL(pdfBlob);
            downloadPdf.download = 'out1_pdf.pdf';
            downloadPdf.style.display = 'inline-block';
            downloadPdf.textContent = 'Download PDF';

            resultEl.innerHTML = '<p style="color: green;">Export completed. Click the links above to download the generated files.</p>';
        });
    </script>
</html>
```
