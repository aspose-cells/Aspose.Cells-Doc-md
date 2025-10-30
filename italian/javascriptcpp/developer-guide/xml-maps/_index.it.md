---
title: Importa XML nel workbook Excel con JavaScript tramite C++
linktitle: Mappe XML
type: docs
weight: 210
url: /it/javascript-cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: Importa dati da file XML in Excel usando Aspose.Cells for JavaScript tramite C++.
---

{{% alert color="primary" %}}

Aspose.Cells permette di importare la mappa XML all’interno della cartella di lavoro usando il metodo [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#importXml-string-string-number-number-). Puoi importare la mappa XML con Microsoft Excel seguendo questi passaggi:

- Seleziona la scheda **Sviluppo**
- Fai clic su **Importa** nella sezione XML e segui i passaggi richiesti.

Dovrai fornire i tuoi dati XML per completare l'importazione. Ecco un [esempio di dati XML](5115037.txt) che puoi utilizzare per i test.

{{% /alert %}}

## **Importa la mappa XML utilizzando Microsoft Excel**

La seguente schermata mostra come importare la mappa XML utilizzando Microsoft Excel.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **Importa mappa XML usando Aspose.Cells for JavaScript tramite C++**

Il seguente codice di esempio mostra come utilizzare [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#importXml-string-string-number-number-). Genera il [file Excel di output](5115036.xlsx) come mostrato in questa schermata.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Import XML</title>
    </head>
    <body>
        <h1>Import XML into Workbook Example</h1>
        <input type="file" id="xmlInput" accept=".xml,.txt" />
        <button id="runExample">Import XML and Save</button>
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
            const fileInput = document.getElementById('xmlInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an XML file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const xmlText = await file.text();

            // Create a workbook
            const workbook = new Workbook();

            // Import your XML Map data starting from cell A1 on Sheet1
            workbook.importXml(xmlText, "Sheet1", 0, 0);

            // Save workbook to XLSX and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">XML imported and workbook saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Argomenti avanzati**
- [Aggiungi mappa XML all’interno della cartella di lavoro usando il metodo XmlMapCollection.add()](/cells/it/javascript-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [Esporta dati XML collegati alla mappa XML all'interno del Workbook](/cells/it/javascript-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [Trova il nome dell'elemento radice della mappa XML](/cells/it/javascript-cpp/find-the-root-element-name-of-xml-map/)
- [Collega le celle agli elementi della mappa XML](/cells/it/javascript-cpp/link-cells-to-xml-map-elements/)
