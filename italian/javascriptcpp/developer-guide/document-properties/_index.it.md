---
title: Gestire le Proprietà del Documento con JavaScript tramite C++
linktitle: Proprietà del documento
type: docs
weight: 80
url: /it/javascript-cpp/managing-document-properties/
description: Impara come Gestire le Proprietà del Documento attraverso le API di Aspose.Cells for JavaScript tramite C++.
keywords: Come Gestire le Proprietà del Documento in JavaScript tramite C++, Ottenere o impostare le Proprietà del Documento usando JavaScript tramite C++, Aggiungere o eliminare Proprietà del Documento via JavaScript tramite C++, Inserire o rimuovere Proprietà del Documento con JavaScript tramite C++, Come accedere alle Proprietà del Documento usando le API di Aspose.Cells for JavaScript tramite C++.
---

## **Introduzione**

Microsoft Excel fornisce la possibilità di aggiungere proprietà ai file di fogli elettronici. Queste proprietà del documento forniscono informazioni utili e sono divise in 2 categorie come dettagliato di seguito.

- Proprietà predefinite di sistema (builtin): Le proprietà incorporano informazioni generali sul documento come il titolo del documento, il nome dell'autore, le statistiche del documento e così via.
- Proprietà definite dall'utente (personalizzate): Proprietà personalizzate definite dall'utente sotto forma di coppia nome-valore.

{{% alert color="primary" %}}

Il punto più importante da conoscere sulle proprietà integrate e personalizzate è che le proprietà integrate possono essere accessibili e modificate, ma non create o rimosse. Tuttavia, le proprietà personalizzate possono essere create e gestite.

{{% /alert %}}

## **Come gestire le proprietà del documento con Microsoft Excel**

Microsoft Excel ti permette di gestire le proprietà del documento dei file Excel in modo WYSIWYG. Segui i passaggi sottostanti per aprire la finestra di dialogo **Proprietà** in Excel 2016.

1. Dal menu **File**, seleziona **Informazioni**.

|**Selezionare il menu Informazioni**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1. Clicca sulla voce **Proprietà** e seleziona "Proprietà avanzate".

|**Selezione Proprietà Avanzate**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. Gestire le proprietà del documento del file.

|**Dialogo Proprietà**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
Nel dialogo Proprietà, ci sono diverse schede, come Generale, Riepilogo, Statistiche, Contenuti e Personalizzati. Ogni scheda aiuta a configurare diversi tipi di informazioni relative al file. La scheda Personalizzati è utilizzata per gestire le proprietà personalizzate.

## **Come lavorare con le proprietà del documento utilizzando Aspose.Cells**

Gli sviluppatori possono gestire dinamicamente le proprietà del documento utilizzando le API di Aspose.Cells. Questa funzionalità aiuta gli sviluppatori a memorizzare informazioni utili insieme al file, come quando il file è stato ricevuto, elaborato, con timestamp e così via.

{{% alert color="primary" %}}

Aspose.Cells for JavaScript tramite C++ scrive direttamente le informazioni sull'API e il Numero di Versione nei documenti di output. Ad esempio, durante la conversione di un Documento in PDF, Aspose.Cells for JavaScript tramite C++ popola il campo **Applicazione** con il valore 'Aspose.Cells' e il campo **Produttore PDF** con il valore, ad esempio 'Aspose.Cells v17.9'.

Si prega di notare che non è possibile istruire Aspose.Cells for JavaScript tramite C++ a modificare o rimuovere queste informazioni dai Documenti di output.

{{% /alert %}}

### **Come accedere alle proprietà del documento**

Le API di Aspose.Cells supportano sia le proprietà del documento integrate che quelle personalizzate. La classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) di Aspose.Cells rappresenta un file Excel e, come un file Excel, la classe [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) può contenere più fogli di lavoro, ciascuno rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet), mentre la raccolta di fogli di lavoro è rappresentata dalla classe [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection).

Usa [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) per accedere alle proprietà del documento del file come descritto di seguito.

- Per accedere alle proprietà integrate del documento, utilizzare [**WorksheetCollection.builtInDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#builtInDocumentProperties--).
- Per accedere alle proprietà personalizzate del documento, utilizzare [**WorksheetCollection.customDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#customDocumentProperties--).

Sia [**WorksheetCollection.builtInDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#builtInDocumentProperties--) che [**WorksheetCollection.customDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#customDocumentProperties--) restituiscono l'istanza di [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/). Questa raccolta contiene [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) oggetti, ciascuno dei quali rappresenta una proprietà del documento, sia integrata che personalizzata.

Spetta all'applicazione decidere come accedere a una proprietà; ad esempio, usando l'indice o il nome della proprietà da [**DocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/), come mostrato nell'esempio sottostante.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Document Properties</title>
    </head>
    <body>
        <h1>Document Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Load Document Properties</button>
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
            const resultEl = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object and opening the Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            // Accessing a custom document property by using the property name
            const customProperty1 = customProperties.get("ContentTypeId");
            // Accessing the same custom document property by using the property index
            const customProperty2 = customProperties.get(0);

            const outputs = [];
            if (customProperty1) {
                outputs.push(`<p>${customProperty1.name} ${customProperty1.value}</p>`);
            }
            if (customProperty2) {
                outputs.push(`<p>${customProperty2.name} ${customProperty2.value}</p>`);
            }
            if (!outputs.length) {
                resultEl.innerHTML = '<p style="color: orange;">No custom document properties found.</p>';
            } else {
                resultEl.innerHTML = outputs.join('');
            }
        });
    </script>
</html>
```

La classe [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) permette di recuperare il nome, il valore e il tipo della proprietà del documento:

- Per ottenere il nome della proprietà, utilizzare [**DocumentProperty.name()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#name--).
- Per ottenere il valore della proprietà, usa [**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--). [**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--) restituisce il valore come Oggetto.
- Per ottenere il tipo di proprietà, usa [**DocumentProperty.type()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#type--). Questa restituisce uno dei valori dell'enumerazione [**PropertyType**](https://reference.aspose.com/cells/javascript-cpp/propertytype/). Dopo aver ottenuto il tipo di proprietà, usa uno dei metodi **DocumentProperty.ToXXX** per ottenere il valore del tipo appropriato invece di usare [**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--). I metodi **DocumentProperty.ToXXX** sono descritti nella tabella sottostante.

{{% alert color="primary" %}}

La classe [**DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) fornisce anche un insieme di metodi che restituiscono i valori di altri tipi di dati.

{{% /alert %}}

|**Nome membro**|**Descrizione**|**Metodo ToXXX**|
| :- | :- | :- |
|Boolean|Il tipo di dati della proprietà è Booleano|ToBool|
|Date|Il tipo di dati della proprietà è DataOra. Nota che Microsoft Excel memorizza solo <br>la parte della data, nessuna ora può essere memorizzata in una proprietà personalizzata di questo tipo|ToDateTime|
|Float|Il tipo di dati della proprietà è Double|ToDouble|
|Number|Il tipo di dati della proprietà è Int32|ToInt|
|String|Il tipo di dato della proprietà è string|ToString|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Retrieve Custom Document Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            let outputHtml = '<h2>Custom Document Properties</h2>';

            // Accessing a custom document property (first)
            const customProperty1 = customProperties.get(0);
            if (customProperty1) {
                // Storing the value of the document property as an object
                const objectValue = customProperty1.value;
                outputHtml += `<p><strong>${customProperty1.name}</strong> (type: ${customProperty1.type}) : ${objectValue}</p>`;
            } else {
                outputHtml += '<p>No first custom property found.</p>';
            }

            // Accessing a custom document property (second)
            const customProperty2 = customProperties.get(1);
            if (customProperty2) {
                // Checking the type of the document property and then storing the value according to that type
                if (customProperty2.type === AsposeCells.PropertyType.String) {
                    const value = customProperty2.value.toString();
                    outputHtml += `<p>${customProperty2.name} : ${value}</p>`;
                } else {
                    outputHtml += `<p>${customProperty2.name} (type: ${customProperty2.type}) : ${customProperty2.value}</p>`;
                }
            } else {
                outputHtml += '<p>No second custom property found.</p>';
            }

            resultDiv.innerHTML = outputHtml;
        });
    </script>
</html>
```

### **Come Aggiungere o Rimuovere Proprietà del Documento Personalizzate**

Come abbiamo descritto in precedenza all'inizio di questo argomento, i programmatori non possono aggiungere o rimuovere proprietà integrate perché queste proprietà sono definite dal sistema, ma è possibile aggiungere o rimuovere proprietà personalizzate poiché queste sono definite dall'utente.

### **Come Aggiungere Proprietà Personalizzate**

Le API Aspose.Cells hanno esposto il metodo [**add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#add-string-string-) per la classe [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/) al fine di aggiungere proprietà personalizzate alla raccolta. Il metodo [**add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#add-string-string-) aggiunge la proprietà al file Excel e restituisce un riferimento alla nuova proprietà del documento come oggetto [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add Custom Document Property</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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

            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                if (!fileInput.files.length) {
                    document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Instantiating a Workbook object and opening the Excel file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Retrieve a list of all custom document properties of the Excel file
                const customProperties = workbook.customDocumentProperties;

                // Adding a custom document property to the Excel file
                customProperties.add("Publisher", "Aspose");

                // Saving the modified Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'out_sample-document-properties.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Modified Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Custom property added successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```

### **Come Configurare Proprietà Personalizzata “Collegamento al contenuto”**

Per creare una proprietà personalizzata collegata al contenuto di un intervallo dato, chiamare il metodo [**CustomDocumentPropertyCollection.addLinkToContent(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#addLinkToContent-string-string-) e passare il nome della proprietà e la sorgente. È possibile verificare se una proprietà è configurata come collegata al contenuto utilizzando la proprietà [**DocumentProperty.isLinkedToContent()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#isLinkedToContent--). Inoltre, è possibile ottenere anche l'intervallo sorgente utilizzando la proprietà [**source()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#source--) della classe [**DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/).

Utilizziamo un file modello semplice di Microsoft Excel nell'esempio. Il workbook ha un intervallo denominato definito **MyRange**, che si riferisce a un valore della cella.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Custom Document Properties</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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
            const fileInput = document.getElementById('fileInput');
            const resultEl = document.getElementById('result');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.worksheets.customDocumentProperties;

            // Add link to content.
            customProperties.addLinkToContent("Owner", "MyRange");

            // Accessing the custom document property by using the property name
            const customProperty1 = customProperties.get("Owner");

            // Check whether the property is linked to content
            const isLinkedToContent = customProperty1.isLinkedToContent;

            // Get the source for the property
            const source = customProperty1.source;

            // Save the file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sample-document-properties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultEl.innerHTML = `<p style="color: green;">Operation completed successfully! Property linked: ${isLinkedToContent}. Source: ${source}. Click the download link to get the modified file.</p>`;
        });
    </script>
</html>
```

### **Come rimuovere proprietà personalizzate**

Per rimuovere proprietà personalizzate usando Aspose.Cells, chiamare il metodo [**DocumentPropertyCollection.remove(string)**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/#remove-string-) e passare il nome della proprietà del documento da rimuovere.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Remove Custom Document Property Example</title>
    </head>
    <body>
        <h1>Remove Custom Document Property Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            // Removing a custom document property named "Publisher"
            customProperties.remove("Publisher");

            // Save the file and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sample-document-properties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom property removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Argomenti avanzati**
- [Aggiunta di proprietà personalizzate visibili all'interno del pannello delle informazioni del documento](/cells/it/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/)
- [Impostazione delle proprietà ScaleCrop e LinksUpToDate delle proprietà del documento integrato](/cells/it/javascript-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Specifica la versione del documento del file Excel utilizzando le proprietà del documento integrato](/cells/it/javascript-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Specificare la lingua del file Excel utilizzando le proprietà di documento incorporate](/cells/it/javascript-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
