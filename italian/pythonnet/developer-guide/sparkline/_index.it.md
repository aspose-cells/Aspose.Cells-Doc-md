---
title: Sparkline in Aspose.Cells for Python via .NET
linktitle: Sparkline
description: Aspose.Cells è una libreria Python per lavorare con file di fogli di calcolo che supporta la creazione di sparkline — grafici in miniatura posizionati all'interno delle celle del foglio di lavoro. Questo articolo spiega come aggiungere e personalizzare sparkline a linea, colonna e vincita/perdita utilizzando la libreria Aspose.Cells.
keywords: Aspose.Cells, libreria Python, foglio di calcolo, sparkline, sparkline a linea, sparkline a colonna, sparkline vincita/perdita, SparklineGroup, SparklineType
type: docs
weight: 195
url: /it/python-net/creating-sparklines/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supporta la creazione di sparkline all'interno delle celle del foglio di lavoro. Le sparkline sono grafici in miniatura che si adattano a una singola cella, fornendo una rapida rappresentazione visiva delle tendenze dei dati. Aspose.Cells supporta sparkline a linea, colonna e vincita/perdita, e ognuna può essere personalizzata per quanto riguarda colore, spessore della linea, punti massimo/minimo e marcatori.

{{% /alert %}}

## **Introduzione**

Le sparkline sono piccoli grafici all'interno delle celle che sono utili quando si desidera visualizzare una rapida tendenza accanto a una riga o colonna di dati senza occupare lo spazio di un grafico completo. Excel supporta tre tipi di sparkline: **linea**, **colonna** e **vincita/perdita**. Aspose.Cells rispecchia questa funzionalità attraverso le API `SparklineGroup` e `SparklineGroupCollection` presenti nel namespace `aspose.cells.charts`.

In Aspose.Cells, ogni sparkline che si aggiunge viene creata tramite `worksheet.sparkline_groups.add(...)`, che restituisce un oggetto `SparklineGroup`. È quindi possibile utilizzare tale oggetto per impostare il tipo di sparkline, l'intervallo di dati, la cella di destinazione e le proprietà visive come il colore della linea, lo spessore della linea, i marcatori e gli indicatori dei punti massimo/minimo.

{{% alert color="primary" %}}

Un singolo `SparklineGroup` può contenere una o più sparkline che condividono lo stesso stile. Quando si chiama `add` e si passa una riga di dati più una singola cella di destinazione, si ottiene una sparkline all'interno di quella cella. Se l'intervallo di destinazione è più ampio di una cella, viene disegnata una sparkline separata in ogni cella di destinazione, tutte utilizzando lo stesso stile e intervallo di dati.

{{% /alert %}}

Questo articolo illustra ciascuno dei tre tipi di sparkline supportati da Aspose.Cells — **Linea**, **Colonna** e **Vincita/Perdita** — e mostra come aggiungerli, personalizzarne i colori e salvare la cartella di lavoro risultante.

## **Sparkline a Linea**

Una sparkline a linea disegna una linea continua attraverso i punti dati di una serie, rendendola la scelta più naturale per mostrare le tendenze nel tempo. In Aspose.Cells, una sparkline a linea viene creata passando `SparklineType.Line` al metodo `sparkline_groups.add`.

Il flusso di lavoro è lo stesso di qualsiasi altro tipo di sparkline:

1. Creare un nuovo `Workbook` e accedere al primo foglio di lavoro.
2. Popolare una riga di dati di origine (ad esempio, riga 1, colonne da A a E) con i valori che si desidera visualizzare.
3. Costruire una `CellArea` che descriva la cella di destinazione in cui verrà disegnata la sparkline.
4. Chiamare `worksheet.sparkline_groups.add(SparklineType.Line, "A1:E1", False, dest)`. Il terzo argomento — `False` — indica ad Aspose.Cells che l'intervallo di dati è orizzontale (una riga), non verticale (una colonna).
5. Facoltativamente, personalizzare il `SparklineGroup` restituito. Per una sparkline a linea è possibile impostare il colore della linea utilizzando `group.line.color` (che si aspetta un `CellsColor` da `aspose.cells.drawing`), regolare lo spessore della linea e attivare/disattivare i marcatori dei punti massimo/minimo.
6. Salvare la cartella di lavoro.

L'esempio seguente crea una cartella di lavoro, scrive i valori 5, -3, 8, -2, 6 nelle celle da A1 a E1 e aggiunge una sparkline a linea nella cella F1 che traccia tali valori. Personalizza inoltre il colore della linea in rosso e abilita i marcatori per i punti massimo e minimo.

```python
import aspose.cells as ac
import System.Drawing

# Passo 1: Crea una cartella di lavoro e ottieni il primo foglio di lavoro
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells

# Passo 2: Scrivi i valori di esempio 5, -3, 8, -2, 6 nelle celle A1:E1
cells["A1"].put_value(5)
cells["B1"].put_value(-3)
cells["C1"].put_value(8)
cells["D1"].put_value(-2)
cells["E1"].put_value(6)

# Passo 3: Costruisci un CellArea che punti alla cella di destinazione F1
dest = ac.CellArea()
dest.start_column = 5   # colonna F (indicizzata a 0)
dest.end_column = 5
dest.start_row = 0      # riga 1 (indicizzata a 0)
dest.end_row = 0

# Passo 4: Aggiungi una sparkline Linea da A1:E1 in F1
# SparklineGroups.Add restituisce l'indice del gruppo appena aggiunto
index = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, dest)
group = worksheet.sparkline_groups[index]

# Passo 5: Crea un CellsColor rosso e assegnalo al colore della linea della sparkline
red = workbook.create_cells_color()
red.color = System.Drawing.Color.Red
group.series_color = red

# Passo 6: Abilita i marcatori del punto massimo e del punto minimo
group.show_high_point = True
group.show_low_point = True

# Passo 7: Salva la cartella di lavoro
workbook.save("output_line.xlsx")
```

## **Sparkline a Colonna**

Una sparkline a colonna rende ogni punto dati come una barra verticale. Questo la rende particolarmente adatta a dati la cui magnitudine è significativa — ad esempio, cifre di vendita mensili o conteggi. In Aspose.Cells, si crea una sparkline a colonna passando `SparklineType.Column` al metodo `sparkline_groups.add`.

La procedura rispecchia l'esempio della sparkline a linea:

1. Creare un nuovo `Workbook` e accedere al primo foglio di lavoro.
2. Popolare lo stesso intervallo di origine (A1:E1) con i valori che si desidera visualizzare.
3. Costruire una `CellArea` che descriva la cella di destinazione.
4. Chiamare `worksheet.sparkline_groups.add(SparklineType.Column, "A1:E1", False, dest)`.
5. Facoltativamente, personalizzare il `SparklineGroup` risultante — ad esempio, impostando `group.type` per confermare il tipo, o modificando il colore delle barre.
6. Salvare la cartella di lavoro in un file di output separato in modo che non sovrascriva l'esempio della sparkline a linea.

L'esempio seguente scrive i valori 5, -3, 8, -2, 6 in A1:E1 e rende una sparkline a colonna in F1. I valori negativi vengono disegnati come barre verso il basso e i valori positivi come barre verso l'alto, il che rende facile individuare a colpo d'occhio i contributi positivi e negativi.

```python
import aspose.cells as ac

# Passo 1: Crea una Workbook e ottieni il primo foglio di lavoro
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

# Passo 4: Aggiungi una sparkline a colonne alla cella di destinazione
idx = worksheet.sparkline_groups.add(
    ac.SparklineType.COLUMN, "A1:E1", False, dest)
group = worksheet.sparkline_groups[idx]

# Passo 5: Verifica il tipo di sparkline leggendo group.Type
print("Sparkline Type added: " + str(group.type))

# Passo 6: Salva la cartella di lavoro
workbook.save("output_column.xlsx")

print("Workbook saved as output_column.xlsx")
```

## **Sparkline Vincita/Perdita**

Una sparkline vincita/perdita è una variante speciale della sparkline a colonna progettata per mostrare solo due esiti: un valore positivo viene disegnato come una barra "in su" (una vittoria) e un valore zero o negativo viene disegnato come una barra "in giù" (una perdita). Le sparkline vincita/perdita sono comunemente utilizzate per visualizzare sequenze di vittorie e sconfitte, risultati superato/fallito o qualsiasi esito binario nel tempo.

In Aspose.Cells, una sparkline vincita/perdita viene creata passando `SparklineType.Stacked` al metodo `sparkline_groups.add`. (Nonostante il nome, `SparklineType.Stacked` è il valore enum utilizzato per richiedere il rendering vincita/perdita.)

La procedura è la stessa degli altri due tipi:

1. Creare un nuovo `Workbook` e accedere al primo foglio di lavoro.
2. Popolare l'intervallo di origine. Poiché le sparkline vincita/perdita trattano ogni valore come una vittoria o una perdita, la magnitudine del valore non è rilevante — conta solo il suo segno. I valori positivi diventano barre in su e i valori non positivi diventano barre in giù.
3. Costruire una `CellArea` che descriva la cella di destinazione.
4. Chiamare `worksheet.sparkline_groups.add(SparklineType.Stacked, "A1:E1", False, dest)`.
5. Facoltativamente, personalizzare il `SparklineGroup` restituito, ad esempio impostando i colori di accento per le barre di vittoria e perdita.
6. Salvare la cartella di lavoro con un nome file distinto in modo che tutti e tre gli esempi possano coesistere su disco.

L'esempio seguente utilizza gli stessi dati di input delle due sezioni precedenti. I valori 5, -3, 8, -2, 6 sono interpretati come vittoria, perdita, vittoria, perdita, vittoria — e la sparkline disegnata in F1 riflette esattamente tale schema.

```python
import aspose.cells as ac
import System.Drawing

# Passo 1: Crea una cartella di lavoro e ottieni il primo foglio di lavoro
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.name = "WinLoss"

# Passo 2: Popola i dati di esempio nella riga 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
worksheet.cells["A1"].put_value(5)
worksheet.cells["B1"].put_value(-3)
worksheet.cells["C1"].put_value(8)
worksheet.cells["D1"].put_value(-2)
worksheet.cells["E1"].put_value(6)

# Passo 3: Costruisci una CellArea che punta a F1 (colonna 5, riga 0)
dest = ac.CellArea()
dest.start_column = 5   # F
dest.end_column = 5
dest.start_row = 0      # riga 1
dest.end_row = 0

# Passo 4: Aggiungi una sparkline Win/Loss (SparklineType.Stacked)
group_index = worksheet.sparkline_groups.add(
    ac.SparklineType.Stacked,
    "A1:E1",
    False,
    dest)
group = worksheet.sparkline_groups[group_index]

# Passo 5: Personalizza il gruppo di sparkline
# Abilita i marcatori dei punti alti e bassi
group.show_high_point = True
group.show_low_point = True
group.show_negative_points = True

# Imposta il colore del punto alto su verde
high_color = workbook.create_cells_color()
high_color.color = System.Drawing.Color.Green
group.high_point_color = high_color

# Imposta il colore del punto basso su rosso
low_color = workbook.create_cells_color()
low_color.color = System.Drawing.Color.Red
group.low_point_color = low_color

# Imposta il colore del punto negativo su arancione
neg_color = workbook.create_cells_color()
neg_color.color = System.Drawing.Color.Orange
group.negative_points_color = neg_color

# Imposta il colore predefinito della serie (usato per le barre positive)
series_color = workbook.create_cells_color()
series_color.color = System.Drawing.Color.SteelBlue
group.series_color = series_color

# Passo 6: Salva la cartella di lavoro
workbook.save("output_winloss.xlsx")

print("Workbook saved successfully: output_winloss.xlsx")
```

## **Combinazione dei Tre Tipi di Sparkline**

I tre esempi precedenti producono ciascuno la propria cartella di lavoro in modo che i file di output siano facili da ispezionare in isolamento. In uno scenario reale, tuttavia, si vorrà spesso confrontare diverse serie di dati affiancate. Il modo più pulito per farlo è inserire più di un gruppo di sparkline nello stesso foglio di lavoro, con ciascun gruppo che rende uno stile diverso.

È possibile aggiungere più oggetti `SparklineGroup` alla stessa `SparklineGroupCollection`, e ciascun gruppo può puntare a una cella di destinazione diversa o a un intervallo diverso. Ad esempio, si potrebbe posizionare una sparkline a linea in F1, una sparkline a colonna in F2 e una sparkline vincita/perdita in F3 — tutte leggendo dagli stessi dati di origine nella riga 1 — in modo che il lettore possa vedere tre diversi trattamenti visivi degli stessi numeri.

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

# Passo 3: Aggiungi un gruppo di sparkline a linee in F1
line_area = ac.CellArea()
line_area.start_column = 5
line_area.end_column = 5
line_area.start_row = 0
line_area.end_row = 0
line_idx = worksheet.sparkline_groups.add(ac.SparklineType.LINE, "A1:E1", False, line_area)
line_group = worksheet.sparkline_groups[line_idx]

# Personalizza il colore della sparkline a linee tramite CellsColor
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

# Personalizza il colore della serie della sparkline a colonne
column_color = workbook.create_cells_color()
column_color.color = System.Drawing.Color.Green
column_group.series_color = column_color

# Passo 5: Aggiungi un gruppo di sparkline Win/Loss (in pila) in F3
stacked_area = ac.CellArea()
stacked_area.start_column = 5
stacked_area.end_column = 5
stacked_area.start_row = 2
stacked_area.end_row = 2
stacked_idx = worksheet.sparkline_groups.add(ac.SparklineType.STACKED, "A1:E1", False, stacked_area)
stacked_group = worksheet.sparkline_groups[stacked_idx]

# Personalizza il colore della serie della sparkline win/loss
stacked_color = workbook.create_cells_color()
stacked_color.color = System.Drawing.Color.DarkOrange
stacked_group.series_color = stacked_color

# Passo 6: Salva la cartella di lavoro
workbook.save("output_all.xlsx")
```

{{% alert color="primary" %}}

Quando si combinano più gruppi di sparkline in un singolo foglio di lavoro, ciascun gruppo è indipendente. Possono condividere lo stesso intervallo di origine o utilizzare intervalli di origine diversi, e possono essere stilizzati indipendentemente. Questo rende facile costruire un piccolo "cruscotto" di visualizzazioni in-cell direttamente all'interno di un foglio di lavoro esistente.

{{% /alert %}}

## **Personalizzazione dell'Aspetto delle Sparkline**

Una volta che un `SparklineGroup` è stato creato e aggiunto a `worksheet.sparkline_groups`, è possibile leggere o modificare diverse delle sue proprietà visive prima di salvare la cartella di lavoro. Le proprietà più comunemente personalizzate sono:

- **`group.type`** — il `SparklineType` (Line, Column o Stacked). Viene impostato quando il gruppo viene aggiunto, ma è possibile rileggerlo per confermare.
- **`group.line.color`** — il colore della linea, espresso come `CellsColor` creato tramite `workbook.create_cells_color()`. Questa è la proprietà da utilizzare per il colore del tratto della sparkline a linea.
- **`group.line.weight`** — lo spessore della linea in punti. Valori più alti producono linee più spesse.
- **Marcatori dei punti massimo/minimo** — flag che attivano piccoli marcatori sui punti dati più alti e più bassi, utili per enfatizzare gli estremi.
- **Marcatori dei punti primo/ultimo/negativo** — flag che attivano/disattivano i marcatori sui punti dati primo, ultimo e negativo.

Per modificare un colore, creare sempre un'istanza di `CellsColor` e assegnarla alla proprietà pertinente. Le proprietà di colore delle sparkline si aspettano il tipo `CellsColor` da `aspose.cells.drawing` — non assegnare direttamente un valore di colore grezzo ad esse. Il metodo `sparkline_groups.add` stesso restituisce un oggetto `SparklineGroup` completamente tipizzato, quindi è possibile concatenare le assegnazioni di proprietà sul valore restituito o memorizzarlo in una variabile locale e personalizzarlo prima di salvare.



{{< app/cells/assistant language="python" >}}