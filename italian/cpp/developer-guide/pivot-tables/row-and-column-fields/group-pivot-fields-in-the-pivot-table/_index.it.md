---
title: Raggruppare i Campi Pivot in una Tabella Pivot
linktitle: Raggruppare i Campi Pivot in una Tabella Pivot
description: Scopri come raggruppare i campi pivot di righe e colonne in una tabella pivot in periodi di date come mesi e trimestri e in intervalli numerici utilizzando PivotField.Group e PivotFieldGroupOptions in Aspose.Cells for C++.
keywords: Aspose.Cells, tabella pivot, raggruppa campo pivot, PivotField.Group, PivotFieldGroupOptions, raggruppamento date, raggruppamento numeri, mesi, trimestri, intervallo numerico, C++
type: docs
weight: 80
url: /it/cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili Scenari di Utilizzo**
- Il raggruppamento dei campi pivot è utile quando un campo di riga o colonna di una tabella pivot contiene molti elementi distinti, ad esempio un campo data con centinaia di date o un campo numerico con molti valori sparsi. Il raggruppamento riunisce tali elementi in sezioni significative: le date in mesi, trimestri e anni, e i numeri in intervalli come 0-1, 2-3, 4-5. Ciò rende una tabella pivot di grandi dimensioni più compatta e facile da analizzare. Aspose.Cells fornisce questa funzionalità tramite il metodo `PivotField.Group()` (raggruppamento automatico per tipo di dati) e `PivotField.Group(PivotFieldGroupOptions)` (opzioni di raggruppamento personalizzate).
- Il raggruppamento per data consolida le singole date in periodi più ampi, come giorni, mesi, trimestri e anni, e costruisce una gerarchia temporale (ad esempio Anni, Trimestri, Mesi). Gli andamenti nel tempo diventano visibili a colpo d'occhio e ogni livello di periodo diventa un campo pivot distinto nell'area delle righe o delle colonne della tabella pivot.
- Il raggruppamento è disponibile solo per i campi posizionati nell'area RIGA o COLONNA di una tabella pivot. Un campo dati (valore) non può essere raggruppato direttamente. Per raggruppare un tale campo è necessario prima aggiungerlo all'area delle righe o delle colonne della tabella pivot.

## **Raggruppare i Campi Pivot Automaticamente**
L'overload senza parametri `PivotField.Group()` analizza il tipo di dati del campo e lo raggruppa automaticamente. Un campo che contiene solo date (e valori vuoti) viene raggruppato per mesi. Un campo che contiene solo numeri (e valori vuoti) viene raggruppato in intervalli numerici utilizzando un intervallo automatico.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    PivotField field = pt.GetRowFields().Get(0);
    field.Group();
    pt.CalculateData();
    wb.Save(u"outputAutoGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Raggruppare i Campi Pivot con Opzioni Personalizzate**
La classe `PivotFieldGroupOptions` fornisce la configurazione di raggruppamento personalizzata. Per i campi data, impostare `StartDate`, `EndDate` e `GroupTypes`. Per i campi numerici, impostare `StartNumber`, `EndNumber` e `Interval`. La proprietà `NewPivotField` controlla se il raggruppamento crea nuovi campi pivot accanto all'originale (consultare la sezione Note alla fine di questo articolo).

### **Raggruppare un Campo Data per Mesi e Trimestri**
Il seguente esempio raggruppa il campo data di riga della tabella pivot di esempio per mesi e trimestri tra una data di inizio e una data di fine. Il codice carica il [file Excel di esempio](sampleGroupPivotFieldsInPivotTable.xlsx), esegue il raggruppamento, calcola i dati della tabella pivot e salva il risultato raggruppato. Lo screenshot mostra l'effetto: il campo data di riga è ora raggruppato per trimestri e mesi.
Si noti che l'ordine dei valori in `options.GroupTypes` viene ignorato. Indipendentemente dall'ordine in cui sono elencati i tipi di gruppo, i campi raggruppati vengono sempre visualizzati dal periodo più ampio al più piccolo: anni, trimestri, mesi, giorni, ore, minuti, secondi. In questo esempio i mesi sono elencati prima dei trimestri in `options.GroupTypes`, eppure i trimestri vengono visualizzati come livello esterno e i mesi come livello interno.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Carica la cartella di lavoro di esempio
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    // Accedi al secondo foglio di lavoro e alla sua tabella pivot
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    // Raggruppa il primo campo riga (un campo data) per mesi e trimestri
    PivotFieldGroupOptions options;
    Date startDate{2008, 1, 1, 0, 0, 0, 0};
    Date endDate{2008, 9, 5, 0, 0, 0, 0};
    options.SetStartDate(startDate);
    options.SetEndDate(endDate);
    // Imposta i tipi di raggruppamento: Mesi e Trimestri
    Vector<PivotGroupByType> groupTypes{ PivotGroupByType::Months, PivotGroupByType::Quarters };
    options.SetGroupTypes(groupTypes);
    // Applica il raggruppamento al primo campo riga
    PivotField rowField = pt.GetRowFields().Get(0);
    rowField.Group(options);
    // Calcola i dati della tabella pivot e salva il file di output
    pt.CalculateData();
    wb.Save(u"outputGroupPivotFieldsInPivotTable.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

![Tabella pivot raggruppata per mesi e trimestri](group-pivot-fields-in-the-pivot-table_1.png)

### **Raggruppare un Campo Numerico in Intervalli**
`FieldTwo` della tabella pivot di esempio è inizialmente un campo dati (valore). Poiché solo i campi di riga o colonna possono essere raggruppati, il codice prima chiama `PivotTable.AddFieldToArea(PivotFieldType.Row, "FieldTwo")` per spostare `FieldTwo` nell'area delle righe, aggiorna la tabella pivot, quindi raggruppa il campo numerico negli intervalli 0-1, 2-3 e 4-5 utilizzando `StartNumber = 0`, `EndNumber = 5` e `Interval = 2`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    pt.AddFieldToArea(PivotFieldType::Row, U16String("FieldTwo"));
    pt.CalculateData();
    PivotFieldGroupOptions options;
    options.SetStartNumber(0);
    options.SetEndNumber(5);
    options.SetInterval(2);
    pt.GetRowFields().Get(1).Group(options);
    pt.CalculateData();
    wb.Save(u"outputNumberGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Note**

{{% alert color="primary" %}}
- Gli overload del metodo `PivotField.GroupBy()` sono deprecati e rimossi dalla superficie API. `PivotField.Group()` e `PivotField.Group(PivotFieldGroupOptions)` sono le sostituzioni.
- In Microsoft Excel, il raggruppamento di un campo numerico SOSTITUISCE il campo pivot originale con gli intervalli raggruppati, mentre il raggruppamento di un campo data crea NUOVI campi pivot (uno per ciascun livello di gruppo, ad esempio Trimestri e Mesi) accanto al campo originale. A partire da Aspose.Cells 26.10, i metodi `PivotField.Group()` seguono lo stesso comportamento di Excel. La proprietà `PivotFieldGroupOptions.NewPivotField` esiste per la compatibilità con le versioni precedenti: il suo valore predefinito è false per il raggruppamento numerico e true per il raggruppamento data-ora; impostarla su false se si desidera che il raggruppamento per data sostituisca il campo pivot originale invece di creare nuovi campi pivot.
- La proprietà `PivotFieldGroupOptions.Interval` ha effetto solo per il raggruppamento numerico e per il raggruppamento di date per giorni (ad esempio, il raggruppamento di date in periodi di 7 giorni); viene ignorata quando le date vengono raggruppate per mesi, trimestri o anni.
{{% /alert %}}

## **Articoli Correlati**
- [Aggiungere Campi di Riga e Colonna nella Tabella Pivot](/cells/it/cpp/pivot-table-add-row-and-column-fields/)
- [Filtrare le Tabelle Pivot per Etichetta o Valore](/cells/it/cpp/filter-by-label-or-value-of-pivot-table/)
- [Aggiungere un Campo Pagina nella Tabella Pivot](/cells/it/cpp/add-page-field-in-pivot-table/)
- [Applicare uno Stile alla Tabella Pivot](/cells/it/cpp/apply-style-to-pivot-table/)
- [Aggiornare la Tabella Pivot](/cells/it/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}