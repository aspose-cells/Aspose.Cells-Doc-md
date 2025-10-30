---
title: Användning av inbyggda stilar
linktitle: Användning av inbyggda stilar
type: docs
weight: 80
url: /sv/javascript-cpp/using-built-in-styles/
description: JavaScript kod för att använda Excels inbyggda stilar med Aspose.Cells for JavaScript via C++.
keywords: JavaScript använder Excels inbyggda stilar, JavaScript programmering för att tillämpa stilar i arbetsboken programmatiskt, programmatisk tillämpning av stilar i arbetsboken, JavaScript tillämpar inbyggda stilar i excel, JavaScript tillämpar inbyggda stilar i arbetsboken, JavaScript kod för att tillämpa inbyggda stilar i arbetsboken, JavaScript kod för att tillämpa inbyggda stilar i excel arbetsboken
---

{{% alert color="primary" %}}  
Aspose.Cells tillhandahåller en stor samling återanvändbara stilar för att formatera en cell i kalkylbladsdokument. Vi kan använda inbyggda stilar i vår arbetsbok och även skapa anpassade stilar.  
{{% /alert %}}  

## **Hur man använder inbyggda stilar**  

Metoden [**Workbook.createBuiltinStyle(BuiltinStyleType)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createBuiltinStyle-builtinstyletype-) och uppräkningen [**BuiltinStyleType**](https://reference.aspose.com/cells/javascript-cpp/builtinstyletype) gör det bekvämt att använda inbyggda stilar. Här är en lista över alla möjliga inbyggda stilar:  

- Tjugo procent Accent 1
- Tjugo procent Accent 2
- Tjugo procent Accent 3
- Tjugo procent Accent 4
- Tjugo procent Accent 5
- Tjugo procent Accent 6
- Fyrtio procent Accent 1
- Fyrtio procent Accent 2
- Fyrtio procent Accent 3
- Fyrtio procent Accent 4
- Fyrtio procent Accent 5
- Fyrtio procent Accent 6
- Sextio procent Accent 1
- Sextio procent Accent 2
- Sextio procent Accent 3
- Sextio procent Accent 4
- Sextio procent Accent 5
- Sextio procent Accent 6
- Accent 1
- Accent 2
- Accent 3
- Accent 4
- Accent 5
- Accent 6
- Dålig
- Beräkning
- KontrolleraCell
- Komma
- Komma1
- Valuta
- Valuta1
- FörklarandeText
- Bra
- Rubrik1
- Rubrik2
- Rubrik3
- Rubrik4
- Hyperlänk
- FöljdHyperlänk
- Inmatning
- LänkadCell
- Neutral
- Normal
- Notis
- Utdata
- Procent
- Titel
- Total
- VarningText
- Radradenivå
- KolumnNivå


## JavaScript-kod för att använda inbyggda stilar  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Output.xlsx</a>
        <a id="downloadLink2" style="display: none;">Download Output.out.ods</a>
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

        document.getElementById('runExample').addEventListener('click', () => {
            // Creating a new Workbook
            const workbook = new Workbook();

            // Creating a built-in style (Title)
            const style = workbook.createBuiltinStyle(AsposeCells.BuiltinStyleType.Title);

            // Accessing first worksheet, its cells, and cell A1
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");

            // Setting cell value and style (converted setter)
            cell.putValue("Aspose");
            cell.style = style;

            // Auto-fit column and row
            worksheet.autoFitColumn(0);
            worksheet.autoFitRow(0);

            // Save as XLSX
            const outputData1 = workbook.save(SaveFormat.Xlsx);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'Output.xlsx';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download Output.xlsx';

            // Save as ODS
            const outputData2 = workbook.save(SaveFormat.Ods);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'Output.out.ods';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download Output.out.ods';

            document.getElementById('result').innerHTML = '<p style="color: green;">Files generated. Click the download links to save them.</p>';
        });
    </script>
</html>
```
