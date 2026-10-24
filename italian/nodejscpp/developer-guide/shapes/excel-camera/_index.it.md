---
title: Excel Camera con Aspose.Cells for Node.js via C++
linktitle: Excel Camera con Aspose.Cells for Node.js via C++
description: Scopri come utilizzare Excel Camera con Aspose.Cells for Node.js via C++ per creare un'immagine dinamica collegata a un intervallo di celle che si aggiorna con i dati di origine e preserva l'intera formattazione dell'area di origine.
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, Excel Camera, immagine dinamica, immagine collegata, Picture.formula, updateSelectedValue, createRange, toImage, Buffer
type: docs
weight: 90
url: /it/nodejs-cpp/excel-camera/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel Camera è un oggetto del foglio di lavoro che mostra un'immagine sempre aggiornata di un intervallo di celle e viene visualizzato sul livello di disegno come un'immagine normale. Aspose.Cells supporta due modalità di creazione: un'immagine dinamica che si aggiorna automaticamente ogni volta che cambiano i dati di origine e un'immagine statica che cattura una sola istantanea di un intervallo. Questo articolo illustra entrambi gli approcci, consentendo di scegliere quello più adatto al layout.

## Che cos'è Excel Camera?
Excel Camera è essenzialmente un oggetto immagine ancorato a una riga e a una colonna specifiche sul livello di disegno del foglio di lavoro. A differenza di una normale immagine inserita, Excel Camera è collegata a un intervallo di origine mediante una formula in stile A1 come `"A1:F10"`. Ogni volta che il contenuto di una cella dell'intervallo cambia, l'immagine di Excel Camera viene aggiornata automaticamente per riflettere il nuovo contenuto. Excel Camera preserva tutta la formattazione dell'area di origine — bordi, colori di sfondo, font e formati numerici — in modo che ogni elemento visibile nelle celle venga riportato anche nella sua immagine. Questo rende Excel Camera particolarmente utile per dashboard, riepiloghi, pannelli laterali e layout di report in cui si desidera un'anteprima di un'area lontana del foglio di lavoro senza dover scorrere il foglio o ripetere i dati. Si applicano due avvertenze: `updateSelectedValue()` deve essere chiamato prima di salvare la cartella di lavoro e il file deve essere esportato in HTML o PDF, poiché questi formati si basano sui dati dell'immagine incorporata anziché su un ricalcolo in tempo reale.

## Metodo 1 — Aggiungere un'immagine dinamica tramite Camera
La Camera dinamica è l'approccio più comune e il più simile allo strumento Camera integrato in Excel. Consiste nell'aggiungere un'immagine priva di contenuto iniziale e nell'assegnarle una `Formula` che fa riferimento all'intervallo di origine. Dopo l'assegnazione della formula, la chiamata a `updateSelectedValue()` aggiorna i dati dell'immagine incorporata, mantenendoli sincronizzati con le celle di origine. La Camera non è implementata mediante una classe dedicata, ma si basa interamente sul tipo standard `Picture`.
Le API principali sono:
- `Pictures.add(int upperLeftRow, int upperLeftColumn, bytes)` — aggiunge un'immagine ancorata alla riga e alla colonna indicate. Il valore `null` per il parametro `stream` crea un'immagine vuota da utilizzare come segnaposto per una Camera dinamica. Il metodo restituisce l'indice della nuova immagine.
- `pictures.get(index)` — recupera dalla raccolta l'oggetto `Picture` corrispondente all'indice specificato.
- `Picture.formula` — una proprietà di tipo string (get/set) che contiene il riferimento in stile A1 all'intervallo di origine che la Camera rispecchia, come `"A1:F10"`.
- `Picture.updateSelectedValue()` — un metodo void che aggiorna i dati dell'immagine incorporata in base alle celle a cui fa riferimento `formula`.

{{% alert color="primary" %}}
`updateSelectedValue()` DEVE essere chiamato prima del salvataggio quando l'output è in formato HTML o PDF; in caso contrario, il file esportato non conterrà i dati dell'immagine e Excel Camera apparirà vuota nel risultato renderizzato.
Il codice seguente crea una cartella di lavoro, aggiunge un'immagine vuota ancorata alla riga 10 e alla colonna 6, la collega all'intervallo di origine `A1:F10` tramite la proprietà `Formula`, aggiorna i dati dell'immagine incorporata e salva la cartella di lavoro.
{{% /alert %}}

```javascript
const aspose = require("aspose.cells.node");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Telecamera dinamica: aggiungi un'immagine vuota, collegala tramite Formula a A1:F10, poi aggiorna
let pictures = worksheet.getPictures();
let index = pictures.add(10, 6, null);
pictures.get(index).setFormula("A1:F10");
pictures.get(index).updateSelectedValue();
workbook.save("output_dynamic.xlsx", aspose.SaveFormat.Xlsx);
```

## Metodo 2 — Aggiungere un'immagine statica tramite Camera
La Camera statica è essenzialmente un'anteprima di un intervallo di celle generata una sola volta. Invece di mantenere un collegamento in tempo reale, l'intervallo viene renderizzato una sola volta in byte di immagine; tali byte vengono racchiusi in un `Buffer` e aggiunti come immagine normale. Il contenuto dell'immagine viene quindi fissato al momento della creazione e non si aggiorna automaticamente quando cambiano le celle di origine.
Le API principali sono:
- `Cells.createRange(address)` — genera un oggetto `Range` da un indirizzo in stile A1 come `"A1:F10"`.
- `Range.toImage(ImageOrPrintOptions options)` — esegue il rendering dell'intervallo in byte di immagine. Il valore `null` utilizza le opzioni di rendering predefinite; sono disponibili overload per controllare più precisamente l'output.
- `new Buffer(byte[] buffer)` — racchiude i byte dell'immagine renderizzata in un `Buffer` che può essere passato a `getPictures().add`.
- `Pictures.add(int upperLeftRow, int upperLeftColumn, bytes)` — aggiunge l'immagine ancorata alla riga e alla colonna indicate; in questo caso, il `Buffer` prodotto dal rendering viene passato come parametro `stream`.
Il codice seguente crea una cartella di lavoro, costruisce un `Range` per `A1:F10`, esegue il rendering in byte di immagine tramite `range.toImage(null)`, inserisce i byte in un `Buffer`, aggiunge l'immagine ancorata alla riga 10 e alla colonna 6 e salva la cartella di lavoro.

```javascript
const aspose = require("aspose.cells.node");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
let range = worksheet.getCells().createRange("A1:F10");
let imageBytes = range.toImage(null);
let pictures = worksheet.getPictures();
pictures.add(10, 6, imageBytes);
workbook.save("output_static.xlsx", aspose.SaveFormat.Xlsx);
```

## Scegliere tra l'approccio dinamico e quello statico
- **Camera dinamica:** si aggiorna a ogni ricalcolo, supporta l'esportazione in HTML e PDF dopo `updateSelectedValue()` e mantiene il comportamento di collegamento in tempo reale per l'intera durata del file.
- **Camera statica:** viene generata mediante un rendering effettuato una sola volta, non viene mai aggiornata ed è utile quando si desidera incorporare un'istantanea visiva fissa al momento della compilazione anziché una rappresentazione in tempo reale dei dati.
Aspose.Cells supporta sia una Camera dinamica con aggiornamento automatico, basata su `Picture.formula` e `updateSelectedValue()`, sia una Camera statica generata una sola volta, basata su `Range.toImage` e `Buffer`. Scegli l'approccio dinamico quando l'output deve rimanere sincronizzato con le celle di origine e quello statico quando è sufficiente un'istantanea visiva fissa al momento della compilazione.

{{< app/cells/assistant language="nodejs-cpp" >}}