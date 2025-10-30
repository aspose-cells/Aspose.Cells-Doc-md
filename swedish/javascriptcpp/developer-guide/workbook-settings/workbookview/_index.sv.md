---
title: Hur man kontrollerar arbetsboksvy med JavaScript via C++
linktitle: Hur man Kontrollerar Workbook View
type: docs
weight: 600
url: /sv/javascript-cpp/how-to-control-workbook-view/
description: Lär dig hur du kontrollerar arbetsboksvisningen genom Aspose.Cells for JavaScript via C++ API.
keywords: Hur man kontrollerar arbetsboksvy JavaScript via C++, Ställ in Excel vy JavaScript via C++, Operera arbetsboksvisning JavaScript via C++, Ställ in arbetsboksvy JavaScript via C++, Kontrolera Excel vy JavaScript via C++.
---

## **Möjliga användningsscenario**
När du behöver justera visningen av Excel-sidor, måste du veta hur man styr varje modul, som horisontella och vertikala skrollningsrutor, om du ska dölja öppna Excel-filer och så vidare. Aspose.Cells for JavaScript via C++ erbjuder denna funktion. Aspose.Cells for JavaScript via C++ tillhandahåller följande egenskaper och metoder för att hjälpa dig att nå dina mål.

- [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--)
- [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--)
- [**WorkbookSettings.isHidden()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHidden--)
- [**WorkbookSettings.isMinimized()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isMinimized--)
- [**WorkbookSettings.windowHeight**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#windowHeight--)
- [**WorkbookSettings.windowWidth**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#windowWidth--)
- [**WorkbookSettings.windowLeft**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#windowLeft--)
- [**WorkbookSettings.windowTop**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#windowTop--)

## **Hur man kontrollerar arbetsboksvy med Aspose.Cells for JavaScript via C++**
Detta exempel visar hur man:

1. Skapa en arbetsbok.
1. Lägga till data till celler i den första arbetsboken.
1. Dölj horisontella och vertikala rullningsfält för Workbook View.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Example - Create/Modify Workbook</h1>
        <p>Select an existing .xls/.xlsx file to modify, or leave empty to create a new workbook.</p>
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
            // If a file is selected, open it; otherwise create a new workbook (matches original Node behavior)
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells (converted putValue => value)
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("C1");
            cell.value = "Price";

            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";

            cell = cells.get("B2");
            cell.value = 5;
            cell = cells.get("B3");
            cell.value = 3;
            cell = cells.get("B4");
            cell.value = 6;
            cell = cells.get("B5");
            cell.value = 4;

            cell = cells.get("C2");
            cell.value = 5;
            cell = cells.get("C3");
            cell.value = 20;
            cell = cells.get("C4");
            cell.value = 30;
            cell = cells.get("C5");
            cell.value = 60;

            // Apply style: createStyle(), font/color adjustments converted from get/set to properties
            cell = cells.get("E10");
            const temp = workbook.createStyle();
            temp.font.color = AsposeCells.Color.Red;
            cell.style = temp;

            // Hide horizontal and vertical scrollbars (converted getSettings().set... -> settings.is... = ...)
            workbook.settings.isHScrollBarVisible = false;
            workbook.settings.isVScrollBarVisible = false;

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

Förhandsgranskning av resultatfil:
<br>
<image src="result.png" width="70%" />
