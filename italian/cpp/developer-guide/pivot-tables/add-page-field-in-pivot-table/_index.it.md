---
title: Aggiungere campi filtro a una tabella pivot in Aspose.Cells for C++
linktitle: Aggiungere campi filtro a una tabella pivot
description: Scopri come aggiungere e configurare i campi filtro nelle tabelle pivot utilizzando Aspose.Cells for C++, inclusi l'aggiunta di campi filtro, il filtro a selezione singola e il filtro a selezione multipla.
keywords: Aspose.Cells, C++, tabella pivot, campo filtro, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtro
type: docs
weight: 250
url: /it/cpp/add-page-field-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta l'intero ciclo di vita dei campi filtro nelle tabelle pivot. È possibile aggiungere un campo filtro tramite un'API di alto livello o tramite la raccolta `PageFields` di livello inferiore, ed è possibile gestire il filtro in modalità selezione singola, cancellarlo per mostrare ogni elemento del filtro, oppure passare il campo alla selezione multipla in modo che gli utenti possano selezionare più elementi del filtro contemporaneamente tramite l'interfaccia con caselle di controllo in Excel.
{{% /alert %}}

## **Introduzione**
Un campo filtro è un campo pivot che controlla *quale sottoinsieme* dei dati di origine viene visualizzato dal corpo della pivot. Gli utenti finali lo vedono come un menu a discesa nella parte superiore di una pivot renderizzata in Excel, e selezionando uno degli elementi del filtro disponibili il corpo della pivot viene ricostruito in modo che vengano riepilogati solo i record appartenenti a quell'elemento del filtro. Un campo pivot diventa un campo filtro quando viene registrato come `PivotFieldType.Page` anziché `PivotFieldType.Row`, `PivotFieldType.Column` o `PivotFieldType.Data`.

## **Aggiungere un campo filtro**

### Aggiungere un campo filtro con AddFieldToArea
L'esempio seguente crea un piccolo set di dati Frutta / Anno / Importo, posiziona una tabella pivot nella cella E3 con `Fruit` nell'area righe, `Amount` nell'area dati e `Year` nell'area filtro, aggiorna la pivot e salva la cartella di lavoro.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Crea una nuova cartella di lavoro
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");
    Cells cells = worksheet.GetCells();
    // Imposta la riga di intestazione
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    // Popola 9 righe di dati di esempio: Frutta, Anno, Importo
    const char* fruits[] = { "apple", "banana", "apple", "grape", "orange", "banana", "grape", "apple", "orange" };
    int years[]   = { 2020, 2021, 2021, 2020, 2022, 2020, 2021, 2022, 2021 };
    int amounts[] = { 100, 200, 150, 120, 180, 90, 130, 170, 110 };
    for (int i = 0; i < 9; ++i)
    {
        cells.Get(i + 1, 0).PutValue(U16String(fruits[i]));
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }
    // Aggiungi una tabella pivot ancorata alla cella E3
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"PivotTable1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    // Aggiungi campi alle loro aree: Frutta come Riga, Importo come Dati, Anno come Campo Pagina
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");
    // Aggiorna e calcola i dati della tabella pivot
    pivotTable.CalculateData();
    // Salva la cartella di lavoro
    workbook.Save(u"pageFieldSample.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### Aggiungere un campo filtro con PageFields.Add
Quando si lavora già con un'istanza di `PivotField`, è possibile passarla direttamente a `PivotTable.PageFields.Add`. La tabella pivot e il campo filtro vengono costruiti esattamente come nello scenario precedente; solo la registrazione finale nell'area filtro viene sostituita con la chiamata API di livello inferiore.

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    // Intestazioni
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    // Dati di esempio (9 righe)
    cells.Get(u"A2").PutValue(u"apple");     cells.Get(u"B2").PutValue(u"2020"); cells.Get(u"C2").PutValue(100);
    cells.Get(u"A3").PutValue(u"apple");     cells.Get(u"B3").PutValue(u"2021"); cells.Get(u"C3").PutValue(150);
    cells.Get(u"A4").PutValue(u"apple");     cells.Get(u"B4").PutValue(u"2022"); cells.Get(u"C4").PutValue(200);
    cells.Get(u"A5").PutValue(u"grape");     cells.Get(u"B5").PutValue(u"2020"); cells.Get(u"C5").PutValue(300);
    cells.Get(u"A6").PutValue(u"grape");     cells.Get(u"B6").PutValue(u"2021"); cells.Get(u"C6").PutValue(400);
    cells.Get(u"A7").PutValue(u"grape");     cells.Get(u"B7").PutValue(u"2022"); cells.Get(u"C7").PutValue(500);
    cells.Get(u"A8").PutValue(u"blueberry"); cells.Get(u"B8").PutValue(u"2020"); cells.Get(u"C8").PutValue(250);
    cells.Get(u"A9").PutValue(u"blueberry"); cells.Get(u"B9").PutValue(u"2021"); cells.Get(u"C9").PutValue(350);
    cells.Get(u"A10").PutValue(u"blueberry");cells.Get(u"B10").PutValue(u"2022");cells.Get(u"C10").PutValue(450);
    // Aggiungi tabella pivot in E3 coprendo A1:C10
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(U16String(u"E3"), U16String(u"A1:C10"), U16String(u"PivotTable1"));
    PivotTable pivotTable = pivotTables.Get(pivotIndex);
    // Frutta -> Riga, Importo -> Dati
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"Amount"));
    // Approccio di basso livello: individuare il PivotField Anno esistente in BaseFields
    // e registrarlo nell'area Pagina tramite PageFields.Add(PivotField).
    PivotFieldCollection baseFields = pivotTable.GetBaseFields();
    int baseFieldCount = baseFields.GetCount();
    for (int i = 0; i < baseFieldCount; ++i) {
        PivotField f = baseFields.Get(i);
        if (f.GetName().ToUtf8() == "Year") {
            pivotTable.GetPageFields().Add(f);
            break;
        }
    }
    // Aggiorna in modo che il nuovo campo pagina venga riflesso nella cartella di lavoro salvata
    pivotTable.CalculateData();
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtro a selezione singola (visualizzazione di un singolo elemento del filtro)**
Nel comportamento predefinito a selezione singola, il campo filtro viene visualizzato come un singolo menu a discesa e il valore intero `PivotField.CurrentPageItem` seleziona quale elemento del filtro guida il corpo della pivot. Assegnando un indice specifico si seleziona quell'unico elemento; assegnando il valore sentinella speciale `0x7FFD` (decimale 32765) il filtro viene cancellato in modo che ogni elemento del filtro venga riepilogato contemporaneamente. La selezione singola è l'impostazione predefinita; non è necessario abilitarla esplicitamente.

### Visualizzazione di tutti gli elementi
Impostando `CurrentPageItem` sul valore magico `0x7FFD` equivale a cancellare il filtro: il corpo della pivot riepiloga ogni elemento del filtro come se non fosse applicato alcun filtro.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");
    U16String fruits[6] = {u"Apple", u"Apple", u"Banana", u"Banana", u"Cherry", u"Cherry"};
    int years[6] = {2022, 2023, 2022, 2023, 2022, 2023};
    int amounts[6] = {100, 150, 80, 120, 200, 250};
    for (int r = 0; r < 6; r++) {
        cells.Get(r + 1, 0).PutValue(fruits[r]);
        cells.Get(r + 1, 1).PutValue(years[r]);
        cells.Get(r + 1, 2).PutValue(amounts[r]);
    }
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int index = pivotTables.Add(u"=A1:C7", u"E3", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(index);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");
    pivotTable.CalculateData();
    pivotTable.GetPageFields().Get(0).SetCurrentPageItem(0x7FFD);
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### Visualizzazione di un elemento specifico
Impostando `CurrentPageItem` su un indice reale si seleziona solo quell'unico elemento del filtro. L'indice è la posizione dell'elemento nell'elenco ordinato degli elementi del campo filtro, quindi ad esempio `1` seleziona il secondo elemento dopo l'ordinamento.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));
    cells.Get(u"A2").PutValue(U16String("Apple"));
    cells.Get(u"B2").PutValue(U16String("2020"));
    cells.Get(u"C2").PutValue(U16String("100"));
    cells.Get(u"A3").PutValue(U16String("Apple"));
    cells.Get(u"B3").PutValue(U16String("2021"));
    cells.Get(u"C3").PutValue(U16String("150"));
    cells.Get(u"A4").PutValue(U16String("Banana"));
    cells.Get(u"B4").PutValue(U16String("2020"));
    cells.Get(u"C4").PutValue(U16String("200"));
    cells.Get(u"A5").PutValue(U16String("Banana"));
    cells.Get(u"B5").PutValue(U16String("2021"));
    cells.Get(u"C5").PutValue(U16String("250"));
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(U16String("A1:C5"), U16String("E3"), U16String("PivotTable1"));
    PivotTable pivotTable = pivotTables.Get(pivotIndex);
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String("Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String("Amount"));
    pivotTable.AddFieldToArea(PivotFieldType::Page, U16String("Year"));
    pivotTable.GetPageFields().Get(0).SetCurrentPageItem(1);
    pivotTable.CalculateData();
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtro a selezione multipla**
Il filtro a selezione multipla trasforma il menu a discesa del filtro in un elenco di caselle di controllo e consente all'utente finale di selezionare più elementi del filtro contemporaneamente. Aspose.Cells espone due proprietà che lavorano insieme. `PivotField.IsMultipleItemSelectionAllowed` deve essere impostato su `true` prima che l'interfaccia a selezione multipla abbia effetto. Dopo che è stato abilitato, `PivotItem.IsHidden` controlla quali elementi appaiono nell'elenco delle caselle di controllo, quindi è possibile mostrare ogni elemento o consentire solo elementi specifici.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <vector>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    // Dati di esempio: Frutta | Anno | Quantità
    cells.Get(0, 0).PutValue(u"Fruit");
    cells.Get(0, 1).PutValue(u"Year");
    cells.Get(0, 2).PutValue(u"Amount");
    std::vector<std::vector<std::string>> data = {
        {"apple",  "2019", "100"},
        {"apple",  "2020", "150"},
        {"apple",  "2021", "200"},
        {"banana", "2019", "110"},
        {"banana", "2020", "160"},
        {"banana", "2021", "210"},
        {"grape",  "2019", "120"},
        {"grape",  "2020", "170"},
        {"grape",  "2021", "220"}
    };
    for (int i = 0; i < (int)data.size(); i++) {
        cells.Get(i + 1, 0).PutValue(U16String(data[i][0].c_str()));
        cells.Get(i + 1, 1).PutValue(std::stoi(data[i][1]));
        cells.Get(i + 1, 2).PutValue(std::stoi(data[i][2]));
    }
    Worksheet pivotSheet = workbook.GetWorksheets().Add(u"Pivot");
    PivotTableCollection pivots = pivotSheet.GetPivotTables();
    int pivotIndex = pivots.Add(u"E3", u"A1:C10", u"PivotTable1");
    PivotTable pivotTable = pivots.Get(pivotIndex);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");
    // — Abilita la selezione multipla sul campo pagina
    pivotTable.GetPageFields().Get(0).SetIsMultipleItemSelectionAllowed(true);
    // Parte A — seleziona TUTTI gli elementi (rendi visibile ogni elemento)
    PivotItemCollection pivotItems = pivotTable.GetPageFields().Get(0).GetPivotItems();
    int itemCount = pivotItems.GetCount();
    for (int i = 0; i < itemCount; i++) {
        pivotItems.Get(i).SetIsHidden(false);
    }
    // Parte B — seleziona solo elementi specifici per valore sorgente
    for (int i = 0; i < itemCount; i++) {
        U16String val = pivotItems.Get(i).GetStringValue();
        std::string s = val.ToUtf8();
        if (s == "2020" || s == "grape" || s == "blueberry") {
            pivotItems.Get(i).SetIsHidden(false);
        } else {
            pivotItems.Get(i).SetIsHidden(true);
        }
    }
    pivotTable.CalculateData();
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

> **Nota:** quando si utilizza il filtro a selezione multipla tramite `PivotItem.IsHidden`, **almeno un `PivotItem` deve rimanere visibile** (`IsHidden == false`). Se ogni elemento è nascosto, Excel si blocca all'apertura del file o visualizza una pivot vuota. Verifica sempre che la tua whitelist a selezione multipla includa almeno un elemento dei dati di origine.

## **Quale API e quale modalità devo utilizzare?**
La tabella seguente riassume quando utilizzare ciascuna API e modalità in modo da poter scegliere la giusta combinazione senza leggere ogni scenario nel dettaglio.
| Scenario / Caso d'uso | API consigliata | Proprietà utilizzata | Note |
|---|---|---|---|
| Aggiungere un campo filtro per nome della colonna di origine (più comune) | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | n/d | Alto livello, una sola riga. Usa questa opzione a meno che non sia necessario un riferimento `PivotField`. |
| Aggiungere un campo filtro quando si ha già un oggetto `PivotField` | `PivotTable.PageFields.Add(PivotField)` | n/d | Usare quando l'oggetto campo è stato ottenuto altrove o deve essere riutilizzato. |
| Filtrare su un singolo elemento del filtro (modalità predefinita) | `PivotField.CurrentPageItem` | impostare su un indice specifico | Ad esempio, `1` mostra il secondo elemento nell'elenco ordinato. |
| Mostrare tutti gli elementi / cancellare il filtro | `PivotField.CurrentPageItem` | impostare su `0x7FFD` | Il valore magico `0x7FFD` (decimale 32765) è il valore sentinella per "tutti gli elementi". |
| Abilitare l'interfaccia a selezione multipla in Excel | `PivotField.IsMultipleItemSelectionAllowed` | impostare su `true` | Richiesto prima che qualsiasi chiamata `IsHidden` abbia effetto. |
| Nascondere / mostrare singoli elementi in un elenco a selezione multipla | `PivotItem.IsHidden` | impostare per elemento | Almeno un elemento deve rimanere visibile (`IsHidden == false`). |

{{% alert color="primary" %}}
Ricorda sempre il vincolo di visibilità quando configuri il filtro a selezione multipla. Se ogni `PivotItem` in un campo filtro a selezione multipla è nascosto, Excel si blocca all'apertura o visualizza una pivot vuota. Crea la tua whitelist basandoti sui dati di origine in modo che almeno un elemento rimanga visibile e le tue cartelle di lavoro salvate si apriranno in modo affidabile su ogni macchina.
{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}