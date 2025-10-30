---
title: Återanvända stilobjekt
linktitle: Återanvända stilobjekt
description: I Aspose.Cells for JavaScript via C++, kan du genom att skapa och använda återanvändbara stilobjekt, förenkla stilhantering och förbättra kodens effektivitet. Vår guide hjälper dig att utnyttja fördelarna med återanvändbara stilobjekt och implementera dem i din applikation.
keywords: Aspose.Cells for JavaScript via C++, Återanvändning av stilobjekt, Stilhantering, Kod effektivitet, Återanvändbara stilar, Applikationsutveckling, API dokumentation, Exempel på kod, Nedladdning, Stöd.
type: docs
weight: 3000
url: /sv/javascript-cpp/reusing-style-objects/
---

{{% alert color="primary" %}}  
Att återanvända stilobjekt kan spara minne och göra ett program snabbare.  
{{% /alert %}}  

För att tillämpa viss formatering på en stor omfattning av celler i en arbetsbok:

1. Skapa en stilobjekt.
1. Ange attributen.
1. Tillämpa stilen på cellerna i området.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Set Font</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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
            // Creating a new workbook (empty)
            const workbook = new Workbook();

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cells
            const cell1 = worksheet.cells.get("A1");
            const cell2 = worksheet.cells.get("B1");

            // Set the styles of both cells to Times New Roman
            const styleObject = workbook.createStyle();
            styleObject.font.color = Color.Red;
            styleObject.font.name = "Times New Roman";
            cell1.style = styleObject;
            cell2.style = styleObject;

            // Put the values inside the cell
            cell1.value = "Hello World!";
            cell2.value = "Hello World!!";

            // Save to XLSX
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SampleOutput_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}}  
Eftersom [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) / [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-)-metoden använder mycket mindre minne och är effektiv, togs den äldre Cell.style-egenskapen som konsumerade mycket onödig minne bort med lanseringen av Aspose.Cells 7.1.0.  
{{% /alert %}}
