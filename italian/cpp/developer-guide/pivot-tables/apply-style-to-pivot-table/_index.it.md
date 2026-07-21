---
title: Applicazione degli stili alle tabelle pivot
linktitle: Applicazione degli stili alle tabelle pivot
description: Scopri come applicare stili predefiniti e personalizzati alle tabelle pivot in Aspose.Cells for C++, incluse le formattazioni automatiche legacy XLS, gli stili denominati moderni di Excel 2007+, gli stili personalizzati per tabelle pivot e la scorciatoia FormatAll.
keywords: Aspose.Cells C++ stile tabella pivot, PivotTableStyleType, AutoFormatType, FormatAll, stile personalizzato, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /it/cpp/apply-style-to-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supporta l'applicazione sia delle formattazioni automatiche legacy per tabelle pivot (destinate ai file `.xls`) sia degli stili denominati moderni o personalizzati per tabelle pivot (destinati ai file `.xlsx`, `.xlsm` e `.xlsb`). L'API da utilizzare dipende dal formato di file in cui la cartella di lavoro viene salvata, non dal formato da cui è stata caricata.

{{% /alert %}}

## **Introduzione**

Aspose.Cells espone due API di stile parallele per le tabelle pivot. La scelta tra esse è determinata dal formato di file in cui si salva la cartella di lavoro, non dal formato da cui viene letta. Una cartella di lavoro caricata da un file `.xls` può essere salvata nuovamente come `.xlsx` e, in tal caso, si applica l'API di stile moderna anziché quella legacy.

Per l'output `.xls` legacy, utilizzare la proprietà `PivotTable.AutoFormatType` insieme all'enumerazione `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Questa API corrisponde al selettore di formattazione automatica offerto dalla versione classica di Excel per le tabelle pivot.

Per l'output `.xlsx`, `.xlsm` e `.xlsb` moderno, sono disponibili due varianti dell'API di stile:

- `PivotTable.PivotTableStyleType` seleziona uno degli stili denominati predefiniti (temi chiari e scuri, inclusi gli stili aggiunti in Excel 2017). Questi preset sono di sola lettura.
- `PivotTable.PivotTableStyleName` seleziona uno stile personalizzato definito dall'utente tramite `Worksheets.TableStyles.AddPivotTableStyle(...)`. Gli stili personalizzati sono necessari ogni volta che si desidera modificare colori, bordi o font oltre a quanto offerto dai preset.

Inoltre, `PivotTable.FormatAll(Style)` è una scorciatoia che applica un singolo oggetto `Style` a ogni cella della tabella pivot, sovrascrivendo qualsiasi impostazione effettuata tramite una delle API basate sul nome di stile sopra indicate. Ciò è utile quando è richiesto un aspetto uniforme indipendentemente dal tema sottostante.

## **Applicare una formattazione automatica predefinita XLS legacy**

`PivotTable.AutoFormatType` accetta un valore dall'enumerazione `Aspose.Cells.Pivot.PivotTableAutoFormatType`. I valori disponibili sono `Report1` fino a `Report10`, `Classic` e `Table1` fino a `Table10`.

{{% alert color="primary" %}}

`AutoFormatType` viene rispettato solo quando la cartella di lavoro viene salvata come `.xls`. Quando la stessa cartella di lavoro viene salvata come `.xlsx`, `.xlsm` o `.xlsb`, Excel ignora questa proprietà e ricorre alle impostazioni `PivotTableStyleType` e `PivotTableStyleName`.

{{% /alert %}}

L'esempio seguente carica una nuova cartella di lavoro, popola i dati di esempio Frutta/Anno/Quantità, aggiunge una tabella pivot, applica `PivotTableAutoFormatType.Report5` e salva il risultato come `.xls`.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Crea una nuova cartella di lavoro
    Workbook workbook;

    // Ottieni il primo foglio di lavoro
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Popola i dati di origine con la riga di intestazione (Frutta, Anno, Quantità)
    // e 9 righe di dati che coprono uva, mirtillo, kiwi, ciliegia nel 2020 e 2021
    sheet.GetCells().Get(0, 0).PutValue(u"Fruit");
    sheet.GetCells().Get(0, 1).PutValue(u"Year");
    sheet.GetCells().Get(0, 2).PutValue(u"Amount");

    sheet.GetCells().Get(1, 0).PutValue(u"grape");
    sheet.GetCells().Get(1, 1).PutValue(2020);
    sheet.GetCells().Get(1, 2).PutValue(50);

    sheet.GetCells().Get(2, 0).PutValue(u"blueberry");
    sheet.GetCells().Get(2, 1).PutValue(2020);
    sheet.GetCells().Get(2, 2).PutValue(30);

    sheet.GetCells().Get(3, 0).PutValue(u"kiwi");
    sheet.GetCells().Get(3, 1).PutValue(2020);
    sheet.GetCells().Get(3, 2).PutValue(25);

    sheet.GetCells().Get(4, 0).PutValue(u"cherry");
    sheet.GetCells().Get(4, 1).PutValue(2020);
    sheet.GetCells().Get(4, 2).PutValue(40);

    sheet.GetCells().Get(5, 0).PutValue(u"grape");
    sheet.GetCells().Get(5, 1).PutValue(2021);
    sheet.GetCells().Get(5, 2).PutValue(60);

    sheet.GetCells().Get(6, 0).PutValue(u"blueberry");
    sheet.GetCells().Get(6, 1).PutValue(2021);
    sheet.GetCells().Get(6, 2).PutValue(35);

    sheet.GetCells().Get(7, 0).PutValue(u"kiwi");
    sheet.GetCells().Get(7, 1).PutValue(2021);
    sheet.GetCells().Get(7, 2).PutValue(28);

    sheet.GetCells().Get(8, 0).PutValue(u"cherry");
    sheet.GetCells().Get(8, 1).PutValue(2021);
    sheet.GetCells().Get(8, 2).PutValue(45);

    sheet.GetCells().Get(9, 0).PutValue(u"grape");
    sheet.GetCells().Get(9, 1).PutValue(2020);
    sheet.GetCells().Get(9, 2).PutValue(45);

    // Aggiungi una tabella pivot nella cella di destinazione E3, denominata "Pivot1", utilizzando l'intervallo di origine A1:C10
    int pivotIndex = sheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = sheet.GetPivotTables().Get(pivotIndex);

    // Assegna i campi: Frutta -> Righe, Anno -> Colonne, Quantità -> Dati
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Applica il formato automatico preimpostato legacy XLS "Report5"
    pivotTable.SetAutoFormatType(PivotTableAutoFormatType::Report5);

    // Salva la cartella di lavoro nel formato legacy .xls
    workbook.Save(u"output.xls");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Applicare uno stile di tabella pivot predefinito denominato moderno**

`PivotTable.PivotTableStyleType` accetta un valore dall'enumerazione `Aspose.Cells.PivotTableStyleType`. L'enumerazione copre i temi chiari da `PivotTableStyleLight1` a `PivotTableStyleLight28` e i temi scuri da `PivotTableStyleDark1` a `PivotTableStyleDark28`. Gli stili aggiunti in Excel 2017 (la seconda ondata di temi chiari e scuri) sono raggiungibili tramite la stessa enumerazione.

Questa è l'API consigliata per qualsiasi formato di file moderno. A differenza della formattazione automatica legacy, lo stile selezionato qui viene renderizzato fedelmente da Excel e sopravvive ai round-trip attraverso altri strumenti Office.

L'esempio seguente utilizza gli stessi dati Frutta/Anno/Quantità, crea una tabella pivot identica, applica `PivotTableStyleDark1` e salva la cartella di lavoro come `.xlsx`.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(150);

    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(200);

    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(180);

    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(120);

    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(170);

    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(210);

    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(190);

    cells.Get(u"A10").PutValue(u"Grape");
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(130);

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleDark1);

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Definire e applicare uno stile di tabella pivot personalizzato**

I preset predefiniti non possono essere modificati. Ogni volta che è necessario sovrascrivere colori, bordi o font, è necessario definire uno stile pivot personalizzato. Il flusso di lavoro si compone di tre passaggi:

1. Aggiungere uno stile personalizzato alla raccolta `TableStyles` della cartella di lavoro tramite `Worksheets.TableStyles.AddPivotTableStyle(string name)`. Questo restituisce l'indice dello stile appena creato.
2. Configurare lo stile aggiungendo elementi (come `WholeTable` o `GrandTotalRow`) tramite `TableStyle.TableStyleElements.Add(TableStyleElementType)`, quindi assegnare un `Style` a ciascun elemento tramite `TableStyleElement.SetElementStyle(Style)`.
3. Applicare lo stile personalizzato alla tabella pivot impostando `PivotTable.PivotTableStyleName` sul nome dello stile. Non utilizzare `PivotTableStyleType` qui, poiché tale proprietà seleziona i preset predefiniti.

{{% alert color="primary" %}}

`PivotTableStyleName` e `PivotTableStyleType` non sono intercambiabili. Utilizzare `PivotTableStyleType` per i preset predefiniti e `PivotTableStyleName` per gli stili personalizzati definiti tramite `AddPivotTableStyle`. Impostare entrambi è innocuo, ma viene reso solo quello corrispondente all'origine prevista.

{{% /alert %}}

I valori di `TableStyleElementType` disponibili includono `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` e `PageFieldValues`.

L'esempio seguente definisce uno stile pivot personalizzato con un bordo nero sottile su `WholeTable` e un font rosso in grassetto su `GrandTotalRow`, quindi lo applica tramite `PivotTableStyleName` e salva come `.xlsx`.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Cells cells = worksheet.GetCells();

    // Popola i dati di origine: riga di intestazione + 9 righe di dati (A1:C10)
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);

    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);

    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);

    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);

    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);

    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);

    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);

    cells.Get(u"A10").PutValue(u"Grape");
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(900);

    // Aggiungi tabella pivot con origine da A1:C10, ancorata in E3, denominata "Pivot1"
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Passaggio 1: registra un nuovo stile di tabella pivot personalizzato e cattura il suo indice
    int styleIndex = workbook.GetWorksheets().GetTableStyles().AddPivotTableStyle(u"CustomPivotStyle");
    TableStyle tableStyle = workbook.GetWorksheets().GetTableStyles().Get(styleIndex);

    // Passaggio 2: aggiungi un elemento WholeTable e applica bordi sottili neri su tutti e quattro i lati
    int wholeTableElementIndex = tableStyle.GetTableStyleElements().Add(TableStyleElementType::WholeTable);
    TableStyleElement wholeTableElement = tableStyle.GetTableStyleElements().Get(wholeTableElementIndex);
    Style wholeTableStyle = workbook.CreateStyle();
    wholeTableStyle.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Black());
    wholeTableStyle.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    wholeTableStyle.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Black());
    wholeTableElement.SetElementStyle(wholeTableStyle);

    // Passaggio 3: aggiungi un elemento GrandTotalRow e applica un carattere rosso in grassetto
    int grandTotalElementIndex = tableStyle.GetTableStyleElements().Add(TableStyleElementType::GrandTotalRow);
    TableStyleElement grandTotalElement = tableStyle.GetTableStyleElements().Get(grandTotalElementIndex);
    Style grandTotalStyle = workbook.CreateStyle();
    grandTotalStyle.GetFont().SetIsBold(true);
    grandTotalStyle.GetFont().SetColor(Color::Red());
    grandTotalElement.SetElementStyle(grandTotalStyle);

    // Passaggio 4: applica lo stile personalizzato per nome (NON tramite PivotTableStyleType, che è per preset predefiniti)
    pivotTable.SetPivotTableStyleName(u"CustomPivotStyle");

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Applicare un singolo stile a ogni cella della tabella pivot con FormatAll**

`PivotTable.FormatAll(Style)` è una scorciatoia che applica un singolo oggetto `Style` a ogni cella della tabella pivot, inclusi l'area dati, le intestazioni di righe e colonne e i totali. Qualsiasi impostazione precedente effettuata tramite `PivotTableStyleType` o `PivotTableStyleName` viene sovrascritta.

{{% alert color="primary" %}}

`FormatAll` sovrascrive sia `PivotTableStyleType` che `PivotTableStyleName`. Utilizzarlo solo quando è richiesto un aspetto uniforme e indipendente dal tema in tutta la tabella pivot.

{{% /alert %}}

L'esempio seguente crea un `Style` con un riempimento solido giallo, un font blu scuro in grassetto e bordi neri sottili su tutti i lati, quindi lo applica con `FormatAll` e salva come `.xlsx`.

```cpp
#include "Aspose.Cells.h"
#include <string>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Riga di intestazione
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");

    // Righe di dati
    worksheet.GetCells().Get(u"A2").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(5000);

    worksheet.GetCells().Get(u"A3").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2020);
    worksheet.GetCells().Get(u"C3").PutValue(3000);

    worksheet.GetCells().Get(u"A4").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(4000);

    worksheet.GetCells().Get(u"A5").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2020);
    worksheet.GetCells().Get(u"C5").PutValue(2000);

    worksheet.GetCells().Get(u"A6").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(6000);

    worksheet.GetCells().Get(u"A7").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2021);
    worksheet.GetCells().Get(u"C7").PutValue(3500);

    worksheet.GetCells().Get(u"A8").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(4500);

    worksheet.GetCells().Get(u"A9").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2021);
    worksheet.GetCells().Get(u"C9").PutValue(2500);

    worksheet.GetCells().Get(u"A10").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B10").PutValue(2021);
    worksheet.GetCells().Get(u"C10").PutValue(5500);

    // Aggiungi tabella pivot: intervallo di origine A1:C10, cella di destinazione E3, nome "Pivot1"
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // Assegna i campi pivot
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Crea uno Stile che verrà applicato a ogni cella della tabella pivot
    Style style = wb.CreateStyle();
    style.SetForegroundColor(Color::Yellow());
    style.SetPattern(BackgroundType::Solid);
    style.GetFont().SetIsBold(true);
    style.GetFont().SetColor(Color::DarkBlue());
    style.GetBorders().Get(BorderType::TopBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::TopBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::BottomBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::BottomBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::LeftBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::LeftBorder).SetColor(Color::Black());
    style.GetBorders().Get(BorderType::RightBorder).SetLineStyle(CellBorderType::Thin);
    style.GetBorders().Get(BorderType::RightBorder).SetColor(Color::Black());

    // Applica FormatAll
    pivotTable.FormatAll(style);

    // Salva la cartella di lavoro
    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Quale API di stile dovrei usare?**

La scelta dell'API di stile dipende dal formato di file in cui si salva. Utilizzare la tabella seguente come riferimento rapido.

| Formato del file di destinazione | API da utilizzare | Note |
|---|---|---|
| `.xls` (legacy) | `PivotTable.AutoFormatType` | Valori da `Aspose.Cells.Pivot.PivotTableAutoFormatType` (ad es. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Ignorato quando si salva nei formati moderni. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, stile predefinito) | `PivotTable.PivotTableStyleType` | Valori da `Aspose.Cells.PivotTableStyleType` (temi chiari/scuri, incluse le aggiunte di Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, stile personalizzato) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | Da utilizzare quando i preset predefiniti non sono sufficienti. Configurare tramite `TableStyleElement.SetElementStyle(...)`. |
| Qualsiasi formato (sovrascrittura uniforme) | `PivotTable.FormatAll(Style)` | Scorciatoia che sovrascrive ogni altra impostazione di stile nell'intera tabella pivot. |

In caso di dubbio, salvare come `.xlsx` e utilizzare `PivotTableStyleType` per i temi predefiniti oppure `PivotTableStyleName` per i temi personalizzati.

{{< app/cells/assistant language="cpp" >}}