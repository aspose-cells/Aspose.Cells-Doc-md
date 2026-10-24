---
title: Raggruppa i campi pivot nella tabella pivot
linktitle: Raggruppa i campi pivot nella tabella pivot
description: Scopri come raggruppare i campi pivot di righe e colonne in una tabella pivot in periodi di date come mesi e trimestri e in intervalli numerici usando PivotField.Group e PivotFieldGroupOptions in Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells, tabella pivot, raggruppa campo pivot, PivotField.Group, PivotFieldGroupOptions, raggruppamento date, raggruppamento numeri, mesi, trimestri, intervallo numerico, JavaScript
type: docs
weight: 80
url: /it/nodejs-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
- Raggruppare i campi pivot è utile quando un campo di riga o colonna di una tabella pivot contiene molti elementi distinti, ad esempio un campo data con centinaia di date o un campo numerico con molti valori sparsi. Il raggruppamento comprime questi elementi in sezioni significative: le date in mesi, trimestri e anni, e i numeri in intervalli come 0-1, 2-3, 4-5. Questo rende una tabella pivot di grandi dimensioni compatta e più facile da analizzare. Aspose.Cells fornisce questa funzionalità tramite il metodo `pivotField.group()` (raggruppamento automatico per tipo di dato) e `pivotField.group(PivotFieldGroupOptions)` (opzioni di raggruppamento personalizzate).
- Il raggruppamento delle date aggrega le singole date in periodi più ampi, come giorni, mesi, trimestri e anni, e crea una gerarchia temporale (ad esempio Anni, Trimestri, Mesi). Le tendenze nel tempo diventano visibili a colpo d'occhio e ogni livello di periodo diventa un campo pivot a sé stante nell'area righe o colonne della tabella pivot.
- Il raggruppamento è disponibile solo per i campi posizionati nell'area RIGHE o COLONNE di una tabella pivot. Un campo dati (valore) non può essere raggruppato direttamente. Per raggruppare tale campo è necessario prima aggiungerlo all'area righe o colonne della tabella pivot.

## **Raggruppa i campi pivot automaticamente**
L'overload senza parametri `pivotField.group()` esamina il tipo di dato del campo e lo raggruppa automaticamente. Un campo che contiene solo date (e vuoti) viene raggruppato per mesi. Un campo che contiene solo numeri (e vuoti) viene raggruppato in intervalli numerici usando un intervallo automatico.

```javascript
const AsposeCells = require("aspose.cells.node");
// Carica la cartella di lavoro di esempio
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Accedi al secondo foglio di lavoro e alla sua tabella pivot
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// Raggruppa automaticamente il primo campo riga.
// Il campo contiene date, quindi viene raggruppato per mesi.
const field = pt.getRowFields().get(0);
field.group();
// Calcola i dati della tabella pivot e salva il file di output
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **Raggruppa i campi pivot con opzioni personalizzate**
La classe `PivotFieldGroupOptions` fornisce la configurazione di raggruppamento personalizzata. Per i campi data, imposta `startDate`, `endDate` e `groupTypes`. Per i campi numerici, imposta `startNumber`, `endNumber` e `interval`. La proprietà `newPivotField` controlla se il raggruppamento crea nuovi campi pivot accanto all'originale (consulta la sezione Nota alla fine di questo articolo).

### **Raggruppa un campo data per mesi e trimestri**
L'esempio seguente raggruppa il campo data delle righe della tabella pivot di esempio per mesi e trimestri tra una data di inizio e una data di fine. Il codice carica il [file Excel di esempio](sampleGroupPivotFieldsInPivotTable.xlsx), esegue il raggruppamento, calcola i dati della tabella pivot e salva il risultato raggruppato. Lo screenshot mostra l'effetto: il campo data delle righe è ora raggruppato per trimestri e mesi.
Nota che l'ordine dei valori in `options.groupTypes` viene ignorato. Indipendentemente dall'ordine in cui sono elencati i tipi di gruppo, i campi raggruppati vengono sempre visualizzati dal periodo più grande al più piccolo: anni, trimestri, mesi, giorni, ore, minuti, secondi. In questo esempio i mesi sono elencati prima dei trimestri in `options.groupTypes`, eppure i trimestri vengono visualizzati come livello esterno e i mesi come livello interno.

```javascript
const AsposeCells = require("aspose.cells.node");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Accedi al secondo foglio di lavoro e alla sua tabella pivot
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// Raggruppa il primo campo riga (un campo data) per mesi e trimestri
let options = new AsposeCells.PivotFieldGroupOptions();
options.setStartDate(new Date(2008, 0, 1));
options.setEndDate(new Date(2008, 8, 5));
options.setGroupTypes([AsposeCells.PivotGroupByType.Months, AsposeCells.PivotGroupByType.Quarters]);
pt.getRowFields().get(0).group(options);
// Calcola i dati della tabella pivot e salva il file di output
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![Tabella pivot raggruppata per mesi e trimestri](group-pivot-fields-in-the-pivot-table_1.png)

### **Raggruppa un campo numerico in intervalli**
`FieldTwo` della tabella pivot di esempio è inizialmente un campo dati (valore). Poiché solo i campi di riga o colonna possono essere raggruppati, il codice prima chiama `pivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")` per spostare `FieldTwo` nell'area righe, aggiorna la tabella pivot, quindi raggruppa il campo numerico negli intervalli 0-1, 2-3 e 4-5 usando `startNumber = 0`, `endNumber = 5` e `interval = 2`.

```javascript
const AsposeCells = require("aspose.cells.node");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Accedi al secondo foglio di lavoro e alla sua tabella pivot
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo è un campo dati: spostalo prima nell'area delle righe,
// perché solo i campi riga/colonna possono essere raggruppati
pt.addFieldToArea(AsposeCells.PivotFieldType.Row, "FieldTwo");
pt.calculateData();
// Raggruppa il campo numerico negli intervalli 0-1, 2-3, 4-5
let options = new AsposeCells.PivotFieldGroupOptions();
options.setStartNumber(0);
options.setEndNumber(5);
options.setInterval(2);
pt.getRowFields().get(1).group(options);
// Calcola i dati della tabella pivot e salva il file di output
pt.calculateData();
wb.save("outputNumberGroupPivotField.xlsx");
```

## **Nota**

{{% alert color="primary" %}}
- Gli overload del metodo `pivotField.groupBy()` sono deprecati e rimossi dalla superficie API. `pivotField.group()` e `pivotField.group(PivotFieldGroupOptions)` sono le sostituzioni.
- In Microsoft Excel, raggruppare un campo numerico SOSTITUISCE il campo pivot originale con gli intervalli raggruppati, mentre raggruppare un campo data crea NUOVI campi pivot (uno per livello di gruppo, ad esempio Trimestri e Mesi) accanto al campo originale. A partire da Aspose.Cells 26.10, i metodi `pivotField.group()` seguono lo stesso comportamento di Excel. La proprietà `pivotFieldGroupOptions.newPivotField` esiste per la compatibilità con le versioni precedenti: per impostazione predefinita è false per il raggruppamento numerico e true per il raggruppamento data-ora; impostala su false se vuoi che il raggruppamento per data sostituisca il campo pivot originale invece di creare nuovi campi pivot.
- La proprietà `pivotFieldGroupOptions.interval` ha effetto solo per il raggruppamento numerico e per il raggruppamento di date per giorni (ad esempio, raggruppare le date in periodi di 7 giorni); viene ignorata quando le date sono raggruppate per mesi, trimestri o anni.
{{% /alert %}}

## **Articoli correlati**
- [Aggiungi campi riga e colonna nella tabella pivot](/cells/it/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Filtra le tabelle pivot per etichetta o valore](/cells/it/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [Aggiungi campo pagina nella tabella pivot](/cells/it/nodejs-cpp/add-page-field-in-pivot-table/)
- [Applica stile alla tabella pivot](/cells/it/nodejs-cpp/apply-style-to-pivot-table/)
- [Aggiorna tabella pivot](/cells/it/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}