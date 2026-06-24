---
title: Sparklines in Aspose.Cells for Python via Java
linktitle: Sparklines
description: Aspose.Cells è una libreria Python via Java per lavorare con file di fogli di calcolo che supporta la creazione di sparkline — grafici in miniatura inseriti all'interno delle celle del foglio di lavoro. Questo articolo spiega come aggiungere e personalizzare sparkline a linee, a colonne e win/loss utilizzando la libreria Aspose.Cells.
keywords: Aspose.Cells, libreria Python via Java, foglio di calcolo, sparkline, sparkline a linee, sparkline a colonne, sparkline win/loss, SparklineGroup, SparklineType
type: docs
weight: 195
url: /it/python-java/creating-sparklines/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supporta la creazione di sparkline all'interno delle celle del foglio di lavoro. Le sparkline sono grafici in miniatura che si adattano a una singola cella, fornendo una rapida rappresentazione visiva delle tendenze dei dati. Aspose.Cells supporta sparkline a linee, a colonne e win/loss, e ognuna può essere personalizzata per quanto riguarda il colore, lo spessore della linea, i punti massimi/minimi e gli indicatori.

{{% /alert %}}

## **Introduzione**

Le sparkline sono piccoli grafici all'interno delle celle utili quando si desidera visualizzare una rapida tendenza accanto a una riga o colonna di dati senza occupare lo spazio di un grafico completo. Excel supporta tre tipi di sparkline: **a linee**, **a colonne** e **win/loss**. Aspose.Cells rispecchia questa funzionalità attraverso le API `SparklineGroup` e `SparklineGroupCollection` presenti nel namespace `Aspose.Cells.Charts`.

In Aspose.Cells, ogni sparkline che si aggiunge viene creata tramite `worksheet.getSparklineGroups().add(...)`, che restituisce un oggetto `SparklineGroup`. È quindi possibile utilizzare tale oggetto per impostare il tipo di sparkline, l'intervallo di dati, la cella di destinazione e le proprietà visive come il colore della linea, lo spessore della linea, gli indicatori e i marcatori dei punti massimi/minimi.

{{% alert color="primary" %}}

Un singolo `SparklineGroup` può contenere una o più sparkline che condividono lo stesso stile. Quando si chiama `add` e si passa una riga di dati più una singola cella di destinazione, si ottiene una sparkline all'interno di quella cella. Se l'intervallo di destinazione è più ampio di una cella, viene disegnata una sparkline separata in ciascuna cella di destinazione, tutte utilizzando lo stesso stile e intervallo di dati.

{{% /alert %}}

Questo articolo illustra ciascuno dei tre tipi di sparkline supportati da Aspose.Cells — **Linee**, **Colonne** e **Win/Loss** — e mostra come aggiungerle, personalizzarne i colori e salvare la cartella di lavoro risultante.

## **Sparkline a linee**

Una sparkline a linee traccia una linea continua attraverso i punti dati di una serie, rendendola la scelta più naturale per mostrare le tendenze nel tempo. In Aspose.Cells, una sparkline a linee viene creata passando `SparklineType.LINE` al metodo `add`.

Il flusso di lavoro è lo stesso di qualsiasi altro tipo di sparkline:

1. Creare una nuova `Workbook` e accedere al primo foglio di lavoro.
2. Popolare una riga di dati di origine (ad esempio, riga 1, colonne da A a E) con i valori che si desidera visualizzare.
3. Costruire un `CellArea` che descriva la cella di destinazione in cui verrà disegnata la sparkline.
4. Chiamare `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`. Il terzo argomento — `false` — indica ad Aspose.Cells che l'intervallo di dati è orizzontale (una riga), non verticale (una colonna).
5. Facoltativamente, personalizzare il `SparklineGroup` restituito. Per una sparkline a linee è possibile impostare il colore della linea utilizzando `group.getLine().getColor()` (che si aspetta un `CellsColor` da `Aspose.Cells.Drawing`), regolare lo spessore della linea e attivare i marcatori dei punti massimi/minimi.
6. Salvare la cartella di lavoro.

Il seguente esempio crea una cartella di lavoro, scrive i valori 5, -3, 8, -2, 6 nelle celle da A1 a E1 e aggiunge una sparkline a linee nella cella F1 che traccia tali valori. Personalizza inoltre il colore della linea in rosso e abilita i marcatori per i punti massimi e minimi.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, SparklineType
from java.awt import Color

# Passaggio 1: Creare una cartella di lavoro e ottenere il primo foglio di lavoro
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()

# Passaggio 2: Scrivere i valori di esempio 5, -3, 8, -2, 6 nelle celle A1:E1
cells.get("A1").putValue(5)
cells.get("B1").putValue(-3)
cells.get("C1").putValue(8)
cells.get("D1").putValue(-2)
cells.get("E1").putValue(6)

# Passaggio 3: Creare un CellArea che punta alla cella di destinazione F1
dest = CellArea()
dest.setStartColumn(5)  # colonna F (indicizzata da 0)
dest.setEndColumn(5)
dest.setStartRow(0)     # riga 1 (indicizzata da 0)
dest.setEndRow(0)

# Passaggio 4: Aggiungere una sparkline Linea da A1:E1 in F1
# SparklineGroups.add restituisce l'indice del gruppo appena aggiunto
index = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(index)

# Passaggio 5: Creare un CellsColor rosso e assegnarlo al colore della linea della sparkline
red = workbook.createCellsColor()
red.setColor(Color.RED)
group.setSeriesColor(red)

# Passaggio 6: Abilitare i marcatori del punto massimo e del punto minimo
group.setShowHighPoint(True)
group.setShowLowPoint(True)

# Passaggio 7: Salvare la cartella di lavoro
workbook.save("output_line.xlsx")

jpype.shutdownJVM()
```

## **Sparkline a colonne**

Una sparkline a colonne rappresenta ciascun punto dati come una barra verticale. Ciò la rende particolarmente adatta a dati la cui magnitudine è significativa — ad esempio, cifre di vendita mensili o conteggi. In Aspose.Cells, si crea una sparkline a colonne passando `SparklineType.COLUMN` al metodo `add`.

La procedura rispecchia l'esempio della sparkline a linee:

1. Creare una nuova `Workbook` e accedere al primo foglio di lavoro.
2. Popolare lo stesso intervallo di origine (A1:E1) con i valori che si desidera visualizzare.
3. Costruire un `CellArea` che descriva la cella di destinazione.
4. Chiamare `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`.
5. Facoltativamente, personalizzare il `SparklineGroup` risultante — ad esempio, impostando `group.getType()` per confermare il tipo, oppure modificando il colore delle barre.
6. Salvare la cartella di lavoro in un file di output separato in modo che non sovrascriva l'esempio della sparkline a linee.

L'esempio seguente scrive i valori 5, -3, 8, -2, 6 in A1:E1 e rende una sparkline a colonne in F1. I valori negativi vengono disegnati come barre rivolte verso il basso e i valori positivi come barre rivolte verso l'alto, il che rende facile individuare a colpo d'occhio i contributi positivi e negativi.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType

# Passo 1: Creare una cartella di lavoro e ottenere il primo foglio di lavoro
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Passo 2: Scrivere valori di esempio in A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.getCells().get(0, i).putValue(values[i])

# Passo 3: Costruire un CellArea che punta a F1 (indice colonna 5, indice riga 0)
dest = CellArea()
dest.setStartColumn(5)
dest.setEndColumn(5)
dest.setStartRow(0)
dest.setEndRow(0)

# Passo 4: Aggiungere uno sparkline di tipo Column alla cella di destinazione
idx = worksheet.getSparklineGroups().add(
    SparklineType.Column, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(idx)

# Passo 5: Confermare il tipo di sparkline leggendo group.Type
print("Sparkline Type added: " + str(group.getType()))

# Passo 6: Salvare la cartella di lavoro
workbook.save("output_column.xlsx")

print("Workbook saved as output_column.xlsx")

jpype.shutdownJVM()
```

## **Sparkline Win/Loss**

Una sparkline win/loss è una variante speciale della sparkline a colonne progettata per mostrare solo due esiti: un valore positivo viene disegnato come una barra "in su" (una vittoria) e un valore zero o negativo viene disegnato come una barra "in giù" (una sconfitta). Le sparkline win/loss sono comunemente utilizzate per visualizzare sequenze di vittorie e sconfitte, risultati di superamento/fallimento o qualsiasi esito binario nel tempo.

In Aspose.Cells, una sparkline win/loss viene creata passando `SparklineType.STACKED` al metodo `add`. (Nonostante il nome, `SparklineType.STACKED` è il valore enum utilizzato per richiedere il rendering win/loss.)

La procedura è la stessa degli altri due tipi:

1. Creare una nuova `Workbook` e accedere al primo foglio di lavoro.
2. Popolare l'intervallo di origine. Poiché le sparkline win/loss trattano ogni valore come una vittoria o una sconfitta, la magnitudine del valore non conta — conta solo il suo segno. I valori positivi diventano barre verso l'alto e i valori non positivi diventano barre verso il basso.
3. Costruire un `CellArea` che descriva la cella di destinazione.
4. Chiamare `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`.
5. Facoltativamente, personalizzare il `SparklineGroup` restituito, ad esempio impostando i colori di accento per le barre di vittoria e di sconfitta.
6. Salvare la cartella di lavoro con un nome file distinto in modo che tutti e tre gli esempi possano coesistere sul disco.

L'esempio seguente utilizza gli stessi dati di input delle due sezioni precedenti. I valori 5, -3, 8, -2, 6 vengono interpretati come vittoria, sconfitta, vittoria, sconfitta, vittoria — e la sparkline disegnata in F1 riflette esattamente tale schema.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, CellsColor, Color

# Passo 1: Crea una cartella di lavoro e ottieni il primo foglio di lavoro
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("WinLoss")

# Passo 2: Popola i dati di esempio nella riga 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# Passo 3: Crea un CellArea che punta a F1 (colonna 5, riga 0)
dest = CellArea()
dest.setStartColumn(5)   # F
dest.setEndColumn(5)
dest.setStartRow(0)      # riga 1
dest.setEndRow(0)

# Passo 4: Aggiungi una sparkline Win/Loss (SparklineType.Stacked)
groupIndex = worksheet.getSparklineGroups().add(
    SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.getSparklineGroups().get(groupIndex)

# Passo 5: Personalizza il gruppo di sparkline
# Abilita i marcatori dei punti alti e bassi
group.setShowHighPoint(True)
group.setShowLowPoint(True)
group.setShowNegativePoints(True)

# Imposta il colore dei punti alti su verde
highColor = workbook.createCellsColor()
highColor.setColor(Color.GREEN)
group.setHighPointColor(highColor)

# Imposta il colore dei punti bassi su rosso
lowColor = workbook.createCellsColor()
lowColor.setColor(Color.RED)
group.setLowPointColor(lowColor)

# Imposta il colore dei punti negativi su arancione
negColor = workbook.createCellsColor()
negColor.setColor(Color.ORANGE)
group.setNegativePointsColor(negColor)

# Imposta il colore predefinito della serie (usato per le barre positive)
seriesColor = workbook.createCellsColor()
seriesColor.setColor(Color.STEELBLUE)
group.setSeriesColor(seriesColor)

# Passo 6: Salva la cartella di lavoro
workbook.save("output_winloss.xlsx")

print("Workbook saved successfully: output_winloss.xlsx")

jpype.shutdownJVM()
```

## **Combinazione dei tre tipi di sparkline**

I tre esempi precedenti producono ciascuno la propria cartella di lavoro in modo che i file di output siano facili da ispezionare isolatamente. In uno scenario reale, tuttavia, si vorra spesso confrontare diverse serie di dati fianco a fianco. Il modo più pulito per farlo è inserire più gruppi di sparkline nello stesso foglio di lavoro, con ciascun gruppo che rende uno stile diverso.

È possibile aggiungere più oggetti `SparklineGroup` alla stessa `SparklineGroupCollection`, e ciascun gruppo può avere come destinazione una cella diversa o un intervallo diverso. Ad esempio, si potrebbe posizionare una sparkline a linee in F1, una sparkline a colonne in F2 e una sparkline win/loss in F3 — tutte leggendo dagli stessi dati di origine nella riga 1 — in modo che il lettore possa vedere tre diversi trattamenti visivi degli stessi numeri.

L'esempio combinato seguente crea una singola cartella di lavoro, popola la riga 1 con i valori 5, -3, 8, -2, 6 e quindi aggiunge tre gruppi di sparkline nelle celle F1, F2 e F3 — uno per ciascun tipo — in modo che il file risultante dimostri tutti e tre gli stili di sparkline contemporaneamente.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, CellsColor, SparklineType
from java.awt import Color

# Passo 1: Crea una Workbook e ottieni il primo foglio di lavoro
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Passo 2: Popola i dati di esempio nella riga 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)

# Passo 3: Aggiungi un gruppo di sparkline di tipo Linea in F1
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", False, lineArea)
lineGroup = worksheet.getSparklineGroups().get(lineIdx)

# Personalizza il colore della sparkline a linea tramite CellsColor
lineColor = workbook.createCellsColor()
lineColor.setColor(Color.BLUE)
lineGroup.setSeriesColor(lineColor)

# Passo 4: Aggiungi un gruppo di sparkline di tipo Colonna in F2
columnArea = CellArea()
columnArea.setStartColumn(5)
columnArea.setEndColumn(5)
columnArea.setStartRow(1)
columnArea.setEndRow(1)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", False, columnArea)
columnGroup = worksheet.getSparklineGroups().get(columnIdx)

# Personalizza il colore della serie della sparkline a colonna
columnColor = workbook.createCellsColor()
columnColor.setColor(Color.GREEN)
columnGroup.setSeriesColor(columnColor)

# Passo 5: Aggiungi un gruppo di sparkline Win/Loss (Stacked) in F3
stackedArea = CellArea()
stackedArea.setStartColumn(5)
stackedArea.setEndColumn(5)
stackedArea.setStartRow(2)
stackedArea.setEndRow(2)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", False, stackedArea)
stackedGroup = worksheet.getSparklineGroups().get(stackedIdx)

# Personalizza il colore della serie della sparkline win/loss
stackedColor = workbook.createCellsColor()
stackedColor.setColor(Color(255, 140, 0))  # DarkOrange
stackedGroup.setSeriesColor(stackedColor)

# Passo 6: Salva la workbook
workbook.save("output_all.xlsx")

jpype.shutdownJVM()
```

{{% alert color="primary" %}}

Quando si combinano più gruppi di sparkline in un singolo foglio di lavoro, ciascun gruppo è indipendente. Possono condividere lo stesso intervallo di origine o utilizzare intervalli di origine diversi, e possono essere stilizzati indipendentemente. Ciò rende facile costruire un piccolo "dashboard" di visualizzazioni all'interno delle celle direttamente in un foglio di lavoro esistente.

{{% /alert %}}

## **Personalizzazione dell'aspetto delle sparkline**

Una volta che un `SparklineGroup` è stato creato e aggiunto a `worksheet.getSparklineGroups()`, è possibile leggere o modificare diverse delle sue proprietà visive prima di salvare la cartella di lavoro. Le proprietà più comunemente personalizzate sono:

- **`group.getType()`** — il `SparklineType` (LINE, COLUMN o STACKED). Viene impostato quando il gruppo viene aggiunto, ma è possibile rileggerlo per confermarlo.
- **`group.getLine().getColor()`** — il colore della linea, espresso come `CellsColor` creato tramite `workbook.createCellsColor()`. Questa è la proprietà da utilizzare per il colore del tratto della sparkline a linee.
- **`group.getLine().getWeight()`** — lo spessore della linea in punti. Valori più alti producono linee più spesse.
- **Marcatori dei punti massimi/minimi** — flag che attivano piccoli marcatori sui punti dati più alti e più bassi, utili per enfatizzare gli estremi.
- **Marcatori dei punti primo/ultimo/negativo** — flag che attivano i marcatori sui punti dati primo, ultimo e negativo.

Per modificare un colore, creare sempre un'istanza di `CellsColor` e assegnarla alla proprietà pertinente. Non assegnare un `java.awt.Color` direttamente alle proprietà di colore delle sparkline — si aspettano il tipo `CellsColor` da `Aspose.Cells.Drawing`. Il metodo `add` stesso restituisce un oggetto `SparklineGroup` completamente tipizzato, quindi è possibile concatenare le assegnazioni di proprietà sul valore restituito o memorizzarlo in una variabile locale e personalizzarlo prima di salvare.



{{< app/cells/assistant language="python" >}}