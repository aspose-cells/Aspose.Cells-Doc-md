---
title: Importa XML in cartella di lavoro Excel con Node.js tramite C++
linktitle: Mappe XML
type: docs
weight: 210
url: /it/nodejs-cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: Importa dati da file XML in Excel usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Aspose.Cells permette di importare la mappa XML all’interno della cartella di lavoro usando il metodo [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#importXml-string-string-number-number-). Puoi importare la mappa XML con Microsoft Excel seguendo questi passaggi:

- Seleziona la scheda **Sviluppo**
- Fai clic su **Importa** nella sezione XML e segui i passaggi richiesti.

Dovrai fornire i tuoi dati XML per completare l'importazione. Ecco un [esempio di dati XML](5115037.txt) che puoi utilizzare per i test.

{{% /alert %}}

## **Importa la mappa XML utilizzando Microsoft Excel**

La seguente schermata mostra come importare la mappa XML utilizzando Microsoft Excel.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **Importa mappa XML usando Aspose.Cells for Node.js via C++**

Il seguente codice di esempio mostra come utilizzare [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#importXml-string-string-number-number-). Genera il [file Excel di output](5115036.xlsx) come mostrato in questa schermata.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create a workbook
const workbook = new AsposeCells.Workbook();

// Local XML file path
const XML = path.join(dataDir, "sampleXML.txt");

// Import your XML Map data starting from cell A1
workbook.importXml(XML, "Sheet1", 0, 0);

// Save workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```

## **Argomenti avanzati**
- [Aggiungi mappa XML all’interno della cartella di lavoro usando il metodo XmlMapCollection.add()](/cells/it/nodejs-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [Esporta dati XML collegati alla mappa XML all'interno del Workbook](/cells/it/nodejs-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [Trova il nome dell'elemento radice della mappa XML](/cells/it/nodejs-cpp/find-the-root-element-name-of-xml-map/)
- [Collega le celle agli elementi della mappa XML](/cells/it/nodejs-cpp/link-cells-to-xml-map-elements/)

{{< app/cells/assistant language="nodejs-cpp" >}}
