---
title: Fotocamera di Excel in Aspose.Cells for Python via Java
linktitle: Fotocamera di Excel
description: Scopri come utilizzare la Fotocamera di Excel in Aspose.Cells for Python via Java per creare un'immagine dinamica collegata a un intervallo di celle che si aggiorna con i dati di origine e mantiene tutta la formattazione dell'origine.
keywords: Aspose.Cells, Python via Java, Fotocamera di Excel, immagine dinamica, immagine collegata, Picture.formula, updateSelectedValue, createRange, toImage, array byte[]
type: docs
weight: 90
url: /it/python-java/excel-camera/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Che cos'è la Fotocamera di Excel?
La Fotocamera di Excel è essenzialmente un oggetto immagine ancorato a una riga e una colonna specifiche sul livello di disegno del foglio di lavoro. A differenza di un'immagine normale inserita, la Fotocamera è collegata a un intervallo di origine tramite una formula in stile A1 come `"A1:F10"`. Ogni volta che una cella all'interno di tale intervallo cambia, l'immagine della Fotocamera viene aggiornata automaticamente per riflettere il nuovo contenuto. La Fotocamera mantiene l'intera formattazione dell'area di origine — bordi, colori di sfondo, caratteri e formati numerici — quindi tutto ciò che è visibile all'interno delle celle appare anche nell'immagine della Fotocamera. Ciò rende la Fotocamera particolarmente utile per dashboard, riepiloghi, pannelli laterali e layout di report in cui si desidera un'anteprima visibile di un'area remota senza scorrere o ripetere i dati. Si applicano due avvertenze: è necessario chiamare `updateSelectedValue()` prima di salvare la cartella di lavoro, e il file verrà esportato in HTML o PDF, perché tali formati si basano sui dati immagine incorporati anziché su un ricalcolo live.

## Metodo 1 — Aggiungere un'immagine Fotocamera dinamica
La Fotocamera dinamica è l'approccio più comune ed è il più vicino allo strumento Fotocamera integrato di Excel. Funziona aggiungendo un'immagine senza contenuto iniziale, quindi assegnandole una formula che fa riferimento all'intervallo di origine. Dopo l'assegnazione della formula, chiamando `updateSelectedValue()` si aggiornano i dati immagine incorporati, in modo che siano sincronizzati con le celle che rispecchia. La Fotocamera non è implementata tramite una classe dedicata — è costruita interamente sul tipo standard `Picture`.
Le API chiave sono:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, input)` — aggiunge un'immagine ancorata alla riga e alla colonna specificate. Passare `None` per il parametro `stream` crea un'immagine vuota che funge da segnaposto per una Fotocamera dinamica. Il metodo restituisce l'indice della nuova immagine.
- `worksheet.getPictures().get(index)` — accessor per recuperare uno specifico `Picture` dalla raccolta.
- `Picture.getFormula()` / `Picture.setFormula()` — ottiene/imposta il riferimento in stile A1 all'intervallo di origine che la Fotocamera rispecchia, come `"A1:F10"`.
- `Picture.updateSelectedValue()` — un metodo void che aggiorna i dati immagine incorporati dalle celle a cui fa riferimento la formula.

{{% alert color="primary" %}}
`updateSelectedValue()` DEVE essere chiamato prima del salvataggio quando l'output è HTML o PDF; altrimenti il file esportato non conterrà i dati immagine e la Fotocamera apparirà vuota nell'output renderizzato.
{{% /alert %}}

Il codice seguente crea una cartella di lavoro, aggiunge un'immagine vuota ancorata alla riga 10 colonna 6, la collega all'intervallo di origine `A1:F10` tramite il metodo `setFormula`, aggiorna i dati immagine incorporati e salva la cartella di lavoro.

```python
import jpype
import jpype.imports
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("CameraDemo")
# Camera Dinamica: aggiunge un'immagine vuota, la collega tramite Formula a A1:F10, poi aggiorna
pictures = worksheet.getPictures()
index = pictures.add(10, 6, None)
pictures.get(index).setFormula("A1:F10")
pictures.get(index).updateSelectedValue()
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX)
```

## Metodo 2 — Aggiungere un'immagine Fotocamera statica
La Fotocamera statica è essenzialmente un'anteprima renderizzata una tantum di un intervallo di celle. Invece di mantenere un collegamento live, si esegue il rendering dell'intervallo in byte di immagine una volta, si avvolgono tali byte in un array `byte[]` e li si aggiungono come un'immagine normale. Il contenuto dell'immagine è quindi fissato al momento della creazione e non si aggiorna automaticamente quando cambiano le celle di origine.
Le API chiave sono:
- `Cells.createRange(String address)` — crea un oggetto `Range` da un indirizzo in stile A1 come `"A1:F10"`.
- `Range.toImage(ImageOrPrintOptions options)` — esegue il rendering dell'intervallo in byte di immagine. Passare `None` usa le opzioni di rendering predefinite; esistono overload per un controllo più fine sull'output.
- `byte[] array(byte[] buffer)` — avvolge i byte dell'immagine renderizzata in un array `byte[]` che può essere passato a `PictureCollection.add`.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, input)` — aggiunge l'immagine ancorata alla riga e alla colonna specificate, questa volta passando l'array `byte[]` prodotto dal rendering.
Il codice seguente crea una cartella di lavoro, costruisce un `Range` per `A1:F10`, lo renderizza in byte di immagine tramite `Range.toImage(None)`, avvolge i byte in un array `byte[]`, aggiunge l'immagine ancorata alla riga 10 colonna 6 e salva la cartella di lavoro.

## Scegliere tra Dinamica e Statica
- **Fotocamera dinamica:** si aggiorna ad ogni ricalcolo, supporta l'esportazione in HTML e PDF dopo `updateSelectedValue()` e mantiene il comportamento di collegamento live per tutta la durata del file.
- **Fotocamera statica:** un rendering una tantum che non si aggiorna mai, utile quando si desidera un'istantanea visiva fissa incorporata al momento della build anziché un mirror live dei dati.
Aspose.Cells for Python via Java supporta sia una Fotocamera dinamica ad aggiornamento automatico basata su `setFormula` più `updateSelectedValue()`, sia una Fotocamera statica one-shot basata su `toImage` più un array `byte[]`. Scegli l'approccio dinamico quando il tuo output deve rimanere sincronizzato con le celle di origine, e scegli l'approccio statico quando hai bisogno solo di un'istantanea visiva fissa al momento della build.

```python
import jpype
import jpype.imports
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("CameraDemo")
# Static Camera: build Range, render to bytes, wrap in ByteArrayInputStream, add as picture
range_ = worksheet.getCells().createRange("A1:F10")
image_bytes = range_.toImage(None)
pictures = worksheet.getPictures()
pictures.add(10, 6, jpype.JArray(jpype.JByte)(image_bytes))
workbook.save("output_static.xlsx", SaveFormat.XLSX)
```

{{< app/cells/assistant language="python" >}}