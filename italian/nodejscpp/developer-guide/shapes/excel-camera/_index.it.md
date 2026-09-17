---
title: Excel Camera in Aspose.Cells for Node.js via C++
linktitle: Excel Camera
description: Scopri come usare Excel Camera in Aspose.Cells for Node.js via C++ per creare un'immagine dinamica collegata a un intervallo di celle che si aggiorna con i dati di origine e conserva tutta la formattazione di origine.
keywords: Aspose.Cells, Aspose.Cells for Node.js via C++, Excel Camera, dynamic picture, linked picture, Picture.formula, updateSelectedValue, createRange, toImage, Buffer
type: docs
weight: 90
url: /it/nodejs-cpp/excel-camera/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel Camera è un oggetto del foglio di lavoro che esegue il rendering di un'immagine live di un intervallo di celle e fluttua sul livello di disegno come un'immagine ordinaria. Aspose.Cells supporta due modalità di creazione: un'immagine dinamica che si aggiorna automaticamente ogni volta che i dati di origine cambiano e un'immagine statica che cattura un'istantanea una tantum di un intervallo. Questo articolo illustra entrambi gli approcci, così potrai scegliere quello più adatto al tuo layout.

## Che cos'è Excel Camera?
Excel Camera è essenzialmente un oggetto immagine ancorato a una riga e una colonna specifiche sul livello di disegno del foglio di lavoro. A differenza di un'immagine normale inserita, la Camera è collegata a un intervallo di origine tramite una formula in stile A1 come `"A1:F10"`. Ogni volta che una cella all'interno di quell'intervallo cambia, l'immagine della Camera viene aggiornata automaticamente per riflettere il nuovo contenuto. La Camera conserva l'intera formattazione dell'area di origine — bordi, colori di sfondo, font e formati numerici — così tutto ciò che appare all'interno delle celle appare anche nell'immagine della Camera. Questo rende la Camera particolarmente utile per dashboard, riepiloghi, pannelli laterali e layout di report in cui si desidera un'anteprima visibile di un'area remota senza dover scorrere o ripetere i dati. Valgono due avvertenze: è necessario chiamare `updateSelectedValue()` prima di salvare la cartella di lavoro, e il file verrà esportato in HTML o PDF, poiché tali formati si basano sui dati immagine incorporati anziché su un ricalcolo live.

## Metodo 1 — Aggiungere un'immagine Camera dinamica
La Camera dinamica è l'approccio più comune ed è il più vicino allo strumento Camera integrato di Excel. Funziona aggiungendo un'immagine senza contenuto iniziale, per poi assegnarle una `Formula` che fa riferimento all'intervallo di origine. Dopo che la formula è stata assegnata, la chiamata a `updateSelectedValue()` aggiorna i dati immagine incorporati in modo che siano sincronizzati con le celle che riflette. La Camera non è implementata tramite una classe dedicata — è costruita interamente sul tipo standard `Picture`.
Le API chiave sono:
- `Pictures.add(int upperLeftRow, int upperLeftColumn, null)` — aggiunge un'immagine ancorata alla riga e colonna specificate. Passare `null` per il parametro `stream` crea un'immagine vuota che funge da segnaposto per una Camera dinamica. Il metodo restituisce l'indice della nuova immagine.
- `pictures.get(index)` — recupera una specifica `Picture` dalla collezione tramite indice.
- `Picture.formula` — una proprietà stringa (get/set) che contiene il riferimento in stile A1 all'intervallo di origine che la Camera riflette, ad esempio `"A1:F10"`.
- `Picture.updateSelectedValue()` — un metodo void che aggiorna i dati immagine incorporati dalle celle referenziate da `formula`.

{{% alert color="primary" %}}
`updateSelectedValue()` DEVE essere chiamato prima del salvataggio quando l'output è HTML o PDF; altrimenti il file esportato non conterrà i dati immagine e la Camera apparirà vuota nell'output renderizzato.
{{% /alert %}}

Il codice seguente crea una cartella di lavoro, aggiunge un'immagine vuota ancorata alla riga 10 colonna 6, la collega all'intervallo di origine `A1:F10` tramite la proprietà `Formula`, aggiorna i dati immagine incorporati e salva la cartella di lavoro.

```javascript
const aspose = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Fotocamera dinamica: aggiungi un'immagine vuota, collecala tramite Formula ad A1:F10, quindi aggiorna
let pictures = worksheet.getPictures();
let index = pictures.add(10, 6, null);
pictures.get(index).setFormula("A1:F10");
pictures.get(index).updateSelectedValue();
workbook.save("output_dynamic.xlsx", aspose.SaveFormat.Xlsx);
```

## Metodo 2 — Aggiungere un'immagine Camera statica
La Camera statica è essenzialmente un'anteprima renderizzata una tantum di un intervallo di celle. Invece di mantenere un collegamento live, si esegue il rendering dell'intervallo in byte di immagine una volta, si avvolgono tali byte in un `Buffer` e li si aggiunge come una normale immagine. Il contenuto dell'immagine è quindi fissato al momento della creazione e non si aggiorna automaticamente quando le celle di origine cambiano.
Le API chiave sono:
- `Cells.createRange(address)` — costruisce un oggetto `Range` da un indirizzo in stile A1 come `"A1:F10"`.
- `Range.toImage(ImageOrPrintOptions options)` — esegue il rendering dell'intervallo in byte di immagine. Passare `null` usa le opzioni di rendering predefinite; esistono overload per un controllo più fine sull'output.
- `new Buffer(byte[] buffer)` — avvolge i byte dell'immagine renderizzata in un `Buffer` che può essere passato a `getPictures().add`.
- `Pictures.add(int upperLeftRow, int upperLeftColumn, null)` — aggiunge l'immagine ancorata alla riga e colonna specificate, questa volta passando il `Buffer` prodotto dal rendering.
Il codice seguente crea una cartella di lavoro, costruisce un `Range` per `A1:F10`, lo rende in byte di immagine tramite `range.toImage(null)`, avvolge i byte in un `Buffer`, aggiunge l'immagine ancorata alla riga 10 colonna 6 e salva la cartella di lavoro.

```javascript
const aspose = require("aspose.cells");
const { MemoryStream } = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Camera Statico: crea Range, renderizza in byte, avvolgi in MemoryStream, aggiungi come immagine
let range = worksheet.getCells().createRange("A1:F10");
let imageBytes = range.toImage(null);
let stream = new MemoryStream();
stream.write(imageBytes);
let pictures = worksheet.getPictures();
pictures.add(10, 6, stream);
workbook.save("output_static.xlsx", aspose.SaveFormat.Xlsx);
```

## Scegliere tra dinamico e statico
- **Camera dinamica:** si aggiorna a ogni ricalcolo, supporta l'esportazione in HTML e PDF dopo `updateSelectedValue()` e conserva il comportamento di collegamento live per tutta la vita del file.
- **Camera statica:** un rendering una tantum che non si aggiorna mai, utile quando si desidera un'istantanea visiva fissa incorporata al momento della build anziché un mirror live dei dati.
Aspose.Cells supporta sia una Camera dinamica ad auto-aggiornamento costruita su `Picture.formula` più `updateSelectedValue()` sia una Camera statica one-shot costruita su `Range.toImage` più un `Buffer`. Scegli l'approccio dinamico quando il tuo output deve rimanere sincronizzato con le celle di origine, e scegli l'approccio statico quando hai bisogno solo di un'istantanea visiva fissa al momento della build.

{{< app/cells/assistant language="nodejs-cpp" >}}