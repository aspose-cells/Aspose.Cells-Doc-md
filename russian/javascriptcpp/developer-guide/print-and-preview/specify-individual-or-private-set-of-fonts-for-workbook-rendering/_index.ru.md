---
title: Задайте индивидуальный или приватный набор шрифтов для отображения книги с помощью JavaScript через C++
linktitle: Указание индивидуального или частного набора шрифтов для рендеринга книги
type: docs
weight: 40
url: /ru/javascript-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/
description: Узнайте, как задавать отдельные или приватные наборы шрифтов для отображения книги с помощью Aspose.Cells for JavaScript на C++.
---

## **Возможные сценарии использования**  

Обычно вы указываете директорию шрифтов или список шрифтов для всех книг, но иногда необходимо задавать отдельные или приватные наборы шрифтов для ваших книг. Aspose.Cells for JavaScript на C++ предоставляет класс [**IndividualFontConfigs**](https://reference.aspose.com/cells/javascript-cpp/individualfontconfigs), который можно использовать для задания индивидуальных или приватных наборов шрифтов для вашей книги.  

## **Указание индивидуального или частного набора шрифтов для рендеринга книги**  

 Следующий пример загружает [пример файла Excel](67338268.xlsx) с его индивидуальным или приватным набором шрифтов, указанных с помощью класса [**IndividualFontConfigs**](https://reference.aspose.com/cells/javascript-cpp/individualfontconfigs). Ознакомьтесь с [шрифтом](67338271.zip), используемым внутри кода, а также с [выходным PDF](67338269.pdf), сгенерированным этим кодом. Следующий скриншот показывает, как выглядит итоговый PDF, если шрифт найден успешно.  

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)  

## **Образец кода**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Specify Individual Or Private Fonts Example</title>
    </head>
    <body>
        <h1>Specify Individual Or Private Fonts Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, IndividualFontConfigs } = AsposeCells;

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

            // Path of your custom font directory.
            const customFontsDir = "C:\\TempDir\\CustomFonts";

            // Specify individual font configs custom font directory.
            const fontConfigs = new IndividualFontConfigs();

            // If you comment this line or if custom font directory is wrong or 
            // if it does not contain required font then output pdf will not be rendered correctly.
            // Converted setFontFolder -> property assignment (first argument used)
            fontConfigs.fontFolder = customFontsDir;

            // Specify load options with font configs.
            const opts = new LoadOptions(AsposeCells.LoadFormat.Xlsx);
            // Converted setFontConfigs -> property assignment
            opts.fontConfigs = fontConfigs;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the sample Excel file with individual font configs.
            const wb = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Save to PDF format.
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
