---
title: Raggruppare i campi pivot nella tabella pivot
linktitle: Raggruppare i campi pivot nella tabella pivot
description: Scopri come raggruppare i campi pivot di righe e colonne in una tabella pivot in periodi di date come mesi e trimestri e in intervalli numerici utilizzando PivotField.group e PivotFieldGroupOptions in Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, tabella pivot, raggruppare campo pivot, PivotField.group, PivotFieldGroupOptions, raggruppamento date, raggruppamento numeri, mesi, trimestri, intervallo numerico, Node.js
type: docs
weight: 80
url: /it/nodejs-java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Scenari di utilizzo possibili**
- Il raggruppamento dei campi pivot è utile quando un campo di riga o di colonna di una tabella pivot contiene molti elementi distinti, ad esempio un campo data con centinaia di date o un campo numerico con molti valori sparsi. Il raggruppamento comprime questi elementi in sezioni significative: le date in mesi, trimestri e anni, e i numeri in intervalli come 0-1, 2-3, 4-5. Questo rende una tabella pivot di grandi dimensioni compatta e più facile da analizzare. Aspose.Cells for Node.js via Java offre questa funzionalità tramite il metodo `PivotField.group()` (raggruppamento automatico per tipo di dato) e `PivotField.group(PivotFieldGroupOptions)` (opzioni di raggruppamento personalizzate).
- Il raggruppamento delle date arrotola le singole date in periodi più ampi, come giorni, mesi, trimestri e anni, e costruisce una gerarchia temporale (ad esempio Anni, Trimestri, Mesi). Gli andamenti nel tempo diventano visibili a colpo d'occhio, e ogni livello di periodo diventa un campo pivot a sé stante nell'area delle righe o delle colonne della tabella pivot.
- Il raggruppamento è disponibile solo per i campi posizionati nell'area RIGHE o COLONNE di una tabella pivot. Un campo dati (valore) non può essere raggruppato direttamente. Per raggruppare un campo di questo tipo è necessario prima aggiungerlo all'area delle righe o delle colonne della tabella pivot.

## **Raggruppare automaticamente i campi pivot**
L'overload senza parametri `PivotField.group()` esamina il tipo di dato del campo e lo raggruppa automaticamente. Un campo che contiene solo date (e valori vuoti) viene raggruppato per mesi. Un campo che contiene solo numeri (e valori vuoti) viene raggruppato in intervalli numerici utilizzando un intervallo automatico.

```javascript
const AsposeCells = require("aspose.cells");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Accedi al secondo foglio di lavoro e alla sua tabella pivot
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// Raggruppa automaticamente il primo campo riga.
// Il campo contiene date, quindi è raggruppato per mesi.
let field = pt.getRowFields().get(0);
field.group();
// Calcola i dati della tabella pivot e salva il file di output
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **Raggruppare i campi pivot con opzioni personalizzate**
La classe `PivotFieldGroupOptions` fornisce una configurazione di raggruppamento personalizzata. Per i campi data, impostare `StartDate`, `EndDate` e `GroupTypes`. Per i campi numerici, impostare `StartNumber`, `EndNumber` e `Interval`. La proprietà `NewPivotField` controlla se il raggruppamento crea nuovi campi pivot accanto a quello originale (vedere la sezione Nota alla fine di questo articolo).

### **Raggruppare un campo data per mesi e trimestri**
L'esempio seguente raggruppa il campo data di riga della tabella pivot di esempio per mesi e trimestri tra una data di inizio e una data di fine. Il codice carica il [file Excel di esempio](sampleGroupPivotFieldsInPivotTable.xlsx), esegue il raggruppamento, calcola i dati della tabella pivot e salva il risultato raggruppato. Lo screenshot mostra l'effetto: il campo data di riga è ora raggruppato per trimestri e mesi.
Si noti che l'ordine dei valori in `options.GroupTypes` viene ignorato. Indipendentemente dall'ordine in cui sono elencati i tipi di gruppo, i campi raggruppati vengono sempre visualizzati dal periodo più ampio al più piccolo: anni, trimestri, mesi, giorni, ore, minuti, secondi. In questo esempio i mesi sono elencati prima dei trimestri in `options.GroupTypes`, eppure i trimestri vengono visualizzati come livello esterno e i mesi come livello interno.

```javascript
const AsposeCells = require("aspose.cells");
// Carica la cartella di lavoro di esempio
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Accedi al secondo foglio di lavoro e alla sua tabella pivot
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// Raggruppa il primo campo riga (un campo data) per mesi e trimestri
const options = new AsposeCells.PivotFieldGroupOptions();
options.setStartDate(new Date(2008, 0, 1));
options.setEndDate(new Date(2008, 8, 5));
options.setGroupTypes([AsposeCells.PivotGroupByType.MONTHS, AsposeCells.PivotGroupByType.QUARTERS]);
pt.getRowFields().get(0).group(options);
// Calcola i dati della tabella pivot e salva il file di output
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![Tabella pivot raggruppata per mesi e trimestri](group-pivot-fields-in-the-pivot-table_1.png)

### **Raggruppare un campo numerico in intervalli**
`FieldTwo` della tabella pivot di esempio è inizialmente un campo dati (valore). Poiché possono essere raggruppati solo i campi di riga o di colonna, il codice chiama prima `pivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")` per spostare `FieldTwo` nell'area delle righe, aggiorna la pivot, quindi raggruppa il campo numerico negli intervalli 0-1, 2-3 e 4-5 utilizzando `StartNumber = 0`, `EndNumber = 5` e `Interval = 2`.

```javascript
const AsposeCells = require("aspose.cells");
// Carica il workbook di esempio
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Accedi al secondo foglio di lavoro e alla sua tabella pivot
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo è un campo dati: spostalo prima nell'area delle righe,
// perché solo i campi riga/colonna possono essere raggruppati
pt.addFieldToArea(AsposeCells.PivotFieldType.ROW, "FieldTwo");
pt.calculateData();
// Raggruppa il campo numerico negli intervalli 0-1, 2-3, 4-5
const options = new AsposeCells.PivotFieldGroupOptions();
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
- Gli overload del metodo `PivotField.GroupBy()` sono deprecati e sono stati rimossi dalla superficie API. I sostituti sono `PivotField.group()` e `PivotField.group(PivotFieldGroupOptions)`.
- In Microsoft Excel, il raggruppamento di un campo numerico SOSTITUISCE il campo pivot originale con gli intervalli raggruppati, mentre il raggruppamento di un campo data crea NUOVI campi pivot (uno per ciascun livello di gruppo, ad esempio Trimestri e Mesi) accanto al campo originale. A partire da Aspose.Cells for Node.js via Java 26.10, i metodi `PivotField.group()` seguono lo stesso comportamento di Excel. La proprietà `PivotFieldGroupOptions.NewPivotField` esiste per la compatibilità con le versioni precedenti: per impostazione predefinita è false per il raggruppamento numerico e true per il raggruppamento di data-ora; impostarla su false se si desidera che il raggruppamento delle date sostituisca il campo pivot originale invece di creare nuovi campi pivot.
- La proprietà `PivotFieldGroupOptions.Interval` ha effetto solo per il raggruppamento numerico e per il raggruppamento delle date per giorni (ad esempio, raggruppamento delle date in periodi di 7 giorni); viene ignorata quando le date vengono raggruppate per mesi, trimestri o anni.
{{% /alert %}}

## **Articoli correlati**
- [Aggiungere campi riga e colonna nella tabella pivot](/cells/it/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Filtrare le tabelle pivot per etichetta o valore](/cells/it/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Aggiungere un campo pagina nella tabella pivot](/cells/it/nodejs-java/add-page-field-in-pivot-table/)
- [Applicare uno stile alla tabella pivot](/cells/it/nodejs-java/apply-style-to-pivot-table/)
- [Aggiornare la tabella pivot](/cells/it/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}