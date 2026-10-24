---
title: Raggruppare i campi pivot nella tabella pivot
linktitle: Raggruppare i campi pivot nella tabella pivot
description: Scopri come raggruppare i campi pivot di riga e colonna in una tabella pivot in periodi di date come mesi e trimestri e in intervalli numerici usando PivotField.group e PivotFieldGroupOptions in Aspose.Cells for Python via Java.
keywords: Aspose.Cells, tabella pivot, raggruppare campo pivot, PivotField.group, PivotFieldGroupOptions, raggruppamento per data, raggruppamento per numero, mesi, trimestri, intervallo numerico, Python
type: docs
weight: 80
url: /it/python-java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari d'uso**
- Il raggruppamento dei campi pivot è utile quando un campo di riga o colonna di una tabella pivot contiene molti elementi distinti, come un campo data con centinaia di date o un campo numerico con molti valori sparsi. Il raggruppamento riunisce questi elementi in sezioni significative: le date in mesi, trimestri e anni, e i numeri in intervalli come 0-1, 2-3, 4-5. Ciò rende una tabella pivot di grandi dimensioni compatta e più facile da analizzare. Aspose.Cells offre questa funzionalità tramite il metodo `PivotField.group()` (raggruppamento automatico per tipo di dato) e `PivotField.group(PivotFieldGroupOptions)` (opzioni di raggruppamento personalizzate).
- Il raggruppamento per data innalza le singole date a periodi più ampi, come giorni, mesi, trimestri e anni, e costruisce una gerarchia temporale (ad esempio Anni, Trimestri, Mesi). Gli andamenti nel tempo diventano visibili a colpo d'occhio e ogni livello di periodo diventa un campo pivot a sé stante nell'area di riga o colonna della tabella pivot.
- Il raggruppamento è disponibile solo per i campi posizionati nell'area RIGA o COLONNA di una tabella pivot. Un campo dati (valore) non può essere raggruppato direttamente. Per raggruppare tale campo è necessario prima aggiungerlo all'area di riga o colonna della tabella pivot.

## **Raggruppare automaticamente i campi pivot**
L'overload senza parametri di `PivotField.group()` esamina il tipo di dato del campo e lo raggruppa automaticamente. Un campo che contiene solo date (e valori vuoti) viene raggruppato per mesi. Un campo che contiene solo numeri (e valori vuoti) viene raggruppato in intervalli numerici usando un intervallo automatico.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# Carica la cartella di lavoro di esempio
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Accedi al secondo foglio di lavoro e alla sua tabella pivot
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# Raggruppa automaticamente il primo campo riga.
# Il campo contiene date, quindi viene raggruppato per mesi.
field = pt.getRowFields().get(0)
field.group()
# Calcola i dati della tabella pivot e salva il file di output
pt.calculateData()
wb.save("outputAutoGroupPivotField.xlsx")
jpype.shutdownJVM()
```

## **Raggruppare i campi pivot con opzioni personalizzate**
La classe `PivotFieldGroupOptions` fornisce la configurazione di raggruppamento personalizzata. Per i campi data, imposta `StartDate`, `EndDate` e `GroupTypes`. Per i campi numerici, imposta `StartNumber`, `EndNumber` e `Interval`. La proprietà `NewPivotField` controlla se il raggruppamento crea nuovi campi pivot accanto all'originale (consulta la sezione Nota alla fine di questo articolo).

### **Raggruppare un campo data per mesi e trimestri**
L'esempio seguente raggruppa il campo data di riga della tabella pivot di esempio per mesi e trimestri tra una data di inizio e una data di fine. Il codice carica il [file Excel di esempio](sampleGroupPivotFieldsInPivotTable.xlsx), esegue il raggruppamento, calcola i dati della tabella pivot e salva il risultato raggruppato. Lo screenshot mostra l'effetto: il campo data di riga è ora raggruppato per trimestri e mesi.
Si noti che l'ordine dei valori in `options.GroupTypes` viene ignorato. Indipendentemente dall'ordine in cui sono elencati i tipi di gruppo, i campi raggruppati vengono sempre visualizzati dal periodo più ampio al più piccolo: anni, trimestri, mesi, giorni, ore, minuti, secondi. In questo esempio i mesi sono elencati prima dei trimestri in `options.GroupTypes`, eppure i trimestri vengono visualizzati come livello esterno e i mesi come livello interno.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldGroupOptions, PivotGroupByType, DateTime
# Carica il workbook di esempio
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Accedi al secondo foglio di lavoro e alla sua tabella pivot
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# Raggruppa il primo campo riga (un campo data) per mesi e trimestri
options = PivotFieldGroupOptions()
options.setStartDate(DateTime(2008, 1, 1))
options.setEndDate(DateTime(2008, 9, 5))
options.setGroupTypes([PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS])
pt.getRowFields().get(0).group(options)
# Calcola i dati della tabella pivot e salva il file di output
pt.calculateData()
wb.save("outputGroupPivotFieldsInPivotTable.xlsx")
jpype.shutdownJVM()
```

![Tabella pivot raggruppata per mesi e trimestri](group-pivot-fields-in-the-pivot-table_1.png)

### **Raggruppare un campo numerico in intervalli**
`FieldTwo` della tabella pivot di esempio è inizialmente un campo dati (valore). Poiché solo i campi di riga o colonna possono essere raggruppati, il codice prima chiama `pivotTable.addFieldToArea(PivotFieldType.ROW, "FieldTwo")` per spostare `FieldTwo` nell'area di riga, aggiorna la tabella pivot, quindi raggruppa il campo numerico negli intervalli 0-1, 2-3 e 4-5 usando `StartNumber = 0`, `EndNumber = 5` e `Interval = 2`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, PivotFieldGroupOptions
# Carica il workbook di esempio
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# Accedi al secondo foglio di lavoro e alla sua tabella pivot
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# FieldTwo è un campo dati: spostalo prima nell'area delle righe,
# perché solo i campi riga/colonna possono essere raggruppati
pt.addFieldToArea(PivotFieldType.ROW, "FieldTwo")
pt.calculateData()
# Raggruppa il campo numerico negli intervalli 0-1, 2-3, 4-5
options = PivotFieldGroupOptions()
options.setStartNumber(0)
options.setEndNumber(5)
options.setInterval(2)
pt.getRowFields().get(1).group(options)
# Calcola i dati della tabella pivot e salva il file di output
pt.calculateData()
wb.save("outputNumberGroupPivotField.xlsx")
jpype.shutdownJVM()
```

## **Nota**

{{% alert color="primary" %}}
- Gli overload del metodo `PivotField.groupBy()` sono deprecati e rimossi dalla superficie API. `PivotField.group()` e `PivotField.group(PivotFieldGroupOptions)` sono le sostituzioni.
- In Microsoft Excel, raggruppare un campo numerico SOSTITUISCE il campo pivot originale con gli intervalli raggruppati, mentre raggruppare un campo data crea NUOVI campi pivot (uno per livello di gruppo, ad esempio Trimestri e Mesi) accanto al campo originale. A partire da Aspose.Cells 26.10, i metodi `PivotField.group()` seguono lo stesso comportamento di Excel. La proprietà `PivotFieldGroupOptions.NewPivotField` esiste per la compatibilità con le versioni precedenti: per impostazione predefinita è false per il raggruppamento numerico e true per il raggruppamento data-ora; impostala su false se desideri che il raggruppamento per data sostituisca il campo pivot originale invece di creare nuovi campi pivot.
- La proprietà `PivotFieldGroupOptions.Interval` ha effetto solo per il raggruppamento numerico e per il raggruppamento di date per giorni (ad esempio, raggruppare le date in periodi di 7 giorni); viene ignorata quando le date sono raggruppate per mesi, trimestri o anni.
{{% /alert %}}

## **Articoli correlati**
- [Aggiungere campi di riga e colonna nella tabella pivot](/cells/it/python-java/pivot-table-add-row-and-column-fields/)
- [Filtrare le tabelle pivot per etichetta o valore](/cells/it/python-java/filter-by-label-or-value-of-pivot-table/)
- [Aggiungere un campo pagina nella tabella pivot](/cells/it/python-java/add-page-field-in-pivot-table/)
- [Applicare uno stile alla tabella pivot](/cells/it/python-java/apply-style-to-pivot-table/)
- [Aggiornare la tabella pivot](/cells/it/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}