---
title: Sparklines in Aspose.Cells for .NET
description: Aspose.Cells è una libreria .NET per lavorare con file di fogli di calcolo che supporta la creazione di sparkline — grafici in miniatura inseriti nelle celle del foglio di lavoro. Questo articolo spiega come aggiungere e personalizzare sparkline a linea, a colonna e win/loss utilizzando la libreria Aspose.Cells.
linktitle: Sparklines
keywords: Aspose.Cells, libreria .NET, foglio di calcolo, sparkline, sparkline a linea, sparkline a colonna, sparkline win/loss, SparklineGroup, SparklineType
type: docs
weight: 195
url: /it/net/creating-sparklines/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta la creazione di sparkline all'interno delle celle del foglio di lavoro. Le sparkline sono grafici in miniatura che si adattano a una singola cella, fornendo una rapida rappresentazione visiva degli andamenti dei dati. Aspose.Cells supporta sparkline a linea, a colonna e win/loss, e ciascuna può essere personalizzata per quanto riguarda colore, spessore della linea, punti massimi/minimi e marcatori.

## **Introduzione**
Le sparkline sono minuscoli grafici all'interno delle celle, utili quando si desidera visualizzare rapidamente un andamento accanto a una riga o colonna di dati senza occupare lo spazio di un grafico completo. Excel supporta tre tipi di sparkline: **linea**, **colonna** e **win/loss**. Aspose.Cells rispecchia questa funzionalità tramite le API `SparklineGroup` e `SparklineGroupCollection` presenti nel namespace `Aspose.Cells.Charts`.
In Aspose.Cells, ogni sparkline aggiunta viene creata tramite `worksheet.SparklineGroups.Add(...)`, che restituisce un oggetto `SparklineGroup`. È quindi possibile utilizzare tale oggetto per impostare il tipo di sparkline, l'intervallo di dati, la cella di destinazione e le proprietà visive come colore della linea, spessore della linea, marcatori e indicatori dei punti massimi/minimi.
Questo articolo illustra ciascuno dei tre tipi di sparkline supportati da Aspose.Cells — **Linea**, **Colonna** e **Win/Loss** — e mostra come aggiungerli, personalizzarne i colori e salvare la cartella di lavoro risultante.

## **Sparkline a Linea**
Una sparkline a linea disegna una linea continua attraverso i punti dati di una serie, rendendola la scelta più naturale per mostrare andamenti nel tempo. In Aspose.Cells, una sparkline a linea viene creata passando `SparklineType.Line` al metodo `SparklineGroups.Add`.
1. Creare un nuovo `Workbook` e accedere al primo foglio di lavoro.
2. Popolare una riga di dati di origine (ad esempio, riga 1, colonne da A a E) con i valori che si desidera visualizzare.
3. Creare un `CellArea` che descriva la cella di destinazione in cui verrà disegnata la sparkline.
4. Chiamare `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`. Il terzo argomento — `false` — indica ad Aspose.Cells che l'intervallo di dati è orizzontale (una riga), non verticale (una colonna).
5. Facoltativamente, personalizzare il `SparklineGroup` restituito. Per una sparkline a linea, è possibile impostare il colore della linea utilizzando `group.Line.Color` (che richiede un `CellsColor` da `Aspose.Cells.Drawing`), regolare lo spessore della linea e attivare/disattivare i marcatori dei punti massimi/minimi.
6. Salvare la cartella di lavoro.
L'esempio seguente crea una cartella di lavoro, scrive i valori 5, -3, 8, -2, 6 nelle celle da A1 a E1 e aggiunge una sparkline a linea nella cella F1 che traccia tali valori. Personalizza inoltre il colore della linea in rosso e abilita i marcatori per i punti massimi e minimi.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
namespace SparklineDemo
{
    public class Program
    {
        public static void Main()
        {
            // Passo 1: Crea una cartella di lavoro e ottieni il primo foglio di lavoro
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            Cells cells = worksheet.Cells;
            // Passo 2: Scrivi i valori di esempio 5, -3, 8, -2, 6 nelle celle A1:E1
            cells["A1"].PutValue(5);
            cells["B1"].PutValue(-3);
            cells["C1"].PutValue(8);
            cells["D1"].PutValue(-2);
            cells["E1"].PutValue(6);
            // Passo 3: Costruisci un CellArea che punta alla cella di destinazione F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // colonna F (indicizzata da 0)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // riga 1 (indicizzata da 0)
            dest.EndRow = 0;
            // Passo 4: Aggiungi una sparkline di tipo Line da A1:E1 in F1
            // SparklineGroups.Add restituisce l'indice del gruppo appena aggiunto
            int index = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[index];
            // Passo 5: Crea un CellsColor rosso e assegnalo al colore della linea della sparkline
            CellsColor red = workbook.CreateCellsColor();
            red.Color = System.Drawing.Color.Red;
            group.SeriesColor = red;
            // Passo 6: Abilita i marcatori del punto massimo e del punto minimo
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            // Passo 7: Salva la cartella di lavoro
            workbook.Save("output_line.xlsx");
        }
    }
}
```

## **Sparkline a Colonna**
Una sparkline a colonna rappresenta ciascun punto dati come una barra verticale. Questo la rende particolarmente adatta a dati la cui magnitudine è significativa — ad esempio, cifre di vendite mensili o conteggi. In Aspose.Cells, si crea una sparkline a colonna passando `SparklineType.Column` al metodo `SparklineGroups.Add`.
La procedura rispecchia l'esempio della sparkline a linea:
1. Creare un nuovo `Workbook` e accedere al primo foglio di lavoro.
2. Popolare una riga di dati di origine (ad esempio, riga 1, colonne da A a E) con i valori che si desidera visualizzare.
3. Creare un `CellArea` che descriva la cella di destinazione.
4. Chiamare `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`.
5. Facoltativamente, personalizzare il `SparklineGroup` risultante — ad esempio, impostando `group.Type` per confermare il tipo, o modificando il colore delle barre.
6. Salvare la cartella di lavoro in un file di output separato, così non sovrascrive l'esempio della sparkline a linea.
L'esempio seguente scrive i valori 5, -3, 8, -2, 6 in A1:E1 e rende una sparkline a colonna in F1. I valori negativi sono disegnati come barre rivolte verso il basso e i valori positivi come barre rivolte verso l'alto, il che rende facile individuare a colpo d'occhio i contributi positivi e negativi.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
namespace SparklineDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // Passo 1: Crea una cartella di lavoro e ottieni il primo foglio di lavoro
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            // Passo 2: Scrivi valori di esempio in A1:E1
            int[] values = { 5, -3, 8, -2, 6 };
            for (int i = 0; i < values.Length; i++)
            {
                worksheet.Cells[0, i].PutValue(values[i]);
            }
            // Passo 3: Costruisci un CellArea che punta a F1 (indice colonna 5, indice riga 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;
            dest.EndColumn = 5;
            dest.StartRow = 0;
            dest.EndRow = 0;
            // Passo 4: Aggiungi uno sparkline di tipo colonna alla cella di destinazione
            int idx = worksheet.SparklineGroups.Add(
                SparklineType.Column, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[idx];
            // Passo 5: Conferma il tipo di sparkline leggendo group.Type
            Console.WriteLine("Sparkline Type added: " + group.Type);
            // Passo 6: Salva la cartella di lavoro
            workbook.Save("output_column.xlsx");
            Console.WriteLine("Workbook saved as output_column.xlsx");
        }
    }
}
```

## **Sparkline Win/Loss**
Una sparkline win/loss è una variante speciale della sparkline a colonna, progettata per mostrare solo due esiti: un valore positivo è disegnato come una barra "in alto" (una vittoria) e un valore zero o negativo è disegnato come una barra "in basso" (una sconfitta). Le sparkline win/loss sono comunemente utilizzate per visualizzare sequenze di vittorie e sconfitte, risultati di pass/fail, o qualsiasi esito binario nel tempo.
In Aspose.Cells, una sparkline win/loss viene creata passando `SparklineType.Stacked` al metodo `SparklineGroups.Add`. (Nonostante il nome, `SparklineType.Stacked` è il valore enum utilizzato per richiedere il rendering win/loss.)
1. Creare un nuovo `Workbook` e accedere al primo foglio di lavoro.
2. Popolare l'intervallo di origine. Poiché le sparkline win/loss trattano ogni valore come una vittoria o una sconfitta, la magnitudine del valore non è rilevante — conta solo il suo segno. I valori positivi diventano barre in alto e i valori non positivi diventano barre in basso.
3. Creare un `CellArea` che descriva la cella di destinazione.
4. Chiamare `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Facoltativamente, personalizzare il `SparklineGroup` restituito, ad esempio impostando colori di accento per le barre di vittoria e sconfitta.
6. Salvare la cartella di lavoro con un nome file distinto, così tutti e tre gli esempi possono coesistere sul disco.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
using Aspose.Cells.Drawing;
namespace SparklineDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            // Passo 1: Crea una cartella di lavoro e ottieni il primo foglio di lavoro
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            worksheet.Name = "WinLoss";
            // Passo 2: Popola i dati di esempio nella riga 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
            worksheet.Cells["A1"].PutValue(5);
            worksheet.Cells["B1"].PutValue(-3);
            worksheet.Cells["C1"].PutValue(8);
            worksheet.Cells["D1"].PutValue(-2);
            worksheet.Cells["E1"].PutValue(6);
            // Passo 3: Costruisci un CellArea che punta a F1 (colonna 5, riga 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // F
            dest.EndColumn = 5;
            dest.StartRow = 0;      // riga 1
            dest.EndRow = 0;
            // Passo 4: Aggiungi uno sparkline Win/Loss (SparklineType.Stacked)
            int groupIndex = worksheet.SparklineGroups.Add(
                SparklineType.Stacked,
                "A1:E1",
                false,
                dest);
            SparklineGroup group = worksheet.SparklineGroups[groupIndex];
            // Passo 5: Personalizza il gruppo di sparkline
            // Abilita i marcatori dei punti alti e bassi
            group.ShowHighPoint = true;
            group.ShowLowPoint = true;
            group.ShowNegativePoints = true;
            // Imposta il colore del punto alto su verde
            CellsColor highColor = workbook.CreateCellsColor();
            highColor.Color = System.Drawing.Color.Green;
            group.HighPointColor = highColor;
            // Imposta il colore del punto basso su rosso
            CellsColor lowColor = workbook.CreateCellsColor();
            lowColor.Color = System.Drawing.Color.Red;
            group.LowPointColor = lowColor;
            // Imposta il colore del punto negativo su arancione
            CellsColor negColor = workbook.CreateCellsColor();
            negColor.Color = System.Drawing.Color.Orange;
            group.NegativePointsColor = negColor;
            // Imposta il colore predefinito della serie (usato per le barre positive)
            CellsColor seriesColor = workbook.CreateCellsColor();
            seriesColor.Color = System.Drawing.Color.SteelBlue;
            group.SeriesColor = seriesColor;
            // Passo 6: Salva la cartella di lavoro
            workbook.Save("output_winloss.xlsx");
            Console.WriteLine("Workbook saved successfully: output_winloss.xlsx");
        }
    }
}
```

## **Combinazione dei Tre Tipi di Sparkline**
L'esempio combinato di seguito crea una singola cartella di lavoro, popola la riga 1 con i valori 5, -3, 8, -2, 6, quindi aggiunge tre gruppi di sparkline nelle celle F1, F2 e F3 — uno per ciascun tipo — in modo che il file risultante dimostri tutti e tre gli stili di sparkline contemporaneamente.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;
// Step 1: Creare una cartella di lavoro e ottenere il primo foglio di lavoro
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
// Step 2: Popolare i dati di esempio nella riga 1 (A1:E1)
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);
// Step 3: Aggiungere un gruppo di sparkline di tipo Linea in F1
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.SparklineGroups[lineIdx];
// Personalizzare il colore della sparkline di tipo Linea tramite CellsColor
CellsColor lineColor = workbook.CreateCellsColor();
lineColor.Color = System.Drawing.Color.Blue;
lineGroup.SeriesColor = lineColor;
// Step 4: Aggiungere un gruppo di sparkline di tipo Colonna in F2
CellArea columnArea = new CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.SparklineGroups[columnIdx];
// Personalizzare il colore della serie della sparkline di tipo Colonna
CellsColor columnColor = workbook.CreateCellsColor();
columnColor.Color = System.Drawing.Color.Green;
columnGroup.SeriesColor = columnColor;
// Step 5: Aggiungere un gruppo di sparkline Win/Loss (Stacked) in F3
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.SparklineGroups[stackedIdx];
// Personalizzare il colore della serie della sparkline win/loss
CellsColor stackedColor = workbook.CreateCellsColor();
stackedColor.Color = System.Drawing.Color.DarkOrange;
stackedGroup.SeriesColor = stackedColor;
// Step 6: Salvare la cartella di lavoro
workbook.Save("output_all.xlsx");
```

## **Personalizzazione dell'Aspetto delle Sparkline**
Una volta che un `SparklineGroup` è stato creato e aggiunto a `worksheet.SparklineGroups`, è possibile leggere o modificare diverse proprietà visive prima di salvare la cartella di lavoro. Le proprietà più comunemente personalizzate sono:
- **`group.Type`** — il `SparklineType` (Line, Column o Stacked). Viene impostato quando il gruppo viene aggiunto, ma è possibile rileggerlo per conferma.
- **`group.Line.Color`** — il colore della linea, espresso come `CellsColor` creato tramite `workbook.CreateCellsColor()`. Questa è la proprietà da utilizzare per il colore del tratto della sparkline a linea.
- **`group.Line.Weight`** — lo spessore della linea in punti. Valori più alti producono linee più spesse.
- **Marcatori dei punti massimi/minimi** — flag che attivano piccoli marcatori sui punti dati più alti e più bassi, utili per evidenziare gli estremi.
- **Marcatori dei punti primo/ultimo/negativo** — flag che attivano/disattivano i marcatori sui punti dati primo, ultimo e negativo.
Per modificare un colore, creare sempre un'istanza di `CellsColor` e assegnarla alla proprietà pertinente. Non assegnare un `System.Drawing.Color` direttamente alle proprietà del colore della sparkline — queste si aspettano il tipo `CellsColor` da `Aspose.Cells.Drawing`. Il metodo `SparklineGroups.Add` stesso restituisce un oggetto `SparklineGroup` completamente tipizzato, quindi è possibile concatenare le assegnazioni di proprietà sul valore restituito o memorizzarlo in una variabile locale e personalizzarlo prima di salvare.
{{% /alert %}}

## Articoli Correlati
- [Convertire Sparkline in Immagine e HTML in Aspose.Cells for .NET](/cells/it/net/convert-sparkline-to-image-and-html/)
- [Aggiungere Campi Filtro a una Tabella Pivot in Aspose.Cells for .NET](/cells/it/net/add-page-field-in-pivot-table/)
- [Applicare Stili alle Tabelle Pivot in Aspose.Cells for .NET](/cells/it/net/apply-style-to-pivot-table/)
- [Modificare il Layout dei Campi Pagina nella Tabella Pivot](/cells/it/net/change-page-field-layout/)
- [Conversione di Excel in Formato OFD](/cells/it/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}