---
title: Gestisci proprietà del documento con Node.js tramite C++
linktitle: Proprietà del documento
type: docs
weight: 80
url: /it/nodejs-cpp/managing-document-properties/
description: Impara come gestire le proprietà del documento attraverso le API Aspose.Cells for Node.js via C++.
keywords: Come gestire le proprietà del documento in Node.js tramite C++, ottenere o impostare proprietà del documento usando Node.js tramite C++, aggiungere o eliminare proprietà del documento tramite Node.js tramite C++, inserire o rimuovere proprietà del documento con Node.js tramite C++, come accedere alle proprietà del documento usando le API Aspose.Cells for Node.js via C++.
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

Aspose.Cells for Node.js via C++ scrive direttamente le informazioni sull'API e il numero di versione nei documenti di output. Ad esempio, al renderizzare un documento in PDF, Aspose.Cells for Node.js via C++ popola il campo **Applicazione** con il valore 'Aspose.Cells' e il campo **Produttore PDF** con il valore, ad esempio 'Aspose.Cells v17.9'.

Si noti che non è possibile istruire Aspose.Cells for Node.js via C++ a cambiare o rimuovere queste informazioni dai documenti di output.

{{% /alert %}}

### **Come accedere alle proprietà del documento**

Le API di Aspose.Cells supportano sia le proprietà del documento integrate che quelle personalizzate. La classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) di Aspose.Cells rappresenta un file Excel e, come un file Excel, la classe [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) può contenere più fogli di lavoro, ciascuno rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet), mentre la raccolta di fogli di lavoro è rappresentata dalla classe [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection).

Usa [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) per accedere alle proprietà del documento del file come descritto di seguito.

- Per accedere alle proprietà integrate del documento, utilizzare [**WorksheetCollection.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getBuiltInDocumentProperties--).
- Per accedere alle proprietà personalizzate del documento, utilizzare [**WorksheetCollection.getCustomDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getCustomDocumentProperties--).

Sia [**WorksheetCollection.getBuiltInDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getBuiltInDocumentProperties--) che [**WorksheetCollection.getCustomDocumentProperties()**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection/#getCustomDocumentProperties--) restituiscono l'istanza di [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/). Questa raccolta contiene [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) oggetti, ciascuno dei quali rappresenta una proprietà del documento, sia integrata che personalizzata.

Spetta all'applicazione decidere come accedere a una proprietà; ad esempio, usando l'indice o il nome della proprietà da [**DocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/), come mostrato nell'esempio sottostante.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample-document-properties.xlsx");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Accessing a custom document property by using the property name
const customProperty1 = customProperties.get("ContentTypeId");
console.log(`${customProperty1.getName()} ${customProperty1.getValue()}`);

// Accessing the same custom document property by using the property index
const customProperty2 = customProperties.get(0);
console.log(`${customProperty2.getName()} ${customProperty2.getValue()}`);
```

La classe [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) permette di recuperare il nome, il valore e il tipo della proprietà del documento:

- Per ottenere il nome della proprietà, utilizzare [**DocumentProperty.getName()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getName--).
- Per ottenere il valore della proprietà, usa [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--). [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--) restituisce il valore come Oggetto.
- Per ottenere il tipo di proprietà, usa [**DocumentProperty.getType()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getType--). Questa restituisce uno dei valori dell'enumerazione [**PropertyType**](https://reference.aspose.com/cells/nodejs-cpp/propertytype/). Dopo aver ottenuto il tipo di proprietà, usa uno dei metodi **DocumentProperty.ToXXX** per ottenere il valore del tipo appropriato invece di usare [**DocumentProperty.getValue()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getValue--). I metodi **DocumentProperty.ToXXX** sono descritti nella tabella sottostante.

{{% alert color="primary" %}}

La classe [**DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/) fornisce anche un insieme di metodi che restituiscono i valori di altri tipi di dati.

{{% /alert %}}

|**Nome membro**|**Descrizione**|**Metodo ToXXX**|
| :- | :- | :- |
|Boolean|Il tipo di dati della proprietà è Booleano|ToBool|
|Date|Il tipo di dati della proprietà è DataOra. Nota che Microsoft Excel memorizza solo <br>la parte della data, nessuna ora può essere memorizzata in una proprietà personalizzata di questo tipo|ToDateTime|
|Float|Il tipo di dati della proprietà è Double|ToDouble|
|Number|Il tipo di dati della proprietà è Int32|ToInt|
|String|Il tipo di dato della proprietà è string|ToString|

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample-document-properties.xlsx");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Accessing a custom document property
const customProperty1 = customProperties.get(0);

// Storing the value of the document property as an object
const objectValue = customProperty1.getValue();

// Accessing a custom document property
const customProperty2 = customProperties.get(1);

// Checking the type of the document property and then storing the value of the
// document property according to that type
if (customProperty2.getType() === AsposeCells.PropertyType.String) {
const value = customProperty2.getValue().toString();
console.log(`${customProperty2.getName()} : ${value}`);
}
```

### **Come Aggiungere o Rimuovere Proprietà del Documento Personalizzate**

Come abbiamo descritto in precedenza all'inizio di questo argomento, i programmatori non possono aggiungere o rimuovere proprietà integrate perché queste proprietà sono definite dal sistema, ma è possibile aggiungere o rimuovere proprietà personalizzate poiché queste sono definite dall'utente.

### **Come Aggiungere Proprietà Personalizzate**

Le API Aspose.Cells hanno esposto il metodo [**add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#add-string-string-) per la classe [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/) al fine di aggiungere proprietà personalizzate alla raccolta. Il metodo [**add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#add-string-string-) aggiunge la proprietà al file Excel e restituisce un riferimento alla nuova proprietà del documento come oggetto [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/).

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Adding a custom document property to the Excel file
customProperties.add("Publisher", "Aspose");

// Saving resultant spreadsheet
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

### **Come Configurare Proprietà Personalizzata “Collegamento al contenuto”**

Per creare una proprietà personalizzata collegata al contenuto di un intervallo dato, chiamare il metodo [**CustomDocumentPropertyCollection.addLinkToContent(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/customdocumentpropertycollection/#addLinkToContent-string-string-) e passare il nome della proprietà e la sorgente. È possibile verificare se una proprietà è configurata come collegata al contenuto utilizzando la proprietà [**DocumentProperty.isLinkedToContent()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#isLinkedToContent--). Inoltre, è possibile ottenere anche l'intervallo sorgente utilizzando la proprietà [**getSource()**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/#getSource--) della classe [**DocumentProperty**](https://reference.aspose.com/cells/nodejs-cpp/documentproperty/).

Utilizziamo un file modello semplice di Microsoft Excel nell'esempio. Il workbook ha un intervallo denominato definito **MyRange**, che si riferisce a un valore della cella.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate an object of Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getWorksheets().getCustomDocumentProperties();

// Add link to content.
customProperties.addLinkToContent("Owner", "MyRange");

// Accessing the custom document property by using the property name
const customProperty1 = customProperties.get("Owner");

// Check whether the property is linked to content
const isLinkedToContent = customProperty1.isLinkedToContent();

// Get the source for the property
const source = customProperty1.getSource();

// Save the file
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

### **Come rimuovere proprietà personalizzate**

Per rimuovere proprietà personalizzate usando Aspose.Cells, chiamare il metodo [**DocumentPropertyCollection.remove(string)**](https://reference.aspose.com/cells/nodejs-cpp/documentpropertycollection/#remove-string-) e passare il nome della proprietà del documento da rimuovere.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample-document-properties.xlsx"));

// Retrieve a list of all custom document properties of the Excel file
const customProperties = workbook.getCustomDocumentProperties();

// Removing a custom document property
customProperties.remove("Publisher");

// Save the file
workbook.save(path.join(dataDir, "out_sample-document-properties.xlsx"));
```

## **Argomenti avanzati**
- [Aggiunta di proprietà personalizzate visibili all'interno del pannello delle informazioni del documento](/cells/it/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/)
- [Impostazione delle proprietà ScaleCrop e LinksUpToDate delle proprietà del documento integrato](/cells/it/nodejs-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Specifica la versione del documento del file Excel utilizzando le proprietà del documento integrato](/cells/it/nodejs-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Specificare la lingua del file Excel utilizzando le proprietà di documento incorporate](/cells/it/nodejs-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
