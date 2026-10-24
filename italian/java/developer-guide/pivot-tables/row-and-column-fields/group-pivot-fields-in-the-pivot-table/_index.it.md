---
title: Raggruppa i campi pivot nella tabella pivot
linktitle: Raggruppa i campi pivot nella tabella pivot
description: Scopri come raggruppare i campi pivot di riga e colonna in una tabella pivot in periodi di date come mesi e trimestri e in intervalli numerici tramite PivotField.group e PivotFieldGroupOptions in Aspose.Cells for Java.
keywords: Aspose.Cells, tabella pivot, raggruppare campo pivot, PivotField.group, PivotFieldGroupOptions, raggruppamento per date, raggruppamento numerico, mesi, trimestri, intervallo numerico, Java
type: docs
weight: 80
url: /it/java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari d'uso**
- Raggruppare i campi pivot è utile quando un campo di riga o colonna di una tabella pivot contiene molti elementi distinti, ad esempio un campo data con centinaia di date o un campo numerico con molti valori sparsi. Il raggruppamento comprime questi elementi in sezioni significative: le date in mesi, trimestri e anni, e i numeri in intervalli come 0-1, 2-3, 4-5. In questo modo una tabella pivot di grandi dimensioni diventa compatta e più facile da analizzare. Aspose.Cells fornisce questa funzionalità tramite il metodo `PivotField.group()` (raggruppamento automatico per tipo di dati) e `PivotField.group(PivotFieldGroupOptions)` (opzioni di raggruppamento personalizzate).
- Il raggruppamento per date innalza le singole date a periodi più ampi, come giorni, mesi, trimestri e anni, e costruisce una gerarchia temporale (ad esempio Anni, Trimestri, Mesi). Gli andamenti nel tempo diventano visibili a colpo d'occhio e ogni livello di periodo diventa un campo pivot a sé stante nell'area di riga o colonna della tabella pivot.
- Il raggruppamento è disponibile solo per i campi posizionati nell'area ROW o COLUMN di una tabella pivot. Un campo dati (valore) non può essere raggruppato direttamente. Per raggruppare tale campo è necessario prima aggiungerlo all'area di riga o colonna della tabella pivot.

## **Raggruppa automaticamente i campi pivot**
L'overload di `PivotField.group()` senza parametri esamina il tipo di dati del campo e lo raggruppa automaticamente. Un campo che contiene solo date (e valori vuoti) viene raggruppato per mesi. Un campo che contiene solo numeri (e valori vuoti) viene raggruppato in intervalli numerici utilizzando un passo automatico.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
PivotField field = pt.getRowFields().get(0);
field.group();
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **Raggruppa i campi pivot con opzioni personalizzate**
La classe `PivotFieldGroupOptions` fornisce la configurazione di raggruppamento personalizzata. Per i campi data, imposta `startDate`, `endDate` e `groupTypes`. Per i campi numerici, imposta `startNumber`, `endNumber` e `interval`. La proprietà `newPivotField` controlla se il raggruppamento crea nuovi campi pivot accanto all'originale (consulta la sezione Nota alla fine di questo articolo).

### **Raggruppa un campo data per mesi e trimestri**
Il seguente esempio raggruppa il campo data di riga della tabella pivot di esempio per mesi e trimestri tra una data di inizio e una data di fine. Il codice carica il [file Excel di esempio](sampleGroupPivotFieldsInPivotTable.xlsx), esegue il raggruppamento, calcola i dati della tabella pivot e salva il risultato raggruppato. Lo screenshot mostra l'effetto: il campo data di riga è ora raggruppato per trimestri e mesi.
Nota che l'ordine dei valori in `options.groupTypes` viene ignorato. Indipendentemente dall'ordine in cui sono elencati i tipi di raggruppamento, i campi raggruppati vengono sempre visualizzati dal periodo più ampio al più piccolo: anni, trimestri, mesi, giorni, ore, minuti, secondi. In questo esempio i mesi sono elencati prima dei trimestri in `options.groupTypes`, eppure i trimestri vengono visualizzati come livello esterno e i mesi come livello interno.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.setStartDate(new com.aspose.cells.DateTime(2008, 1, 1));
options.setEndDate(new com.aspose.cells.DateTime(2008, 9, 5));
options.setGroupTypes(new int[] { PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS });
pt.getRowFields().get(0).group(options);
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![Tabella pivot raggruppata per mesi e trimestri](group-pivot-fields-in-the-pivot-table_1.png)

### **Raggruppa un campo numerico in intervalli**
`FieldTwo` della tabella pivot di esempio è inizialmente un campo dati (valore). Poiché solo i campi di riga o colonna possono essere raggruppati, il codice prima chiama `PivotTable.addFieldToArea(PivotFieldType.ROW, "FieldTwo")` per spostare `FieldTwo` nell'area di riga, aggiorna la pivot, quindi raggruppa il campo numerico negli intervalli 0-1, 2-3 e 4-5 usando `startNumber = 0`, `endNumber = 5` e `interval = 2`.

```java
import com.aspose.cells.*;
// Carica il workbook di esempio
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// Accedi al secondo foglio di lavoro e alla sua tabella pivot
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo è un campo dati: spostalo prima nell'area delle righe,
// perché solo i campi riga/colonna possono essere raggruppati
pt.addFieldToArea(PivotFieldType.ROW, "FieldTwo");
pt.calculateData();
// Raggruppa il campo numerico negli intervalli 0-1, 2-3, 4-5
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
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
- Gli overload del metodo `PivotField.groupBy()` sono deprecati e rimossi dalla superficie API. `PivotField.group()` e `PivotField.group(PivotFieldGroupOptions)` sono i sostituti.
- In Microsoft Excel, raggruppare un campo numerico SOSTITUISCE il campo pivot originale con gli intervalli raggruppati, mentre raggruppare un campo data crea NUOVI campi pivot (uno per livello di raggruppamento, ad esempio Trimestri e Mesi) accanto al campo originale. A partire da Aspose.Cells 26.10, i metodi `PivotField.group()` seguono lo stesso comportamento di Excel. La proprietà `PivotFieldGroupOptions.newPivotField` esiste per compatibilità con le versioni precedenti: per impostazione predefinita è false per il raggruppamento numerico e true per il raggruppamento data-ora; impostala su false se desideri che il raggruppamento per date sostituisca il campo pivot originale invece di creare nuovi campi pivot.
- La proprietà `PivotFieldGroupOptions.interval` ha effetto solo per il raggruppamento numerico e per il raggruppamento di date per giorni (ad esempio, raggruppare le date in periodi di 7 giorni); viene ignorata quando le date sono raggruppate per mesi, trimestri o anni.
{{% /alert %}}

## **Articoli correlati**
- [Aggiungere campi di riga e colonna nella tabella pivot](/cells/it/java/pivot-table-add-row-and-column-fields/)
- [Filtrare le tabelle pivot per etichetta o valore](/cells/it/java/filter-by-label-or-value-of-pivot-table/)
- [Aggiungere un campo pagina nella tabella pivot](/cells/it/java/add-page-field-in-pivot-table/)
- [Applicare uno stile alla tabella pivot](/cells/it/java/apply-style-to-pivot-table/)
- [Aggiornare la tabella pivot](/cells/it/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}