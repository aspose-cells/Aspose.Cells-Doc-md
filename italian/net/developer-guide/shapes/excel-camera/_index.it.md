---
title: Telecamera di Excel in Aspose.Cells for .Net
linktitle: Telecamera di Excel
description: Scopri come utilizzare la Telecamera di Excel in Aspose.Cells for .Net per creare un'immagine dinamica collegata a un intervallo di celle che si aggiorna automaticamente con i dati di origine e preserva tutta la formattazione dell'area di origine.
keywords: Aspose.Cells, .NET, Telecamera di Excel, immagine dinamica, immagine collegata, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, MemoryStream
type: docs
weight: 90
url: /it/net/excel-camera/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

La Telecamera di Excel è un oggetto del foglio di lavoro che visualizza un'immagine in tempo reale di un intervallo di celle e si trova sul livello di disegno come un'immagine normale. Aspose.Cells supporta due modalità di creazione: un'immagine dinamica che si aggiorna automaticamente ogni volta che cambiano i dati di origine e un'immagine statica che acquisisce un'istantanea dell'area in un momento specifico. Questo articolo illustra entrambi gli approcci, consentendoti di scegliere quello più adatto al layout.

## Che cos'è la Telecamera di Excel?
La Telecamera di Excel è essenzialmente un oggetto `Picture` ancorato a una riga e a una colonna specifiche del livello di disegno del foglio di lavoro. A differenza di un'immagine normale inserita nel foglio, la Telecamera è collegata a un intervallo di origine mediante una formula in stile A1, ad esempio `"A1:F10"`. Ogni volta che una cella dell'intervallo viene modificata, l'immagine della Telecamera viene aggiornata automaticamente per riflettere il nuovo contenuto. La Telecamera preserva l'intera formattazione dell'area di origine — bordi, colori di sfondo, tipi di carattere e formati numerici — in modo che tutto ciò che è visibile nelle celle appaia anche nell'immagine della Telecamera. Questo rende la Telecamera particolarmente utile per dashboard, riepiloghi, pannelli laterali e layout di report in cui si desidera un'anteprima visibile di un'area remota senza dover scorrere il foglio o duplicare i dati. Si applicano due avvertenze: è necessario chiamare `UpdateSelectedValue()` prima di salvare la cartella di lavoro e il file deve essere esportato in HTML o PDF, perché questi formati si basano sui dati dell'immagine incorporata anziché su un ricalcolo in tempo reale.

## Metodo 1 — Aggiungere una Telecamera dinamica
La Telecamera dinamica è l'approccio più comune e corrisponde più da vicino allo strumento Telecamera integrato in Excel. Funziona aggiungendo un'immagine inizialmente vuota e assegnando alla proprietà `Formula` un riferimento all'intervallo di origine. Dopo l'assegnazione, la chiamata a `UpdateSelectedValue()` aggiorna i dati dell'immagine incorporata, mantenendoli sincronizzati con le celle a cui fa riferimento. La Telecamera non dispone di una classe dedicata, ma si basa interamente sul tipo `Picture` standard.
Le API principali sono:
- `PictureCollection.Add(int upperLeftRow, int upperLeftColumn, Stream stream)` — aggiunge un'immagine ancorata alla riga e alla colonna specificate. Il passaggio di `null` per il parametro `stream` crea un'immagine vuota che funge da segnaposto per una Telecamera dinamica. Il metodo restituisce l'indice della nuova immagine.
- `worksheet.Pictures[index]` — accesso tramite indicizzatore per recuperare un oggetto `Picture` specifico dalla raccolta.
- `Picture.Formula` — proprietà di tipo stringa (get/set) che contiene il riferimento in stile A1 all'intervallo di origine riprodotto dalla Telecamera, ad esempio `"A1:F10"`.
- `Picture.UpdateSelectedValue()` — metodo `void` che aggiorna i dati dell'immagine incorporata dalle celle a cui fa riferimento `Formula`.

{{% alert color="primary" %}}
`UpdateSelectedValue()` DEVE essere chiamato prima del salvataggio quando l'output è HTML o PDF; in caso contrario, il file esportato non conterrà i dati dell'immagine e la Telecamera apparirà vuota nell'output renderizzato.
Il codice seguente crea una cartella di lavoro, aggiunge un'immagine vuota ancorata alla riga 10 e alla colonna 6, la collega all'intervallo di origine `A1:F10` tramite la proprietà `Formula`, aggiorna i dati dell'immagine incorporata e salva la cartella di lavoro.
{{% /alert %}}

```csharp
using System;
using System.IO;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Drawing;
var workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "CameraDemo";
// Camera dinamica: aggiungi un'immagine vuota, collegala tramite Formula a A1:F10, quindi aggiorna
var pictures = worksheet.Pictures;
int index = pictures.Add(10, 6, (Stream)null);
pictures[0].Formula = "A1:F10";
pictures[0].UpdateSelectedValue();
workbook.Save("output_dynamic.xlsx", SaveFormat.Xlsx);
```

## Metodo 2 — Aggiungere una Telecamera statica
La Telecamera statica è essenzialmente un'anteprima dell'intervallo di celle renderizzata una sola volta. Invece di mantenere un collegamento in tempo reale, si converte l'intervallo in un'immagine, si racchiudono i byte risultanti in un `MemoryStream` e si aggiunge il flusso come immagine normale. Il contenuto dell'immagine rimane quindi fissato al momento della creazione e non si aggiorna automaticamente quando le celle di origine vengono modificate.
Le API principali sono:
- `Cells.CreateRange(string address)` — costruisce un oggetto `Range` da un indirizzo in stile A1, ad esempio `"A1:F10"`.
- `Range.ToImage(ImageOrPrintOptions options)` — rende l'intervallo producendo i byte dell'immagine. Il passaggio di `null` usa le opzioni di rendering predefinite; sono disponibili sovraccarichi per un controllo più preciso dell'output.
- `new MemoryStream(byte[] buffer)` — racchiude i byte dell'immagine renderizzata in un `MemoryStream` che può essere passato a `PictureCollection.Add`.
- `PictureCollection.Add(int upperLeftRow, int upperLeftColumn, Stream stream)` — aggiunge l'immagine ancorata alla riga e alla colonna specificate, questa volta passando il `MemoryStream` prodotto dal rendering.
Il codice seguente crea una cartella di lavoro, costruisce un `Range` per `A1:F10`, acquisisce i byte dell'immagine tramite `Range.ToImage(null)`, racchiude i byte in un `MemoryStream`, aggiunge l'immagine ancorata alla riga 10 e alla colonna 6 e salva la cartella di lavoro.

```csharp
using System;
using System.IO;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Drawing;
var workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "CameraDemo";
// Camera statica: costruisci Range, esegui il rendering in byte, racchiudilo in MemoryStream, aggiungilo come immagine
var range = workbook.Worksheets[0].Cells.CreateRange("A1:F10");
var pictures = worksheet.Pictures;
pictures.Add(10, 6, new MemoryStream(range.ToImage(null)));
workbook.Save("output_static.xlsx", SaveFormat.Xlsx);
```

## Scelta tra una Telecamera dinamica e una statica
- **Telecamera dinamica:** si aggiorna a ogni ricalcolo, supporta l'esportazione in HTML e PDF dopo `UpdateSelectedValue()` e preserva il comportamento di collegamento in tempo reale per l'intera durata del file.
- **Telecamera statica:** un singolo rendering che non viene mai aggiornato, utile quando è necessario incorporare un'istantanea visiva fissa al momento della compilazione anziché mantenere una replica in tempo reale dei dati.
Aspose.Cells supporta sia una Telecamera dinamica con aggiornamento automatico, basata su `Picture.Formula` e `UpdateSelectedValue()`, sia una Telecamera statica basata su `Range.ToImage` e `MemoryStream`, che esegue un solo rendering. Scegli l'approccio dinamico quando l'output deve rimanere sincronizzato con le celle di origine e quello statico quando è necessario disporre soltanto di un'istantanea visiva fissa al momento della compilazione.

## Articoli correlati
- [Convertire Sparkline in immagine e HTML in Aspose.Cells for .Net](/cells/it/net/convert-sparkline-to-image-and-html/)
- [Inserimento di un'immagine in una cella](/cells/it/net/inserting-an-image-into-a-cell/)
- [Aggiungere campi filtro a una tabella pivot in Aspose.Cells for .Net](/cells/it/net/add-page-field-in-pivot-table/)
- [Applicare stili alle tabelle pivot in Aspose.Cells for .Net](/cells/it/net/apply-style-to-pivot-table/)
- [Modificare il layout del campo pagina in una tabella pivot](/cells/it/net/change-page-field-layout/)

{{< app/cells/assistant language="csharp" >}}