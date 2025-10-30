---
title: Upptäcka tomma arbetsblad med JavaScript via C++
linktitle: Upptäcka tomma kalkylblad
type: docs
weight: 410
url: /sv/javascript-cpp/detecting-empty-worksheets/
description: Denna artikel visar kod som förklarar hur man programmässigt upptäcker tomma arbetsblad i Excel arbetsböcker med JavaScript API med C++ bibliotek.
keywords: upptäcka tomt arbetsblad JavaScript via C++, hitta tomt excel arbetsblad JavaScript via C++
---

## **Kontrollera Populerade celler**

Kalkylblad kan ha ett eller flera celler fyllda med värden där ett värde kan vara enkelt (text, numeriskt, datum/tid) eller en formel eller ett formelbaserat värde. I så fall är det lätt att upptäcka om ett givet kalkylblad är tomt eller inte. Det vi behöver kontrollera är [**Cells.maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--) eller [**Cells.maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--) egenskaperna. Om dessa egenskaper returnerar noll eller positiva värden, innebär det att ett eller flera celler har fyllts; dock, om något av dessa egenskaper returnerar -1, indikerar det att inget av cellerna har fyllts i det givna kalkylbladet.

{{% alert color="primary" %}}

Kollektionerna för rader & kolumner har nollbaserade index; därför betyder en cell vid rad 0 och kolumn 0 den första cellen i kalkylbladet, vilket är A1.

{{% /alert %}}

## **Kontrollera toma initialiserade celler**

Alla celler med värden är automatiskt initialiserade; dock finns det en möjlighet att ett kalkylblad har celler endast med formatering. I ett sådant scenario kommer egenskaperna [**Cells.maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--) eller [**Cells.maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--) att returnera -1, vilket indikerar att inga fyllda värden finns, men initialiserade celler på grund av cellformatering kan inte upptäckas med denna metod. För att kontrollera om ett kalkylblad har tomma initierade celler rekommenderas att använda `Enumerator.MoveNext`-metoden på enumeratorn som erhållits från [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)-samlingen. Om `Enumerator.MoveNext`-metoden returnerar **true**, betyder det att det finns en eller flera initialiserade celler i det givna kalkylbladet.

## **Kontrollera former**

Det är möjligt att ett givet kalkylblad inte har några fyllda celler; dock kan det innehålla former & objekt såsom kontroller, diagram, bilder och så vidare. Om vi behöver kontrollera om ett kalkylblad innehåller någon form kan vi göra det genom att inspektera [**ShapeCollection.count**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#count--)-egenskapen. Positiva värden indikerar att det finns former i kalkylbladet.

## **Programmeringsexempel**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Non-Empty Worksheets Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const book = new Workbook(new Uint8Array(arrayBuffer));

            const messages = [];

            // Loop over all worksheets in the workbook
            for (let i = 0; i < book.worksheets.count; i++) {
                const sheet = book.worksheets.get(i);
                // Check if worksheet has populated cells
                if (sheet.cells.maxDataRow !== -1) {
                    messages.push(`${sheet.name} is not empty because one or more cells are populated`);
                }
                // Check if worksheet has shapes
                else if (sheet.shapes.count > 0) {
                    messages.push(`${sheet.name} is not empty because there are one or more shapes`);
                }
                // Check if worksheet has empty initialized cells
                else {
                    const range = sheet.cells.maxDisplayRange;
                    const rangeIterator = range.getEnumerator();
                    if (rangeIterator.moveNext()) {
                        messages.push(`${sheet.name} is not empty because one or more cells are initialized`);
                    }
                }
            }

            if (messages.length) {
                resultDiv.innerHTML = '<ul>' + messages.map(m => `<li>${m}</li>`).join('') + '</ul>';
            } else {
                resultDiv.innerHTML = '<p style="color: green;">No non-empty worksheets found.</p>';
            }
        });
    </script>
</html>
```
