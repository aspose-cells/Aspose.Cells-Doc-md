---
title: Sparklines in Aspose.Cells for Python via Java
description: Aspose.Cells è una libreria Python via Java per lavorare con file di fogli di calcolo che supporta la creazione di sparkline, ovvero minigrafici inseriti all'interno delle celle del foglio di lavoro. Questo articolo spiega come aggiungere e personalizzare sparkline a linea, a colonna e vincita/perdita utilizzando la libreria Aspose.Cells.
linktitle: Sparkline
keywords: Aspose.Cells, libreria Python via Java, foglio di calcolo, sparkline, sparkline a linea, sparkline a colonna, sparkline vincita/perdita, SparklineGroup, SparklineType
type: docs
weight: 195
url: /it/python-java/creating-sparklines/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta la creazione di sparkline all'interno delle celle del foglio di lavoro. Le sparkline sono minigrafici che si adattano a una singola cella, fornendo una rapida rappresentazione visiva delle tendenze dei dati. Aspose.Cells supporta sparkline a linea, a colonna e vincita/perdita, e ciascuna può essere personalizzata per quanto riguarda colore, spessore della linea, punti massimo/minimo e indicatori.

## **Introduzione**
Le sparkline sono piccoli grafici all'interno delle celle, utili quando si desidera visualizzare una rapida tendenza accanto a una riga o colonna di dati senza occupare lo spazio di un grafico completo. Excel supporta tre tipi di sparkline: **linea**, **colonna** e **vincita/perdita**. Aspose.Cells rispecchia questa funzionalità attraverso le API `SparklineGroup` e `SparklineGroupCollection` presenti nel namespace `Aspose.Cells.Charts`.
In Aspose.Cells, ogni sparkline aggiunta viene creata tramite `worksheet.getSparklineGroups().add(...)`, che restituisce un oggetto `SparklineGroup`. È quindi possibile utilizzare tale oggetto per impostare il tipo di sparkline, l'intervallo di dati, la cella di destinazione e le proprietà visive come il colore della linea, lo spessore della linea, gli indicatori e gli indicatori dei punti massimo/minimo.
Questo articolo illustra ciascuno dei tre tipi di sparkline supportati da Aspose.Cells — **Linea**, **Colonna** e **Vincita/Perdita** — e mostra come aggiungerli, personalizzarne i colori e salvare la cartella di lavoro risultante.

## **Sparkline a linea**
Una sparkline a linea disegna una linea continua attraverso i punti dati di una serie, rendendola la scelta più naturale per mostrare le tendenze nel tempo. In Aspose.Cells, una sparkline a linea viene creata passando `SparklineType.LINE` al metodo `add`.
1. Creare un nuovo `Workbook` e accedere al primo foglio di lavoro.
2. Popolare una riga di dati di origine (ad esempio, riga 1, colonne da A a E) con i valori che si desidera visualizzare.
3. Creare un `CellArea` che descriva la cella di destinazione in cui verrà disegnata la sparkline.
4. Chiamare `worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", false, dest)`. Il terzo argomento — `false` — indica ad Aspose.Cells che l'intervallo di dati è orizzontale (una riga), non verticale (una colonna).
5. Facoltativamente, personalizzare il `SparklineGroup` restituito. Per una sparkline a linea è possibile impostare il colore della linea utilizzando `group.getLine().getColor()` (che si aspetta un `CellsColor` da `Aspose.Cells.Drawing`), regolare lo spessore della linea e attivare/disattivare gli indicatori dei punti massimo/minimo.
6. Salvare la cartella di lavoro.
L'esempio seguente crea una cartella di lavoro, scrive i valori 5, -3, 8, -2, 6 nelle celle da A1 a E1 e aggiunge una sparkline a linea nella cella F1 che traccia tali valori. Personalizza inoltre il colore della linea in rosso e abilita gli indicatori per i punti massimo e minimo.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, CellsColor, SparklineType
from java.awt import Color
# Step 1: Create a Workbook and get the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Step 2: Populate sample data in row 1 (A1:E1)
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)
# Step 3: Add a Line sparkline group at F1
lineArea = CellArea()
lineArea.setStartColumn(5)
lineArea.setEndColumn(5)
lineArea.setStartRow(0)
lineArea.setEndRow(0)
lineIdx = worksheet.getSparklineGroups().add(SparklineType.LINE, "A1:E1", False, lineArea)
lineGroup = worksheet.getSparklineGroups().get(lineIdx)
# Customize the line sparkline color via CellsColor
lineColor = workbook.createCellsColor()
lineColor.setColor(Color.BLUE)
lineGroup.setSeriesColor(lineColor)
# Step 4: Add a Column sparkline group at F2
columnArea = CellArea()
columnArea.setStartColumn(5)
columnArea.setEndColumn(5)
columnArea.setStartRow(1)
columnArea.setEndRow(1)
columnIdx = worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", False, columnArea)
columnGroup = worksheet.getSparklineGroups().get(columnIdx)
# Customize the column sparkline series color
columnColor = workbook.createCellsColor()
columnColor.setColor(Color.GREEN)
columnGroup.setSeriesColor(columnColor)
# Step 5: Add a Win/Loss (Stacked) sparkline group at F3
stackedArea = CellArea()
stackedArea.setStartColumn(5)
stackedArea.setEndColumn(5)
stackedArea.setStartRow(2)
stackedArea.setEndRow(2)
stackedIdx = worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", False, stackedArea)
stackedGroup = worksheet.getSparklineGroups().get(stackedIdx)
# Customize the win/loss sparkline series color
stackedColor = workbook.createCellsColor()
stackedColor.setColor(Color(255, 140, 0))  # DarkOrange
stackedGroup.setSeriesColor(stackedColor)
# Step 6: Save the workbook
workbook.save("output_all.xlsx")
jpype.shutdownJVM()
```

## **Sparkline a colonna**
Una sparkline a colonna rende ciascun punto dati come una barra verticale. Questo la rende particolarmente adatta a dati la cui grandezza è significativa — ad esempio, cifre di vendite mensili o conteggi. In Aspose.Cells, si crea una sparkline a colonna passando `SparklineType.COLUMN` al metodo `add`.
La procedura rispecchia l'esempio della sparkline a linea:
1. Creare un nuovo `Workbook` e accedere al primo foglio di lavoro.
3. Creare un `CellArea` che descriva la cella di destinazione.
4. Chiamare `worksheet.getSparklineGroups().add(SparklineType.COLUMN, "A1:E1", false, dest)`.
5. Facoltativamente, personalizzare il `SparklineGroup` risultante — ad esempio, impostando `group.getType()` per confermare il tipo, oppure modificando il colore della barra.
6. Salvare la cartella di lavoro in un file di output separato in modo che non sovrascriva l'esempio della sparkline a linea.
L'esempio seguente scrive i valori 5, -3, 8, -2, 6 in A1:E1 e rende una sparkline a colonna in F1. I valori negativi vengono disegnati come barre rivolte verso il basso e i valori positivi come barre rivolte verso l'alto, il che rende facile individuare a colpo d'occhio i contributi positivi e negativi.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType
# Passo 1: Crea una cartella di lavoro e ottieni il primo foglio di lavoro
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Passo 2: Scrivi valori di esempio in A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.getCells().get(0, i).putValue(values[i])
# Passo 3: Crea un CellArea che punta a F1 (indice colonna 5, indice riga 0)
dest = CellArea()
dest.setStartColumn(5)
dest.setEndColumn(5)
dest.setStartRow(0)
dest.setEndRow(0)
# Passo 4: Aggiungi una sparkline di tipo Colonna alla cella di destinazione
idx = worksheet.getSparklineGroups().add(
    SparklineType.Column, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(idx)
# Passo 5: Conferma il tipo di sparkline leggendo group.Type
print("Sparkline Type added: " + str(group.getType()))
# Passo 6: Salva la cartella di lavoro
workbook.save("output_column.xlsx")
print("Workbook saved as output_column.xlsx")
jpype.shutdownJVM()
```

## **Sparkline Vincita/Perdita**
Una sparkline vincita/perdita è una variante speciale della sparkline a colonna, progettata per mostrare solo due esiti: un valore positivo viene disegnato come una barra "in alto" (una vincita) e un valore zero o negativo viene disegnato come una barra "in basso" (una perdita). Le sparkline vincita/perdita sono comunemente utilizzate per visualizzare sequenze di vittorie e sconfitte, risultati superato/fallito o qualsiasi esito binario nel tempo.
In Aspose.Cells, una sparkline vincita/perdita viene creata passando `SparklineType.STACKED` al metodo `add`. (Nonostante il nome, `SparklineType.STACKED` è il valore enum utilizzato per richiedere il rendering vincita/perdita.)
1. Creare un nuovo `Workbook` e accedere al primo foglio di lavoro.
2. Popolare l'intervallo di origine. Poiché le sparkline vincita/perdita trattano ogni valore come una vincita o una perdita, la grandezza del valore non è rilevante — conta solo il suo segno. I valori positivi diventano barre in alto e i valori non positivi diventano barre in basso.
3. Creare un `CellArea` che descriva la cella di destinazione.
4. Chiamare `worksheet.getSparklineGroups().add(SparklineType.STACKED, "A1:E1", false, dest)`.
5. Facoltativamente, personalizzare il `SparklineGroup` restituito, ad esempio impostando i colori principali per le barre di vincita e perdita.
6. Salvare la cartella di lavoro con un nome file distinto in modo che tutti e tre gli esempi possano coesistere sul disco.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, CellArea, SparklineType, CellsColor, Color
# Step 1: Create a Workbook and get the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.setName("WinLoss")
# Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.getCells().get("A1").putValue(5)
worksheet.getCells().get("B1").putValue(-3)
worksheet.getCells().get("C1").putValue(8)
worksheet.getCells().get("D1").putValue(-2)
worksheet.getCells().get("E1").putValue(6)
# Step 3: Build a CellArea pointing to F1 (column 5, row 0)
dest = CellArea()
dest.setStartColumn(5)   # F
dest.setEndColumn(5)
dest.setStartRow(0)      # row 1
dest.setEndRow(0)
# Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
groupIndex = worksheet.getSparklineGroups().add(
    SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.getSparklineGroups().get(groupIndex)
# Step 5: Customize the sparkline group
# Enable high-point and low-point markers
group.setShowHighPoint(True)
group.setShowLowPoint(True)
group.setShowNegativePoints(True)
# Set the high-point color to green
highColor = workbook.createCellsColor()
highColor.setColor(Color.GREEN)
group.setHighPointColor(highColor)
# Set the low-point color to red
lowColor = workbook.createCellsColor()
lowColor.setColor(Color.RED)
group.setLowPointColor(lowColor)
# Set the negative-point color to orange
negColor = workbook.createCellsColor()
negColor.setColor(Color.ORANGE)
group.setNegativePointsColor(negColor)
# Set the default series color (used for positive bars)
seriesColor = workbook.createCellsColor()
seriesColor.setColor(Color.STEELBLUE)
group.setSeriesColor(seriesColor)
# Step 6: Save the workbook
workbook.save("output_winloss.xlsx")
print("Workbook saved successfully: output_winloss.xlsx")
jpype.shutdownJVM()
```

## **Combinazione di tutti e tre i tipi di sparkline**
L'esempio combinato seguente crea una singola cartella di lavoro, popola la riga 1 con i valori 5, -3, 8, -2, 6, quindi aggiunge tre gruppi di sparkline nelle celle F1, F2 e F3 — uno per ciascun tipo — in modo che il file risultante dimostri tutti e tre gli stili di sparkline contemporaneamente.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, CellArea, SparklineType
from java.awt import Color
# Step 1: Create a Workbook and get the first worksheet
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
# Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells.get("A1").putValue(5)
cells.get("B1").putValue(-3)
cells.get("C1").putValue(8)
cells.get("D1").putValue(-2)
cells.get("E1").putValue(6)
# Step 3: Build a CellArea pointing to destination cell F1
dest = CellArea()
dest.setStartColumn(5)  # column F (0-indexed)
dest.setEndColumn(5)
dest.setStartRow(0)     # row 1 (0-indexed)
dest.setEndRow(0)
# Step 4: Add a Line sparkline from A1:E1 into F1
# SparklineGroups.add returns the index of the newly added group
index = worksheet.getSparklineGroups().add(SparklineType.Line, "A1:E1", False, dest)
group = worksheet.getSparklineGroups().get(index)
# Step 5: Create a red CellsColor and assign it to the sparkline line color
red = workbook.createCellsColor()
red.setColor(Color.RED)
group.setSeriesColor(red)
# Step 6: Enable high-point and low-point markers
group.setShowHighPoint(True)
group.setShowLowPoint(True)
# Step 7: Save the workbook
workbook.save("output_line.xlsx")
jpype.shutdownJVM()
```

## **Personalizzazione dell'aspetto delle sparkline**
Una volta che un `SparklineGroup` è stato creato e aggiunto a `worksheet.getSparklineGroups()`, è possibile leggere o modificare diverse proprietà visive prima di salvare la cartella di lavoro. Le proprietà più comunemente personalizzate sono:
- **`group.getType()`** — il `SparklineType` (LINE, COLUMN o STACKED). Viene impostato quando il gruppo viene aggiunto, ma è possibile rileggerlo per confermarlo.
- **`group.getLine().getColor()`** — il colore della linea, espresso come `CellsColor` creato tramite `workbook.createCellsColor()`. Questa è la proprietà da utilizzare per il colore del tratto della sparkline a linea.
- **`group.getLine().getWeight()`** — lo spessore della linea in punti. Valori più alti producono linee più spesse.
- **Indicatori dei punti massimo/minimo** — flag che attivano piccoli indicatori sui punti dati più alti e più bassi, utili per evidenziare gli estremi.
- **Indicatori dei punti primo/ultimo/negativo** — flag che attivano/disattivano gli indicatori sui punti dati primo, ultimo e negativo.
Per modificare un colore, creare sempre un'istanza di `CellsColor` e assegnarla alla proprietà pertinente. Non assegnare direttamente un `java.awt.Color` alle proprietà del colore delle sparkline — esse si aspettano il tipo `CellsColor` da `Aspose.Cells.Drawing`. Il metodo `add` stesso restituisce un oggetto `SparklineGroup` completamente tipizzato, quindi è possibile concatenare le assegnazioni di proprietà sul valore restituito o memorizzarlo in una variabile locale e personalizzarlo prima di salvare.
{{% /alert %}}

{{< app/cells/assistant language="python" >}}