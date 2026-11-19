---
title: Filtraggio delle tabelle pivot per etichetta o valore
linktitle: Filtraggio delle tabelle pivot per etichetta o valore
description: Aspose.Cells for C++ offre funzionalità complete di filtraggio delle tabelle pivot. Questo articolo spiega come filtrare i dati di una tabella pivot utilizzando filtri per etichetta, filtri per data, filtri per valore, filtri Top 10 e come nascondere o mostrare gli elementi pivot.
keywords: Aspose.Cells, libreria C++, foglio di lavoro, tabella pivot, filtro, filtro per etichetta, filtro per valore, filtro per data, filtro Top 10, elemento pivot, nascondere un elemento pivot
type: docs
weight: 10
url: /it/cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells offre cinque strategie pratiche per filtrare i dati visualizzati in una tabella pivot. È possibile applicare filtri per etichetta ai campi riga o colonna contenenti testo, utilizzare filtri per data quando il campo contiene solo celle con data e ora oppure celle vuote, applicare filtri per valore in base ai numeri aggregati, utilizzare filtri Top 10 per classificare gli elementi in base a un campo valore, oppure nascondere e mostrare manualmente singoli elementi pivot tramite la proprietà `IsHidden`. Ogni strategia può essere applicata tramite API dedicate disponibili nelle classi `PivotField` e `PivotItem`.
{{% /alert %}}

## **Introduzione**
Le tabelle pivot sono potenti strumenti analitici, ma i riepiloghi iniziali spesso contengono molte più informazioni di quante ne siano necessarie per il report. Il filtraggio è il meccanismo principale per restringere una tabella pivot alle righe, alle colonne o ai valori rilevanti per un report specifico. Aspose.Cells for C++ offre funzionalità di filtraggio equivalenti a quelle disponibili in Microsoft Excel e le espone a livello programmatico, consentendo di automatizzare completamente la generazione dei report.
Le seguenti strategie di filtraggio sono illustrate in questo articolo:
1. **Filtro per etichetta** — filtra gli elementi di un campo riga o colonna in base alle rispettive etichette testuali.
2. **Filtro per data** — filtra i campi riga o colonna che contengono solo celle con valori di data e ora oppure vuote.
3. **Filtro per valore** — filtra gli elementi in base ai valori aggregati di un campo dati.
4. **Filtro Top 10** — mostra solo i N elementi con i valori più elevati o più bassi, classificati in base a un campo valore.
5. **Nascondere/Mostrare elementi pivot** — controlla manualmente la visibilità di ogni singolo elemento di un campo.
Ogni approccio utilizza un metodo specifico della classe `PivotField` o una proprietà della classe `PivotItem`. Dopo l'applicazione di un filtro, è necessario chiamare `GetPivotCache().Refresh()` sulla tabella pivot, in modo che i dati memorizzati nella cache e i valori calcolati riflettano il nuovo stato del filtro.

## **Filtro per etichetta**
Un filtro per etichetta consente di filtrare gli elementi di un campo riga o colonna confrontando le relative didascalie testuali con un modello. È utile quando si desidera visualizzare solo i prodotti il cui nome inizia con una lettera specifica, contiene una determinata parola o corrisponde a un altro criterio basato sulla didascalia.
Aspose.Cells espone il filtraggio per etichetta tramite il metodo `PivotField.FilterByLabel(PivotFilterType, const char16_t*)`. L'enumerazione `PivotFilterType` include, tra gli altri, valori come `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank` e `CaptionIsBlank`. Il secondo argomento specifica la stringa di etichetta utilizzata per il confronto.
L'esempio seguente carica una cartella di lavoro contenente una tabella pivot esistente, applica un filtro per etichetta in modo che rimangano visibili solo gli elementi le cui didascalie iniziano con un prefisso specificato, aggiorna la tabella pivot e salva il risultato.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    U16String fileName(u"sample.xlsx");
    U16String prefix(u"B");
    // Load the existing workbook containing a pivot table
    Workbook wb(fileName);
    // Access the worksheet by index (first worksheet)
    Worksheet ws = wb.GetWorksheets().Get(0);
    // Access the pivot table by index
    PivotTable pt = ws.GetPivotTables().Get(0);
    // Retrieve the first row PivotField
    PivotField rowField = pt.GetRowFields().Get(0);
    // Apply the label filter — show only row items whose labels begin with the supplied prefix
    rowField.FilterByLabel(PivotFilterType::CaptionBeginsWith, prefix, U16String(u""));
    // Refresh and recalculate the pivot table data so the filter takes effect
    pt.GetPivotCache().Refresh();
    // Save the workbook back to disk
    wb.Save(fileName);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtro per data**
I filtri per data consentono di restringere una tabella pivot in base a criteri come il giorno corrente, la settimana scorsa, il mese in corso, il prossimo trimestre o un intervallo di date specifico. Sono filtri specializzati che operano esclusivamente su campi contenenti informazioni relative a data e ora.

{{% alert color="primary" %}}
Il filtro per data funziona solo quando l'area delle righe o delle colonne è composta esclusivamente da celle con data e ora oppure vuote. Se il campo di origine contiene altri tipi di dati, come numeri o testo, il filtro per data non produce il risultato previsto. Prima di applicare il filtro, assicurarsi che il campo sia formattato come data e che tutti i valori siano istanze `DateTime` valide o che le celle corrispondenti siano vuote.
Aspose.Cells espone il filtraggio per data tramite il metodo `PivotField.FilterByDate(PivotFilterType, const Vector<DateTime>& values)`. L'enumerazione `PivotFilterType` contiene valori specifici per le date, tra cui `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` e `Between`. A seconda del tipo di filtro selezionato, passare uno o due valori `DateTime` (per `Between`, passare la data di inizio e quella di fine).
L'esempio seguente carica una cartella di lavoro con una tabella pivot la cui area delle righe contiene un campo data, applica un filtro per data che limita gli elementi visibili a un intervallo di date specifico, aggiorna la tabella pivot e salva la cartella di lavoro.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    std::string inputPath = "sample.xlsx";
    std::string outputPath = "output_filtered.xlsx";
    if (!std::filesystem::exists(inputPath))
    {
        // Source workbook not found.
        Aspose::Cells::Cleanup();
        return -1;
    }
    // Load the existing workbook that contains the pivot table
    Workbook workbook(U16String(inputPath.c_str()));
    // Access the worksheet that holds the pivot table (by index)
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Access the pivot table by index
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    // Retrieve the date PivotField from the row area
    PivotField dateField = pivotTable.GetRowFields().Get(0);
    // Define the date criterion for the Between filter
    Date startDate{2020, 1, 1, 0, 0, 0, 0};
    Date endDate{2020, 12, 31, 0, 0, 0, 0};
    // Apply the date filter on the pivot field
    dateField.FilterByDate(PivotFilterType::DateBetween, startDate, endDate);
    // Refresh and recalculate the pivot table so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    // Persist the workbook
    workbook.Save(U16String(outputPath.c_str()));
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtro per valore**
I filtri per valore operano sui valori aggregati che una tabella pivot calcola nell'area dati. A differenza dei filtri per etichetta, confrontano i totali numerici con una soglia. Gli scenari tipici includono la visualizzazione dei soli prodotti la cui somma delle vendite supera un importo obiettivo o delle sole regioni il cui numero di transazioni rientra in un intervallo.
Aspose.Cells espone il filtraggio per valore tramite il metodo `PivotField.FilterByValue(PivotField valueField, PivotFilterType filterType, const Vector<Variant>& values)`. Il parametro `filterType` accetta valori quali `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` e `ValueLessThanOrEqual`. Il parametro `valueField` specifica quale campo dati deve essere valutato, mentre gli argomenti finali forniscono i valori di soglia.
L'esempio seguente carica una cartella di lavoro con una tabella pivot, applica un filtro per valore che mantiene solo gli elementi le cui vendite aggregate superano una soglia numerica, aggiorna la tabella pivot e salva la cartella di lavoro.

```cpp
#include "Aspose.Cells.h"
#include <cfloat>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sample.xlsx");
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    PivotField rowField = pivotTable.GetRowFields().Get(0);
    PivotField dataField = pivotTable.GetDataFields().Get(0);
    int dataFieldIndex = -1;
    int dataFieldCount = pivotTable.GetDataFields().GetCount();
    for (int i = 0; i < dataFieldCount; i++)
    {
        PivotField current = pivotTable.GetDataFields().Get(i);
        if (current.GetName() == dataField.GetName())
        {
            dataFieldIndex = i;
            break;
        }
    }
    if (dataFieldIndex >= 0)
    {
        rowField.FilterByValue(dataFieldIndex, PivotFilterType::ValueGreaterThan, 5000, DBL_MAX);
    }
    // Refresh and recalculate the pivot table so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtro Top 10**
Il filtro Top 10 è una forma specializzata di filtro per valore che mantiene solo i N elementi con i valori più elevati o più bassi, in base a un campo valore selezionato. È comunemente utilizzato per generare report classificati, come «10 prodotti principali in base al fatturato» o «5 regioni in fondo alla classifica in base al numero di vendite».

{{% alert color="primary" %}}
Il filtro Top 10 è efficace solo quando la tabella pivot contiene uno o più campi valore nell'area dati. In assenza di almeno un campo valore, non esiste una misura aggregata rispetto alla quale classificare gli elementi e il filtro non può essere applicato.
Aspose.Cells espone il filtraggio Top 10 tramite il metodo `PivotField.FilterTop10(int32_t valueFieldIndex, PivotFilterType type, bool isTop, int32_t itemCount)`. Il parametro `valueFieldIndex` è l'indice del campo dati i cui valori aggregati vengono utilizzati per classificare gli elementi. Il parametro `type` determina se `itemCount` esprime un numero di elementi o una percentuale (`PivotFilterType::Count` mantiene un numero fisso di elementi, mentre `PivotFilterType::Percent` mantiene una percentuale di elementi e `itemCount` rappresenta la percentuale stessa). Il parametro `isTop` indica se mantenere gli elementi in cima alla classifica (`true`) o in fondo alla classifica (`false`), mentre `itemCount` definisce quanti elementi o quale percentuale mantenere.
L'esempio seguente carica una cartella di lavoro con una tabella pivot che contiene un campo valore, applica un filtro Top 10 per mantenere solo i 10 elementi con il valore più elevato della somma delle vendite, aggiorna la tabella pivot e salva la cartella di lavoro.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <stdexcept>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    U16String inputPath(u"input.xlsx");
    U16String outputPath(u"output.xlsx");
    Workbook workbook(inputPath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);
    if (pivotTable.GetDataFields().GetCount() == 0) {
        throw std::runtime_error("Pivot table has no value (data) PivotField.");
    }
    PivotField valueField = pivotTable.GetDataFields().Get(0);
    PivotField rowField = pivotTable.GetRowFields().Get(0);
    int valueFieldIndex = 0;
    rowField.FilterTop10(valueFieldIndex, PivotFilterType::Count, true, 10);
    // Refresh the pivot table data and recalculate it so the filter takes effect
    pivotTable.GetPivotCache().Refresh();
    workbook.Save(outputPath);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Filtro tramite nascondere o mostrare elementi pivot**
Oltre alle API di filtraggio strutturato, Aspose.Cells consente di controllare direttamente la visibilità di ciascun elemento pivot. Scorrendo la raccolta `PivotItems` di un `PivotField` e impostando la proprietà `IsHidden`, è possibile nascondere selettivamente elementi specifici senza applicare un filtro basato su formule. L'impostazione `IsHidden = true` nasconde l'elemento dalla tabella pivot; l'impostazione `IsHidden = false` lo rende nuovamente visibile.
Questo approccio è utile quando la regola di filtraggio è irregolare o specifica per un singolo elemento, ad esempio per nascondere un piccolo numero di categorie specifiche che non devono comparire in un report determinato. L'esempio seguente carica una cartella di lavoro contenente una tabella pivot, nasconde un elemento specifico in base al nome, illustra come mostrarlo, aggiorna la tabella pivot e salva la cartella di lavoro.

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Load an existing workbook containing a pivot table
    Workbook workbook(u"pivot_table_sample.xlsx");
    // Access the first worksheet which contains the pivot table
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    // Access the pivot table by index (the first pivot table on the sheet)
    PivotTable pivotTable = sheet.GetPivotTables().Get(0);
    // Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
    PivotField pivotField = pivotTable.GetRowFields().Get(0);
    // Iterate through the PivotItems collection of the selected PivotField
    int itemCount = pivotField.GetPivotItems().GetCount();
    for (int i = 0; i < itemCount; i++)
    {
        PivotItem item = pivotField.GetPivotItems().Get(i);
        U16String name = item.GetName();
        std::string nameStr = name.ToUtf8();
        // Hide pivot items that match a specific name/criterion
        if (nameStr == "Item1" || nameStr == "Item2")
        {
            item.SetIsHidden(true);
        }
        // Demonstrate unhiding: re-show a previously hidden pivot item
        if (nameStr == "Item3")
        {
            item.SetIsHidden(false);
        }
    }
    // Refresh and recalculate the pivot table so changes take effect
    pivotTable.GetPivotCache().Refresh();
    // Save the workbook — hidden items stay in the underlying data
    // but are excluded from the displayed pivot table output
    workbook.Save(u"output_pivot_filtered.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Riepilogo**
Aspose.Cells for C++ offre un insieme completo di funzionalità di filtraggio delle tabelle pivot, corrispondenti a quelle disponibili in Microsoft Excel. I filtri per etichetta, per data e per valore coprono gli scenari analitici più comuni, mentre il filtro Top 10 gestisce i report basati su classifiche. Quando la regola di filtraggio è irregolare, la proprietà `PivotItem.IsHidden` offre un'alternativa flessibile applicabile ai singoli elementi. La combinazione di queste strategie — ad esempio, l'applicazione di un filtro per etichetta e il successivo occultamento di elementi specifici — consente a creare interamente da codice report basati su tabelle pivot e mirati con precisione.

## Articoli correlati
- [Inserire una tabella pivot](/cells/it/cpp/create-pivot-table/)
- [Aggiungere campi riga e colonna a una tabella pivot in Aspose.Cells for C++](/cells/it/cpp/pivot-table-add-row-and-column-fields/)
- [Aggiungere campi filtro a una tabella pivot in Aspose.Cells for C++](/cells/it/cpp/add-page-field-in-pivot-table/)
- [Gestire i campi valore delle tabelle pivot in Aspose.Cells for C++](/cells/it/cpp/manage-value-fields/)
- [Aggiornare le tabelle pivot e le relative cache in Aspose.Cells for C++](/cells/it/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}