---
title: Convertire file XLSX in formato PDF con JavaScript via C++
linktitle: Converti il file XLSX nel Formato PDF
type: docs
weight: 30
url: /it/javascript-cpp/convert-xlsx-file-to-pdf-format/
description: Questa guida spiega come convertire un file Excel (XLSX) in formato PDF utilizzando Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

Il formato PDF (Portable Document Format) rappresenta documenti in modo indipendente dal software, dall'hardware e dal sistema operativo utilizzati per crearli. Un file PDF può contenere una combinazione qualsiasi di testo, grafica e immagini in maniera indipendente dal dispositivo e dalla risoluzione. I file PDF sono spesso compressi, quindi occupano meno spazio rispetto al file originale.

A volte, è necessario convertire un file Microsoft Excel in PDF. Per farlo, è richiesta una soluzione rapida, sicura, accurata e affidabile che consenta di distribuire documenti PDF in tutto il mondo. Esistono numerosi strumenti di conversione che possono eseguire questa operazione. Ma devi assicurarti che il layout del documento Excel originale venga mantenuto nel file PDF di output. Immagini, grafici, forme, formattazione dei dati, font, attributi, colori, impostazioni della pagina, orientamento del testo, bordi, grafici ecc. devono essere resi con precisione e accuratezza. [Aspose.Cells](https://products.aspose.com/cells/javascript-cpp/) garantisce una conversione ad alta fedeltà.

Questo documento è progettato per fornire una comprensione completa di come un documento Microsoft Excel (contenente immagini, grafici, formattazione ecc.) può essere convertito in PDF. A tal fine, mostra come creare una semplice applicazione console in JavaScript via C++ che converte un file Excel in PDF usando l’API Aspose.Cells. La conversione viene eseguita con un alto livello di precisione e accuratezza.

{{% /alert %}}

## **Conversione di Excel in PDF**

Questo esempio utilizza un file Excel (SampleInput.xlsx) come modello. Il libro contiene fogli di lavoro con grafici e immagini. Ogni foglio contiene diversi tipi di formattazione utilizzando font, attributi, colori, effetti di ombreggiatura e bordi. Nel primo foglio c’è un grafico a colonne e nell’ultimo un’immagine.

### **Il file Excel di modello**

Il file modello ha tre fogli di lavoro, inclusi grafici e immagini come sezioni multimediali. Il primo foglio ha grafici e l’ultimo un’immagine come mostrato nelle schermate.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|Il primo foglio di lavoro **(Previsioni di vendita)**|Il secondo foglio di lavoro **(Rapporto di vendita)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Il terzo foglio di lavoro **(Inserimento dati)**|L'ultimo foglio di lavoro **(Immagine)**|

### **Processo di conversione**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Excel to PDF</title>
    </head>
    <body>
        <h1>Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;"></a>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object with the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the PDF file
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare il metodo [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) proprio prima di esportare il foglio di calcolo in PDF. In questo modo si garantisce che i valori dipendenti dalle formule siano ricalcolati e i valori corretti siano visualizzati nel PDF.

{{% /alert %}}

### **Risultato**

Quando il codice sopra è stato eseguito, viene creato un file PDF nella cartella Files della directory dell'applicazione.
Gli screenshot seguenti mostrano le pagine PDF. Nota che gli header e i footer sono mantenuti anche nel file PDF di output.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|Il primo foglio di lavoro **(Previsioni di vendita)**|Il secondo foglio di lavoro **(Rapporto di vendita)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Il terzo foglio di lavoro **(Inserimento dati)**|L'ultimo foglio di lavoro **(Immagine)**|
