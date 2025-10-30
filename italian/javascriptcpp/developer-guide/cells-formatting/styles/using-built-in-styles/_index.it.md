---
title: Uso degli Stili Incorporati
linktitle: Uso degli Stili Incorporati
type: docs
weight: 80
url: /it/javascript-cpp/using-built-in-styles/
description: Codice JavaScript per usare gli stili integrati di Excel con Aspose.Cells for JavaScript tramite C++.
keywords: JavaScript usa gli stili integrati di Excel, applica programmaticamente gli stili nel workbook, applica programmaticamente gli stili nel workbook, JavaScript applica gli stili integrati in Excel, JavaScript applica gli stili integrati nel workbook, codice JavaScript applica gli stili integrati nel workbook, codice JavaScript applica gli stili integrati in Excel workbook
---

{{% alert color="primary" %}}  
Aspose.Cells fornisce una vasta raccolta di stili riutilizzabili per formattare una cella nel documento di foglio di calcolo. Possiamo utilizzare gli stili incorporati nel nostro workbook e anche creare stili personalizzati.  
{{% /alert %}}  

## **Come utilizzare gli stili incorporati**  

Il metodo [**Workbook.createBuiltinStyle(BuiltinStyleType)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createBuiltinStyle-builtinstyletype-) e l'enumerazione [**BuiltinStyleType**](https://reference.aspose.com/cells/javascript-cpp/builtinstyletype) rendono comodo l'uso degli stili incorporati. Ecco un elenco di tutti gli stili incorporati possibili:  

- TwentyPercentAccent1
- TwentyPercentAccent2
- TwentyPercentAccent3
- QuindiciPercentAccent4
- QuindiciPercentAccent5
- QuindiciPercentAccent6
- QuarantaPercentAccent1
- QuarantaPercentAccent2
- QuarantaPercentAccent3
- QuarantaPercentAccent4
- QuarantaPercentAccent5
- QuarantaPercentAccent6
- SessantaPercentAccent1
- SessantaPercentAccent2
- SessantaPercentAccent3
- SessantaPercentAccent4
- SessantaPercentAccent5
- SessantaPercentAccent6
- Accent1
- Accent2
- Accent3
- Accent4
- Accent5
- Accent6
- Cattivo
- Calcolo
- VerificaCella
- Virgola
- Virgola1
- Valuta
- Valuta1
- TestoEsplicativo
- Buono
- Intestazione1
- Intestazione2
- Intestazione3
- Intestazione4
- Collegamento ipertestuale
- CollegamentoIpertestuale
- Input
- CellaaCollegata
- Neutrale
- Normale
- Nota
- Output
- Percentuale
- Titolo
- Totale
- TestoAvviso
- LivelloRiga
- LivelloColonna


## Codice JavaScript per usare gli stili integrati  
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
