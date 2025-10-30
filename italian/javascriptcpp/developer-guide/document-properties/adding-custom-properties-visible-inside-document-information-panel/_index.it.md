---
title: Aggiunta di proprietà personalizzate visibili nel pannello delle informazioni sul documento con JavaScript tramite C++
linktitle: Aggiunta di proprietà personalizzate visibili all interno del pannello delle informazioni sul documento
type: docs
weight: 300
url: /it/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Impara come aggiungere proprietà personalizzate a un oggetto workbook usando Aspose.Cells for JavaScript tramite C++. Queste proprietà possono essere visualizzate nel pannello delle informazioni sul documento.
---

## **Aggiunta di proprietà personalizzate visibili all'interno del pannello delle informazioni del documento**

Aspose.Cells for JavaScript tramite C++ può essere usato per aggiungere proprietà personalizzate all'interno dell'oggetto workbook visibili nel pannello delle informazioni sul documento. Puoi aprire il pannello delle informazioni sul documento in Microsoft Excel tramite i comandi File > Info > Proprietà > Mostra pannello del documento.

Usa il metodo [**ContentTypePropertyCollection.add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/contenttypepropertycollection/#add-string-string-) per aggiungere una proprietà personalizzata che sarà visibile nel Pannello Informazioni Documento.

Il codice di esempio seguente aggiunge due proprietà personalizzate. La prima proprietà non ha alcun tipo e la seconda ha un tipo come DateTime. Una volta aperto il file Excel generato da questo codice, vedrai queste due proprietà all'interno del Pannello Informazioni Documento.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Adding Custom Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Create Workbook with Custom Properties</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            // Create workbook object
            const workbook = new Workbook();

            // Add simple property without any type
            workbook.contentTypeProperties.add("MK31", "Simple Data");

            // Add date time property with type
            workbook.contentTypeProperties.add("MK32", "04-Mar-2015", "DateTime");

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddingCustomPropertiesVisible_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Articolo correlato**

{{% alert color="primary" %}}

- [Utilizza parti XML personalizzate in Aspose.Cells](/cells/it/net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
