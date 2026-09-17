---
title: Excel Camera in Aspose.Cells for Node.js via Java
linktitle: Excel Camera
description: Scopri come usare Excel Camera in Aspose.Cells for Node.js via Java per creare un'immagine dinamica collegata a un intervallo di celle che si aggiorna con i dati di origine e conserva tutta la formattazione sorgente.
keywords: Aspose.Cells, Aspose.Cells for Node.js via Java, Excel Camera, immagine dinamica, immagine collegata, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, Buffer
type: docs
weight: 90
url: /it/nodejs-java/excel-camera/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel Camera è un oggetto del foglio di lavoro che visualizza un'immagine live di un intervallo di celle e fluttua sul livello di disegno come un'immagine normale. Aspose.Cells supporta due modalità di creazione, un'immagine dinamica che si aggiorna automaticamente ogni volta che i dati di origine cambiano e un'immagine statica che cattura un'istantanea una tantum di un intervallo. Questo articolo illustra entrambi gli approcci così puoi scegliere quello più adatto al tuo layout.

## Cos'è Excel Camera?
Excel Camera è essenzialmente un oggetto immagine ancorato a una riga e colonna specifiche sul livello di disegno del foglio di lavoro. A differenza di un'immagine inserita normale, la Camera è collegata a un intervallo di origine tramite una formula in stile A1 come `"A1:F10"`. Ogni volta che una cella all'interno di quell'intervallo cambia, l'immagine della Camera viene aggiornata automaticamente per riflettere il nuovo contenuto. La Camera conserva l'intera formattazione dell'area di origine — bordi, colori di sfondo, font e formati numerici — quindi tutto ciò che è visibile nelle celle appare anche nell'immagine della Camera. Questo rende la Camera particolarmente utile per dashboard, riepiloghi, pannelli laterali e layout di report in cui vuoi un'anteprima visibile di un'area remota senza scorrere o ripetere i dati. Si applicano due avvertenze: devi chiamare `updateSelectedValue()` prima di salvare la cartella di lavoro, e il file verrà esportato in HTML o PDF, perché quei formati si basano sui dati immagine incorporati piuttosto che su un ricalcolo live.

## Metodo 1 — Aggiungere un'Immagine Camera Dinamica
La Camera dinamica è l'approccio più comune ed è il più vicino allo strumento Camera integrato di Excel. Funziona aggiungendo un'immagine senza contenuto iniziale, quindi assegnandole una `Formula` che fa riferimento all'intervallo di origine. Dopo che la formula è stata assegnata, chiamare `updateSelectedValue()` aggiorna i dati immagine incorporati così che siano sincronizzati con le celle che essa rispecchia. La Camera non è implementata tramite una classe dedicata — è costruita interamente sul tipo standard `Picture`.
Le API chiave sono:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — aggiunge un'immagine ancorata alla riga e colonna specificate. Passare `null` per il parametro `stream` crea un'immagine vuota che funge da segnaposto per una Camera dinamica. Il metodo restituisce l'indice della nuova immagine.
- `worksheet.getPictures().get(index)` — accesso tramite indicizzatore per recuperare una specifica `Picture` dalla raccolta.
- `Picture.Formula` — una proprietà stringa (`getFormula()`/`setFormula()`) che contiene il riferimento in stile A1 all'intervallo di origine che la Camera rispecchia, come `"A1:F10"`.
- `Picture.updateSelectedValue()` — un metodo void che aggiorna i dati immagine incorporati dalle celle referenziate da `Formula`.

{{% alert color="primary" %}}
`updateSelectedValue()` DEVE essere chiamato prima del salvataggio quando l'output è HTML o PDF; altrimenti il file esportato non conterrà i dati dell'immagine e la Camera apparirà vuota nell'output renderizzato.
{{% /alert %}}

Il seguente codice crea una cartella di lavoro, aggiunge un'immagine vuota ancorata a riga 10 colonna 6, la collega all'intervallo di origine `A1:F10` tramite la proprietà `Formula`, aggiorna i dati immagine incorporati e salva la cartella di lavoro.

```javascript
const aspose = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Dynamic Camera: aggiungi un'immagine vuota, collegala tramite Formula a A1:F10, quindi aggiorna
let pictures = worksheet.getPictures();
let index = pictures.add(10, 6, null);
pictures.get(index).setFormula("A1:F10");
pictures.get(index).updateSelectedValue();
workbook.save("output_dynamic.xlsx", aspose.SaveFormat.XLSX);
```

## Metodo 2 — Aggiungere un'Immagine Camera Statica
La Camera statica è essenzialmente un'anteprima renderizzata una tantum di un intervallo di celle. Invece di mantenere un collegamento live, renderizzi l'intervallo in byte di immagine una volta, avvolgi quei byte in un `ByteArrayInputStream` e li aggiungi come un'immagine normale. Il contenuto dell'immagine viene quindi fissato al momento della creazione e non si aggiorna automaticamente quando le celle di origine cambiano.
Le API chiave sono:
- `Cells.createRange(String address)` — costruisce un oggetto `Range` da un indirizzo in stile A1 come `"A1:F10"`.
- `Range.toImage(ImageOrPrintOptions options)` — rende l'intervallo in byte di immagine. Passare `null` usa le opzioni di rendering predefinite; esistono overload per un controllo più fine sull'output.
- `new ByteArrayInputStream(byte[] buffer)` — avvolge i byte dell'immagine renderizzata in un `ByteArrayInputStream` che può essere passato a `PictureCollection.add`.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — aggiunge l'immagine ancorata alla riga e colonna specificate, questa volta passando il `ByteArrayInputStream` prodotto dal rendering.
Il seguente codice crea una cartella di lavoro, costruisce un `Range` per `A1:F10`, lo rende in byte di immagine tramite `range.toImage(null)`, avvolge i byte in un `ByteArrayInputStream`, aggiunge l'immagine ancorata a riga 10 colonna 6 e salva la cartella di lavoro.

```javascript
const aspose = require("aspose.cells");
let workbook = new aspose.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Camera statica: costruisce un intervallo, lo rende in byte, lo avvolge in ByteArrayInputStream, lo aggiunge come immagine
let range = worksheet.getCells().createRange("A1:F10");
let imageBytes = range.toImage(null);
let pictures = worksheet.getPictures();
pictures.add(10, 6, new aspose.ByteArrayInputStream(imageBytes));
workbook.save("output_static.xlsx", aspose.SaveFormat.XLSX);
```

## Scegliere tra Dinamica e Statica
- **Camera Dinamica:** si aggiorna ad ogni ricalcolo, supporta l'esportazione in HTML e PDF dopo `updateSelectedValue()`, e preserva il comportamento di collegamento live per tutta la durata del file.
- **Camera Statica:** un render una tantum che non si aggiorna mai, utile quando vuoi un'istantanea visiva fissa incorporata al momento della build piuttosto che un mirror live dei dati.
Aspose.Cells supporta sia una Camera dinamica ad aggiornamento automatico costruita su `Picture.Formula` più `updateSelectedValue()` sia una Camera statica one-shot costruita su `Range.toImage` più un `ByteArrayInputStream`. Scegli l'approccio dinamico quando il tuo output deve rimanere sincronizzato con le celle di origine, e scegli l'approccio statico quando hai bisogno solo di un'istantanea visiva fissa al momento della build.

{{< app/cells/assistant language="nodejs-java" >}}