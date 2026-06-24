---
title: Sparkline in Aspose.Cells for .NET
linktitle: Sparklines
description: Aspose.Cells è una libreria .NET per lavorare con file di fogli di calcolo che supporta la creazione di sparkline — piccoli grafici posizionati all'interno delle celle del foglio di lavoro. Questo articolo spiega come aggiungere e personalizzare sparkline a linea, a colonna e win/loss utilizzando la libreria Aspose.Cells.
keywords: Aspose.Cells, libreria .NET, foglio di calcolo, sparkline, sparkline a linea, sparkline a colonna, sparkline win/loss, SparklineGroup, SparklineType
type: docs
weight: 195
url: /it/net/creating-sparklines/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supporta la creazione di sparkline all'interno delle celle del foglio di lavoro. Le sparkline sono piccoli grafici che si adattano a una singola cella, fornendo una rapida rappresentazione visiva delle tendenze dei dati. Aspose.Cells supporta sparkline a linea, a colonna e win/loss, e ciascuna può essere personalizzata per quanto riguarda colore, spessore della linea, punti massimo/minimo e marcatori.

{{% /alert %}}

## **Introduzione**

Le sparkline sono piccoli grafici all'interno delle celle che sono utili quando si desidera visualizzare una rapida tendenza accanto a una riga o colonna di dati senza occupare lo spazio di un grafico completo. Excel supporta tre tipi di sparkline: **linea**, **colonna** e **win/loss**. Aspose.Cells rispecchia questa funzionalità attraverso le API `SparklineGroup` e `SparklineGroupCollection` presenti nel namespace `Aspose.Cells.Charts`.

In Aspose.Cells, ogni sparkline che si aggiunge viene creata tramite `worksheet.SparklineGroups.Add(...)`, che restituisce un oggetto `SparklineGroup`. È quindi possibile utilizzare tale oggetto per impostare il tipo di sparkline, l'intervallo di dati, la cella di destinazione e le proprietà visive come il colore della linea, lo spessore della linea, i marcatori e gli indicatori dei punti massimo/minimo.

{{% alert color="primary" %}}

Un singolo `SparklineGroup` può contenere una o più sparkline che condividono lo stesso stile. Quando si chiama `Add` e si passa una riga di dati più una singola cella di destinazione, si ottiene una sparkline all'interno di tale cella. Se l'intervallo di destinazione è più ampio di una cella, viene disegnata una sparkline separata in ogni cella di destinazione, tutte utilizzando lo stesso stile e intervallo di dati.

{{% /alert %}}

Questo articolo illustra ciascuno dei tre tipi di sparkline supportati da Aspose.Cells — **Linea**, **Colonna** e **Win/Loss** — e mostra come aggiungerli, personalizzarne i colori e salvare la cartella di lavoro risultante.

## **Sparkline a Linea**

Una sparkline a linea disegna una linea continua attraverso i punti dati di una serie, rendendola la scelta più naturale per mostrare le tendenze nel tempo. In Aspose.Cells, una sparkline a linea viene creata passando `SparklineType.Line` al metodo `SparklineGroups.Add`.

Il flusso di lavoro è lo stesso di qualsiasi altro tipo di sparkline:

1. Creare una nuova `Workbook` e accedere al primo foglio di lavoro.
2. Popolare una riga di dati di origine (ad esempio, riga 1, colonne da A a E) con i valori che si desidera visualizzare.
3. Creare un `CellArea` che descriva la cella di destinazione in cui verrà disegnata la sparkline.
4. Chiamare `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`. Il terzo argomento — `false` — indica ad Aspose.Cells che l'intervallo di dati è orizzontale (una riga), non verticale (una colonna).
5. Facoltativamente, personalizzare il `SparklineGroup` restituito. Per una sparkline a linea è possibile impostare il colore della linea utilizzando `group.Line.Color` (che si aspetta un `CellsColor` da `Aspose.Cells.Drawing`), regolare lo spessore della linea e attivare/disattivare i marcatori dei punti massimo/minimo.
6. Salvare la cartella di lavoro.

L'esempio seguente crea una cartella di lavoro, scrive i valori 5, -3, 8, -2, 6 nelle celle da A1 a E1 e aggiunge una sparkline a linea nella cella F1 che traccia tali valori. Personalizza inoltre il colore della linea in rosso e abilita i marcatori per i punti massimo e minimo.

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

            // Passo 3: Crea un CellArea che punta alla cella di destinazione F1
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // colonna F (indicizzata a 0)
            dest.EndColumn = 5;
            dest.StartRow = 0;      // riga 1 (indicizzata a 0)
            dest.EndRow = 0;

            // Passo 4: Aggiungi una sparkline Linea da A1:E1 a F1
            // SparklineGroups.Add restituisce l'indice del gruppo appena aggiunto
            int index = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest);
            SparklineGroup group = worksheet.SparklineGroups[index];

            // Passo 5: Crea un CellsColor rosso e assegnalo al colore della linea della sparkline
            CellsColor red = workbook.CreateCellsColor();
            red.Color = System.Drawing.Color.Red;
            group.SeriesColor = red;

            // Passo 6: Abilita i marcatori del punto alto e del punto basso
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

1. Creare una nuova `Workbook` e accedere al primo foglio di lavoro.
2. Popolare lo stesso intervallo di origine (A1:E1) con i valori che si desidera visualizzare.
3. Creare un `CellArea` che descriva la cella di destinazione.
4. Chiamare `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`.
5. Facoltativamente, personalizzare il `SparklineGroup` risultante — ad esempio, impostando `group.Type` per confermare il tipo, o modificando il colore delle barre.
6. Salvare la cartella di lavoro in un file di output separato in modo che non sovrascriva l'esempio della sparkline a linea.

L'esempio seguente scrive i valori 5, -3, 8, -2, 6 in A1:E1 e visualizza una sparkline a colonna in F1. I valori negativi sono disegnati come barre rivolte verso il basso e i valori positivi come barre rivolte verso l'alto, il che rende facile individuare a colpo d'occhio i contributi positivi e negativi.

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

            // Passo 4: Aggiungi una sparkline a colonne alla cella di destinazione
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

Una sparkline win/loss è una variante speciale della sparkline a colonna progettata per mostrare solo due risultati: un valore positivo viene disegnato come una barra "in alto" (una vittoria) e un valore zero o negativo viene disegnato come una barra "in basso" (una sconfitta). Le sparkline win/loss sono comunemente utilizzate per visualizzare sequenze di vittorie e sconfitte, risultati di superamento/fallimento o qualsiasi esito binario nel tempo.

In Aspose.Cells, una sparkline win/loss viene creata passando `SparklineType.Stacked` al metodo `SparklineGroups.Add`. (Nonostante il nome, `SparklineType.Stacked` è il valore enum utilizzato per richiedere il rendering win/loss.)

La procedura è la stessa degli altri due tipi:

1. Creare una nuova `Workbook` e accedere al primo foglio di lavoro.
2. Popolare l'intervallo di origine. Poiché le sparkline win/loss trattano ogni valore come una vittoria o una sconfitta, la magnitudine del valore non è importante — solo il suo segno. I valori positivi diventano barre verso l'alto e i valori non positivi diventano barre verso il basso.
3. Creare un `CellArea` che descriva la cella di destinazione.
4. Chiamare `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Facoltativamente, personalizzare il `SparklineGroup` restituito, ad esempio impostando i colori di accento per le barre di vittoria e sconfitta.
6. Salvare la cartella di lavoro con un nome file distinto in modo che tutti e tre gli esempi possano coesistere sul disco.

L'esempio seguente utilizza gli stessi dati di input delle due sezioni precedenti. I valori 5, -3, 8, -2, 6 sono interpretati come vittoria, sconfitta, vittoria, sconfitta, vittoria — e la sparkline disegnata in F1 riflette esattamente tale schema.

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
            // Passaggio 1: Crea una cartella di lavoro e ottieni il primo foglio di lavoro
            Workbook workbook = new Workbook();
            Worksheet worksheet = workbook.Worksheets[0];
            worksheet.Name = "WinLoss";

            // Passaggio 2: Popola i dati di esempio nella riga 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
            worksheet.Cells["A1"].PutValue(5);
            worksheet.Cells["B1"].PutValue(-3);
            worksheet.Cells["C1"].PutValue(8);
            worksheet.Cells["D1"].PutValue(-2);
            worksheet.Cells["E1"].PutValue(6);

            // Passaggio 3: Costruisci un CellArea che punta a F1 (colonna 5, riga 0)
            CellArea dest = new CellArea();
            dest.StartColumn = 5;   // F
            dest.EndColumn = 5;
            dest.StartRow = 0;      // riga 1
            dest.EndRow = 0;

            // Passaggio 4: Aggiungi uno sparkline Win/Loss (SparklineType.Stacked)
            int groupIndex = worksheet.SparklineGroups.Add(
                SparklineType.Stacked,
                "A1:E1",
                false,
                dest);
            SparklineGroup group = worksheet.SparklineGroups[groupIndex];

            // Passaggio 5: Personalizza il gruppo di sparkline
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

            // Passaggio 6: Salva la cartella di lavoro
            workbook.Save("output_winloss.xlsx");

            Console.WriteLine("Workbook saved successfully: output_winloss.xlsx");
        }
    }
}
```

## **Combinazione di Tutti e Tre i Tipi di Sparkline**

I tre esempi precedenti producono ciascuno la propria cartella di lavoro in modo che i file di output siano facili da ispezionare in isolamento. In uno scenario reale, tuttavia, si vorra spesso confrontare più serie di dati affiancate. Il modo più pulito per farlo è inserire più gruppi di sparkline nello stesso foglio di lavoro, con ciascun gruppo che visualizza uno stile diverso.

È possibile aggiungere più oggetti `SparklineGroup` alla stessa `SparklineGroupCollection`, e ciascun gruppo può avere come destinazione una cella diversa o un intervallo diverso. Ad esempio, è possibile posizionare una sparkline a linea in F1, una sparkline a colonna in F2 e una sparkline win/loss in F3 — tutte leggendo dagli stessi dati di origine nella riga 1 — in modo che il lettore possa vedere tre diversi trattamenti visivi degli stessi numeri.

L'esempio combinato seguente crea una singola cartella di lavoro, popola la riga 1 con i valori 5, -3, 8, -2, 6, e quindi aggiunge tre gruppi di sparkline nelle celle F1, F2 e F3 — uno di ciascun tipo — in modo che il file risultante dimostri tutti e tre gli stili di sparkline contemporaneamente.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Charts;

// Passo 1: Creare una cartella di lavoro e ottenere il primo foglio di lavoro
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Passo 2: Popolare i dati di esempio nella riga 1 (A1:E1)
worksheet.Cells["A1"].PutValue(5);
worksheet.Cells["B1"].PutValue(-3);
worksheet.Cells["C1"].PutValue(8);
worksheet.Cells["D1"].PutValue(-2);
worksheet.Cells["E1"].PutValue(6);

// Passo 3: Aggiungere un gruppo di sparkline a linee in F1
CellArea lineArea = new CellArea();
lineArea.StartColumn = 5;
lineArea.EndColumn = 5;
lineArea.StartRow = 0;
lineArea.EndRow = 0;
int lineIdx = worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, lineArea);
SparklineGroup lineGroup = worksheet.SparklineGroups[lineIdx];

// Personalizzare il colore della sparkline a linee tramite CellsColor
CellsColor lineColor = workbook.CreateCellsColor();
lineColor.Color = System.Drawing.Color.Blue;
lineGroup.SeriesColor = lineColor;

// Passo 4: Aggiungere un gruppo di sparkline a colonne in F2
CellArea columnArea = new CellArea();
columnArea.StartColumn = 5;
columnArea.EndColumn = 5;
columnArea.StartRow = 1;
columnArea.EndRow = 1;
int columnIdx = worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, columnArea);
SparklineGroup columnGroup = worksheet.SparklineGroups[columnIdx];

// Personalizzare il colore della serie di sparkline a colonne
CellsColor columnColor = workbook.CreateCellsColor();
columnColor.Color = System.Drawing.Color.Green;
columnGroup.SeriesColor = columnColor;

// Passo 5: Aggiungere un gruppo di sparkline Win/Loss (in pila) in F3
CellArea stackedArea = new CellArea();
stackedArea.StartColumn = 5;
stackedArea.EndColumn = 5;
stackedArea.StartRow = 2;
stackedArea.EndRow = 2;
int stackedIdx = worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, stackedArea);
SparklineGroup stackedGroup = worksheet.SparklineGroups[stackedIdx];

// Personalizzare il colore della serie di sparkline win/loss
CellsColor stackedColor = workbook.CreateCellsColor();
stackedColor.Color = System.Drawing.Color.DarkOrange;
stackedGroup.SeriesColor = stackedColor;

// Passo 6: Salvare la cartella di lavoro
workbook.Save("output_all.xlsx");
```

{{% alert color="primary" %}}

Quando si combinano più gruppi di sparkline in un singolo foglio di lavoro, ciascun gruppo è indipendente. Possono condividere lo stesso intervallo di origine o utilizzare intervalli di origine diversi, e possono essere stilizzati indipendentemente. Questo rende facile costruire un piccolo "dashboard" di visualizzazioni all'interno delle celle direttamente all'interno di un foglio di lavoro esistente.

{{% /alert %}}

## **Personalizzazione dell'Aspetto delle Sparkline**

Una volta che un `SparklineGroup` è stato creato e aggiunto a `worksheet.SparklineGroups`, è possibile leggere o modificare diverse delle sue proprietà visive prima di salvare la cartella di lavoro. Le proprietà più comunemente personalizzate sono:

- **`group.Type`** — il `SparklineType` (Line, Column o Stacked). Viene impostato quando il gruppo viene aggiunto, ma è possibile rileggerlo per confermare.
- **`group.Line.Color`** — il colore della linea, espresso come `CellsColor` creato tramite `workbook.CreateCellsColor()`. Questa è la proprietà da utilizzare per il colore del tratto della sparkline a linea.
- **`group.Line.Weight`** — lo spessore della linea in punti. Valori più alti producono linee più spesse.
- **Marcatori dei punti massimo/minimo** — flag che attivano piccoli marcatori sui punti dati più alti e più bassi, utili per enfatizzare gli estremi.
- **Marcatori dei punti primo/ultimo/negativo** — flag che attivano/disattivano i marcatori sui punti dati primo, ultimo e negativo.

Per cambiare un colore, creare sempre un'istanza di `CellsColor` e assegnarla alla proprietà pertinente. Non assegnare un `System.Drawing.Color` direttamente alle proprietà del colore delle sparkline — si aspettano il tipo `CellsColor` da `Aspose.Cells.Drawing`. Il metodo `SparklineGroups.Add` stesso restituisce un oggetto `SparklineGroup` completamente tipizzato, quindi è possibile concatenare le assegnazioni delle proprietà sul valore restituito o memorizzarlo in una variabile locale e personalizzarlo prima del salvataggio.

## **Articoli Correlati**

- [Accesso alle Celle di un Foglio di Lavoro](/cells/it/net/accessing-cells-of-a-worksheet/)
- [Formattare le Celle del Foglio di Lavoro in una Cartella di Lavoro](/cells/it/net/format-worksheet-cells-in-a-workbook/)
- [Personalizzazione dei Grafici](/cells/it/net/customizing-charts/)
- [Creare Grafici Dinamici](/cells/it/net/create-dynamic-charts/)
- [Gestire i dati dei file Excel](/cells/it/net/cells-data/)

{{< app/cells/assistant language="csharp" >}}