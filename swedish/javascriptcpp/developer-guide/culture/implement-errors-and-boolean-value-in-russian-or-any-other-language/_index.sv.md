---
title: Implementera fel och booleska värden på ryska eller annat språk med JavaScript via C++
linktitle: Implementera fel och booleska värden på ryska eller något annat språk
type: docs
weight: 40
url: /sv/javascript-cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Lär dig hur man implementerar fel och booleska värden på olika språk med Aspose.Cells for JavaScript via C++. 
---

## **Möjliga användningsscenario**

Om du använder Microsoft Excel på ryskt språk eller något annat språk, visas fel och booleska värden enligt det språket. Du kan åstadkomma liknande beteende med Aspose.Cells for JavaScript via C++ genom att använda [**WorkbookSettings.globalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#globalizationSettings--)-egenskapen. Du måste åsidosätta följande metoder i [**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings)-klassen.

- [**GlobalizationSettings.errorValueString(string)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#errorValueString-string-)
- [**GlobalizationSettings.booleanValueString(boolean)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#booleanValueString-boolean-)

## **Implementera fel och booleska värden på ryska eller något annat språk**

Följande exempelkod illustrerar hur man implementerar fel och booleskt värde på ryska eller något annat språk. Kontrollera den [Exempel Excel-filen](73990159.xlsx) som används i denna kod och dess [Utdata-PDF](73990160.pdf). Skärmbilden visar skillnaden mellan Exempel Excel-filen och Utdata-PDF för referens.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Exempelkod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #downloadLink { display: none; margin-top: 10px; display: inline-block; }
            #result p { margin: 8px 0; }
        </style>
    </head>
    <body>
        <h1>Russian Globalization Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink">Download Result</a>
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

        // Russian Globalization
        class RussianGlobalization extends AsposeCells.GlobalizationSettings {
            errorValueString(err) {
                switch (err.toUpperCase()) {
                    case "#NAME?":
                        return "#RussianName-имя?";
                }
                return "RussianError-ошибка";
            }

            booleanValueString(bv) {
                return bv ? "RussianTrue-правда" : "RussianFalse-ложный";
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the source workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set GlobalizationSettings in Russian Language
            workbook.settings.globalizationSettings = new RussianGlobalization();

            // Calculate the formula
            workbook.calculateFormula();

            // Save the workbook in pdf format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRussianGlobalization.pdf';
            downloadLink.style.display = 'inline-block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
