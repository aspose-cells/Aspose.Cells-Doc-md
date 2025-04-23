---
title: Inserisci tabella pivot
linktitle: Tabelle Pivot
type: docs
weight: 160
url: /it/net/create-pivot-table/
description: Creare e formattare tabelle pivot di file di fogli di calcolo di Excel.
---

## **Creare tabella pivot**

È possibile utilizzare Aspose.Cells per aggiungere tabelle pivot ai fogli di calcolo in modo programmato.

### **Modello di oggetto di tabella pivot**

Aspose.Cells fornisce un insieme speciale di classi nello spazio dei nomi [**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot) che vengono utilizzate per creare e controllare le tabelle pivot. Queste classi vengono utilizzate per creare e impostare gli oggetti [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable), i mattoni di costruzione di una tabella pivot. Gli oggetti sono:

- [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) rappresenta un campo in un [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) rappresenta una raccolta di tutti gli oggetti [**PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) in [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) rappresenta una tabella pivot su un foglio di lavoro.
- [**PivotTableCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) rappresenta una raccolta di tutti gli oggetti [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) su un foglio di lavoro.

### **Creare una semplice tabella pivot utilizzando Aspose.Cells**

1. Aggiungi dati a un foglio di lavoro utilizzando il metodo [**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) dell'oggetto [**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell).
   Questi dati verranno utilizzati come origine dati della tabella pivot.
1. Aggiungi una tabella pivot al foglio di lavoro chiamando il metodo [**add**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index) della raccolta [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection), incapsulata nell'oggetto Foglio di lavoro.
1. Accedi al nuovo oggetto [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) dalla raccolta [**PivotTables**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) passando l'indice di PivotTable.
1. Utilizza uno qualsiasi degli oggetti [**PivotTable**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) (spiegati sopra) per gestire la tabella pivot.

Dopo aver eseguito il codice di esempio, viene aggiunta una tabella pivot al foglio di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}

Quando si assegna un intervallo di celle come origine dati, l'intervallo deve andare dall'angolo in alto a sinistra a quello in basso a destra. Ad esempio, "A1:C3" è valido ma "C3:A1" non lo è.

{{% /alert %}}

## **Argomenti avanzati**
- [Funzione di consolidamento](/cells/it/net/consolidation-function/)
- [Ordinamento personalizzato in tabella pivot](/cells/it/net/custom-sorting-in-pivot-table/)
- [Personalizza le impostazioni di globalizzazione per la tabella pivot](/cells/it/net/customize-globalization-settings-for-pivot-table/)
- [Disabilita i riquadri delle tabelle pivot](/cells/it/net/disable-pivot-table-ribbons/)
- [Trova e aggiorna le tabelle pivot nidificate o figlie della tabella pivot principale](/cells/it/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [Formattazione tabella pivot](/cells/it/net/formatting-pivot-table/)
- [Ottieni la fonte di dati della connessione esterna della tabella pivot](/cells/it/net/get-external-connection-data-source-of-pivot-table/)
- [Ottieni la data di aggiornamento della tabella pivot e le informazioni sull'aggiornamento da chi](/cells/it/net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [Raggruppa i campi pivot nella tabella pivot](/cells/it/net/group-pivot-fields-in-the-pivot-table/)
- [Analisi dei record memorizzati nella cache della tabella pivot durante il caricamento del file Excel](/cells/it/net/parsing-pivot-cached-records-while-loading-excel-file/)
- [Tabella pivot e dati di origine](/cells/it/net/pivot-table-and-source-data/)
- [Nascondi e ordina i datidelle tabelle pivot](/cells/it/net/pivot-table-hide-and-sort-data/)
- [Aggiornare e calcolare la tabella pivot con elementi calcolati](/cells/it/net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Salva la tabella pivot in un file ODS](/cells/it/net/save-pivot-table-in-ods-file/)
- [Mostra l'opzione pagine filtro report](/cells/it/net/show-report-filter-pages-option/)
- [Lavorare con i formati di visualizzazione dei dati dei campi dati nella tabella pivot](/cells/it/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
