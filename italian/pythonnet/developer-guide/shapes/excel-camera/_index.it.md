---
title: Excel Camera in Aspose.Cells for Python via .NET
linktitle: Excel Camera
description: Scopri come utilizzare Excel Camera in Aspose.Cells for Python via .NET per creare un'immagine dinamica collegata a un intervallo di celle che si aggiorna con i dati di origine e conserva tutta la formattazione sorgente.
keywords: Aspose.Cells, Python, Excel Camera, dynamic picture, linked picture, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, BytesIO
type: docs
weight: 90
url: /it/python-net/excel-camera/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel Camera è un oggetto del foglio di lavoro che esegue il rendering di un'immagine live di un intervallo di celle e fluttua sul livello di disegno come un'immagine ordinaria. Aspose.Cells supporta due modalità di creazione: un'immagine dinamica che si aggiorna automaticamente ogni volta che i dati di origine cambiano e un'immagine statica che cattura un'istantuna una tantum di un intervallo. Questo articolo illustra entrambi gli approcci in modo che tu possa scegliere quello più adatto al tuo layout.

## Che cos'è Excel Camera?
Excel Camera è essenzialmente un oggetto immagine ancorato a una riga e colonna specifica sul livello di disegno del foglio di lavoro. A differenza di un'immagine regolarmente inserita, la Camera è collegata a un intervallo sorgente tramite una formula in stile A1 come `"A1:F10"`. Ogni volta che una cella all'interno di quell'intervallo cambia, l'immagine della Camera viene aggiornata automaticamente per riflettere il nuovo contenuto. La Camera conserva l'intera formattazione dell'area sorgente — bordi, colori di sfondo, caratteri e formati numerici — così tutto ciò che è visibile all'interno delle celle appare anche all'interno dell'immagine della Camera. Ciò rende la Camera particolarmente utile per dashboard, riepiloghi, pannelli laterali e layout di report in cui si desidera un'anteprima visibile di un'area remota senza scorrere o ripetere i dati. Si applicano due avvertenze: è necessario chiamare `update_selected_value()` prima di salvare la cartella di lavoro e il file verrà esportato in HTML o PDF, perché tali formati si basano sui dati immagine incorporati anziché su un ricalcolo live.

## Metodo 1 — Aggiungere un'immagine Camera dinamica
La Camera dinamica è l'approccio più comune ed è la corrispondenza più vicina allo strumento Camera integrato di Excel. Funziona aggiungendo un'immagine senza contenuto iniziale e poi assegnandole una `formula` che fa riferimento all'intervallo sorgente. Dopo che la formula è stata assegnata, la chiamata a `update_selected_value()` aggiorna i dati immagine incorporati in modo che siano sincronizzati con le celle che rispecchiano. La Camera non è implementata tramite una classe dedicata — è costruita interamente sul tipo `Picture` standard.
Le API chiave sono:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, Stream stream)` — aggiunge un'immagine ancorata alla riga e colonna specificate. Passare `None` per il parametro `stream` crea un'immagine vuota che funge da segnaposto per una Camera dinamica. Il metodo restituisce l'indice della nuova immagine.
- `worksheet.pictures[index]` — accesso tramite indicizzatore per recuperare una specifica `Picture` dalla raccolta.
- `picture.formula` — una proprietà stringa (get/set) che contiene il riferimento in stile A1 all'intervallo sorgente che la Camera rispecchia, come `"A1:F10"`.
- `picture.update_selected_value()` — un metodo void che aggiorna i dati immagine incorporati dalle celle a cui fa riferimento `formula`.

{{% alert color="primary" %}}
`update_selected_value()` DEVE essere chiamato prima del salvataggio quando l'output è HTML o PDF; altrimenti il file esportato non conterrà i dati immagine e la Camera apparirà vuota nell'output renderizzato.
{{% /alert %}}

Il seguente codice crea una cartella di lavoro, aggiunge un'immagine vuota ancorata alla riga 10 colonna 6, la collega all'intervallo sorgente `A1:F10` tramite la proprietà `formula`, aggiorna i dati immagine incorporati e salva la cartella di lavoro.

```python
from aspose.cells import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "CameraDemo"
# Camera Dinamica: aggiungi un'immagine vuota, collegalo tramite formula a A1:F10, poi aggiorna
pictures = worksheet.pictures
index = pictures.add(10, 6, None)
pictures[index].formula = "A1:F10"
pictures[index].update_selected_value()
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX)
```

## Metodo 2 — Aggiungere un'immagine Camera statica
La Camera statica è essenzialmente un'anteprima renderizzata una tantum di un intervallo di celle. Invece di mantenere un collegamento live, si renderizza l'intervallo in byte immagine una volta, si avvolgono tali byte in un `BytesIO` e li si aggiunge come immagine regolare. Il contenuto dell'immagine viene quindi fissato al momento della creazione e non si aggiorna automaticamente quando le celle sorgente cambiano.
Le API chiave sono:
- `Cells.create_range(string address)` — costruisce un oggetto `Range` da un indirizzo in stile A1 come `"A1:F10"`.
- `Range.to_image(ImageOrPrintOptions options)` — renderizza l'intervallo in byte immagine. Passare `None` utilizza le opzioni di rendering predefinite; esistono overload per un controllo più fine sull'output.
- `BytesIO(byte[] buffer)` — avvolge i byte immagine renderizzati in un `BytesIO` che può essere passato a `PictureCollection.add`.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, Stream stream)` — aggiunge l'immagine ancorata alla riga e colonna specificate, questa volta passando il `BytesIO` prodotto dal rendering.
Il seguente codice crea una cartella di lavoro, costruisce un `Range` per `A1:F10`, lo renderizza in byte immagine tramite `Range.to_image(null)`, avvolge i byte in un `BytesIO`, aggiunge l'immagine ancorata alla riga 10 colonna 6 e salva la cartella di lavoro.

```python
from io import BytesIO
from aspose.cells import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "CameraDemo"
# Static Camera: build Range, render to bytes, wrap in BytesIO, add as picture
range_ = worksheet.cells.create_range("A1:F10")
pictures = worksheet.pictures
pictures.add(10, 6, BytesIO(range_.to_image(None)))
workbook.save("output_static.xlsx", SaveFormat.XLSX)
```

## Scegliere tra Dinamico e Statico
- **Camera Dinamica:** si aggiorna ad ogni ricalcolo, supporta l'esportazione in HTML e PDF dopo `update_selected_value()` e conserva il comportamento di collegamento live per tutta la durata del file.
- **Camera Statica:** un rendering una tantum che non si aggiorna mai, utile quando si desidera un'istantanea visiva fissa incorporata al momento della build anziché un mirror live dei dati.
Aspose.Cells supporta sia una Camera dinamica ad auto-aggiornamento costruita su `picture.formula` più `update_selected_value()` sia una Camera statica one-shot costruita su `Range.to_image` più un `BytesIO`. Scegli l'approccio dinamico quando il tuo output deve rimanere sincronizzato con le celle sorgente e scegli l'approccio statico quando hai bisogno solo di un'istantanea visiva fissa al momento della build.

{{< app/cells/assistant language="python-net" >}}