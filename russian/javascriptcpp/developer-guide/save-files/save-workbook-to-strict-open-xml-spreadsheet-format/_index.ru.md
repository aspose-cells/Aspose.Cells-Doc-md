---
title: Сохранение рабочей книги в строгом формате Open XML Spreadsheet с помощью JavaScript через C++
linktitle: Сохранить книгу в формате строгой открытой электронной таблицы XML
type: docs
weight: 150
url: /ru/javascript-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/
description: Научитесь сохранять рабочую книгу в формате Strict Open XML Spreadsheet с помощью Aspose.Cells for JavaScript через C++.
---

## **Возможные сценарии использования**

Aspose.Cells for JavaScript через C++ позволяет сохранять рабочую книгу в формате *Strict Open XML Spreadsheet*. Для этого он предоставляет свойство [**WorkbookSettings.compliance**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#compliance--). Если установить его значение как [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompliance), то итоговый файл Excel будет сохранен в формате Strict Open XML Spreadsheet.

## **Сохранить книгу в формате Strict Open XML Spreadsheet**

Следующий пример кода создает рабочую книгу и устанавливает значение свойства [**WorkbookSettings.compliance**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#compliance--) как [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompliance), затем сохраняет ее как [выходной файл Excel](67338272.xlsx). Если открыть выходной файл Excel в Microsoft Excel и выбрать «Сохранить как…», вы увидите его формат как *Strict Open XML Spreadsheet*, что показано на этом скриншоте.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Save Workbook to Strict Open XML Spreadsheet Format</title>
    </head>
    <body>
        <h1>Save Workbook to Strict Open XML Spreadsheet Format</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, OoxmlCompliance, Utils } = AsposeCells;

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
            // Create a new workbook
            const workbook = new Workbook();

            // Specify - Strict Open XML Spreadsheet - Format.
            workbook.settings.compliance = OoxmlCompliance.Iso29500_2008_Strict;

            // Access first worksheet and set value in B4
            const worksheet = workbook.worksheets.get(0);
            const b4 = worksheet.cells.get("B4");
            b4.value = "This Excel file has Strict Open XML Spreadsheet format.";

            // Save to output Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved to Strict Open XML Spreadsheet format. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
