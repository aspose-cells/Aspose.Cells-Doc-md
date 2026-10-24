---
title: Raggruppare i campi pivot nella tabella pivot
linktitle: Raggruppare i campi pivot nella tabella pivot
description: Scopri come raggruppare i campi pivot di riga e colonna in una tabella pivot in periodi di date come mesi e trimestri e in intervalli numerici utilizzando PivotField.Group e PivotFieldGroupOptions in Aspose.Cells for Python via .NET.
keywords: Aspose.Cells, tabella pivot, raggruppare campo pivot, PivotField.Group, PivotFieldGroupOptions, raggruppamento date, raggruppamento numeri, mesi, trimestri, intervallo numerico, Python via .NET
type: docs
weight: 80
url: /it/python-net/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari d'uso**
- Il raggruppamento dei campi pivot è utile quando un campo di riga o colonna di una tabella pivot contiene molti elementi distinti, ad esempio un campo data con centinaia di date o un campo numerico con molti valori sparsi. Il raggruppamento riduce questi elementi in sezioni significative: le date in mesi, trimestri e anni, e i numeri in intervalli come 0-1, 2-3, 4-5. Ciò rende una grande tabella pivot compatta e più facile da analizzare. Aspose.Cells for Python via .NET fornisce questa funzionalità tramite il metodo `pivot_field.group()` (raggruppamento automatico per tipo di dati) e `pivot_field.group(pivot_field_group_options)` (opzioni di raggruppamento personalizzate).
- Il raggruppamento per date aggrega le singole date in periodi più ampi, come giorni, mesi, trimestri e anni, e costruisce una gerarchia temporale (ad esempio Anni, Trimestri, Mesi). Le tendenze nel tempo diventano visibili a colpo d'occhio e ogni livello di periodo diventa un campo pivot a sé stante nell'area riga o colonna della tabella pivot.
- Il raggruppamento è disponibile solo per i campi posizionati nell'area RIGA o COLONNA di una tabella pivot. Un campo dati (valore) non può essere raggruppato direttamente. Per raggruppare tale campo è necessario prima aggiungerlo all'area riga o colonna della tabella pivot.

## **Raggruppare i campi pivot automaticamente**
L'overload senza parametri `pivot_field.group()` esamina il tipo di dati del campo e lo raggruppa automaticamente. Un campo che contiene solo date (e valori vuoti) viene raggruppato per mesi. Un campo che contiene solo numeri (e valori vuoti) viene raggruppato in intervalli numerici utilizzando un intervallo automatico.

```python
import aspose.cells as ac
# Carica il workbook di esempio
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Accedi al secondo foglio di lavoro e alla sua tabella pivot
pt = wb.worksheets[1].pivot_tables[0]
# Raggruppa automaticamente il primo campo riga.
# Il campo contiene date, quindi viene raggruppato per mesi.
field = pt.row_fields[0]
field.group()
# Calcola i dati della tabella pivot e salva il file di output
pt.calculate_data()
wb.save("outputAutoGroupPivotField.xlsx")
```

## **Raggruppare i campi pivot con opzioni personalizzate**
La classe `PivotFieldGroupOptions` fornisce una configurazione di raggruppamento personalizzata. Per i campi data, impostare `start_date`, `end_date` e `group_types`. Per i campi numerici, impostare `start_number`, `end_number` e `interval`. La proprietà `new_pivot_field` controlla se il raggruppamento crea nuovi campi pivot accanto all'originale (consultare la sezione Nota alla fine di questo articolo).

### **Raggruppare un campo data per mesi e trimestri**
L'esempio seguente raggruppa il campo data di riga della tabella pivot di esempio per mesi e trimestri tra una data di inizio e una data di fine. Il codice carica il [file Excel di esempio](sampleGroupPivotFieldsInPivotTable.xlsx), esegue il raggruppamento, calcola i dati della tabella pivot e salva il risultato raggruppato. Lo screenshot mostra l'effetto: il campo data di riga è ora raggruppato per trimestri e mesi.
Nota che l'ordine dei valori in `options.group_types` viene ignorato. Indipendentemente dall'ordine in cui sono elencati i tipi di gruppo, i campi raggruppati vengono sempre visualizzati dal periodo più ampio al più piccolo: anni, trimestri, mesi, giorni, ore, minuti, secondi. In questo esempio i mesi sono elencati prima dei trimestri in `options.group_types`, eppure i trimestri vengono visualizzati come livello esterno e i mesi come livello interno.

```python
import aspose.cells as ac
from datetime import datetime
from aspose.cells.pivot import PivotGroupByType
from aspose.cells.pivot import PivotFieldGroupOptions
# Carica il workbook di esempio
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Accedi al secondo foglio di lavoro e alla sua tabella pivot
pt = wb.worksheets[1].pivot_tables[0]
# Raggruppa il primo campo riga (un campo data) per mesi e trimestri
options = PivotFieldGroupOptions()
options.start_date = datetime(2008, 1, 1)
options.end_date = datetime(2008, 9, 5)
options.group_types = [PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS]
pt.row_fields[0].group(options)
# Calcola i dati della tabella pivot e salva il file di output
pt.calculate_data()
wb.save("outputGroupPivotFieldsInPivotTable.xlsx")
```

![Tabella pivot raggruppata per mesi e trimestri](group-pivot-fields-in-the-pivot-table_1.png)

### **Raggruppare un campo numerico in intervalli**
`FieldTwo` della tabella pivot di esempio è inizialmente un campo dati (valore). Poiché possono essere raggruppati solo i campi di riga o colonna, il codice prima chiama `pivot_table.add_field_to_area(PivotFieldType.ROW, "FieldTwo")` per spostare `FieldTwo` nell'area riga, aggiorna la tabella pivot, quindi raggruppa il campo numerico negli intervalli 0-1, 2-3 e 4-5 utilizzando `start_number=0`, `end_number=5` e `interval=2`.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldGroupOptions
# Carica la cartella di lavoro di esempio
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Accedi al secondo foglio di lavoro e alla sua tabella pivot
pt = wb.worksheets[1].pivot_tables[0]
# FieldTwo è un campo dati: spostalo prima nell'area delle righe,
# perché solo i campi riga/colonna possono essere raggruppati
pt.add_field_to_area(PivotFieldType.ROW, "FieldTwo")
pt.calculate_data()
# Raggruppa il campo numerico negli intervalli 0-1, 2-3, 4-5
options = PivotFieldGroupOptions()
options.start_number = 0.0
options.end_number = 5.0
options.interval = 2.0
pt.row_fields[1].group(options)
# Calcola i dati della tabella pivot e salva il file di output
pt.calculate_data()
wb.save("outputNumberGroupPivotField.xlsx")
```

## **Nota**

{{% alert color="primary" %}}
- Gli overload del metodo `pivot_field.group_by()` sono deprecati e rimossi dalla superficie API. `pivot_field.group()` e `pivot_field.group(pivot_field_group_options)` sono i metodi che li sostituiscono.
- In Microsoft Excel, il raggruppamento di un campo numerico SOSTITUISCE il campo pivot originale con gli intervalli raggruppati, mentre il raggruppamento di un campo data crea NUOVI campi pivot (uno per livello di gruppo, ad esempio Trimestri e Mesi) accanto al campo originale. A partire da Aspose.Cells 26.10, i metodi `pivot_field.group()` seguono lo stesso comportamento di Excel. La proprietà `PivotFieldGroupOptions.new_pivot_field` esiste per compatibilità con le versioni precedenti: per impostazione predefinita è false per il raggruppamento numerico e true per il raggruppamento data-ora; impostarla su false se si desidera che il raggruppamento per date sostituisca il campo pivot originale invece di creare nuovi campi pivot.
- La proprietà `PivotFieldGroupOptions.interval` ha effetto solo per il raggruppamento numerico e per il raggruppamento di date per giorni (ad esempio, raggruppare le date in periodi di 7 giorni); viene ignorata quando le date sono raggruppate per mesi, trimestri o anni.
{{% /alert %}}

## **Articoli correlati**
- [Aggiungere campi di riga e colonna nella tabella pivot](/cells/it/python-net/pivot-table-add-row-and-column-fields/)
- [Filtrare le tabelle pivot per etichetta o valore](/cells/it/python-net/filter-by-label-or-value-of-pivot-table/)
- [Aggiungere un campo pagina nella tabella pivot](/cells/it/python-net/add-page-field-in-pivot-table/)
- [Applicare uno stile alla tabella pivot](/cells/it/python-net/apply-style-to-pivot-table/)
- [Aggiornare la tabella pivot](/cells/it/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}