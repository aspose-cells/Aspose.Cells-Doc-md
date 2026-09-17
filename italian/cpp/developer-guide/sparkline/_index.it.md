---
title: Sparklines in Aspose.Cells for C++
description: Aspose.Cells è una libreria C++ per lavorare con file di fogli di calcolo che supporta la creazione di sparkline, ovvero grafici in miniatura inseriti all'interno delle celle del foglio di lavoro. Questo articolo spiega come aggiungere e personalizzare sparkline a linea, a colonne e vincita/perdita utilizzando la libreria Aspose.Cells.
linktitle: Sparklines
keywords: Aspose.Cells, libreria C++, foglio di calcolo, sparklines, sparkline a linea, sparkline a colonne, sparkline vincita/perdita, SparklineGroup, SparklineType
type: docs
weight: 195
url: /it/cpp/creating-sparklines/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta la creazione di sparkline all'interno delle celle del foglio di lavoro. Le sparkline sono grafici in miniatura che si adattano a una singola cella, offrendo una rapida rappresentazione visiva degli andamenti dei dati. Aspose.Cells supporta sparkline a linea, a colonne e vincita/perdita, ciascuna delle quali può essere personalizzata per quanto riguarda colore, spessore della linea, punti massimo/minimo e indicatori.

## **Introduzione**
Le sparkline sono piccoli grafici all'interno delle celle, utili quando si desidera visualizzare rapidamente un andamento accanto a una riga o colonna di dati, senza occupare lo spazio di un grafico completo. Excel supporta tre tipi di sparkline: **a linea**, **a colonne** e **vincita/perdita**. Aspose.Cells rispecchia questa funzionalità attraverso le API `SparklineGroup` e `SparklineGroupCollection` presenti nel namespace `Aspose.Cells.Charts`.
In Aspose.Cells, ogni sparkline che aggiungi viene creata tramite `worksheet.SparklineGroups.Add(...)`, che restituisce un oggetto `SparklineGroup`. Puoi quindi utilizzare tale oggetto per impostare il tipo di sparkline, l'intervallo di dati, la cella di destinazione e le proprietà visive come il colore della linea, lo spessore della linea, gli indicatori e gli indicatori dei punti massimo/minimo.
Questo articolo illustra ciascuno dei tre tipi di sparkline supportati da Aspose.Cells — **Linea**, **Colonne** e **Vincita/Perdita** — e mostra come aggiungerli, personalizzarne i colori e salvare la cartella di lavoro risultante.

## **Sparkline a Linea**
Una sparkline a linea disegna una linea continua attraverso i punti dati di una serie, risultando la scelta più naturale per mostrare andamenti nel tempo. In Aspose.Cells, una sparkline a linea viene creata passando `SparklineType.Line` al metodo `SparklineGroups.Add`.
1. Crea una nuova `Workbook` e accedi al primo foglio di lavoro.
2. Popola una riga di dati sorgente (ad esempio, riga 1, colonne da A a E) con i valori che desideri visualizzare.
3. Crea un `CellArea` che descriva la cella di destinazione in cui verrà disegnata la sparkline.
4. Chiama `worksheet.SparklineGroups.Add(SparklineType.Line, "A1:E1", false, dest)`. Il terzo argomento, `false`, indica ad Aspose.Cells che l'intervallo di dati è orizzontale (una riga), non verticale (una colonna).
5. Personalizza facoltativamente il `SparklineGroup` restituito. Per una sparkline a linea puoi impostare il colore della linea tramite `group.Line.Color` (che si aspetta un `CellsColor` da `Aspose.Cells.Drawing`), regolare lo spessore della linea e attivare/disattivare gli indicatori dei punti massimo/minimo.
6. Salva la cartella di lavoro.
L'esempio seguente crea una cartella di lavoro, scrive i valori 5, -3, 8, -2, 6 nelle celle da A1 a E1 e aggiunge una sparkline a linea nella cella F1 che traccia tali valori. Personalizza inoltre il colore della linea in rosso e abilita gli indicatori per i punti massimo e minimo.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Passo 1: Creare una cartella di lavoro e ottenere il primo foglio di lavoro
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // Passo 2: Scrivere i valori di esempio 5, -3, 8, -2, 6 nelle celle A1:E1
    cells.Get(u"A1").PutValue(5);
    cells.Get(u"B1").PutValue(-3);
    cells.Get(u"C1").PutValue(8);
    cells.Get(u"D1").PutValue(-2);
    cells.Get(u"E1").PutValue(6);
    // Passo 3: Costruire una CellArea che punta alla cella di destinazione F1
    CellArea dest;
    dest.StartColumn = 5;   // colonna F (indicizzata a 0)
    dest.EndColumn = 5;
    dest.StartRow = 0;      // riga 1 (indicizzata a 0)
    dest.EndRow = 0;
    // Passo 4: Aggiungere una sparkline Linea da A1:E1 in F1
    int index = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(index);
    // Passo 5: Creare un CellsColor rosso e assegnarlo al colore della linea della sparkline
    CellsColor red = workbook.CreateCellsColor();
    red.SetColor(Color::Red());
    group.SetSeriesColor(red);
    // Passo 6: Abilitare i marcatori di punto alto e punto basso
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    // Passo 7: Salvare la cartella di lavoro
    workbook.Save(u"output_line.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sparkline a Colonne**
Una sparkline a colonne rappresenta ciascun punto dati come una barra verticale, risultando particolarmente adatta per dati la cui magnitudine è significativa, ad esempio le cifre di vendita mensili o i conteggi. In Aspose.Cells, crei una sparkline a colonne passando `SparklineType.Column` al metodo `SparklineGroups.Add`.
La procedura rispecchia l'esempio della sparkline a linea:
1. Crea una nuova `Workbook` e accedi al primo foglio di lavoro.
2. Crea un `CellArea` che descriva la cella di destinazione.
3. Chiama `worksheet.SparklineGroups.Add(SparklineType.Column, "A1:E1", false, dest)`.
4. Personalizza facoltativamente il `SparklineGroup` risultante, ad esempio impostando `group.Type` per confermare il tipo, oppure modificando il colore delle barre.
5. Salva la cartella di lavoro in un file di output separato, in modo che non sovrascriva l'esempio della sparkline a linea.
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
    // Passo 3: Creare un'area di celle che punta a F1 (indice colonna 5, indice riga 0)
    CellArea dest;
    dest.StartColumn = 5;
    dest.EndColumn = 5;
    dest.StartRow = 0;
    dest.EndRow = 0;
    // Passo 4: Aggiungere una sparkline di tipo colonna alla cella di destinazione
    int idx = worksheet.GetSparklineGroups().Add(
        SparklineType::Column, u"A1:E1", false, dest);
    SparklineGroup group = worksheet.GetSparklineGroups().Get(idx);
    // Passo 5: Confermare il tipo di sparkline leggendo group.Type
    std::cout << "Tipo di sparkline aggiunto: " << static_cast<int>(group.GetType()) << std::endl;
    // Passo 6: Salvare la cartella di lavoro
    wb.Save(u"output_column.xlsx");
    std::cout << "Cartella di lavoro salvata come output_column.xlsx" << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Sparkline Vincita/Perdita**
Una sparkline vincita/perdita è una variante speciale della sparkline a colonne, progettata per mostrare solo due esiti: un valore positivo è disegnato come una barra verso l'alto (una vincita) e un valore zero o negativo come una barra verso il basso (una perdita). Le sparkline vincita/perdita sono comunemente utilizzate per visualizzare sequenze di vincite e perdite, risultati di successo/fallimento o qualsiasi esito binario nel tempo.
In Aspose.Cells, una sparkline vincita/perdita viene creata passando `SparklineType.Stacked` al metodo `SparklineGroups.Add`. (Nonostante il nome, `SparklineType.Stacked` è il valore enum utilizzato per richiedere il rendering vincita/perdita.)
1. Crea una nuova `Workbook` e accedi al primo foglio di lavoro.
2. Popola l'intervallo sorgente. Poiché le sparkline vincita/perdita trattano ogni valore come una vincita o una perdita, la magnitudine del valore non è rilevante, conta solo il suo segno. I valori positivi diventano barre verso l'alto e i valori non positivi diventano barre verso il basso.
3. Crea un `CellArea` che descriva la cella di destinazione.
4. Chiama `worksheet.SparklineGroups.Add(SparklineType.Stacked, "A1:E1", false, dest)`.
5. Personalizza facoltativamente il `SparklineGroup` restituito, ad esempio impostando colori di accento per le barre di vincita e di perdita.
6. Salva la cartella di lavoro con un nome file distinto, in modo che tutti e tre gli esempi possano coesistere sul disco.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Passo 1: Crea un Workbook e ottieni il primo foglio di lavoro
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"WinLoss");
    // Passo 2: Popola i dati di esempio nella riga 1: A1=5, B1=-3, C1=8, D1=-2, E1=6
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);
    // Passo 3: Costruisci un CellArea che punta a F1 (colonna 5, riga 0)
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
    // Abilita i marcatori dei punti alti e bassi
    group.SetShowHighPoint(true);
    group.SetShowLowPoint(true);
    group.SetShowNegativePoints(true);
    // Imposta il colore del punto alto su verde
    CellsColor highColor = workbook.CreateCellsColor();
    highColor.SetColor(Color::Green());
    group.SetHighPointColor(highColor);
    // Imposta il colore del punto basso su rosso
    CellsColor lowColor = workbook.CreateCellsColor();
    lowColor.SetColor(Color::Red());
    group.SetLowPointColor(lowColor);
    // Imposta il colore del punto negativo su arancione
    CellsColor negColor = workbook.CreateCellsColor();
    negColor.SetColor(Color::Orange());
    group.SetNegativePointsColor(negColor);
    // Imposta il colore predefinito della serie (usato per le barre positive)
    CellsColor seriesColor = workbook.CreateCellsColor();
    seriesColor.SetColor(Color::SteelBlue());
    group.SetSeriesColor(seriesColor);
    // Passo 6: Salva il workbook
    workbook.Save(u"output_winloss.xlsx");
    std::cout << "Workbook salvato con successo: output_winloss.xlsx" << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Combinazione dei Tre Tipi di Sparkline**
L'esempio combinato seguente crea una singola cartella di lavoro, popola la riga 1 con i valori 5, -3, 8, -2, 6 e quindi aggiunge tre gruppi di sparkline nelle celle F1, F2 e F3, uno per ciascun tipo, in modo che il file risultante dimostri tutti e tre gli stili di sparkline contemporaneamente.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Passo 1: Crea una cartella di lavoro e ottieni il primo foglio di lavoro
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Passo 2: Popola i dati di esempio nella riga 1 (A1:E1)
    worksheet.GetCells().Get(u"A1").PutValue(5);
    worksheet.GetCells().Get(u"B1").PutValue(-3);
    worksheet.GetCells().Get(u"C1").PutValue(8);
    worksheet.GetCells().Get(u"D1").PutValue(-2);
    worksheet.GetCells().Get(u"E1").PutValue(6);
    // Passo 3: Aggiungi un gruppo di sparkline Linea in F1
    CellArea lineArea;
    lineArea.StartColumn = 5;
    lineArea.EndColumn = 5;
    lineArea.StartRow = 0;
    lineArea.EndRow = 0;
    int lineIdx = worksheet.GetSparklineGroups().Add(SparklineType::Line, u"A1:E1", false, lineArea);
    SparklineGroup lineGroup = worksheet.GetSparklineGroups().Get(lineIdx);
    // Personalizza il colore della sparkline Linea tramite CellsColor
    CellsColor lineColor = workbook.CreateCellsColor();
    lineColor.SetColor(Color::Blue());
    lineGroup.SetSeriesColor(lineColor);
    // Passo 4: Aggiungi un gruppo di sparkline Colonna in F2
    CellArea columnArea;
    columnArea.StartColumn = 5;
    columnArea.EndColumn = 5;
    columnArea.StartRow = 1;
    columnArea.EndRow = 1;
    int columnIdx = worksheet.GetSparklineGroups().Add(SparklineType::Column, u"A1:E1", false, columnArea);
    SparklineGroup columnGroup = worksheet.GetSparklineGroups().Get(columnIdx);
    // Personalizza il colore della serie della sparkline Colonna
    CellsColor columnColor = workbook.CreateCellsColor();
    columnColor.SetColor(Color::Green());
    columnGroup.SetSeriesColor(columnColor);
    // Passo 5: Aggiungi un gruppo di sparkline Win/Loss (Stacked) in F3
    CellArea stackedArea;
    stackedArea.StartColumn = 5;
    stackedArea.EndColumn = 5;
    stackedArea.StartRow = 2;
    stackedArea.EndRow = 2;
    int stackedIdx = worksheet.GetSparklineGroups().Add(SparklineType::Stacked, u"A1:E1", false, stackedArea);
    SparklineGroup stackedGroup = worksheet.GetSparklineGroups().Get(stackedIdx);
    // Personalizza il colore della serie della sparkline win/loss
    CellsColor stackedColor = workbook.CreateCellsColor();
    stackedColor.SetColor(Color::FromArgb(0xFF8C00));
    stackedGroup.SetSeriesColor(stackedColor);
    // Passo 6: Salva la cartella di lavoro
    workbook.Save(u"output_all.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Personalizzazione dell'Aspetto delle Sparkline**
Una volta che un `SparklineGroup` è stato creato e aggiunto a `worksheet.SparklineGroups`, è possibile leggere o modificare diverse proprietà visive prima di salvare la cartella di lavoro. Le proprietà più comunemente personalizzate sono:
- **`group.Type`** — il `SparklineType` (Line, Column o Stacked). Viene impostato quando il gruppo viene aggiunto, ma è possibile rileggerlo per confermarlo.
- **`group.Line.Color`** — il colore della linea, espresso come `CellsColor` creato tramite `workbook.CreateCellsColor()`. È la proprietà da utilizzare per il colore del tratto delle sparkline a linea.
- **`group.Line.Weight`** — lo spessore della linea in punti. Valori più alti producono linee più spesse.
- **Indicatori dei punti massimo/minimo** — flag che attivano piccoli indicatori sui punti dati più alti e più bassi, utili per enfatizzare gli estremi.
- **Indicatori dei punti primo/ultimo/negativo** — flag che attivano/disattivano gli indicatori sui punti dati primo, ultimo e negativo.
Per modificare un colore, crea sempre un'istanza di `CellsColor` e assegnala alla proprietà pertinente. Non assegnare direttamente un valore di colore grezzo alle proprietà di colore delle sparkline, che si aspettano il tipo `CellsColor` di `Aspose.Cells.Drawing`. Il metodo `SparklineGroups.Add` stesso restituisce un oggetto `SparklineGroup` completamente tipizzato, quindi è possibile concatenare le assegnazioni di proprietà sul valore restituito oppure memorizzarlo in una variabile locale e personalizzarlo prima di salvare.
{{% /alert %}}cpp

{{< app/cells/assistant language="cpp" >}}