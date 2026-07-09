---
title: Convertire Sparkline in Immagine e HTML in Aspose.Cells for Python via Java
linktitle: Convert Sparkline to Image and HTML
description: Scopri come renderizzare le sparkline di Aspose.Cells in immagini autonome per l'incorporamento nelle celle ed esportare fogli di lavoro ricchi di sparkline in HTML utilizzando HtmlSaveOptions.
keywords: Aspose.Cells, Python via Java, sparkline, Sparkline.toImage, Cell.embeddedImage, HtmlSaveOptions, renderizzare sparkline, convertire sparkline in immagine, esportare sparkline in HTML
type: docs
weight: 120
url: /it/python-java/convert-sparkline-to-image-and-html/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Le sparkline sono grafici in miniatura posizionati all'interno delle celle del foglio di lavoro. Aspose.Cells consente di estrarre ogni sparkline come immagine autonoma (da incorporare in un'altra cella o in un report esterno) e di esportare l'intero foglio di lavoro ricco di sparkline in HTML per la distribuzione basata su browser. La proprietà `Cell.embedded_image` utilizzata in questo articolo è disponibile in **Aspose.Cells 26.5 e versioni successive**.
{{% /alert %}}

## **Introduzione**

Le sparkline rappresentano un modo compatto per visualizzare le tendenze direttamente all'interno di un foglio di lavoro. Mentre gli utenti di Excel le vedono direttamente, molti scenari reali richiedono che una sparkline lasci la cella, ad esempio per essere incorporata in una cella diversa come immagine statica, allegata a un'email automatizzata o renderizzata come parte di un report HTML pubblicato sul web.

Aspose.Cells supporta entrambe queste operazioni. Il metodo `Sparkline.to_image` renderizza una singola sparkline in un flusso e i byte risultanti possono essere assegnati a `Cell.embedded_image`, così l'immagine viene memorizzata all'interno di una singola cella della cartella di lavoro. Separatamente, `HtmlSaveOptions` consente di convertire l'intera cartella di lavoro, comprese le sparkline, in un file HTML autonomo. Questo articolo illustra entrambi i flussi di lavoro end to end.

## **Flusso di lavoro 1 — Renderizzare le Sparkline in Immagini e Incorporarle nelle Celle**

In questo flusso di lavoro creerai un foglio di lavoro che contiene un piccolo intervallo di valori sorgente, aggiungerai tre diversi gruppi di sparkline (Linea, Colonna e In pila/Win-Loss) a quell'intervallo, renderizzerai ciascun gruppo come PNG e scriverai quei byte PNG nelle celle adiacenti come immagini incorporate. Il risultato finale è un singolo file `.xlsx` che contiene sia le sparkline attive sia le loro controparti immagine renderizzate.

### **Istruzioni passo per passo**

1. Definisci una directory di lavoro e assicurati che esista sul disco.
2. Crea una nuova `Workbook` e ottieni un riferimento al primo `Worksheet`.
3. Popola le celle da `A1` a `E1` con cinque valori numerici di esempio (ad esempio, vendite giornaliere o letture di temperatura).
4. Aggiungi tre oggetti `SparklineGroup` al foglio di lavoro chiamando `worksheet.sparkline_groups.add(...)`:
   - Un gruppo `SparklineType.LINE` ancorato a `F1`, con intervallo di dati `A1:E1`.
   - Un gruppo `SparklineType.COLUMN` ancorato a `G1`, con intervallo di dati `A1:E1`.
   - Un gruppo `SparklineType.STACKED` (win/loss) ancorato a `H1`, con intervallo di dati `A1:E1`.
5. Crea un'istanza di `ImageOrPrintOptions` e imposta il suo `image_type` su `ImageType.PNG` in modo che ogni sparkline venga renderizzata come PNG trasparente.
6. Per ciascuno dei tre gruppi, renderizza la sua singola sparkline utilizzando `group.sparklines[0].to_image(byte_array_output_stream, image_options)`, converti il `ByteArrayOutputStream` in un `byte[]` (oppure leggi il suo `to_byte_array()` in `bytes` di Python) e assegna i byte rispettivamente a `worksheet.cells["F2"].embedded_image`, `worksheet.cells["G2"].embedded_image` e `worksheet.cells["H2"].embedded_image`.
7. Salva la cartella di lavoro come `output_with_sparklines.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, ImageType, ImageOrPrintOptions, Sparkline
from jpype import JClass

ByteArrayOutputStream = JClass('java.io.ByteArrayOutputStream')

# Crea una nuova cartella di lavoro e accedi al primo foglio di lavoro
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Popola i dati di esempio nelle celle A1:E1
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# Aggiungi un gruppo di sparkline a linee ancorato a F1 (colonna 5, riga 0)
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, lineArea)

# Aggiungi un gruppo di sparkline a colonne ancorato a G1 (colonna 6, riga 0)
columnArea = CellArea()
columnArea.setStartColumn(6)
columnArea.setEndColumn(6)
columnArea.setStartRow(0)
columnArea.setEndRow(0)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.Column, "A1:E1", False, columnArea)

# Aggiungi un gruppo di sparkline Win/Loss (In pila) ancorato a H1 (colonna 7, riga 0)
stackedArea = CellArea()
stackedArea.setStartColumn(7)
stackedArea.setEndColumn(7)
stackedArea.setStartRow(0)
stackedArea.setEndRow(0)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.Stacked, "A1:E1", False, stackedArea)

# Configura le opzioni dell'immagine per l'output PNG
imageOptions = ImageOrPrintOptions()
imageOptions.setImageType(ImageType.Png)

# Converti lo sparkline a linee in immagine e incorporalo nella cella F2
lineSp = worksheet.getSparklineGroups().get(lineIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
lineSp.toImage(ms, imageOptions)
worksheet.getCells().get("F2").setEmbeddedImage(ms.toByteArray())

# Converti lo sparkline a colonne in immagine e incorporalo nella cella G2
columnSp = worksheet.getSparklineGroups().get(columnIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
columnSp.toImage(ms, imageOptions)
worksheet.getCells().get("G2").setEmbeddedImage(ms.toByteArray())

# Converti lo sparkline Win/Loss in immagine e incorporalo nella cella H2
stackedSp = worksheet.getSparklineGroups().get(stackedIdx).getSparklines().get(0)
ms = ByteArrayOutputStream()
stackedSp.toImage(ms, imageOptions)
worksheet.getCells().get("H2").setEmbeddedImage(ms.toByteArray())

# Salva la cartella di lavoro su disco
workbook.save("output_with_sparklines.xlsx")

jpype.shutdownJVM()
```

Il codice sopra produce una cartella di lavoro in cui ogni rappresentazione visiva di una sparkline è duplicata in due forme: la sparkline nativa attiva ancorata alla riga 1, e un'immagine PNG statica incorporata direttamente in una cella adiacente sulla riga 2. Poiché le immagini risiedono all'interno del file stesso, la cartella di lavoro rimane un singolo artefatto autonomo che può essere inviato via email o archiviato senza rompere i riferimenti alle immagini incorporate. Renderizza ciascun gruppo di sparkline come PNG, converti il `ByteArrayOutputStream` in un `byte[]` (oppure usa `to_byte_array()` per ottenere un oggetto Python `bytes`) e assegna l'array alla proprietà `embedded_image` della cella di destinazione: l'assegnazione è ciò che rende l'immagine parte del contenuto memorizzato della cella.

{{% alert color="primary" %}}
Poiché ogni gruppo di sparkline è ancorato a una singola cella, puoi accedervi tramite l'indicizzatore `group.sparklines[0]` invece di enumerare con un ciclo `for`. Ciò mantiene breve il codice di rendering e corrisponde al tipico schema "una sparkline per cella di ancoraggio". La memorizzazione dei byte dell'immagine tramite `Cell.embedded_image` richiede Aspose.Cells 26.5 o versioni successive.
{{% /alert %}}

## **Flusso di lavoro 2 — Esportare il Foglio di Lavoro con Sparkline in HTML**

Una volta che la cartella di lavoro contiene sparkline attive (e opzionalmente le controparti immagine incorporate), l'intero foglio di lavoro può essere pubblicato sul web salvandolo come HTML. La classe `HtmlSaveOptions` espone le opzioni necessarie per controllare questa esportazione; in questo flusso di lavoro riutilizzerai il file `output_with_sparklines.xlsx` prodotto dal Flusso di lavoro 1 e lo convertirai in un documento HTML pulito e a pagina singola.

### **Istruzioni passo per passo**

1. Assicurati che il file `output_with_sparklines.xlsx` prodotto dal Flusso di lavoro 1 sia disponibile sul disco nella tua directory di lavoro.
2. Carica quel file in una nuova istanza di `Workbook`.
3. Crea un'istanza di `HtmlSaveOptions` e imposta la sua proprietà `export_active_worksheet_only` su `True` in modo che il file HTML risultante contenga solo il foglio di lavoro attivo anziché l'intera cartella di lavoro.
4. Chiama `workbook.save("sparklines.html", html_options)` per scrivere l'output HTML sul disco.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, HtmlSaveOptions

workbook = Workbook("output_with_sparklines.xlsx")
htmlOptions = HtmlSaveOptions()
htmlOptions.setExportActiveWorksheetOnly(True)
workbook.save("sparklines.html", htmlOptions)

jpype.shutdownJVM()
```

Il codice sopra prende la cartella di lavoro ricca di sparkline dal Flusso di lavoro 1 e la trasforma in un file HTML portatile. Le sparkline vengono preservate come rendering SVG o PNG inline all'interno dell'HTML generato, a seconda della modalità di esportazione, così gli utenti finali possono visualizzare le tendenze in qualsiasi browser moderno senza bisogno di Excel installato. Impostando `export_active_worksheet_only` su `True`, eviti di pubblicare accidentalmente fogli nascosti o dati ausiliari: viene esportato solo il foglio di lavoro attualmente visibile all'utente.

{{% alert color="primary" %}}
La classe `HtmlSaveOptions` offre proprietà aggiuntive per ottimizzare l'output, come `export_hidden_worksheet`, `export_images_as_base64` e `encoding`. Regolale secondo le necessità del tuo target di distribuzione.
{{% /alert %}}

## **Riepilogo API**

I flussi di lavoro sopra si basano su un piccolo insieme di API di Aspose.Cells che lavorano insieme.

- `SparklineGroup` e l'accessore alla collezione `worksheet.sparkline_groups` sono utilizzati per dichiarare il tipo (Linea, Colonna, In pila), l'intervallo di dati e la cella di ancoraggio per ciascun gruppo di sparkline. In questo articolo ogni gruppo è ancorato a una singola cella, quindi il gruppo viene raggiunto tramite `worksheet.sparkline_groups[i]`.
- `Sparkline` e l'indicizzatore `group.sparklines[0]` restituiscono la singola sparkline all'interno di un gruppo. Poiché ogni gruppo nell'esempio contiene esattamente una sparkline, non è necessario alcun ciclo `for`.
- `Sparkline.to_image(OutputStream, ImageOrPrintOptions)` è il metodo di rendering che scrive un'immagine della sparkline in un `OutputStream` fornito (come un `ByteArrayOutputStream`). Il metodo restituisce `void`; devi leggere i byte dal flusso dopo la chiamata.
- `Cell.embedded_image` è una proprietà `byte[]` che memorizza un'immagine all'interno di una singola cella. È disponibile in **Aspose.Cells 26.5 e versioni successive** ed è il modo consigliato per reimportare una sparkline renderizzata da `to_image` nella stessa cartella di lavoro.
- `HtmlSaveOptions.export_active_worksheet_only` (un `bool`) limita l'esportazione HTML al foglio di lavoro attivo. È una delle proprietà più comunemente utilizzate su `HtmlSaveOptions` quando si generano report a pagina singola.
- `ImageOrPrintOptions.image_type` risiede nel namespace `com.aspose.cells.drawing` e seleziona il formato dell'immagine (ad esempio, `ImageType.PNG`) utilizzato durante il rendering con `to_image` e quando si stampano fogli di lavoro come immagini.

## **Articoli correlati**

- [Sparkline in Aspose.Cells for Aspose.Cells for Python via Java](/cells/it/python-java/sparkline/)
- [Inserimento di un'Immagine in una Cella](/cells/it/python-java/inserting-an-image-into-a-cell/)

{{< app/cells/assistant language="python" >}}