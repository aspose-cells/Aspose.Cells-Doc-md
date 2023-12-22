---
title: Inserisci tabella pivot
linktitle: Tabelle pivot
type: docs
weight: 160
url: /it/python-net/create-pivot-table/
description: Crea e formatta la tabella pivot con Aspose.Cells for Python via .NET.
keywords: Create Pivot Table, Insert Pivot Table, Format Pivot Table.
---
##  **Crea tabella pivot**

È possibile utilizzare Aspose.Cells for Python via .NET per aggiungere tabelle pivot ai fogli di calcolo a livello di codice.

###  **Modello a oggetti della tabella pivot**

 Aspose.Cells for Python via .NET fornisce una serie speciale di classi nella[**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/) spazio dei nomi utilizzato per creare e controllare le tabelle pivot. Queste classi vengono utilizzate per creare e impostare[**Tabella pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/)oggetti, gli elementi costitutivi di una tabella pivot. Gli oggetti sono:

- [**Campo pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) rappresenta un campo in a[**Tabella pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**Collezione PivotField**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfieldcollection) rappresenta una raccolta di tutti i[**Campo pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield) oggetti in[**Tabella pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**Tabella pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)rappresenta una tabella pivot in un foglio di lavoro.
- [**Raccolta tabelle pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) rappresenta una raccolta di tutti i[**Tabella pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)oggetti su un foglio di lavoro.

###  **Creazione di una tabella pivot semplice utilizzando Aspose.Cells**

1.  Aggiungi dati a un foglio di lavoro utilizzando il file[**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell) dell'oggetto[**put_valore**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) metodo.
 Questi dati verranno utilizzati come origine dati della tabella pivot.
1.  Aggiungi una tabella pivot al foglio di lavoro chiamando il metodo[**Tabelle pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) collezione[**aggiungere**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str)metodo, che è incapsulato nell'oggetto Worksheet.
1.  Accedi al nuovo[**Tabella pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) oggetto da[**Tabelle pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection)raccolta passando l'indice della tabella pivot.
1.  Utilizzare uno qualsiasi dei[**Tabella pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable)oggetti (spiegati sopra) per gestire la tabella pivot.

Dopo aver eseguito il codice di esempio, una tabella pivot viene aggiunta al foglio di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-CreatePivotTable-1.py" >}}

{{% alert color="primary" %}}

Quando si assegna un intervallo di celle come origine dati, l'intervallo deve andare dall'alto a sinistra all'angolo in basso a destra. Ad esempio, "A1:C3" è valido ma "C3:A1" no.

{{% /alert %}}

##  **Argomenti avanzati**
- [Funzione di consolidamento](/cells/it/python-net/consolidation-function/)
- [Ordinamento personalizzato nella tabella pivot](/cells/it/python-net/custom-sorting-in-pivot-table/)
- [Personalizza le impostazioni di globalizzazione per la tabella pivot](/cells/it/python-net/customize-globalization-settings-for-pivot-table/)
- [Disabilita i nastri della tabella pivot](/cells/it/python-net/disable-pivot-table-ribbons/)
- [Trova e aggiorna le tabelle pivot nidificate o figlie della tabella pivot padre](/cells/it/python-net/find-and-refresh-the-nested-or-children-pivot-tables-of-parent-pivot-table/)
- [Formattazione della tabella pivot](/cells/it/python-net/formatting-pivot-table/)
- [Ottieni l'origine dati della connessione esterna della tabella pivot](/cells/it/python-net/get-external-connection-data-source-of-pivot-table/)
- [Ottieni la data di aggiornamento della tabella pivot e aggiorna le informazioni in base a chi](/cells/it/python-net/get-pivot-table-refresh-date-and-refresh-by-who-information/)
- [Raggruppare i campi pivot nella tabella pivot](/cells/it/python-net/group-pivot-fields-in-the-pivot-table/)
- [Analisi dei record memorizzati nella cache del pivot durante il caricamento del file Excel](/cells/it/python-net/parsing-pivot-cached-records-while-loading-excel-file/)
- [Tabella pivot e dati di origine](/cells/it/python-net/pivot-table-and-source-data/)
- [Tabella pivot Nascondi e ordina i dati](/cells/it/python-net/pivot-table-hide-and-sort-data/)
- [Aggiorna e calcola la tabella pivot con gli elementi calcolati](/cells/it/python-net/refresh-and-calculate-pivot-table-having-calculated-items/)
- [Salva la tabella pivot nel file ODS](/cells/it/python-net/save-pivot-table-in-ods-file/)
- [Mostra l'opzione delle pagine di filtro del report](/cells/it/python-net/show-report-filter-pages-option/)
- [Lavorare con i formati di visualizzazione dei dati di DataField nella tabella pivot](/cells/it/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/)
