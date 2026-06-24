---
title: Sparklines in Aspose.Cells for C++
linktitle: Sparklines
description: Aspose.Cells è una libreria C++ per lavorare con file di fogli di calcolo che supporta la creazione di sparklines — piccoli grafici inseriti all'interno delle celle del foglio di lavoro. Questo articolo spiega come aggiungere e personalizzare sparklines a linee, colonne e win/loss utilizzando la libreria Aspose.Cells.
keywords: Aspose.Cells, libreria C++, foglio di calcolo, sparklines, sparkline a linee, sparkline a colonne, sparkline win/loss, SparklineGroup, SparklineType
type: docs
weight: 195
url: /it/cpp/creating-sparklines/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supporta la creazione di sparklines all'interno delle celle del foglio di lavoro. Le sparklines sono piccoli grafici che si adattano a una singola cella, fornendo una rapida rappresentazione visiva dell'andamento dei dati. Aspose.Cells supporta sparklines a linee, colonne e win/loss, e ciascuna può essere personalizzata per quanto riguarda colore, spessore della linea, punti massimi/minimi e indicatori.

{{% /alert %}}

## **Introduzione**

Le sparklines sono piccoli grafici all'interno delle celle, utili quando si desidera visualizzare rapidamente un andamento accanto a una riga o colonna di dati senza occupare lo spazio di un grafico completo. Excel supporta tre tipi di sparklines: **linea**, **colonna** e **win/loss**. Aspose.Cells rispecchia questa funzionalità tramite le API `SparklineGroup` e `SparklineGroupCollection` presenti nel namespace `Aspose.Cells.Charts`.

In Aspose.Cells, ogni sparkline aggiunta viene creata tramite `worksheet.SparklineGroups.Add(...)`, che restituisce un oggetto `SparklineGroup`. È quindi possibile utilizzare tale oggetto per impostare il tipo di sparkline, l'intervallo di dati, la cella di destinazione e le proprietà visive come colore della linea, spessore della linea, indicatori e indicatori dei punti massimo/minimo.

{{% alert color="primary" %}}

Un singolo `SparklineGroup` può contenere una o più sparklines che condividono lo stesso stile. Quando si chiama `Add` e si passa una riga di dati più una singola cella di destinazione, si ottiene una sparkline all'interno di quella cella. Se l'intervallo di destinazione è più ampio di una cella, viene disegnata una sparkline separata in ciascuna cella di destinazione, tutte utilizzando lo stesso stile e lo stesso intervallo di dati.

{{% /alert %}}

Questo articolo illustra ciascuno dei tre tipi di sparkline supportati da Aspose.Cells — **Linea**, **Colonna** e **Win/Loss** — e mostra come aggiungerli, personalizzarne i colori e salvare la cartella di lavoro risultante.

## **Sparklines a linee**

Una sparkline a linee disegna una linea continua attraverso i punti dati di una serie, rendendola la scelta più naturale per mostrare andamenti nel tempo. In Aspose.Cells, una sparkline a linee viene creata passando `SparklineType.Line` al metodo `SparklineGroups.Add`.

Il flusso di lavoro è lo stesso di qualsiasi altro tipo di sparkline:

1. Creare un nuovo `Workbook` e accedere al primo foglio di lavoro.
2. Popolare una riga di dati di origine (ad esempio, riga 1, colonne da A a E) con i valori che si desidera visualizzare.
3. Costruire un `CellArea` che descriva la cella di destinazione in cui verrà disegnata la sparkline.
4. Chiamare `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`. Il terzo argomento — `false` — indica ad Aspose.Cells che l'intervallo di dati è orizzontale (una riga), non verticale (una colonna).
5. Facoltativamente, personalizzare il `SparklineGroup` restituito. Per una sparkline a linee è possibile impostare il colore della linea tramite `group.Line.Color` (che si aspetta un `CellsColor` da `Aspose.Cells.Drawing`), regolare lo spessore della linea e attivare/disattivare gli indicatori dei punti massimo/minimo.
6. Salvare la cartella di lavoro.

L'esempio seguente crea una cartella di lavoro, scrive i valori 5, -3, 8, -2, 6 nelle celle da A1 a E1, e aggiunge una sparkline a linee nella cella F1 che traccia tali valori. Personalizza inoltre il colore della linea in rosso e abilita gli indicatori per i punti massimo e minimo.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Passo 1: Crea una cartella di lavoro e ottieni il primo foglio di lavoro
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Passo 2: Scrivi i valori di esempio 5, -3, 8, -2, 6 nelle celle A1:E1
    cells.Get(u"A1").PutValue(5);
    cells.Get(u"B1").PutValue(-3);
    cells.Get(u"C1").PutValue(8);
    cells.Get(u"D1").PutValue(-2);
    cells.Get(u"E1").PutValue(6);

    // Passo 3: Costruisci un CellArea che punti alla cella di destinazione F1
    CellArea dest;
    dest.StartColumn = 5;   // colonna F (0-indicizzata)
    dest.EndColumn = 5;
    dest.StartRow = 0;      // riga 1 (0-indicizzata)
    dest.EndRow = 0;

    // Passo 4: Aggiungi uno sparkline di tipo Linea da A1:E1 a F1
    int index = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(index);

    // Passo 5: Crea un CellsColor rosso e assegnalo al colore della linea dello sparkline
    CellsColor red = workbook.CreateCellsColor();
    red.SetColor(Color::Red());
    group.SetSeriesColor(red);

    // Passo 6: Abilita i marcatori del punto massimo e del punto minimo
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);

    // Passo 7: Salva la cartella di lavoro
    workbook.Save(u"output_line.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sparklines a colonne**

Una sparkline a colonne rappresenta ciascun punto dati come una barra verticale. Ciò la rende particolarmente adatta a dati la cui grandezza è significativa — ad esempio, cifre di vendita mensili o conteggi. In Aspose.Cells, si crea una sparkline a colonne passando `SparklineType.Column` al metodo `SparklineGroups.Add`.

La procedura rispecchia l'esempio della sparkline a linee:

1. Creare un nuovo `Workbook` e accedere al primo foglio di lavoro.
2. Popolare lo stesso intervallo di origine (A1:E1) con i valori che si desidera visualizzare.
3. Costruire un `CellArea` che descriva la cella di destinazione.
4. Chiamare `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`.
5. Facoltativamente, personalizzare il `SparklineGroup` risultante — ad esempio, impostando `group.Type` per confermare il tipo, o modificando il colore delle barre.
6. Salvare la cartella di lavoro in un file di output separato in modo che non sovrascriva l'esempio della sparkline a linee.

L'esempio seguente scrive i valori 5, -3, 8, -2, 6 in A1:E1 e rende una sparkline a colonne in F1. I valori negativi sono disegnati come barre rivolte verso il basso e i valori positivi come barre rivolte verso l'alto, il che rende facile individuare a colpo d'occhio i contributi positivi e negativi.

```cpp
#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Passo 1: Creare una cartella di lavoro e ottenere il primo foglio di lavoro
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Passo 2: Scrivere valori di esempio in A1:E1
    int values[5] = { 5, -3, 8, -2, 6 };
    Cells cells = worksheet.GetCells();
    for (int i = 0; i < 5; i++) {
        cells.Get(0, i).PutValue(values[i]);
    }

    // Passo 3: Costruire un CellArea che punti a F1 (indice colonna 5, indice riga 0)
    CellArea dest;
    dest.StartColumn = 5;
    dest.EndColumn = 5;
    dest.StartRow = 0;
    dest.EndRow = 0;

    // Passo 4: Aggiungere una sparkline a colonne alla cella di destinazione
    int idx = worksheet.GetSparklineGroups().Add(
        SparklineType::Column, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(idx);

    // Passo 5: Confermare il tipo di sparkline leggendo group.Type
    std::cout << "Sparkline Type added: " << static_cast<int>(group.GetType()) << std::endl;

    // Passo 6: Salvare la cartella di lavoro
    wb.Save(u"output_column.xlsx");

    std::cout << "Workbook saved as output_column.xlsx" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sparklines Win/Loss**

Una sparkline win/loss è una variante speciale della sparkline a colonne progettata per mostrare solo due esiti: un valore positivo viene disegnato come una barra "in alto" (una vittoria) e un valore zero o negativo viene disegnato come una barra "in basso" (una sconfitta). Le sparklines win/loss sono comunemente utilizzate per visualizzare sequenze di vittorie e sconfitte, risultati di superamento/fallimento, o qualsiasi esito binario nel tempo.

In Aspose.Cells, una sparkline win/loss viene creata passando `SparklineType.Stacked` al metodo `SparklineGroups.Add`. (Nonostante il nome, `SparklineType.Stacked` è il valore enum utilizzato per richiedere il rendering win/loss.)

La procedura è la stessa degli altri due tipi:

1. Creare un nuovo `Workbook` e accedere al primo foglio di lavoro.
2. Popolare l'intervallo di origine. Poiché le sparklines win/loss trattano ogni valore come una vittoria o una sconfitta, la grandezza del valore non ha importanza — solo il suo segno. I valori positivi diventano barre in alto e i valori non positivi diventano barre in basso.
3. Costruire un `CellArea` che descriva la cella di destinazione.
4. Chiamare `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Facoltativamente, personalizzare il `SparklineGroup` restituito, ad esempio impostando i colori di accento per le barre di vittoria e sconfitta.
6. Salvare la cartella di lavoro con un nome file distinto in modo che tutti e tre gli esempi possano coesistere sul disco.

L'esempio seguente utilizza gli stessi dati di input delle due sezioni precedenti. I valori 5, -3, 8, -2, 6 sono interpretati come vittoria, sconfitta, vittoria, sconfitta, vittoria — e la sparkline disegnata in F1 riflette esattamente tale schema.

```cpp
#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Passo 1: Crea una cartella di lavoro e ottieni il primo foglio di lavoro
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"WinLoss");

    // Passo 2: Popola i dati di esempio nella riga 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    // Passo 3: Costruisci un'area di celle che punta a F1 (colonna 5, riga 0)
    CellArea dest;
    dest.StartColumn = 5;   // F
    dest.EndColumn = 5;
    dest.StartRow = 0;      // riga 1
    dest.EndRow = 0;

    // Passo 4: Aggiungi una sparkline Win/Loss (SparklineType.Stacked)
    int groupIndex = worksheet.GetSparklineGroups().Add(
        SparklineType::Stacked,
        u"A1:E1",
        false,
        dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(groupIndex);

    // Passo 5: Personalizza il gruppo di sparkline
    // Abilita i marcatori del punto massimo e del punto minimo
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    group.SetShowNegativePoints(true);

    // Imposta il colore del punto massimo su verde
    CellsColor highColor = workbook.CreateCellsColor();
    highColor.SetColor(Color::Green());
    group.SetHighPointColor(highColor);

    // Imposta il colore del punto minimo su rosso
    CellsColor lowColor = workbook.CreateCellsColor();
    lowColor.SetColor(Color::Red());
    group.SetLowPointColor(lowColor);

    // Imposta il colore dei punti negativi su arancione
    CellsColor negColor = workbook.CreateCellsColor();
    negColor.SetColor(Color::Orange());
    group.SetNegativePointsColor(negColor);

    // Imposta il colore predefinito della serie (usato per le barre positive)
    CellsColor seriesColor = workbook.CreateCellsColor();
    seriesColor.SetColor(Color::SteelBlue());
    group.SetSeriesColor(seriesColor);

    // Passo 6: Salva la cartella di lavoro
    workbook.Save(u"output_winloss.xlsx");

    std::cout << "Workbook saved successfully: output_winloss.xlsx" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Combinazione di tutti e tre i tipi di Sparkline**

I tre esempi precedenti producono ciascuno la propria cartella di lavoro in modo che i file di output siano facili da ispezionare in isolamento. In uno scenario reale, tuttavia, si vorrà spesso confrontare diverse serie di dati affiancate. Il modo più pulito per farlo è inserire più di un gruppo di sparklines nello stesso foglio di lavoro, con ciascun gruppo che rende uno stile diverso.

È possibile aggiungere più oggetti `SparklineGroup` alla stessa `SparklineGroupCollection`, e ciascun gruppo può puntare a una cella di destinazione diversa o a un intervallo diverso. Ad esempio, è possibile inserire una sparkline a linee in F1, una sparkline a colonne in F2, e una sparkline win/loss in F3 — tutte leggendo dagli stessi dati di origine nella riga 1 — in modo che il lettore possa vedere tre diversi trattamenti visivi degli stessi numeri.

L'esempio combinato seguente crea una singola cartella di lavoro, popola la riga 1 con i valori 5, -3, 8, -2, 6, e quindi aggiunge tre gruppi di sparklines nelle celle F1, F2 e F3 — uno per ciascun tipo — in modo che il file risultante dimostri tutti e tre gli stili di sparkline contemporaneamente.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Passaggio 1: Creare una cartella di lavoro e ottenere il primo foglio di lavoro
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Passaggio 2: Popolare i dati di esempio nella riga 1 (A1:E1)
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);

    // Passaggio 3: Aggiungere un gruppo di sparkline lineari in F1
    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, lineArea);
    SparklineGroup lineGroup = worksheet.GetSparklineGroups().Get(lineIdx);

    // Personalizzare il colore della sparkline lineare tramite CellsColor
    CellsColor lineColor = workbook.CreateCellsColor();
    lineColor.SetColor(Color::Blue());
    lineGroup.SetSeriesColor(lineColor);

    // Passaggio 4: Aggiungere un gruppo di sparkline a colonne in F2
    CellArea columnArea;
    columnArea.StartColumn = 5;
    columnArea.EndColumn = 5;
    columnArea.StartRow = 1;
    columnArea.EndRow = 1;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, u"A1:E1", false, columnArea);
    SparklineGroup columnGroup = worksheet.GetSparklineGroups().Get(columnIdx);

    // Personalizzare il colore della serie della sparkline a colonne
    CellsColor columnColor = workbook.CreateCellsColor();
    columnColor.SetColor(Color::Green());
    columnGroup.SetSeriesColor(columnColor);

    // Passaggio 5: Aggiungere un gruppo di sparkline Win/Loss (impilate) in F3
    CellArea stackedArea;
    stackedArea.StartColumn = 5;
    stackedArea.EndColumn = 5;
    stackedArea.StartRow = 2;
    stackedArea.EndRow = 2;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, u"A1:E1", false, stackedArea);
    SparklineGroup stackedGroup = worksheet.GetSparklineGroups().Get(stackedIdx);

    // Personalizzare il colore della serie della sparkline win/loss
    CellsColor stackedColor = workbook.CreateCellsColor();
    stackedColor.SetColor(Color::FromArgb(0xFF8C00));
    stackedGroup.SetSeriesColor(stackedColor);

    // Passaggio 6: Salvare la cartella di lavoro
    workbook.Save(u"output_all.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Quando si combinano più gruppi di sparklines in un singolo foglio di lavoro, ciascun gruppo è indipendente. Possono condividere lo stesso intervallo di origine o utilizzare intervalli di origine diversi, e possono essere stilizzati indipendentemente. Ciò rende facile costruire un piccolo "cruscotto" di visualizzazioni all'interno delle celle direttamente all'interno di un foglio di lavoro esistente.

{{% /alert %}}

## **Personalizzazione dell'aspetto delle Sparkline**

Una volta che un `SparklineGroup` è stato creato e aggiunto a `worksheet.SparklineGroups`, è possibile leggere o modificare diverse delle sue proprietà visive prima di salvare la cartella di lavoro. Le proprietà più comunemente personalizzate sono:

- **`group.Type`** — il `SparklineType` (Line, Column o Stacked). Viene impostato quando il gruppo viene aggiunto, ma è possibile rileggerlo per conferma.
- **`group.Line.Color`** — il colore della linea, espresso come `CellsColor` creato tramite `workbook.CreateCellsColor()`. Questa è la proprietà da utilizzare per il colore del tratto della sparkline a linee.
- **`group.Line.Weight`** — lo spessore della linea in punti. Valori più alti producono linee più spesse.
- **Indicatori dei punti massimo/minimo** — flag che attivano piccoli indicatori sui punti dati più alti e più bassi, utili per enfatizzare gli estremi.
- **Indicatori dei punti primo/ultimo/negativo** — flag che attivano/disattivano gli indicatori sui punti dati primo, ultimo e negativo.

Per modificare un colore, creare sempre un'istanza di `CellsColor` e assegnarla alla proprietà pertinente. Non assegnare un valore di colore grezzo direttamente alle proprietà di colore delle sparklines — si aspettano il tipo `CellsColor` di `Aspose.Cells.Drawing`. Il metodo `SparklineGroups.Add` stesso restituisce un oggetto `SparklineGroup` completamente tipizzato, quindi è possibile concatenare le assegnazioni di proprietà sul valore restituito o memorizzarlo in una variabile locale e personalizzarlo prima di salvare.



{{< app/cells/assistant language="cpp" >}}