---
title: Convertire Sparkline in Immagine e HTML in Aspose.Cells for Python via .NET
linktitle: Convert Sparkline to Image and HTML
description: Scopri come renderizzare le sparkline di Aspose.Cells in immagini standalone per l'incorporamento nelle celle ed esportare fogli di lavoro ricchi di sparkline in HTML utilizzando HtmlSaveOptions in Python via .NET.
keywords: Aspose.Cells, Python via .NET, sparkline, sparkline.to_image, cell.embedded_image, HtmlSaveOptions, render sparkline, convert sparkline to image, export sparkline to HTML
type: docs
weight: 120
url: /it/python-net/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Le sparkline sono grafici in miniatura posizionati all'interno delle celle del foglio di lavoro. Aspose.Cells consente di estrarre ogni sparkline come immagine standalone (da incorporare in un'altra cella o in un report esterno) e anche di esportare l'intero foglio di lavoro ricco di sparkline in HTML per la distribuzione basata su browser. La proprietà `cell.embedded_image` utilizzata in questo articolo è disponibile in **Aspose.Cells 26.5 e versioni successive**.
{{% /alert %}}

## **Introduzione**

Le sparkline rappresentano un modo compatto per visualizzare i trend direttamente all'interno di un foglio di lavoro. Mentre gli utenti di Excel le vedono sul posto, molti scenari reali richiedono che una sparkline lasci la cella — ad esempio, per essere incorporata in una cella diversa come immagine statica, allegata a un'email automatizzata, o renderizzata come parte di un report HTML pubblicato sul web.

Aspose.Cells supporta entrambe queste operazioni. Il metodo `sparkline.to_image` renderizza una singola sparkline in uno stream, e i byte risultanti possono essere assegnati a `cell.embedded_image` in modo che l'immagine venga memorizzata all'interno di una singola cella della cartella di lavoro. Separatamente, `HtmlSaveOptions` consente di convertire l'intera cartella di lavoro — sparkline incluse — in un file HTML autonomo. Questo articolo illustra entrambi i flussi di lavoro end to end.

## **Flusso di lavoro 1 — Renderizzare le Sparkline in Immagini e Incorporarle nelle Celle**

In questo flusso di lavoro creerai un foglio di lavoro che contiene un piccolo intervallo di valori sorgente, collegherai tre diversi gruppi di sparkline (Linea, Colonna e In pila/Win-Loss) a tale intervallo, renderizzerai ciascun gruppo come PNG e scriverai i byte PNG nelle celle adiacenti come immagini incorporate. Il risultato finale è un singolo file `.xlsx` che contiene sia le sparkline attive sia le loro controparti immagine renderizzate.

### **Istruzioni Passo per Passo**

1. Definire una directory di lavoro e assicurarsi che esista sul disco.
2. Creare una nuova `Workbook` e ottenere un riferimento al primo `Worksheet`.
3. Popolare le celle da `A1` a `E1` con cinque valori numerici di esempio (ad esempio, vendite giornaliere o letture di temperatura).
4. Aggiungere tre oggetti `SparklineGroup` al foglio di lavoro chiamando `worksheet.sparkline_groups.add(...)`:
   - Un gruppo `SparklineType.LINE` ancorato in `F1`, con intervallo dati `A1:E1`.
   - Un gruppo `SparklineType.COLUMN` ancorato in `G1`, con intervallo dati `A1:E1`.
   - Un gruppo `SparklineType.STACKED` (win/loss) ancorato in `H1`, con intervallo dati `A1:E1`.
5. Creare un'istanza di `ImageOrPrintOptions` e impostare il suo `image_type` su `ImageType.PNG` in modo che ogni sparkline venga renderizzata come PNG trasparente.
6. Per ciascuno dei tre gruppi, renderizzare la sua singola sparkline utilizzando `group.sparklines[0].to_image(memory_stream, image_options)`, convertire lo stream `BytesIO` in un oggetto `bytes` e assegnare l'array rispettivamente a `worksheet.cells["F2"].embedded_image`, `worksheet.cells["G2"].embedded_image` e `worksheet.cells["H2"].embedded_image`.
7. Salvare la cartella di lavoro come `output_with_sparklines.xlsx`.

```python
import aspose.cells as ac

# Crea una nuova cartella di lavoro e accedi al primo foglio di lavoro
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]

# Popola dati di esempio nelle celle A1:E1
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# Aggiunge un gruppo di sparkline a Linea ancorato a F1 (colonna 5, riga 0)
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)

# Aggiunge un gruppo di sparkline a Colonna ancorato a G1 (colonna 6, riga 0)
column_area = ac.CellArea()
column_area.start_column = 6
column_area.end_column = 6
column_area.start_row = 0
column_area.end_row = 0
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)

# Aggiunge un gruppo di sparkline Win/Loss (In pila) ancorato a H1 (colonna 7, riga 0)
stacked_area = ac.CellArea()
stacked_area.start_column = 7
stacked_area.end_column = 7
stacked_area.start_row = 0
stacked_area.end_row = 0
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)

# Configura le opzioni immagine per l'output PNG
image_options = ac.ImageOrPrintOptions()
image_options.image_type = ac.ImageType.PNG

# Converte la sparkline a Linea in immagine e la incorpora nella cella F2
line_sp = worksheet.sparkline_groups[line_idx].sparklines[0]
ms = ac.MemoryStream()
line_sp.to_image(ms, image_options)
worksheet.cells["F2"].embedded_image = ms.to_array()

# Converte la sparkline a Colonna in immagine e la incorpora nella cella G2
column_sp = worksheet.sparkline_groups[column_idx].sparklines[0]
ms = ac.MemoryStream()
column_sp.to_image(ms, image_options)
worksheet.cells["G2"].embedded_image = ms.to_array()

# Converte la sparkline Win/Loss in immagine e la incorpora nella cella H2
stacked_sp = worksheet.sparkline_groups[stacked_idx].sparklines[0]
ms = ac.MemoryStream()
stacked_sp.to_image(ms, image_options)
worksheet.cells["H2"].embedded_image = ms.to_array()

# Salva la cartella di lavoro su disco
workbook.save("output_with_sparklines.xlsx")
```

Il codice sopra produce una cartella di lavoro in cui ogni rappresentazione visiva di una sparkline è duplicata in due forme: la sparkline nativa attiva ancorata alla riga 1, e un'immagine PNG statica incorporata direttamente in una cella adiacente sulla riga 2. Poiché le immagini vivono all'interno del file stesso, la cartella di lavoro rimane un singolo artefatto autonomo che può essere inviato via email o archiviato senza rompere i riferimenti delle immagini incorporate. Renderizza ogni gruppo di sparkline come PNG, converti lo stream `BytesIO` in un oggetto `bytes` e assegna i byte alla proprietà `embedded_image` della cella di destinazione — l'assegnazione è ciò che rende l'immagine parte del contenuto memorizzato della cella.

{{% alert color="primary" %}}
Poiché ogni gruppo di sparkline è ancorato a una singola cella, è possibile accedervi tramite l'indicizzatore `group.sparklines[0]` invece di enumerare con un ciclo `for`. Questo mantiene il codice di rendering breve e corrisponde al tipico schema "una sparkline per cella di ancoraggio". La memorizzazione dei byte dell'immagine tramite `cell.embedded_image` richiede Aspose.Cells 26.5 o versioni successive.
{{% /alert %}}

## **Flusso di lavoro 2 — Esportare il Foglio di Lavoro con Sparkline in HTML**

Una volta che la cartella di lavoro contiene sparkline attive (e opzionalmente controparti immagine incorporate), l'intero foglio di lavoro può essere pubblicato sul web salvandolo come HTML. La classe `HtmlSaveOptions` espone le opzioni necessarie per controllare questa esportazione; in questo flusso di lavoro riutilizzerai il file `output_with_sparklines.xlsx` prodotto dal Flusso di lavoro 1 e lo convertirai in un documento HTML pulito e a pagina singola.

### **Istruzioni Passo per Passo**

1. Assicurarsi che il file `output_with_sparklines.xlsx` prodotto dal Flusso di lavoro 1 sia disponibile sul disco nella directory di lavoro.
2. Caricare quel file in una nuova istanza di `Workbook`.
3. Istanziare `HtmlSaveOptions` e impostare la sua proprietà `export_active_worksheet_only` su `True` in modo che il file HTML risultante contenga solo il foglio di lavoro attivo anziché l'intera cartella di lavoro.
4. Chiamare `workbook.save("sparklines.html", html_options)` per scrivere l'output HTML sul disco.

```python
import aspose.cells as ac

workbook = ac.Workbook("output_with_sparklines.xlsx")
html_options = ac.HtmlSaveOptions()
html_options.export_active_worksheet_only = True
workbook.save("sparklines.html", html_options)
```

Il codice sopra prende la cartella di lavoro ricca di sparkline dal Flusso di lavoro 1 e la trasforma in un file HTML portatile. Le sparkline vengono preservate come rendering SVG o PNG inline all'interno dell'HTML generato, a seconda della modalità di esportazione, così gli utenti finali possono visualizzare i trend in qualsiasi browser moderno senza bisogno di Excel installato. Impostando `export_active_worksheet_only` su `True`, si evita di pubblicare accidentalmente fogli nascosti o dati ausiliari — viene esportato solo il foglio di lavoro attualmente visibile all'utente.

{{% alert color="primary" %}}
La classe `HtmlSaveOptions` offre proprietà aggiuntive per la regolazione fine dell'output, come `export_hidden_worksheet`, `export_images_as_base64` e `encoding`. Regolale secondo necessità per il tuo target di distribuzione.
{{% /alert %}}

## **Riepilogo delle API**

I flussi di lavoro sopra si basano su un piccolo insieme di API di Aspose.Cells che lavorano insieme.

- `SparklineGroup` e l'accessore alla collezione `worksheet.sparkline_groups` sono utilizzati per dichiarare il tipo (Linea, Colonna, In pila), l'intervallo dati e la cella di ancoraggio per ciascun gruppo di sparkline. In questo articolo ciascun gruppo è ancorato a una singola cella, quindi il gruppo viene raggiunto tramite `worksheet.sparkline_groups[i]`.
- `Sparkline` e l'indicizzatore `group.sparklines[0]` restituiscono la singola sparkline all'interno di un gruppo. Poiché ogni gruppo nell'esempio contiene esattamente una sparkline, non è richiesto alcun ciclo `for`.
- `sparkline.to_image(Stream, ImageOrPrintOptions)` è il metodo di rendering che scrive un'immagine della sparkline in uno stream fornito. Il metodo restituisce `None`; i byte si leggono dallo stream dopo la chiamata.
- `cell.embedded_image` è una proprietà `bytes` che memorizza un'immagine all'interno di una singola cella. È disponibile in **Aspose.Cells 26.5 e versioni successive** ed è il modo consigliato per riportare una sparkline renderizzata da `to_image` nella stessa cartella di lavoro.
- `html_save_options.export_active_worksheet_only` (un `bool`) limita l'esportazione HTML al foglio di lavoro attivo. È una delle proprietà più comunemente utilizzate di `HtmlSaveOptions` quando si generano report a pagina singola.
- `image_or_print_options.image_type` vive nel namespace `aspose.cells.drawing` e seleziona il formato immagine (ad esempio, `ImageType.PNG`) utilizzato durante il rendering con `to_image` e durante la stampa dei fogli di lavoro in immagini.

## **Articoli Correlati**

- [Sparklines in Aspose.Cells for Python via .NET](/cells/it/python-net/sparkline/)
- [Inserimento di un'Immagine in una Cella](/cells/it/python-net/inserting-an-image-into-a-cell/)
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for Python via .NET](/cells/it/python-net/SmartMarker-Single-Cell-Array-Rendering/)

{{< app/cells/assistant language="python" >}}