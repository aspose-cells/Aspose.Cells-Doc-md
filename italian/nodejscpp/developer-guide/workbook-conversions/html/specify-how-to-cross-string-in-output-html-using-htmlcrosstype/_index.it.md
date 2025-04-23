---
title: Specifica come attraversare la stringa nel HTML di output usando HtmlCrossType con Node.js tramite C++
linktitle: Specificare come attraversare la stringa nell output HTML usando HtmlCrossType
type: docs
weight: 140
url: /it/nodejs-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Impara come controllare il trabocco delle stringhe in HTML impostando HtmlCrossType in Aspose.Cells for Node.js via C++. 
---

## **Possibili Scenari di Utilizzo**

Quando una cella contiene testo o stringa ma è più grande della larghezza della cella, la stringa trabocca se la cella successiva nella colonna successiva è nulla o vuota. Quando salvi il tuo file Excel in HTML, puoi controllare questo trabocco specificando il tipo di attraversamento usando l'enumerazione [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype). Ha i seguenti valori:

- **HtmlCrossType.Default**: Mostra come MS Excel; dipende dalla cella successiva. Se la cella successiva è nulla, la stringa attraversa o verrà troncata.

- **HtmlCrossType.MSExport**: Visualizza la stringa come esportazione HTML di MS Excel.

- **HtmlCrossType.Cross**: Mostra la stringa incrociata in HTML; le prestazioni per la creazione di grandi file HTML saranno più di dieci volte più veloci rispetto all'impostazione del valore su Default o FitToCell.

- **HtmlCrossType.FitToCell**: Mostra solo la stringa all'interno della larghezza della cella.

## **Specifica come attraversare la stringa nell'output HTML utilizzando HtmlCrossType**

Il codice di esempio seguente carica il [file Excel di esempio](51740732.xlsx) e lo salva in formato HTML specificando diversi [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype). Si prega di scaricare gli [HTML di output](51740734.zip) generati con questo codice. Il file Excel di esempio contiene l'immagine bordata di colore rosso come mostrato in questo screenshot che mostra l'effetto dei valori [**HtmlCrossType**](https://reference.aspose.com/cells/nodejs-cpp/htmlcrosstype) sull'HTML di output.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Codice di Esempio**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHtmlCrossStringType.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Specify HTML Cross Type
const opts = new AsposeCells.HtmlSaveOptions();
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.Default);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.MSExport);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.Cross);
opts.setHtmlCrossStringType(AsposeCells.HtmlCrossType.FitToCell);

// Output Html
workbook.save("out" + opts.getHtmlCrossStringType() + ".htm", opts);
```
