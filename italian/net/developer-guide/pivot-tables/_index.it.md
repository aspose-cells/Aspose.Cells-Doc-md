---
title: Inserisci tabella pivot
linktitle: Tabelle pivot
type: docs
weight: 160
url: /it/net/create-pivot-table/
description: Crea e formatta tabelle pivot di file di fogli di calcolo Excel.
---
## **Crea tabella pivot**

È possibile utilizzare Aspose.Cells per aggiungere tabelle pivot ai fogli di calcolo in modo programmatico.

### **Modello a oggetti tabella pivot**

Aspose.Cells fornisce una serie speciale di classi nel[**Aspose.Cells.Pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot) spazio dei nomi utilizzato per creare e controllare le tabelle pivot. Queste classi vengono utilizzate per creare e impostare[**Tabella pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)oggetti, gli elementi costitutivi di una tabella pivot. Gli oggetti sono:

- [**Campo pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) rappresenta un campo in a[**Tabella pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) rappresenta una raccolta di tutte le[**Campo pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfield) oggetti nel[**Tabella pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable).
- [**Tabella pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)rappresenta una tabella pivot in un foglio di lavoro.
- [**Raccolta di tabelle pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) rappresenta una raccolta di tutte le[**Tabella pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)oggetti su un foglio di lavoro.

### **Creazione di una tabella pivot semplice utilizzando Aspose.Cells**

1. Aggiungere dati a un foglio di lavoro utilizzando il[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) dell'oggetto[**PutValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/putvalue/index) metodo.
 Questi dati verranno utilizzati come origine dati della tabella pivot.
1.  Aggiungi una tabella pivot al foglio di lavoro chiamando il metodo[**Tabelle pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection) della collezione[**Inserisci**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection/methods/add/index)metodo, che è incapsulato nell'oggetto Worksheet.
1.  Accedi al nuovo[**Tabella pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable) oggetto dal[**Tabelle pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottablecollection)raccolta passando l'indice della tabella pivot.
1.  Usa uno qualsiasi dei[**Tabella pivot**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable)oggetti (spiegati sopra) per gestire la tabella pivot.

Dopo aver eseguito il codice di esempio, al foglio di lavoro viene aggiunta una tabella pivot.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-CreatePivotTable-1.cs" >}}

{{% alert color="primary" %}}

Quando si assegna un intervallo di celle come origine dati, l'intervallo deve andare da in alto a sinistra a in basso a destra. Ad esempio, "A1:C3" è valido ma "C3:A1" no.

{{% /alert %}}

## **Argomenti avanzati**
- [Funzione di consolidamento](/cells/it/net/consolidation-function/)
- [Ordinamento personalizzato nella tabella pivot](/cells/it/net/custom-sorting-in-pivot-table/)
- [Personalizza le impostazioni di globalizzazione per la tabella pivot](/cells/it/net/customize-globalization-settings-for-pivot-table/)
- [Disattiva i nastri della tabella pivot](/cells/it/net/disable-pivot-table-ribbons/)
- [Trova e aggiorna le tabelle pivot nidificate o figlie della tabella pivot padre](/cells/it/net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [Formattazione della tabella pivot](/cells/it/net/formatting-pivot-table/)
- [Ottieni l'origine dati della connessione esterna della tabella pivot](/cells/it/net/get-external-connection-data-source-of-pivot-table/)
- [Ottieni la data di aggiornamento della tabella pivot e aggiorna le informazioni in base a chi](/cells/it/net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [Raggruppa i campi pivot nella tabella pivot](/cells/it/net/group-pivot-fields-in-the-pivot-table/)
- [Analisi dei record memorizzati nella cache pivot durante il caricamento del file Excel](/cells/it/net/parsing-pivot-cached-records-while-loading-excel-file/)
- [Tabella pivot e dati di origine](/cells/it/net/pivot-table-and-source-data/)
- [Tabella pivot Nascondi e ordina i dati](/cells/it/net/pivot-table-hide-and-sort-data/)
- [Aggiorna e calcola la tabella pivot con elementi calcolati](/cells/it/net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Salva la tabella pivot nel file ODS](/cells/it/net/save-pivot-table-in-ods-file/)
- [Opzione Mostra pagine filtro report](/cells/it/net/show-report-filter-pages-option/)
- [Utilizzo dei formati di visualizzazione dei dati di DataField nella tabella pivot](/cells/it/net/working-with-data-display-formats-of-datafield-in-pivot-table/)
