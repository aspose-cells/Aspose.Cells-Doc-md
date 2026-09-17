---
title: Excel Camera in Aspose.Cells for Java
linktitle: Excel Camera
description: Scopri come utilizzare Excel Camera in Aspose.Cells for Java per creare un'immagine dinamica collegata a un intervallo di celle che si aggiorna con i dati di origine e conserva l'intera formattazione dell'area sorgente.
keywords: Aspose.Cells, Java, Excel Camera, immagine dinamica, immagine collegata, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, ByteArrayInputStream
type: docs
weight: 90
url: /it/java/excel-camera/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel Camera è un oggetto del foglio di lavoro che rende un'immagine live di un intervallo di celle e fluttua sul livello di disegno come un'immagine ordinaria. Aspose.Cells supporta due modalità di creazione, un'immagine dinamica che si aggiorna automaticamente ogni volta che i dati di origine cambiano e un'immagine statica che cattura un'istantanea una tantum di un intervallo. Questo articolo illustra entrambi gli approcci così potrai scegliere quello che si adatta al tuo layout.

## What Is Excel Camera?
Excel Camera è essenzialmente un oggetto immagine ancorato a una riga e colonna specifiche sul livello di disegno del foglio di lavoro. A differenza di un'immagine normale inserita, la Camera è collegata a un intervallo di origine tramite una formula in stile A1 come `"A1:F10"`. Ogni volta che una cella all'interno di quell'intervallo cambia, l'immagine della Camera viene aggiornata automaticamente per riflettere il nuovo contenuto. La Camera conserva l'intera formattazione dell'area di origine — bordi, colori di sfondo, caratteri e formati numerici — così tutto ciò che è visibile all'interno delle celle appare anche nell'immagine della Camera. Ciò rende la Camera particolarmente utile per dashboard, riepiloghi, pannelli laterali e layout di report in cui si desidera un'anteprima visibile di un'area remota senza scorrere o ripetere i dati. Ci sono due avvertenze: è necessario chiamare `updateSelectedValue()` prima di salvare la cartella di lavoro, e il file verrà esportato in HTML o PDF, perché tali formati si basano sui dati immagine incorporati piuttosto che su un ricalcolo live.

## Method 1 — Add a Dynamic Camera Picture
La Camera dinamica è l'approccio più comune ed è la corrispondenza più vicina allo strumento Camera integrato di Excel. Funziona aggiungendo un'immagine senza contenuto iniziale, quindi assegnandole una `Formula` che fa riferimento all'intervallo di origine. Dopo l'assegnazione della formula, la chiamata a `updateSelectedValue()` aggiorna i dati immagine incorporati in modo che siano sincronizzati con le celle di cui è il mirror. La Camera non è implementata tramite una classe dedicata — è costruita interamente sul tipo standard `Picture`.
Le API chiave sono:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — aggiunge un'immagine ancorata alla riga e colonna indicate. Passare `null` per il parametro `stream` crea un'immagine vuota che funge da segnaposto per una Camera dinamica. Il metodo restituisce l'indice della nuova immagine.
- `worksheet.getPictures().get(index)` — accesso tramite indicizzatore per recuperare una specifica `Picture` dalla raccolta.
- `Picture.setFormula(String value)` — imposta il riferimento in stile A1 all'intervallo di origine di cui la Camera è il mirror, come `"A1:F10"`.
- `Picture.updateSelectedValue()` — un metodo void che aggiorna i dati immagine incorporati dalle celle a cui fa riferimento `Formula`.

{{% alert color="primary" %}}
`updateSelectedValue()` DEVE essere chiamato prima del salvataggio quando l'output è HTML o PDF; altrimenti il file esportato non conterrà i dati immagine e la Camera apparirà vuota nell'output renderizzato.
{{% /alert %}}

Il codice seguente crea una cartella di lavoro, aggiunge un'immagine vuota ancorata alla riga 10 colonna 6, la collega all'intervallo di origine `A1:F10` tramite `setFormula`, aggiorna i dati immagine incorporati e salva la cartella di lavoro.

```java
import java.io.InputStream;
import com.aspose.cells.PictureCollection;
import com.aspose.cells.SaveFormat;
import com.aspose.cells.Workbook;
import com.aspose.cells.Worksheet;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Fotocamera Dinamica: aggiungi un'immagine vuota, collegalo tramite Formula a A1:F10, poi aggiorna
PictureCollection pictures = worksheet.getPictures();
int index = pictures.add(10, 6, (InputStream) null);
pictures.get(index).setFormula("A1:F10");
pictures.get(index).updateSelectedValue();
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX);
```

## Method 2 — Add a Static Camera Picture
La Camera statica è essenzialmente un'anteprima renderizzata una tantum di un intervallo di celle. Invece di mantenere un collegamento live, si rende l'intervallo in byte di immagine una volta, si avvolgono tali byte in un `ByteArrayInputStream` e li si aggiungono come un'immagine normale. Il contenuto dell'immagine è quindi fissato al momento della creazione e non si aggiorna automaticamente quando le celle di origine cambiano.
Le API chiave sono:
- `Cells.createRange(String address)` — costruisce un oggetto `Range` da un indirizzo in stile A1 come `"A1:F10"`.
- `Range.toImage(ImageOrPrintOptions options)` — rende l'intervallo in byte di immagine. Passare `null` usa le opzioni di rendering predefinite; esistono overload per un controllo più fine sull'output.
- `new ByteArrayInputStream(byte[] buffer)` — avvolge i byte dell'immagine renderizzata in un `ByteArrayInputStream` che può essere passato a `PictureCollection.add`.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, InputStream stream)` — aggiunge l'immagine ancorata alla riga e colonna indicate, questa volta passando il `ByteArrayInputStream` prodotto dal rendering.
Il codice seguente crea una cartella di lavoro, costruisce un `Range` per `A1:F10`, lo rende in byte di immagine tramite `Range.toImage(null)`, avvolge i byte in un `ByteArrayInputStream`, aggiunge l'immagine ancorata alla riga 10 colonna 6 e salva la cartella di lavoro.

```java
import java.io.ByteArrayInputStream;
import com.aspose.cells.PictureCollection;
import com.aspose.cells.Range;
import com.aspose.cells.SaveFormat;
import com.aspose.cells.Workbook;
import com.aspose.cells.Worksheet;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("CameraDemo");
// Camera statica: crea Range, esegui il rendering in byte, avvolgi in ByteArrayInputStream, aggiungi come immagine
Range range = worksheet.getCells().createRange("A1:F10");
PictureCollection pictures = worksheet.getPictures();
pictures.add(10, 6, new ByteArrayInputStream(range.toImage(null)));
workbook.save("output_static.xlsx", SaveFormat.XLSX);
```

## Choosing Between Dynamic and Static
- **Camera dinamica:** si aggiorna a ogni ricalcolo, supporta l'esportazione in HTML e PDF dopo `updateSelectedValue()`, e conserva il comportamento di collegamento live per tutta la durata del file.
- **Camera statica:** un rendering una tantum che non si aggiorna mai, utile quando si desidera un'istantanea visiva fissa incorporata al momento della build anziché un mirror live dei dati.
Aspose.Cells supporta sia una Camera con auto-refresh dinamico costruita su `Picture.Formula` più `updateSelectedValue()` sia una Camera one-shot statica costruita su `Range.toImage` più un `ByteArrayInputStream`. Scegli l'approccio dinamico quando il tuo output deve rimanere sincronizzato con le celle di origine, e scegli l'approccio statico quando hai bisogno solo di un'istantanea visiva fissa al momento della build.

## Related Articles
- [Convertire Sparkline in immagine e HTML in Aspose.Cells for Java](/cells/it/java/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="java" >}}