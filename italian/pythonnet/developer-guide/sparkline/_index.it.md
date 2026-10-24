---
title: Sparkline in Aspose.Cells for Python tramite .NET
description: Aspose.Cells è una libreria Python per lavorare con file di fogli di calcolo che supporta la creazione di sparkline, ovvero grafici in miniatura inseriti all'interno delle celle del foglio di lavoro. Questo articolo spiega come aggiungere e personalizzare le sparkline a linea, a colonna e di tipo win/loss tramite Aspose.Cells.
linktitle: Sparkline
keywords: Aspose.Cells, libreria Python, foglio di calcolo, sparkline, sparkline a linea, sparkline a colonna, sparkline win/loss, SparklineGroup, SparklineType
type: docs
weight: 195
url: /it/python-net/creating-sparklines/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta la creazione di sparkline all'interno delle celle del foglio di lavoro. Le sparkline sono grafici in miniatura che si adattano a una singola cella, offrendo una rapida rappresentazione visiva dell'andamento dei dati. Aspose.Cells supporta le sparkline a linea, a colonna e win/loss, ciascuna delle quali può essere personalizzata per quanto riguarda colore, spessore della linea, punti massimo/minimo e marcatori.
{{% /alert %}}

## **Introduzione**
Le sparkline sono minuscoli grafici all'interno delle celle, utili quando si desidera visualizzare un rapido andamento accanto a una riga o colonna di dati senza occupare lo spazio di un grafico completo. Excel supporta tre tipi di sparkline: **linea**, **colonna** e **win/loss**. Aspose.Cells rispecchia questa capacità attraverso le API `SparklineGroup` e `SparklineGroupCollection` presenti nel namespace `aspose.cells.charts`.
In Aspose.Cells, ogni sparkline che aggiungi viene creata tramite `worksheet.sparkline_groups.add(...)`, che restituisce un oggetto `SparklineGroup`. Puoi quindi utilizzare tale oggetto per impostare il tipo di sparkline, l'intervallo di dati, la cella di destinazione e le proprietà visive come il colore della linea, lo spessore della linea, i marcatori e gli indicatori dei punti massimo/minimo.
Questo articolo esamina ciascuno dei tre tipi di sparkline supportati da Aspose.Cells — **Linea**, **Colonna** e **Win/Loss** — e mostra come aggiungerli, personalizzare i loro colori e salvare la cartella di lavoro risultante.

## **Sparkline a Linea**
Una sparkline a linea disegna una linea continua attraverso i punti dati di una serie, rendendola la scelta più naturale per mostrare l'andamento nel tempo. In Aspose.Cells, una sparkline a linea viene creata passando `SparklineType.LINE` al metodo `sparkline_groups.add`.
1. Crea un nuovo `Workbook` e accedi al primo foglio di lavoro.
2. Popola una riga di dati di origine (ad esempio, riga 1, colonne da A a E) con i valori che desideri visualizzare.
3. Crea un `CellArea` che descriva la cella di destinazione in cui verrà disegnata la sparkline.
4. Chiama `worksheet.sparkline_groups.add(SparklineType.LINE, "A1:E1", False, dest)`. Il terzo argomento — `False` — indica ad Aspose.Cells che l'intervallo di dati è orizzontale (una riga), non verticale (una colonna).
5. Facoltativamente, personalizza il `SparklineGroup` restituito. Per una sparkline a linea puoi impostare il colore della linea utilizzando `group.line.color` (che si aspetta un `CellsColor` da `aspose.cells.drawing`), regolare lo spessore della linea e attivare/disattivare i marcatori dei punti massimo/minimo.
6. Salva la cartella di lavoro.
Il seguente esempio crea una cartella di lavoro, scrive i valori 5, -3, 8, -2, 6 nelle celle da A1 a E1 e aggiunge una sparkline a linea nella cella F1 che traccia tali valori. Personalizza inoltre il colore della linea in rosso e abilita i marcatori per i punti massimo e minimo.

## **Sparkline a Colonna**
Una sparkline a colonna rende ciascun punto dati come una barra verticale. Ciò la rende particolarmente adatta a dati la cui magnitudine è significativa, ad esempio le cifre di vendita mensili o i conteggi. In Aspose.Cells, crei una sparkline a colonna passando `SparklineType.COLUMN` al metodo `sparkline_groups.add`.
La procedura rispecchia l'esempio della sparkline a linea:
1. Crea un nuovo `Workbook` e accedi al primo foglio di lavoro.
2. Crea un `CellArea` che descriva la cella di destinazione.
3. Chiama `worksheet.sparkline_groups.add(SparklineType.COLUMN, "A1:E1", False, dest)`.
4. Facoltativamente, personalizza il `SparklineGroup` risultante, ad esempio impostando `group.type` per confermare il tipo, oppure modificando il colore della barra.
5. Salva la cartella di lavoro in un file di output separato in modo che non sovrascriva l'esempio della sparkline a linea.
L'esempio seguente scrive i valori 5, -3, 8, -2, 6 in A1:E1 e rende una sparkline a colonna in F1. I valori negativi sono disegnati come barre rivolte verso il basso e i valori positivi come barre rivolte verso l'alto, il che rende facile individuare a colpo d'occhio i contributi positivi e negativi.

```python
import aspose.cells as ac
from aspose.cells.charts import SparklineType
# Passaggio 1: Crea una cartella di lavoro e ottieni il primo foglio di lavoro
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Passaggio 2: Scrivi valori di esempio in A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.cells.get(0, i).put_value(values[i])
# Passaggio 3: Crea un CellArea che punta a F1 (indice della colonna 5, indice della riga 0)
dest = ac.CellArea()
dest.start_column = 5
dest.end_column = 5
dest.start_row = 0
dest.end_row = 0
# Passaggio 4: Aggiungi uno sparkline a colonna alla cella di destinazione
idx = worksheet.sparkline_groups.add(
    SparklineType.COLUMN, "A1:E1", False, dest)
group = worksheet.sparkline_groups[idx]
# Passaggio 5: Conferma il tipo di sparkline leggendo group.Type
print("Sparkline Type added: " + str(group.type))
# Passaggio 6: Salva la cartella di lavoro
workbook.save("output_column.xlsx")
print("Workbook saved as output_column.xlsx")
```

## **Sparkline Win/Loss**
Una sparkline win/loss è una variante speciale della sparkline a colonna progettata per mostrare solo due risultati: un valore positivo viene disegnato come una barra 'in alto' (una vittoria) e un valore zero o negativo come una barra 'in basso' (una sconfitta). Le sparkline win/loss sono comunemente utilizzate per visualizzare sequenze di vittorie e sconfitte, risultati di superamento/fallimento o qualsiasi esito binario nel tempo.
In Aspose.Cells, una sparkline win/loss viene creata passando `SparklineType.STACKED` al metodo `sparkline_groups.add`. (Nonostante il nome, `SparklineType.STACKED` è il valore enum utilizzato per richiedere il rendering win/loss.)
1. Crea un nuovo `Workbook` e accedi al primo foglio di lavoro.
2. Popola l'intervallo di origine. Poiché le sparkline win/loss trattano ogni valore come una vittoria o una sconfitta, la magnitudine del valore non è rilevante, ma solo il suo segno. I valori positivi diventano barre in alto e i valori non positivi diventano barre in basso.
3. Crea un `CellArea` che descriva la cella di destinazione.
4. Chiama `worksheet.sparkline_groups.add(SparklineType.STACKED, "A1:E1", False, dest)`.
5. Facoltativamente, personalizza il `SparklineGroup` restituito, ad esempio impostando i colori di accento per le barre di vittoria e sconfitta.
6. Salva la cartella di lavoro con un nome file distinto in modo che tutti e tre gli esempi possano coesistere sul disco.

## **Combinazione di tutti e tre i tipi di Sparkline**
L'esempio combinato seguente crea una singola cartella di lavoro, popola la riga 1 con i valori 5, -3, 8, -2, 6 e quindi aggiunge tre gruppi di sparkline nelle celle F1, F2 e F3, uno per ciascun tipo, in modo che il file risultante dimostri tutti e tre gli stili di sparkline contemporaneamente.

```python
import aspose.cells as ac
from aspose.cells.charts import SparklineType
from aspose.pydrawing import Color
# Passaggio 1: Creare un workbook e ottenere il primo foglio di lavoro
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Passaggio 2: Popolare i dati di esempio nella riga 1 (A1:E1)
worksheet.cells.get("A1").put_value(5)
worksheet.cells.get("B1").put_value(-3)
worksheet.cells.get("C1").put_value(8)
worksheet.cells.get("D1").put_value(-2)
worksheet.cells.get("E1").put_value(6)
# Passaggio 3: Aggiungere un gruppo di sparkline a linee in F1
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(SparklineType.LINE, "A1:E1", False, line_area)
line_group = worksheet.sparkline_groups[line_idx]
# Personalizzare il colore della sparkline a linee tramite CellsColor
line_color = workbook.create_cells_color()
line_color.color = Color.blue
line_group.series_color = line_color
# Passaggio 4: Aggiungere un gruppo di sparkline a colonne in F2
column_area = ac.CellArea()
column_area.start_column = 5
column_area.end_column = 5
column_area.start_row = 1
column_area.end_row = 1
column_idx = worksheet.sparkline_groups.add(SparklineType.COLUMN, "A1:E1", False, column_area)
column_group = worksheet.sparkline_groups[column_idx]
# Personalizzare il colore della serie di sparkline a colonne
column_color = workbook.create_cells_color()
column_color.color = Color.green
column_group.series_color = column_color
# Passaggio 5: Aggiungere un gruppo di sparkline vittoria/sconfitta (impilato) in F3
stacked_area = ac.CellArea()
stacked_area.start_column = 5
stacked_area.end_column = 5
stacked_area.start_row = 2
stacked_area.end_row = 2
stacked_idx = worksheet.sparkline_groups.add(SparklineType.STACKED, "A1:E1", False, stacked_area)
stacked_group = worksheet.sparkline_groups[stacked_idx]
# Personalizzare il colore della serie di sparkline vittoria/sconfitta
stacked_color = workbook.create_cells_color()
stacked_color.color = Color.dark_orange
stacked_group.series_color = stacked_color
# Passaggio 6: Salvare il workbook
workbook.save("output_all.xlsx")
```

## **Personalizzazione dell'aspetto della Sparkline**
Una volta che un `SparklineGroup` è stato creato e aggiunto a `worksheet.sparkline_groups`, puoi leggere o modificare diverse delle sue proprietà visive prima di salvare la cartella di lavoro. Le proprietà più comunemente personalizzate sono:
- **`group.type`** — il `SparklineType` (Line, Column o Stacked). Viene impostato quando il gruppo viene aggiunto, ma puoi rileggerlo per confermarlo.
- **`group.line.color`** — il colore della linea, espresso come `CellsColor` creato tramite `workbook.create_cells_color()`. Questa è la proprietà da utilizzare per il colore del tratto della sparkline a linea.
- **`group.line.weight`** — lo spessore della linea in punti. Valori più alti producono linee più spesse.
- **Marcatori dei punti massimo/minimo** — flag che attivano piccoli marcatori sui punti dati più alti e più bassi, utili per enfatizzare gli estremi.
- **Marcatori dei punti primo/ultimo/negativo** — flag che attivano/disattivano i marcatori sui punti dati primo, ultimo e negativo.
Per cambiare un colore, crea sempre un'istanza di `CellsColor` e assegnala alla proprietà rilevante. Le proprietà del colore della sparkline si aspettano il tipo `CellsColor` da `aspose.cells.drawing`, non assegnare direttamente un valore di colore grezzo. Il metodo `sparkline_groups.add` stesso restituisce un oggetto `SparklineGroup` completamente tipizzato, quindi puoi concatenare le assegnazioni di proprietà sul valore restituito o memorizzarlo in una variabile locale e personalizzarlo prima di salvare.
1. Create a new `Workbook` and access the first worksheet.
3. Build a `CellArea` describing the destination cell.
4. Call `worksheet.sparkline_groups.add(SparklineType.COLUMN, "A1:E1", False, dest)`.
5. Optionally customize the resulting `SparklineGroup` — for example, by setting `group.type` to confirm the type, or by tweaking the bar color.
6. Save the workbook to a separate output file so it does not overwrite the line sparkline example.python

```python
import aspose.cells as ac
from aspose.cells.charts import SparklineType
from aspose.pydrawing import Color
# Step 1: Create a Workbook and get the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells
# Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells.get("A1").put_value(5)
cells.get("B1").put_value(-3)
cells.get("C1").put_value(8)
cells.get("D1").put_value(-2)
cells.get("E1").put_value(6)
# Step 3: Build a CellArea pointing to destination cell F1
dest = ac.CellArea()
dest.start_column = 5   # column F (0-indexed)
dest.end_column = 5
dest.start_row = 0      # row 1 (0-indexed)
dest.end_row = 0
# Step 4: Add a Line sparkline from A1:E1 into F1
# SparklineGroups.Add returns the index of the newly added group
index = worksheet.sparkline_groups.add(SparklineType.LINE, "A1:E1", False, dest)
group = worksheet.sparkline_groups[index]
# Step 5: Create a red CellsColor and assign it to the sparkline line color
red = workbook.create_cells_color()
red.color = Color.red
group.series_color = red
# Step 6: Enable high-point and low-point markers
group.show_high_point = True
group.show_low_point = True
# Step 7: Save the workbook
workbook.save("output_line.xlsx")
```

```python
import aspose.cells as ac
from aspose.cells.charts import SparklineType
from aspose.pydrawing import Color
# Step 1: Create a Workbook and get the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "WinLoss"
# Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.cells.get("A1").put_value(5)
worksheet.cells.get("B1").put_value(-3)
worksheet.cells.get("C1").put_value(8)
worksheet.cells.get("D1").put_value(-2)
worksheet.cells.get("E1").put_value(6)
# Step 3: Build a CellArea pointing to F1 (column 5, row 0)
dest = ac.CellArea()
dest.start_column = 5   # F
dest.end_column = 5
dest.start_row = 0      # row 1
dest.end_row = 0
# Step 4: Add a Win/Loss sparkline (SparklineType.STACKED)
group_index = worksheet.sparkline_groups.add(
    SparklineType.STACKED,
    "A1:E1",
    False,
    dest)
group = worksheet.sparkline_groups[group_index]
# Step 5: Customize the sparkline group
# Enable high-point and low-point markers
group.show_high_point = True
group.show_low_point = True
group.show_negative_points = True
# Set the high-point color to green
high_color = workbook.create_cells_color()
high_color.color = Color.green
group.high_point_color = high_color
# Set the low-point color to red
low_color = workbook.create_cells_color()
low_color.color = Color.red
group.low_point_color = low_color
# Set the negative-point color to orange
neg_color = workbook.create_cells_color()
neg_color.color = Color.orange
group.negative_points_color = neg_color
# Set the default series color (used for positive bars)
series_color = workbook.create_cells_color()
series_color.color = Color.steel_blue
group.series_color = series_color
# Step 6: Save the workbook
workbook.save("output_winloss.xlsx")
print("Workbook saved successfully: output_winloss.xlsx")
```

{{< app/cells/assistant language="python-net" >}}