---
title: Usa parti XML personalizzate in Aspose.Cells con Node.js tramite C++
linktitle: Usare Parti XML Personalizzate in Aspose.Cells
type: docs
weight: 390
url: /it/nodejs-cpp/use-custom-xml-parts-in-aspose-cells/
description: Impara come usare parti XML personalizzate in Aspose.Cells for Node.js via C++. Integra i dati XML esterni all’interno dei file Excel senza problemi.
--- 

## Utilizzo di Parti XML Personalizzate in Aspose.Cells

Le Parti XML personalizzate sono i dati XML memorizzati da diverse applicazioni, come SharePoint, all’interno del file Excel. Questi dati sono consumati da varie applicazioni che ne hanno bisogno. Microsoft Excel non utilizza questi dati, quindi non esiste un’interfaccia grafica per aggiungerli. Puoi visualizzare questi dati cambiando l’estensione di **.xlsx** in **.zip** e aprendo il file con **WinZip**. Puoi anche aprire il file ZIP usando qualsiasi utility di compressione di terze parti come WinRAR o WinZip. I dati sono presenti nella cartella **customXml**.

Puoi aggiungere parti XML personalizzate usando Aspose.Cells tramite il metodo [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/).

Il seguente esempio di codice utilizza il metodo [**ContentTypePropertyCollection**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/) e aggiunge il **Catalogo XML dei Libri** e il suo nome è **BookStore**. L'immagine seguente mostra il risultato di questo codice. Come puoi vedere, il Catalogo XML dei Libri è aggiunto all'interno del nodo BookStore, che è il nome di questa proprietà.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## Codice Node.js per usare parti XML personalizzate

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "output.xlsx");

// The sample XML that will be injected to Workbook
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

// Create an instance of Workbook class
const workbook = new AsposeCells.Workbook();

// Add Custom XML Part to ContentTypePropertyCollection
workbook.getContentTypeProperties().add("BookStore", booksXML);

// Save the resultant spreadsheet
workbook.save(filePath);
```

## Articolo Correlato

- [Aggiunta di proprietà personalizzate visibili all'interno del pannello delle informazioni del documento](/cells/it/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/)
{{< app/cells/assistant language="nodejs-cpp" >}}
