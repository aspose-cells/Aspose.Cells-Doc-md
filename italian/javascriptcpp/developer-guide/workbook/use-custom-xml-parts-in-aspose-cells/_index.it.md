---
title: Usa parti XML personalizzate in Aspose.Cells con JavaScript tramite C++
linktitle: Usare Parti XML Personalizzate in Aspose.Cells
type: docs
weight: 390
url: /it/javascript-cpp/use-custom-xml-parts-in-aspose-cells/
description: Impara come usare le parti XML personalizzate in Aspose.Cells for JavaScript tramite C++. Integra i dati XML esterni nei file Excel senza problemi.
---

## Utilizzo di Parti XML Personalizzate in Aspose.Cells

Le Parti XML personalizzate sono i dati XML memorizzati da diverse applicazioni, come SharePoint, all’interno del file Excel. Questi dati sono consumati da varie applicazioni che ne hanno bisogno. Microsoft Excel non utilizza questi dati, quindi non esiste un’interfaccia grafica per aggiungerli. Puoi visualizzare questi dati cambiando l’estensione di **.xlsx** in **.zip** e aprendo il file con **WinZip**. Puoi anche aprire il file ZIP usando qualsiasi utility di compressione di terze parti come WinRAR o WinZip. I dati sono presenti nella cartella **customXml**.

Puoi aggiungere parti XML personalizzate usando Aspose.Cells for JavaScript tramite C++ tramite il metodo [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/).

Il seguente esempio di codice utilizza il metodo [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/) e aggiunge il **Catalogo XML dei Libri** e il suo nome è **BookStore**. L'immagine seguente mostra il risultato di questo codice. Come puoi vedere, il Catalogo XML dei Libri è aggiunto all'interno del nodo BookStore, che è il nome di questa proprietà.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Codice JavaScript per usare parti XML personalizzate

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Custom XML to Workbook Example</h1>
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

        const booksXML = `<catalog>
<book>
<title>Complete C#</title>
<price>44</price>
</book>
<book>
<title>Complete Java</title>
<price>76</price>
</book>
<book>
<title>Complete SharePoint</title>
<price>55</price>
</book>
<book>
<title>Complete PHP</title>
<price>63</price>
</book>
<book>
<title>Complete VB.NET</title>
<price>72</price>
</book>
</catalog>`;

        document.getElementById('runExample').addEventListener('click', async () => {
            // Create an instance of Workbook class
            const workbook = new Workbook();

            // Add Custom XML Part to ContentTypePropertyCollection
            workbook.contentTypeProperties.add("BookStore", booksXML);

            // Save the resultant spreadsheet
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom XML added and file prepared. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## Articolo Correlato

- [Aggiunta di proprietà personalizzate visibili all'interno del pannello delle informazioni del documento](/cells/it/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/)
