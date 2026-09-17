---
title: Excel Camera in Aspose.Cells for .NET
linktitle: Excel Camera
description: Scopri come utilizzare Excel Camera in Aspose.Cells for .NET per creare un'immagine dinamica collegata a un intervallo di celle che si aggiorna con i dati di origine e preserva tutta la formattazione dell'origine.
keywords: Aspose.Cells, .NET, Excel Camera, immagine dinamica, immagine collegata, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, MemoryStream
type: docs
weight: 90
url: /it/net/excel-camera/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel Camera è un oggetto del foglio di lavoro che riproduce un'immagine live di un intervallo di celle e fluttua sul livello di disegno come una normale immagine. Aspose.Cells supporta due modalità di creazione, un'immagine dinamica che si aggiorna automaticamente ogni volta che i dati di origine cambiano e un'immagine statica che cattura un'istantanea una tantum di un intervallo. Questo articolo illustra entrambi gli approcci in modo che tu possa scegliere quello più adatto al tuo layout.

## What Is Excel Camera?
Excel Camera è essenzialmente un oggetto immagine ancorato a una riga e una colonna specifiche sul livello di disegno del foglio di lavoro. A differenza di un'immagine inserita normale, la Camera è collegata a un intervallo di origine tramite una formula in stile A1 come `"A1:F10"`. Ogni volta che una cella all'interno di tale intervallo cambia, l'immagine della Camera viene aggiornata automaticamente per riflettere il nuovo contenuto. La Camera preserva la formattazione completa dell'area di origine — bordi, colori di sfondo, font e formati numerici — quindi tutto ciò che è visibile all'interno delle celle appare anche nell'immagine della Camera. Questo rende la Camera particolarmente utile per dashboard, riepiloghi, pannelli laterali e layout di report in cui si desidera un'anteprima visibile di un'area remota senza scorrere o ripetere i dati. Si applicano due avvertenze: è necessario chiamare `UpdateSelectedValue()` prima di salvare la cartella di lavoro, e il file verrà esportato in HTML o PDF, perché tali formati si basano sui dati immagine incorporati anziché su un ricalcolo live.

## Method 1 — Add a Dynamic Camera Picture
La Camera dinamica è l'approccio più comune ed è la corrispondenza più vicina allo strumento Camera integrato di Excel. Funziona aggiungendo un'immagine senza contenuto iniziale, quindi assegnandole una `Formula` che fa riferimento all'intervallo di origine. Dopo l'assegnazione della formula, la chiamata a `UpdateSelectedValue()` aggiorna i dati dell'immagine incorporata in modo che siano sincronizzati con le celle che rispecchia. La Camera non è implementata tramite una classe dedicata — è costruita interamente sul tipo `Picture` standard.
Le API chiave sono:
- `PictureCollection.Add(int upperLeftRow, int upperLeftColumn, Stream stream)` — aggiunge un'immagine ancorata alla riga e colonna specificate. Passando `null` per il parametro `stream` si crea un'immagine vuota che funge da segnaposto per una Camera dinamica. Il metodo restituisce l'indice della nuova immagine.
- `worksheet.Pictures[index]` — accesso tramite indicizzatore per recuperare una specifica `Picture` dalla raccolta.
- `Picture.Formula` — una proprietà stringa (get/set) che contiene il riferimento in stile A1 all'intervallo di origine che la Camera rispecchia, come `"A1:F10"`.
- `Picture.UpdateSelectedValue()` — un metodo void che aggiorna i dati dell'immagine incorporata dalle celle referenziate da `Formula`.

{{% alert color="primary" %}}
`UpdateSelectedValue()` DEVE essere chiamato prima del salvataggio quando l'output è HTML o PDF; altrimenti il file esportato non conterrà i dati dell'immagine e la Camera apparirà vuota nell'output renderizzato.
{{% /alert %}}

Il seguente codice crea una cartella di lavoro, aggiunge un'immagine vuota ancorata alla riga 10 colonna 6, la collega all'intervallo di origine `A1:F10` tramite la proprietà `Formula`, aggiorna i dati dell'immagine incorporata e salva la cartella di lavoro.

```csharp
using System;
using System.IO;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Drawing;
var workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "CameraDemo";
// Dynamic Camera: add an empty picture, link it via Formula to A1:F10, then refresh
var pictures = worksheet.Pictures;
int index = pictures.Add(10, 6, (Stream)null);
pictures[0].Formula = "A1:F10";
pictures[0].UpdateSelectedValue();
workbook.Save("output_dynamic.xlsx", SaveFormat.Xlsx);
```

## Method 2 — Add a Static Camera Picture
La Camera statica è essenzialmente un'anteprima renderizzata una sola volta di un intervallo di celle. Invece di mantenere un collegamento live, si esegue il rendering dell'intervallo in byte di immagine una volta, si avvolgono quei byte in un `MemoryStream` e li si aggiunge come immagine normale. Il contenuto dell'immagine viene quindi fissato al momento della creazione e non si aggiorna automaticamente quando le celle di origine cambiano.
Le API chiave sono:
- `Cells.CreateRange(string address)` — crea un oggetto `Range` da un indirizzo in stile A1 come `"A1:F10"`.
- `Range.ToImage(ImageOrPrintOptions options)` — esegue il rendering dell'intervallo in byte di immagine. Passando `null` vengono utilizzate le opzioni di rendering predefinite; esistono overload per un controllo più fine sull'output.
- `new MemoryStream(byte[] buffer)` — avvolge i byte dell'immagine renderizzata in un `MemoryStream` che può essere inserito in `PictureCollection.Add`.
- `PictureCollection.Add(int upperLeftRow, int upperLeftColumn, Stream stream)` — aggiunge l'immagine ancorata alla riga e colonna specificate, questa volta passando il `MemoryStream` prodotto dal rendering.
Il seguente codice crea una cartella di lavoro, crea un `Range` per `A1:F10`, ne esegue il rendering in byte di immagine tramite `Range.ToImage(null)`, avvolge i byte in un `MemoryStream`, aggiunge l'immagine ancorata alla riga 10 colonna 6 e salva la cartella di lavoro.

```csharp
using System;
using System.IO;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Drawing;
var workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "CameraDemo";
// Static Camera: build Range, render to bytes, wrap in MemoryStream, add as picture
var range = workbook.Worksheets[0].Cells.CreateRange("A1:F10");
var pictures = worksheet.Pictures;
pictures.Add(10, 6, new MemoryStream(range.ToImage(null)));
workbook.Save("output_static.xlsx", SaveFormat.Xlsx);
```

## Choosing Between Dynamic and Static
- **Camera Dinamica:** si aggiorna ad ogni ricalcolo, supporta l'esportazione HTML e PDF dopo `UpdateSelectedValue()` e preserva il comportamento di collegamento live per tutta la durata del file.
- **Camera Statica:** un rendering una tantum che non si aggiorna mai, utile quando si desidera un'istantanea visiva fissa incorporata al momento della creazione anziché un mirror live dei dati.
Aspose.Cells supporta sia una Camera dinamica ad auto-aggiornamento costruita su `Picture.Formula` più `UpdateSelectedValue()` sia una Camera statica one-shot costruita su `Range.ToImage` più un `MemoryStream`. Scegli l'approccio dinamico quando il tuo output deve rimanere sincronizzato con le celle di origine, e scegli l'approccio statico quando hai bisogno solo di un'istantanea visiva fissa al momento della creazione.

## Related Articles
- [Convert Sparkline to Image and HTML in Aspose.Cells for .NET](/cells/it/net/convert-sparkline-to-image-and-html/)
- [Inserting an Image into a Cell](/cells/it/net/inserting-an-image-into-a-cell/)
- [Add Filter Fields to a Pivot Table in Aspose.Cells for .NET](/cells/it/net/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for .NET](/cells/it/net/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/it/net/change-page-field-layout/)

{{< app/cells/assistant language="csharp" >}}