---
title: Fotocamera Excel in Aspose.Cells for Python via .NET
linktitle: Fotocamera Excel
description: Scopri come utilizzare la Fotocamera Excel in Aspose.Cells for Python via .NET per creare un'immagine dinamica collegata a un intervallo di celle che si aggiorna con i dati di origine e preserva tutta la formattazione della sorgente.
keywords: Aspose.Cells, Python, Fotocamera Excel, immagine dinamica, immagine collegata, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, BytesIO
type: docs
weight: 90
url: /it/python-net/excel-camera/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

La Fotocamera Excel è un oggetto del foglio di lavoro che esegue il rendering di un'immagine in tempo reale di un intervallo di celle e fluttua sul livello di disegno come un'immagine ordinaria. Aspose.Cells supporta due modalità di creazione: un'immagine dinamica che si aggiorna automaticamente ogni volta che cambiano i dati di origine e un'immagine statica che acquisisce una singola istantanea di un intervallo. Questo articolo illustra entrambi gli approcci, consentendo di scegliere quello più adatto al layout.

## Che cos'è la Fotocamera Excel?
Essenzialmente, la Fotocamera Excel è un oggetto `Picture` ancorato a una riga e a una colonna specifiche sul livello di disegno del foglio di lavoro. A differenza di un'immagine convenzionale inserita, la Fotocamera Excel è collegata a un intervallo di origine tramite una formula in stile A1, ad esempio `"A1:F10"`. Ogni volta che una cella dell'intervallo viene modificata, l'immagine della Fotocamera Excel viene aggiornata automaticamente per riflettere il nuovo contenuto. La Fotocamera Excel preserva l'intera formattazione dell'area di origine — bordi, colori di sfondo, tipi di carattere e formati numerici — in modo che tutto ciò che è visibile nelle celle appaia anche nell'immagine della Fotocamera Excel. La Fotocamera Excel è particolarmente utile per cruscotti, riepiloghi, pannelli laterali e layout di report nei quali si desidera un'anteprima visibile di un'area remota senza dover scorrere o ripetere i dati. Due aspetti richiedono attenzione: è necessario chiamare `update_selected_value()` prima di salvare la cartella di lavoro e il file verrà esportato in HTML o PDF, poiché questi formati si basano sui dati dell'immagine incorporata anziché su un ricalcolo in tempo reale.

## Metodo 1 — Aggiungere un'immagine dinamica tramite la Fotocamera Excel
La Fotocamera dinamica è l'approccio più comune ed è quello più vicino allo strumento Fotocamera integrato in Excel. Funziona aggiungendo un'immagine senza contenuto iniziale, quindi assegnandole una `formula` che fa riferimento all'intervallo di origine. Dopo l'assegnazione della formula, la chiamata a `update_selected_value()` aggiorna i dati dell'immagine incorporata, sincronizzandoli con il contenuto delle celle a cui corrisponde. La Fotocamera Excel non è implementata tramite una classe dedicata, ma è interamente basata sul tipo standard `Picture`.
Le API principali sono:
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, Stream stream)` — aggiunge un'immagine ancorata alla riga e alla colonna specificate. Il passaggio di `None` al parametro `stream` crea un'immagine vuota che funge da segnaposto per una Fotocamera dinamica. Il metodo restituisce l'indice della nuova immagine.
- `worksheet.pictures[index]` — accesso tramite indicizzatore per recuperare un oggetto `Picture` specifico dalla raccolta.
- `picture.formula` — una proprietà string (get/set) che contiene il riferimento in stile A1 all'intervallo di origine da cui la Fotocamera Excel deriva la propria immagine, ad esempio `"A1:F10"`.
- `picture.update_selected_value()` — un metodo void che aggiorna i dati dell'immagine incorporata dalle celle a cui `formula` fa riferimento.

{{% alert color="primary" %}}
`update_selected_value()` DEVE essere chiamato prima del salvataggio quando l'output è HTML o PDF; in caso contrario, il file esportato non conterrà i dati dell'immagine e la Fotocamera Excel apparirà vuota nel risultato del rendering.
Il codice seguente crea una cartella di lavoro, aggiunge un'immagine vuota ancorata alla riga 10 e alla colonna 6, la collega all'intervallo di origine `A1:F10` tramite la proprietà `formula`, aggiorna i dati dell'immagine incorporata e salva la cartella di lavoro.
{{% /alert %}}

```python
from aspose.cells import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "CameraDemo"
# Fotocamera dinamica: aggiungi un'immagine vuota, collegala tramite formula a A1:F10, quindi aggiorna
pictures = worksheet.pictures
index = pictures.add(10, 6, None)
pictures[index].formula = "A1:F10"
pictures[index].update_selected_value()
workbook.save("output_dynamic.xlsx", SaveFormat.XLSX)
```

## Metodo 2 — Aggiungere un'immagine statica tramite la Fotocamera Excel
La Fotocamera statica è essenzialmente un'anteprima di un intervallo di celle sottoposta a rendering una sola volta. Invece di mantenere un collegamento in tempo reale, l'intervallo viene sottoposto a rendering una sola volta per ottenere i byte dell'immagine; questi byte vengono quindi incapsulati in un `BytesIO` e aggiunti come immagine normale. Il contenuto dell'immagine rimane quindi fissato al momento della creazione e non si aggiorna automaticamente quando cambiano le celle di origine.
Le API principali sono:
- `Cells.create_range(string address)` — costruisce un oggetto `Range` da un indirizzo in stile A1, come `"A1:F10"`.
- `Range.to_image(ImageOrPrintOptions options)` — esegue il rendering dell'intervallo producendo byte di immagine. Il passaggio di `None` utilizza le opzioni di rendering predefinite; sono disponibili sovraccarichi per un controllo più preciso dell'output.
- `BytesIO(byte[] buffer)` — incapsula i byte dell'immagine renderizzata in un `BytesIO` che può essere fornito a `PictureCollection.add`.
- `PictureCollection.add(int upperLeftRow, int upperLeftColumn, Stream stream)` — aggiunge l'immagine ancorata alla riga e alla colonna specificate, questa volta passando il `BytesIO` prodotto dal rendering.
Il codice seguente crea una cartella di lavoro, costruisce un oggetto `Range` per `A1:F10`, ne esegue il rendering per ottenere i byte dell'immagine tramite `Range.to_image(null)`, li incapsula in un `BytesIO`, aggiunge l'immagine ancorata alla riga 10 e alla colonna 6 e salva la cartella di lavoro.

```python
from io import BytesIO
from aspose.cells import Workbook, SaveFormat
workbook = Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "CameraDemo"
# Camera statica: crea Range, renditizza in byte, avvolgi in BytesIO, aggiungi come immagine
range_ = worksheet.cells.create_range("A1:F10")
pictures = worksheet.pictures
pictures.add(10, 6, BytesIO(range_.to_image(None)))
workbook.save("output_static.xlsx", SaveFormat.XLSX)
```

## Scelta tra la modalità dinamica e quella statica
- **Fotocamera dinamica:** si aggiorna a ogni ricalcolo, supporta l'esportazione in HTML e PDF dopo `update_selected_value()` e preserva il comportamento di collegamento in tempo reale per l'intero ciclo di vita del file.
- **Fotocamera statica:** è una rappresentazione generata una sola volta che non si aggiorna mai; è utile quando si desidera un'istantanea visiva fissa incorporata al momento della compilazione, anziché una replica dei dati sincronizzata in tempo reale.
Aspose.Cells supporta sia una Fotocamera dinamica con aggiornamento automatico, basata su `picture.formula` e `update_selected_value()`, sia una Fotocamera statica generata una sola volta, basata su `Range.to_image` e `BytesIO`. Utilizzare l'approccio dinamico quando l'output deve restare sincronizzato con le celle di origine; l'approccio statico è invece indicato quando è sufficiente un'istantanea visiva fissa al momento della compilazione.

{{< app/cells/assistant language="python-net" >}}