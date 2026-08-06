---
title: Filtrare le tabelle pivot per etichetta o valore
linktitle: Filtrare le tabelle pivot per etichetta o valore
description: Aspose.Cells for C++ supporta funzionalità complete di filtraggio delle tabelle pivot. Questo articolo spiega come filtrare i dati di una tabella pivot utilizzando filtri per etichetta, filtri per data, filtri per valore, filtri primi 10 e nascondendo o mostrando singoli elementi pivot.
keywords: Aspose.Cells, libreria C++, foglio di calcolo, tabella pivot, filtro, filtro per etichetta, filtro per valore, filtro per data, filtro primi 10, elemento pivot, nascondi elemento pivot
type: docs
weight: 10
url: /it/cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Aspose.Cells offre cinque strategie pratiche per filtrare i dati visualizzati in una tabella pivot. È possibile applicare filtri per etichetta ai campi di riga o colonna basati su testo, utilizzare filtri per data quando il campo contiene solo celle data-ora o vuote, applicare filtri per valore sui numeri aggregati, utilizzare filtri primi 10 per classificare in base a un campo valore, oppure nascondere e mostrare manualmente i singoli elementi pivot tramite la proprietà `IsHidden`. Ogni strategia è esposta tramite API dedicate sulle classi `PivotField` e `PivotItem`.
{{% /alert %}}
## **Introduzione**
Le tabelle pivot sono potenti strumenti analitici, ma i riepiloghi grezzi spesso contengono molte più informazioni di quelle effettivamente necessarie da presentare. Il filtraggio è il meccanismo principale per ridurre una tabella pivot alle righe, colonne o valori rilevanti per un report specifico. Aspose.Cells for C++ rispecchia le funzionalità di filtraggio disponibili in Microsoft Excel, esponendole in modo programmatico così che la generazione dei report possa essere completamente automatizzata.
Le seguenti strategie di filtraggio sono trattate in questo articolo:
1. **Filtro per etichetta** — filtra gli elementi dei campi di riga o colonna in base alle loro etichette di testo.
2. **Filtro per data** — filtra i campi di riga o colonna che contengono solo valori data-ora (o vuoti).
3. **Filtro per valore** — filtra gli elementi in base ai valori aggregati di un campo dati.
4. **Filtro primi 10** — mostra solo i primi o gli ultimi N elementi classificati in base a un campo valore.
5. **Nascondi/Mostra elementi pivot** — controlla manualmente la visibilità di ogni singolo elemento in un campo.
Ogni approccio utilizza un metodo diverso sulla classe `PivotField` o una proprietà sulla classe `PivotItem`. Dopo aver applicato qualsiasi filtro, è necessario chiamare `RefreshData()` e `CalculateData()` sulla tabella pivot in modo che i dati memorizzati nella cache e i valori calcolati riflettano il nuovo stato del filtro.
## **Filtro per etichetta**
Un filtro per etichetta consente di filtrare gli elementi di un campo di riga o colonna confrontando le relative didascalie di testo con un modello. Ciò è utile quando si desidera visualizzare solo i prodotti i cui nomi iniziano con una determinata lettera, contengono una parola specifica o soddisfano altri criteri basati sulla didascalia.
Aspose.Cells espone il filtraggio per etichetta tramite il metodo `PivotField.FilterByLabel(PivotFilterType, const char16_t*)`. L'enumerazione `PivotFilterType` include valori come `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` e così via. Il secondo argomento fornisce la stringa dell'etichetta utilizzata per il confronto.
L'esempio seguente carica una cartella di lavoro contenente una tabella pivot esistente, applica un filtro per etichetta in modo che solo gli elementi le cui didascalie inizino con un prefisso specificato rimangano visibili, aggiorna la tabella pivot e salva il risultato.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    U16String fileName(u"sample.xlsx");
    U16String prefix(u"B");

    // Carica la cartella di lavoro esistente contenente una tabella pivot
    Workbook wb(fileName);

    // Accedi al foglio di lavoro tramite indice (primo foglio di lavoro)
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Accedi alla tabella pivot tramite indice
    PivotTable pt = ws.GetPivotTables().Get(0);

    // Recupera il primo PivotField di riga
    PivotField rowField = pt.GetRowFields().Get(0);

    // Applica il filtro per etichetta — mostra solo gli elementi di riga le cui etichette iniziano con il prefisso fornito
    rowField.FilterByLabel(PivotFilterType::CaptionBeginsWith, prefix, U16String(u""));

    // Aggiorna e ricalcola i dati della tabella pivot affinché il filtro abbia effetto
    pt.RefreshData();

    // Salva la cartella di lavoro su disco
    wb.Save(fileName);

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Filtro per data**
I filtri per data consentono di restringere una tabella pivot in base a criteri basati sulla data, come oggi, settimana scorsa, questo mese, prossimo trimestre o un intervallo di date specifico. Sono filtri specializzati che funzionano solo con i campi che memorizzano informazioni data-ora.
{{% alert color="primary" %}}
Il filtro per data funziona solo quando l'area di riga o colonna contiene esclusivamente celle data-ora o valori vuoti. Se il campo sottostante contiene altri tipi di dati, come numeri o testo, il filtro per data non produrrà il risultato atteso. Assicurarsi che il campo sia formattato come data e che tutti i valori siano istanze valide di `DateTime` oppure celle vuote prima di applicare questo filtro.
{{% /alert %}}
Aspose.Cells espone il filtraggio per data tramite il metodo `PivotField.FilterByDate(PivotFilterType, const Vector<DateTime>& values)`. L'enumerazione `PivotFilterType` contiene valori dedicati alle date come `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` e `Between`. A seconda del tipo di filtro scelto, si passano uno o due valori `DateTime` (per `Between` si passano le date di inizio e fine).
L'esempio seguente carica una cartella di lavoro con una tabella pivot la cui area di riga contiene un campo data, applica un filtro per data che limita gli elementi visibili a un determinato intervallo di date, aggiorna la tabella pivot e salva la cartella di lavoro.
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
        // Cartella di lavoro sorgente non trovata.
        Aspose::Cells::Cleanup();
        return -1;
    }

    // Carica la cartella di lavoro esistente che contiene la tabella pivot
    Workbook workbook(U16String(inputPath.c_str()));

    // Accedi al foglio di lavoro che contiene la tabella pivot (per indice)
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accedi alla tabella pivot per indice
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Recupera il PivotField della data dall'area delle righe
    PivotField dateField = pivotTable.GetRowFields().Get(0);

    // Definisci il criterio di data per il filtro Between
    Date startDate{2020, 1, 1, 0, 0, 0, 0};
    Date endDate{2020, 12, 31, 0, 0, 0, 0};

    // Applica il filtro data sul campo pivot
    dateField.FilterByDate(PivotFilterType::DateBetween, startDate, endDate);

    // Aggiorna e ricalcola la tabella pivot affinché il filtro abbia effetto
    // Salva la cartella di lavoro
    workbook.Save(U16String(outputPath.c_str()));

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Filtro per valore**
I filtri per valore operano sui valori aggregati che una tabella pivot calcola nella sua area dati. Invece di confrontare le etichette di testo, confrontano i totali numerici con una soglia. Casi d'uso tipici includono mostrare solo i prodotti la cui somma delle vendite supera un importo target oppure solo le regioni il cui conteggio di transazioni rientra in un intervallo.
Aspose.Cells espone il filtraggio per valore tramite il metodo `PivotField.FilterByValue(PivotField valueField, PivotFilterType filterType, const Vector<Variant>& values)`. Il parametro `filterType` utilizza valori come `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` e `ValueLessThanOrEqual`. Il parametro `valueField` specifica quale campo dati deve essere valutato, e gli argomenti finali forniscono i valori di soglia.
L'esempio seguente carica una cartella di lavoro con una tabella pivot, applica un filtro per valore che mantiene solo gli elementi le cui vendite aggregate superano una soglia numerica, aggiorna la tabella pivot e salva la cartella di lavoro.
```cpp
#include "Aspose.Cells.h"
#include <cfloat>

using namespace Aspose::Cells;

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

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Filtro primi 10**
Il filtro primi 10 è una forma specializzata di filtro per valore che mantiene solo gli N elementi più alti o più bassi in base a un campo valore scelto. È comunemente utilizzato per i report di classificazione come "top 10 prodotti per ricavi" oppure "bottom 5 regioni per numero di vendite".
{{% alert color="primary" %}}
Il filtro primi 10 è efficace solo quando la tabella pivot dispone di uno o più campi valore nell'area dati. Senza almeno un campo valore, non esiste una misura aggregata rispetto alla quale classificare gli elementi e il filtro non può essere applicato.
{{% /alert %}}
Aspose.Cells espone il filtraggio primi 10 tramite il metodo `PivotField.FilterTop10(int32_t itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)`. Il parametro `itemCount` definisce quanti elementi mantenere, `isTop` indica se mantenere gli elementi superiori (true) o inferiori (false), `valueField` fa riferimento al campo dati utilizzato per la classificazione e `filterType` controlla come viene calcolato il valore (tipicamente `Sum`, ma anche `Count` e `Percent`).
L'esempio seguente carica una cartella di lavoro con una tabella pivot che contiene un campo valore, applica un filtro primi 10 per mantenere solo i 10 elementi più alti in base alla somma delle vendite, aggiorna la tabella pivot e salva la cartella di lavoro.
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

    rowField.FilterTop10(10, PivotFilterType::Sum, true, valueFieldIndex);

    workbook.Save(outputPath);

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Filtro tramite nascondere o mostrare gli elementi pivot**
Oltre alle API di filtraggio strutturate, Aspose.Cells consente di controllare direttamente la visibilità di ogni singolo elemento pivot. Iterando attraverso la raccolta `PivotItems` di un `PivotField` e attivando la proprietà `IsHidden`, è possibile sopprimere selettivamente elementi specifici senza applicare un filtro basato su formule. Impostando `IsHidden = true` si nasconde l'elemento dalla tabella pivot; impostando `IsHidden = false` lo si rende nuovamente visibile.
Questo approccio è utile quando la regola di filtraggio è irregolare o specifica per gli elementi, come nel caso di nascondere un piccolo numero di categorie denominate che non devono apparire in un determinato report. L'esempio seguente carica una tabella pivot, nasconde un elemento specifico per nome, mostra come ripristinarne la visibilità, aggiorna la tabella pivot e salva la cartella di lavoro.
```cpp
ells.h"
#include <string>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Carica una cartella di lavoro esistente contenente una tabella pivot
    Workbook workbook(u"pivot_table_sample.xlsx");

    // Accedi al primo foglio di lavoro che contiene la tabella pivot
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Accedi alla tabella pivot tramite indice (la prima tabella pivot nel foglio)
    PivotTable pivotTable = sheet.GetPivotTables().Get(0);

    // Recupera il PivotField target (il primo campo etichetta di riga in cui nasconderemo/mostreremo gli elementi)
    PivotField pivotField = pivotTable.GetRowFields().Get(0);

    // Itera attraverso la collezione PivotItems del PivotField selezionato
    int itemCount = pivotField.GetPivotItems().GetCount();
    for (int i = 0; i < itemCount; i++)
    {
        PivotItem item = pivotField.GetPivotItems().Get(i);

        U16String name = item.GetName();
        std::string nameStr = name.ToUtf8();

        // Nascondi gli elementi pivot che corrispondono a un nome/criterio specifico
        if (nameStr == "Item1" || nameStr == "Item2")
        {
            item.SetIsHidden(true);
        }

        // Dimostra come mostrare nuovamente: ri-mostra un elemento pivot precedentemente nascosto
        if (nameStr == "Item3")
        {
            item.SetIsHidden(false);
        }
    }

    // Aggiorna e ricalcola la tabella pivot in modo che le modifiche abbiano effetto
    pivotTable.CalculateData();

    // Salva la cartella di lavoro — gli elementi nascosti rimangono nei dati sottostanti
    // ma sono esclusi dall'output visualizzato della tabella pivot
    workbook.Save(u"output_pivot_filtered.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## **Riepilogo**
Aspose.Cells for C++ fornisce un set completo di funzionalità di filtraggio delle tabelle pivot che corrispondono a quelle disponibili in Microsoft Excel. I filtri per etichetta, data e valore coprono gli scenari analitici più comuni, mentre il filtro primi 10 gestisce i report di classificazione. Quando la regola di filtraggio è irregolare, la proprietà `PivotItem.IsHidden` offre un fallback flessibile a livello di elemento. Combinare queste strategie — ad esempio applicando un filtro per etichetta e poi nascondendo elementi specifici — consente di costruire report di tabelle pivot mirati esclusivamente tramite codice.
{{< app/cells/assistant language="cpp" >}}