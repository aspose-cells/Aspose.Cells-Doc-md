---
title: Inserisci tabella pivot
linktitle: Tabelle Pivot
type: docs
weight: 160
url: /it/python-net/create-pivot-table/
description: Creare e formattare Tabella Pivot con Aspose.Cells per Python via .NET.
keywords: Creare Tabella Pivot, Inserire Tabella Pivot, Formattare Tabella Pivot.
---

## **Creare tabella pivot**

È possibile utilizzare Aspose.Cells per Python via .NET per aggiungere tabelle pivot ai fogli di calcolo in modo programmatico.

### **Modello di oggetto di tabella pivot**

Aspose.Cells per Python via .NET fornisce un insieme speciale di classi nello spazio dei nomi [**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/) che vengono utilizzate per creare e controllare tabelle pivot. Queste classi vengono utilizzate per creare e impostare oggetti [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/), i mattoni di costruzione di una tabella pivot. Gli oggetti sono:

- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) rappresenta un campo in un [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection) rappresenta una raccolta di tutti gli oggetti [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield) in [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) rappresenta una tabella pivot su un foglio di lavoro.
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) rappresenta una raccolta di tutti gli oggetti [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) su un foglio di lavoro.

### **Creare una semplice tabella pivot utilizzando Aspose.Cells**

1. Aggiungi dati a un foglio di lavoro utilizzando il metodo [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) dell'oggetto [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).
   Questi dati verranno utilizzati come origine dati della tabella pivot.
1. Aggiungi una tabella pivot al foglio di lavoro chiamando il metodo [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str) della raccolta [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection), incapsulata nell'oggetto Foglio di lavoro.
1. Accedi al nuovo oggetto [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) dalla raccolta [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) passando l'indice di PivotTable.
1. Utilizza uno qualsiasi degli oggetti [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) (spiegati sopra) per gestire la tabella pivot.

Dopo aver eseguito il codice di esempio, viene aggiunta una tabella pivot al foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-CreatePivotTable-1.py" >}}

{{% alert color="primary" %}}

Quando si assegna un intervallo di celle come origine dati, l'intervallo deve andare dall'angolo in alto a sinistra a quello in basso a destra. Ad esempio, "A1:C3" è valido ma "C3:A1" non lo è.

{{% /alert %}}

## **Argomenti avanzati**
- [Funzione di consolidamento](/cells/it/python-net/consolidation-function/)
- [Ordinamento personalizzato in tabella pivot](/cells/it/python-net/custom-sorting-in-pivot-table/)
- [Personalizza le impostazioni di globalizzazione per la tabella pivot](/cells/it/python-net/customize-globalization-settings-for-pivot-table/)
- [Disabilita i riquadri delle tabelle pivot](/cells/it/python-net/disable-pivot-table-ribbons/)
- [Trova e aggiorna le tabelle pivot nidificate o figlie della tabella pivot principale](/cells/it/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [Formattazione tabella pivot](/cells/it/python-net/formatting-pivot-table/)
- [Ottieni la fonte di dati della connessione esterna della tabella pivot](/cells/it/python-net/get-external-connection-data-source-of-pivot-table/)
- [Ottieni la data di aggiornamento della tabella pivot e le informazioni sull'aggiornamento da chi](/cells/it/python-net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [Raggruppa i campi pivot nella tabella pivot](/cells/it/python-net/group-pivot-fields-in-the-pivot-table/)
- [Analisi dei record memorizzati nella cache della tabella pivot durante il caricamento del file Excel](/cells/it/python-net/parsing-pivot-cached-records-while-loading-excel-file/)
- [Tabella pivot e dati di origine](/cells/it/python-net/pivot-table-and-source-data/)
- [Nascondi e ordina i datidelle tabelle pivot](/cells/it/python-net/pivot-table-hide-and-sort-data/)
- [Aggiornare e calcolare la tabella pivot con elementi calcolati](/cells/it/python-net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Salva la tabella pivot in un file ODS](/cells/it/python-net/save-pivot-table-in-ods-file/)
- [Mostra l'opzione pagine filtro report](/cells/it/python-net/show-report-filter-pages-option/)
- [Lavorare con i formati di visualizzazione dei dati dei campi dati nella tabella pivot](/cells/it/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/)
{{< app/cells/assistant language="python-net" >}}
