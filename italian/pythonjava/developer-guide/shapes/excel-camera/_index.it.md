---
title: Fotocamera Excel in Aspose.Cells for Python via Java
linktitle: Fotocamera Excel
description: Scopri come utilizzare la Fotocamera Excel in Aspose.Cells for Python via Java per creare un'immagine dinamica collegata a un intervallo di celle che si aggiorna con i dati di origine e conserva tutta la formattazione originale.
keywords: Aspose.Cells, Python via Java, Fotocamera Excel, immagine dinamica, immagine collegata, Picture.formula, updateSelectedValue, createRange, toImage, byte[] array
type: docs
weight: 90
url: /it/python-java/excel-camera/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

La Fotocamera Excel è un oggetto del foglio di lavoro che visualizza un'immagine in tempo reale di un intervallo di celle e galleggia sul livello di disegno come un'immagine ordinaria. Aspose.Cells for Python via Java supporta due modalità di creazione: un'immagine dinamica che si aggiorna automaticamente ogni volta che i dati di origine cambiano e un'immagine statica che cattura un'istantanea unica di un intervallo. Questo articolo illustra entrambi gli approcci in modo che tu possa scegliere quello più adatto al tuo layout.

## Cos'è la Fotocamera Excel?
La Fotocamera Excel è essenzialmente un oggetto immagine ancorato a una riga e colonna specifiche sul livello di disegno del foglio di lavoro. A differenza di un'immagine inserita regolarmente, la Fotocamera è collegata a un intervallo di origine tramite una formula in stile A1, ad esempio `"A1:F10"`. Ogni volta che una cella all'interno di quell'intervallo viene modificata, l'immagine della Fotocamera viene aggiornata automaticamente per riflettere il nuovo contenuto. La Fotocamera conserva tutta la formattazione dell'area di origine — bordi, colori di sfondo, caratteri e formati numerici — in modo che tutto ciò che è visibile nelle celle appaia anche nell'immagine della Fotocamera. Questo la rende particolarmente utile per dashboard, riepiloghi, pannelli laterali e layout di report in cui si desidera un'anteprima visibile di un'area remota senza scorrere o duplicare i dati. Due avvertenze importanti: è necessario chiamare `updateSelectedValue()` prima di salvare la cartella di lavoro, e il file deve essere esportato in HTML o PDF, poiché tali formati si basano sui dati immagine incorporati anziché su un ricalcolo live.

## Metodo 1 — Aggiungere un'immagine dinamica della Fotocamera
L'approccio dinamico è il più comune e corrisponde maggiormente allo strumento Fotocamera integrato di Excel. Funziona aggiungendo un'immagine senza contenuto iniziale, quindi assegnandole una formula che fa riferimento all'intervallo di origine. Dopo aver impostato la formula, la chiamata a `updateSelectedValue()` aggiorna i dati immagine incorporati in modo che siano sincronizzati con le celle corrispondenti. La Fotocamera non è implementata tramite una classe dedicata — è costruita interamente sul tipo standard `Picture`.
Le API chiave sono:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, input)` — aggiunge un'immagine ancorata alla riga e colonna specificate. Passare `None` per il parametro `stream` crea un'immagine vuota che funge da placeholder per una Fotocamera dinamica. Il metodo restituisce l'indice della nuova immagine.
- `worksheet.getPictures().get(index)` — accessor per recuperare una specifica `Picture` dalla collezione.
- `Picture.getFormula()` / `Picture.setFormula()` — ottiene/imposta il riferimento in stile A1 all'intervallo di origine che la Fotocamera replica, ad esempio `"A1:F10"`.
- `Picture.updateSelectedValue()` — metodo void che aggiorna i dati immagine incorporati dalle celle referenziate dalla formula.

{{% alert color="primary" %}}
`updateSelectedValue()` DEVE essere chiamato prima del salvataggio quando l'output è HTML o PDF; altrimenti il file esportato non conterrà i dati dell'immagine e la Fotocamera apparirà vuota nel risultato renderizzato.
Il codice seguente crea una cartella di lavoro, aggiunge un'immagine vuota ancorata alla riga 10 colonna 6, la collega all'intervallo di origine `A1:F10` tramite il metodo `setFormula`, aggiorna i dati immagine incorporati e salva la cartella di lavoro.
{{% /alert %}}

```python
import jpype
import jpype.imports
from asposecells.api import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("CameraDemo")
# Dynamic Camera: add an empty picture, link it via Formula to A1:F10, then refresh
pictures = worksheet.getPictures()
index = pictures.add(10, 6, b"")
pictures.get(index).setFormula("A1:F10")
pictures.get(index).updateSelectedValue()
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX)
```

## Metodo 2 — Aggiungere un'immagine statica della Fotocamera
La Fotocamera statica è essenzialmente un'anteprima renderizzata una sola volta di un intervallo di celle. Invece di mantenere un collegamento live, si renderizza l'intervallo in byte immagine una volta, si avvolgono tali byte in un array `byte[]`, e si aggiungono come immagine regolare. Il contenuto dell'immagine rimane fissato al momento della creazione e non si aggiorna automaticamente quando le celle di origine cambiano.
Le API chiave sono:
- `Cells.createRange(String address)` — costruisce un oggetto `Range` a partire da un indirizzo in stile A1, ad esempio `"A1:F10"`.
- `Range.toImage(ImageOrPrintOptions options)` — renderizza l'intervallo in byte immagine. Passare `None` utilizza le opzioni di rendering predefinite; esistono overload per un controllo più fine sull'output.
- `byte[] array(byte[] buffer)` — avvolge i byte dell'immagine renderizzata in un `byte[] array` che può essere fornito a `PictureCollection.add`.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, input)` — aggiunge l'immagine ancorata alla riga e colonna specificate, questa volta passando il `byte[] array` prodotto dal rendering.
Il codice seguente crea una cartella di lavoro, costruisce un `Range` per `A1:F10`, lo renderizza in byte immagine tramite `Range.toImage(None)`, avvolge i byte in un `byte[] array`, aggiunge l'immagine ancorata alla riga 10 colonna 6 e salva la cartella di lavoro.

```python
import jpype
import jpype.imports
from asposecells.api import Workbook, SaveFormat
from java.io import ByteArrayInputStream
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("CameraDemo")
# Static Camera: build Range, render to bytes, wrap in ByteArrayInputStream, add as picture
range_ = worksheet.getCells().createRange("A1:F10")
image_bytes = range_.toImage(None)
pictures = worksheet.getPictures()
pictures.add(10, 6, ByteArrayInputStream(image_bytes))
workbook.save("output_static.xlsx", SaveFormat.XLSX)
```

## Scegliere tra Dinamico e Statico
- **Fotocamera dinamica:** si aggiorna ad ogni ricalcolo, supporta l'esportazione in HTML e PDF dopo `updateSelectedValue()`, e conserva il comportamento di collegamento live per tutta la durata del file.
- **Fotocamera statica:** un rendering unico che non si aggiorna mai, utile quando si desidera un'istantanea visiva fissa incorporata al momento della generazione anziché uno specchio live dei dati.

Aspose.Cells for Python via Java supporta sia una Fotocamera dinamica, auto-aggiornante, basata su `setFormula` più `updateSelectedValue()`, sia una Fotocamera statica, a singola emissione, basata su `toImage` più un `byte[] array`. Scegli l'approccio dinamico quando l'output deve rimanere sincronizzato con le celle di origine, e scegli l'approccio statico quando è sufficiente un'istantanea visiva fissa al momento della costruzione.

{{< app/cells/assistant language="python" >}}