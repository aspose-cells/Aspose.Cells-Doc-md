---
title: Importazione intelligente e posizionamento dati con Smart Markers
linktitle: Marcatori intelligenti
type: docs
weight: 190
url: /it/net/using-smart-markers/
description: Importazione e posizionamento intelligenti dei dati secondo i file Excel di modello con la libreria Aspose.Cells.
---

## **Perché importare dati in Excel con Smart Markers**
L'uso di Smart Markers per importare dati in Excel semplifica l'integrazione dei dati combinando un design basato su template con il binding dinamico dei dati. Questo metodo è particolarmente valido in strumenti come Aspose.Cells, dove i marker agiscono come segnaposto nei template per popolarsi automaticamente con dati provenienti da fonti diverse. Di seguito i motivi principali per adottare questo metodo:

1. Efficienza nelle relazioni ripetitive: Riutilizzo del template, modelli Excel predefiniti con marker incorporati (ad esempio &=$VariableName, &=DataSource.Field) che possono essere riutilizzati su più dataset, eliminando la riformattazione manuale. Per esempio, rapporti finanziari o fogli di inventario richiedono solo l'aggiornamento della fonte dati, non la ricostruzione dei layout. Binding dati automatizzato, i Smart Markers si collegano direttamente a fonti dati (ad esempio database, JavaBeans, array). Le modifiche ai dati di origine si riflettono automaticamente sul file Excel generato, riducendo errori di copia/incolla.

2. Supporto per strutture dati complesse: Integrazione multi-source, un singolo template può unire dati da diverse fonti (ad esempio variabili, array, ResultSet). Gestione dei dati gerarchici, dati annidati (ad esempio record raggruppati) possono essere elaborati usando marker come &=subtotal9:Person.id per generare riepiloghi (sum, media) per ogni gruppo direttamente in Excel.

3. Preservazione delle funzionalità di Excel: i Smart Markers convivono con le funzioni di Excel come formule, formattazione condizionale e grafici. Per esempio: Calcoli dinamici usando &==C{r}*D{r} applicano formule specifiche per riga durante l'iniezione dei dati. I template mantengono stili predefiniti (ad esempio intestazioni, colori celle), garantendo coerenza senza aggiustamenti post-importazione.

4. Capacità avanzate di automazione: Integrazione con sorgenti dati personalizzate, gli sviluppatori possono implementare interfacce come ICellsDataTable (in .NET) per mappare strutture dati proprietarie ai marker. Questo supporta dati in tempo reale provenienti da API o sensori. Elaborazione batch, strumenti come Aspose.Cells’ WorkbookDesigner consentono operazioni di massa (ad esempio generare oltre 1000 fatture in un'unica esecuzione) ciclando sui dataset.

5. Riduzione di sforzo di sviluppo e manutenzione: Separazione di logica e design, i designer gestiscono i template in Excel (nessun codice), mentre gli sviluppatori gestiscono la logica dei dati. Questo accelera le iterazioni. Riduzione degli errori, la mappatura automatica dei dati minimizza i rischi di inserimenti manuali. Per esempio, i dati di sensori analizzati in VC++ possono essere compilati automaticamente nei template Excel tramite interfacce di oggetto, evitando errori di trascrizione.

## **Codice esempio per l'importazione di DataTable con Smart Markers**
Il seguente esempio di codice ha una sorgente di dati con 6 record. Vogliamo mostrare solo 3 record in un foglio di lavoro, poi gli altri record si sposteranno automaticamente sul secondo foglio di lavoro. Nota che anche il secondo foglio deve avere lo stesso tag di marker intelligente e devi chiamare il metodo [WorkbookDesigner.Process(sheetIndex, isPreserved)](https://reference.aspose.com/cells/net/aspose.cells.workbookdesigner/process/methods/2) per entrambi i fogli. Consulta il [file Excel di output](SmartMarkerDataTableToExcel.xlsx) generato dal codice come riferimento.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-ImportDataTableToExcel.cs" >}}

## **Codice di esempio per l'importazione di dati JSON con Smart Markers**
Aspose.Cells for .NET supporta dati JSON nei smart markers. Il codice di esempio carica un modello di tabella, importa intelligentemente i dati JSON per il riempimento e calcola poi i dati della tabella. Per favore controlla [file modello](table.xlsx), [file JSON](table.json) e lo screenshot del file Excel generato con il seguente codice.

|**Il primo foglio del file table.xlsx mostra gli smart markers.**|
| :- |
|![todo:image_alt_text](tabletemplate.png)|

|**Lo screenshot del file Excel di output.**|
| :- |
|![todo:image_alt_text](tableresult.png)|

Dati json come segue:
```json data
{
	"Items" : [
		{
			"ItemName" : "A123",
			"Description" : "Peonies",
			"Qty" : "55",
			"UnitPrice" : "3.05"			
		},
		{
			"ItemName" : "B456",
			"Description" : "Tulips",
			"Qty" : "45",
			"UnitPrice" : "2.66",
		},
		{
			"ItemName" : "K789",
			"Description" : "Buttercup",
			"Qty" : "68",
			"UnitPrice" : "8.35",
		}
	]
}
```
L'esempio seguente mostra come funziona.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "SmartMarkers-ImportJsonToTable.cs" >}}

## **Codice di esempio per l'importazione di oggetti annidati con Smart Markers**
Aspose.Cells supporta oggetti annidati in smart markers, gli oggetti annidati devono essere semplici. Utilizziamo un file di modello semplice. Vedi il foglio di calcolo del designer che contiene alcuni smart markers annidati.

|**Il primo foglio di calcolo del file SM_NestedObjects.xlsx mostra smart markers annidati.**|
| :- |
|![todo:image_alt_text](using-smart-markers_7.png)|
L'esempio seguente mostra come funziona.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-SmartMarkers-UsingNestedObjects-1.cs" >}}


## **Argomenti avanzati**
- [Parametri di Smart Marker](/cells/it/net/smart-marker-parameters/)
- [Aggiunta di Oggetti Anonimi o Personalizzati in SmartMarkers](/cells/it/net/adding-anonymous-or-custom-object-into-smartmarkers/)
- [Auto Popolare i Dati di Smart Marker in Altri Fogli di Lavoro se i Dati sono Troppo Numerosi](/cells/it/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [Formattazione Smart Markers](/cells/it/net/formatting-smart-markers/)
- [Ottenere Notifiche durante la Fusione dei Dati con Smart Markers](/cells/it/net/getting-notifications-while-merging-data-with-smart-markers/)
- [Imposta origine dati personalizzata per WorkbookDesigner](/cells/it/net/set-custom-datasource-for-workbookdesigner/)
- [Mostra apostrofo iniziale nelle celle](/cells/it/net/show-leading-apostrophe-in-cells/)
- [Utilizzo del parametro Formula nel campo di Smart Marker](/cells/it/net/using-formula-parameter-in-smart-marker-field/)
- [Importazione intelligente di elementi di array per indice in Excel con Smart Markers](/cells/it/net/how-to-import-array-element-by-index-with-smart-markers/)
- [Importazione intelligente di elementi di array tramite slicer in Excel con Smart Markers](/cells/it/net/how-to-import-array-element-by-slicer-with-smart-markers/)
- [Importazione intelligente di JSON in Excel con Smart Markers](/cells/it/net/how-to-import-json-into-excel-with-smart-markers/)
- [Importazione intelligente di oggetti annidati in Excel con Smart Markers](/cells/it/net/how-to-import-nested-objects-with-smart-markers/)
- [Importazione intelligente di array variabili in Excel con Smart Markers](/cells/it/net/how-to-import-variable-arrays-with-smart-markers/)
- [Come usare i Marker Immagine nei Smart Markers](/cells/it/net/how-to-use-image-markers-in-smart-markers/)
- [Come raggruppare i dati nei Smart Markers](/cells/it/net/how-to-group-data-in-smart-markers/)

{{< app/cells/assistant language="csharp" >}}
