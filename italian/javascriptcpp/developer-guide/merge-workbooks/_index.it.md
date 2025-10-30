---
title: Combinare più cartelle di lavoro in un unica cartella di lavoro con JavaScript tramite C++
linktitle: Unione Cartelle di Lavoro
type: docs
weight: 66
url: /it/javascript-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Impara come combinare più cartelle di lavoro in un unica cartella di lavoro usando Aspose.Cells for JavaScript tramite C++. 
---

{{% alert color="primary" %}}

A volte è necessario combinare cartelle di lavoro con contenuti vari come immagini, grafici e dati in un'unica cartella di lavoro. Aspose.Cells for JavaScript tramite C++ supporta questa funzione. Questo articolo mostra come creare un'applicazione console e combinare le cartelle di lavoro con poche righe di codice semplici usando Aspose.Cells.

{{% /alert %}}

## **Unione Cartelle di Lavoro con Immagini e Grafici**

Il codice di esempio combina due cartelle di lavoro in un'unica cartella di lavoro usando Aspose.Cells for JavaScript tramite C++. Il codice carica le cartelle di lavoro sorgente, utilizza il metodo [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#combine-workbook-) per combinarle e salva la cartella di lavoro risultante.

### **Cartelle di Lavoro di Origine**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **Cartelle di Lavoro di Output**

- [combined.xlsx](5473095.xlsx)

### **Screenshot**

Di seguito sono riportati gli screenshot delle cartelle di lavoro di origine e di output.

{{% alert color="primary" %}}

Puoi utilizzare qualsiasi cartella di lavoro di origine. Queste immagini sono solo a scopo illustrativo.

{{% /alert %}}

**Il primo foglio di lavoro della cartella di lavoro dei grafici - sovrapposto** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**Secondo foglio di lavoro della cartella di lavoro dei grafici - linea** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**Primo foglio di lavoro della cartella di immagini - immagine** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**Tutti e tre i fogli di lavoro nel libro combinato - sovrapposti, linea, immagine** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Combine Workbooks Example</title>
    </head>
    <body>
        <h1>Combine Workbooks Example</h1>
        <p>Select two Excel files to combine:</p>
        <input type="file" id="fileInput1" accept=".xls,.xlsx" />
        <input type="file" id="fileInput2" accept=".xls,.xlsx" />
        <button id="runExample">Combine Workbooks</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            const fileInput1 = document.getElementById('fileInput1');
            const fileInput2 = document.getElementById('fileInput2');

            if (!fileInput1.files.length || !fileInput2.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select two Excel files.</p>';
                return;
            }

            const file1 = fileInput1.files[0];
            const file2 = fileInput2.files[0];

            const arrayBuffer1 = await file1.arrayBuffer();
            const arrayBuffer2 = await file2.arrayBuffer();

            // Open the first excel file.
            const sourceBook1 = new Workbook(new Uint8Array(arrayBuffer1));

            // Open the second excel file.
            const sourceBook2 = new Workbook(new Uint8Array(arrayBuffer2));

            // Combining the two workbooks
            sourceBook1.combine(sourceBook2);

            // Save the combined workbook and provide download link
            const outputData = sourceBook1.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Combined.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Combined Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbooks combined successfully! Click the download link to get the combined file.</p>';
        });
    </script>
</html>
```

## **Argomenti avanzati**
- [Unisci più fogli di lavoro in un'unica scheda](/cells/it/javascript-cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [Unire file](/cells/it/javascript-cpp/merge-files/)
