---
title: Cambiare il font solo sui caratteri Unicode specifici durante il salvataggio in PDF con JavaScript via C++
linktitle: Cambia il Font solo per i caratteri Unicode specifici durante il salvataggio in PDF
type: docs
weight: 260
url: /it/javascript-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Scopri come modificare il font di caratteri Unicode specifici durante il salvataggio in PDF usando Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}} 

Alcuni caratteri Unicode non possono essere visualizzati dal font specificato dall'utente. Uno di questi caratteri Unicode è **Trattino Non-Rotoso** (U+2011) e il suo numero Unicode è 8209. Questo carattere non può essere visualizzato con **Times New Roman**, ma può essere visualizzato con altri font come **Arial Unicode MS**.

Quando si verifica un carattere del genere all'interno di una parola o frase in un font specifico come Times New Roman, Aspose.Cells cambia il font dell'intera parola o frase in un font che può mostrare questo carattere, come Arial Unicode o MS.

Tuttavia, questo comportamento non è desiderabile per alcuni utenti e vogliono modificare solo il font di quel carattere specifico invece di cambiare il font di tutta la parola o frase.

Per risolvere questo problema, Aspose.Cells fornisce la proprietà `PdfSaveOptions.isFontSubstitutionCharGranularity` che deve essere impostata su true in modo che il font di caratteri non visualizzabili venga modificato solo se necessario, mentre il resto della parola o frase rimarrà nel font originale.

{{% /alert %}} 

## **Esempio**
Lo screenshot seguente confronta i due file PDF generati dal codice di esempio qui sotto.

Uno viene generato senza impostare la proprietà `PdfSaveOptions.isFontSubstitutionCharGranularity` e l'altro dopo aver impostato la proprietà su true.

Come si può vedere nel primo PDF, il font dell'intera frase è cambiato da Times New Roman a Arial Unicode MS a causa dell'en dash non break. Nel secondo PDF, solo il font dell'en dash non break è cambiato.

|**Primo file Pdf**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**Secondo file Pdf**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Codice di Esempio**


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
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Result PDF 1</a>
        <a id="downloadLink2" style="display: none;">Download Result PDF 2</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '<p>Running example...</p>';

            // Create workbook object
            const workbook = new Workbook();

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cells
            const cell1 = worksheet.cells.get("A1");
            const cell2 = worksheet.cells.get("B1");

            // Set the styles of both cells to Times New Roman
            let style = cell1.style;
            style.font.name = "Times New Roman";
            cell1.style = style;
            cell2.style = style;

            // Put the values inside the cell
            cell1.value = "Hello without Non-Breaking Hyphen";
            cell2.value = "Hello" + String.fromCharCode(8209) + " with Non-Breaking Hyphen";

            // Autofit the columns
            worksheet.autoFitColumns();

            // Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
            const outputData1 = workbook.save(SaveFormat.Pdf);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'SampleOutput_out.pdf';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download SampleOutput_out.pdf';

            // Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true
            const opts = new PdfSaveOptions();
            opts.isFontSubstitutionCharGranularity = true;
            const outputData2 = workbook.save(SaveFormat.Pdf, opts);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'SampleOutput2_out.pdf';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download SampleOutput2_out.pdf';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Use the download links to get the generated PDFs.</p>';
        });
    </script>
</html>
```
