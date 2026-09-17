---
title: Sparklines in Aspose.Cells for Python via .NET
description: Aspose.Cells is a Python library for working with spreadsheet files that supports creating sparklines — miniature charts placed inside worksheet cells. This article explains how to add and customize line, column, and win/loss sparklines using the Aspose.Cells library.
linktitle: Sparklines
keywords: Aspose.Cells, Python library, spreadsheet, sparklines, line sparkline, column sparkline, win/loss sparkline, SparklineGroup, SparklineType
type: docs
weight: 195
url: /it/python-net/creating-sparklines/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta la creazione di sparklines all'interno delle celle del foglio di lavoro. Le sparklines sono grafici in miniatura che si adattano a una singola cella, offrendo una rapida rappresentazione visiva delle tendenze dei dati. Aspose.Cells supporta sparklines di tipo linea, colonna e win/loss, e ciascuna può essere personalizzata in termini di colore, spessore della linea, punti massimo/minimo e indicatori.

## **Introduzione**
Le sparklines sono piccoli grafici all'interno delle celle, utili quando si desidera visualizzare rapidamente una tendenza accanto a una riga o colonna di dati senza occupare lo spazio di un grafico completo. Excel supporta tre tipi di sparklines: **linea**, **colonna** e **win/loss**. Aspose.Cells rispecchia questa funzionalità attraverso le API `SparklineGroup` e `SparklineGroupCollection` presenti nel namespace `aspose.cells.charts`.
In Aspose.Cells, ogni sparkline che aggiungi viene creata tramite `worksheet.sparkline_groups.add(...)`, che restituisce un oggetto `SparklineGroup`. Puoi quindi utilizzare tale oggetto per impostare il tipo di sparkline, l'intervallo di dati, la cella di destinazione e le proprietà visive come il colore della linea, lo spessore della linea, gli indicatori e gli indicatori dei punti massimo/minimo.
Questo articolo illustra ciascuno dei tre tipi di sparkline supportati da Aspose.Cells — **Linea**, **Colonna** e **Win/Loss** — e mostra come aggiungerli, personalizzare i loro colori e salvare la cartella di lavoro risultante.

## **Sparklines di tipo Linea**
Una sparkline di tipo linea disegna una linea continua attraverso i punti dati di una serie, rendendola la scelta più naturale per mostrare le tendenze nel tempo. In Aspose.Cells, una sparkline di tipo linea viene creata passando `SparklineType.Line` al metodo `sparkline_groups.add`.
1. Crea una nuova `Workbook` e accedi al primo foglio di lavoro.
2. Popola una riga di dati di origine (ad esempio, riga 1, colonne da A a E) con i valori che desideri visualizzare.
3. Crea un `CellArea` che descriva la cella di destinazione in cui verrà disegnata la sparkline.
4. Chiama `worksheet.sparkline_groups.add(SparklineType.Line, "A1:E1", False, dest)`. Il terzo argomento — `False` — indica ad Aspose.Cells che l'intervallo di dati è orizzontale (una riga), non verticale (una colonna).
5. Facoltativamente, personalizza il `SparklineGroup` restituito. Per una sparkline di tipo linea puoi impostare il colore della linea usando `group.line.color` (che richiede un `CellsColor` da `aspose.cells.drawing`), regolare lo spessore della linea e attivare gli indicatori dei punti massimo/minimo.
6. Salva la cartella di lavoro.
L'esempio seguente crea una cartella di lavoro, scrive i valori 5, -3, 8, -2, 6 nelle celle da A1 a E1 e aggiunge una sparkline di tipo linea nella cella F1 che traccia tali valori. Personalizza inoltre il colore della linea in rosso e abilita gli indicatori per i punti massimo e minimo.

```python
import aspose.cells as ac
import System.Drawing
# Step 1: Create a Workbook and get the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "WinLoss"
# Step 2: Populate sample data in row 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)
# Step 3: Build a CellArea pointing to F1 (column 5, row 0)
dest = ac.CellArea()
dest.start_column = 5   # F
dest.end_column = 5
dest.start_row = 0      # row 1
dest.end_row = 0
# Step 4: Add a Win/Loss sparkline (SparklineType.Stacked)
group_index = worksheet.sparkline_groups.add(
    ac.SparklineType.Stacked,
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
high_color.color = System.Drawing.Color.Green
group.high_point_color = high_color
# Set the low-point color to red
low_color = workbook.create_cells_color()
low_color.color = System.Drawing.Color.Red
group.low_point_color = low_color
# Set the negative-point color to orange
neg_color = workbook.create_cells_color()
neg_color.color = System.Drawing.Color.Orange
group.negative_points_color = neg_color
# Set the default series color (used for positive bars)
series_color = workbook.create_cells_color()
series_color.color = System.Drawing.Color.SteelBlue
group.series_color = series_color
# Step 6: Save the workbook
workbook.save("output_winloss.xlsx")
print("Workbook saved successfully: output_winloss.xlsx")
```

## **Sparklines di tipo Colonna**
Una sparkline di tipo colonna rende ciascun punto dati come una barra verticale. Questo la rende particolarmente adatta a dati la cui magnitudine è significativa — ad esempio, cifre di vendite mensili o conteggi. In Aspose.Cells, crei una sparkline di tipo colonna passando `SparklineType.Column` al metodo `sparkline_groups.add`.
La procedura rispecchia l'esempio della sparkline di tipo linea:
1. Crea una nuova `Workbook` e accedi al primo foglio di lavoro.
3. Crea un `CellArea` che descriva la cella di destinazione.
4. Chiama `worksheet.sparkline_groups.add(SparklineType.Column, "A1:E1", False, dest)`.
5. Facoltativamente, personalizza il `SparklineGroup` risultante — ad esempio, impostando `group.type` per confermare il tipo, oppure modificando il colore delle barre.
6. Salva la cartella di lavoro in un file di output separato in modo che non sovrascriva l'esempio della sparkline di tipo linea.
L'esempio seguente scrive i valori 5, -3, 8, -2, 6 in A1:E1 e visualizza una sparkline di tipo colonna in F1. I valori negativi vengono disegnati come barre rivolte verso il basso e i valori positivi come barre rivolte verso l'alto, il che rende facile individuare a colpo d'occhio i contributi positivi e negativi.

```python
import aspose.cells as ac
# Passo 1: Crea una cartella di lavoro e ottieni il primo foglio di lavoro
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Passo 2: Scrivi valori di esempio in A1:E1
values = [5, -3, 8, -2, 6]
for i in range(len(values)):
    worksheet.cells[0, i].put_value(values[i])
# Passo 3: Costruisci un CellArea che punta a F1 (indice colonna 5, indice riga 0)
dest = ac.CellArea()
dest.start_column = 5
dest.end_column = 5
dest.start_row = 0
dest.end_row = 0
# Passo 4: Aggiungi una sparkline di tipo Column alla cella di destinazione
idx = worksheet.sparkline_groups.add(
    ac.SparklineType.COLUMN, "A1:E1", False, dest)
group = worksheet.sparkline_groups[idx]
# Passo 5: Conferma il tipo di sparkline leggendo group.Type
print("Sparkline Type added: " + str(group.type))
# Passo 6: Salva la cartella di lavoro
workbook.save("output_column.xlsx")
print("Workbook saved as output_column.xlsx")
```

## **Sparklines di tipo Win/Loss**
Una sparkline di tipo win/loss è una variante speciale della sparkline di tipo colonna progettata per mostrare solo due esiti: un valore positivo viene disegnato come barra "in alto" (una vittoria) e un valore pari a zero o negativo viene disegnato come barra "in basso" (una sconfitta). Le sparklines win/loss sono comunemente utilizzate per visualizzare sequenze di vittorie e sconfitte, risultati di superamento/fallimento o qualsiasi esito binario nel tempo.
In Aspose.Cells, una sparkline di tipo win/loss viene creata passando `SparklineType.Stacked` al metodo `sparkline_groups.add`. (Nonostante il nome, `SparklineType.Stacked` è il valore enum utilizzato per richiedere il rendering win/loss.)
1. Crea una nuova `Workbook` e accedi al primo foglio di lavoro.
2. Popola l'intervallo di origine. Poiché le sparklines win/loss trattano ogni valore come una vittoria o una sconfitta, la magnitudine del valore non è rilevante — solo il suo segno lo è. I valori positivi diventano barre verso l'alto e i valori non positivi diventano barre verso il basso.
3. Crea un `CellArea` che descriva la cella di destinazione.
4. Chiama `worksheet.sparkline_groups.add(SparklineType.Stacked, "A1:E1", False, dest)`.
5. Facoltativamente, personalizza il `SparklineGroup` restituito, ad esempio impostando colori di accento per le barre di vittoria e sconfitta.
6. Salva la cartella di lavoro con un nome file distinto in modo che tutti e tre gli esempi possano coesistere sul disco.

```python
import aspose.cells as ac
import System.Drawing
# Step 1: Create a Workbook and get the first worksheet
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells
# Step 2: Write sample values 5, -3, 8, -2, 6 into cells A1:E1
cells["A1"].put_value(5)
cells["B1"].put_value(-3)
cells["C1"].put_value(8)
cells["D1"].put_value(-2)
cells["E1"].put_value(6)
# Step 3: Build a CellArea pointing to destination cell F1
dest = ac.CellArea()
dest.start_column = 5   # column F (0-indexed)
dest.end_column = 5
dest.start_row = 0      # row 1 (0-indexed)
dest.end_row = 0
# Step 4: Add a Line sparkline from A1:E1 into F1
# SparklineGroups.Add returns the index of the newly added group
index = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, dest)
group = worksheet.sparkline_groups[index]
# Step 5: Create a red CellsColor and assign it to the sparkline line color
red = workbook.create_cells_color()
red.color = System.Drawing.Color.Red
group.series_color = red
# Step 6: Enable high-point and low-point markers
group.show_high_point = True
group.show_low_point = True
# Step 7: Save the workbook
workbook.save("output_line.xlsx")
```

## **Combinazione dei tre tipi di Sparkline**
L'esempio combinato seguente crea una singola cartella di lavoro, popola la riga 1 con i valori 5, -3, 8, -2, 6, e quindi aggiunge tre gruppi di sparkline nelle celle F1, F2 e F3 — uno per ciascun tipo — in modo che il file risultante dimostri tutti e tre gli stili di sparkline contemporaneamente.

```python
import aspose.cells as ac
import System.Drawing
# Passo 1: Crea una cartella di lavoro e ottieni il primo foglio di lavoro
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Passo 2: Popola i dati di esempio nella riga 1 (A1:E1)
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)
# Passo 3: Aggiungi un gruppo di sparkline lineari in F1
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)
line_group = worksheet.sparkline_groups[line_idx]
# Personalizza il colore della sparkline lineare tramite CellsColor
line_color = workbook.create_cells_color()
line_color.color = System.Drawing.Color.Blue
line_group.series_color = line_color
# Passo 4: Aggiungi un gruppo di sparkline a colonne in F2
column_area = ac.CellArea()
column_area.start_column = 5
column_area.end_column = 5
column_area.start_row = 1
column_area.end_row = 1
column_idx = worksheet.sparkline_groups.add(ac.SparklineType.COLUMN, "A1:E1", False, column_area)
column_group = worksheet.sparkline_groups[column_idx]
# Personalizza il colore della serie di sparkline a colonne
column_color = workbook.create_cells_color()
column_color.color = System.Drawing.Color.Green
column_group.series_color = column_color
# Passo 5: Aggiungi un gruppo di sparkline Win/Loss (impilate) in F3
stacked_area = ac.CellArea()
stacked_area.start_column = 5
stacked_area.end_column = 5
stacked_area.start_row = 2
stacked_area.end_row = 2
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)
stacked_group = worksheet.sparkline_groups[stacked_idx]
# Personalizza il colore della serie di sparkline win/loss
stacked_color = workbook.create_cells_color()
stacked_color.color = System.Drawing.Color.DarkOrange
stacked_group.series_color = stacked_color
# Passo 6: Salva la cartella di lavoro
workbook.save("output_all.xlsx")
```

## **Personalizzazione dell'aspetto delle Sparkline**
Una volta che un `SparklineGroup` è stato creato e aggiunto a `worksheet.sparkline_groups`, puoi leggere o modificare diverse delle sue proprietà visive prima di salvare la cartella di lavoro. Le proprietà più comunemente personalizzate sono:
- **`group.type`** — il `SparklineType` (Line, Column o Stacked). Viene impostato quando il gruppo viene aggiunto, ma puoi rileggerlo per confermarlo.
- **`group.line.color`** — il colore della linea, espresso come un `CellsColor` creato tramite `workbook.create_cells_color()`. Questa è la proprietà da utilizzare per il colore del tratto della sparkline di tipo linea.
- **`group.line.weight`** — lo spessore della linea in punti. Valori più alti producono linee più spesse.
- **Indicatori dei punti massimo/minimo** — flag che attivano piccoli indicatori sui punti dati più alti e più bassi, utili per evidenziare gli estremi.
- **Indicatori dei punti primo/ultimo/negativo** — flag che attivano/disattivano gli indicatori sui punti dati primo, ultimo e negativo.
Per modificare un colore, crea sempre un'istanza di `CellsColor` e assegnala alla proprietà pertinente. Le proprietà del colore delle sparkline richiedono il tipo `CellsColor` da `aspose.cells.drawing` — non assegnare direttamente un valore di colore grezzo. Il metodo `sparkline_groups.add` stesso restituisce un oggetto `SparklineGroup` completamente tipizzato, così puoi concatenare le assegnazioni delle proprietà sul valore restituito oppure memorizzarlo in una variabile locale e personalizzarlo prima di salvare.
{{% /alert %}}

{{< app/cells/assistant language="python" >}}