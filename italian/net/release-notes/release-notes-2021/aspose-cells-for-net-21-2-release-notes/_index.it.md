---
title: Aspose.Cells for .NET 21.2 Note di rilascio
type: docs
weight: 29
url: /it/net/aspose-cells-for-net-21-2-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 21.2](https://www.nuget.org/packages/Aspose.Cells/21.2.0).

{{% /alert %}}

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSNET-42427|Supporta la percentuale del formato di visualizzazione della colonna per la tabella pivot|Nuova caratteristica|
|CELLSNET-44288|Utilizzo di LightCells API con file XLSB|Nuova caratteristica|
|CELLSNET-47817|Aggiorna l'origine dati quando modifichi il grafico a cascata in Istogramma.|Aumento|
|CELLSNETCORE-99|Supporta l'aggiornamento dell'icona di visualizzazione per oggetti jpg, zip, msg incorporati.|Aumento|
|CELLSNET-47827|Aspetta CalcolaFormula|Prestazione|
|CELLSNET-47832|Cells.DeleteBlankRows non finisce mai (ciclo infinito) su un particolare foglio di lavoro|Prestazione|
|CELLSNETCORE-98|Caricamento dei risultati xlsb con l'eccezione OOM|Prestazione|
|CELLSNET-47805|Posizione errata di alcune polilinee durante il salvataggio di file .html.|Insetto|
|CELLSNET-47810|La posizione della freccia è sbagliata|Insetto|
|CELLSNET-43717|L'ordinamento dei campi pivot non esegue il rendering in PDF|Insetto|
|CELLSNET-43751|L'ordinamento delle etichette di riga viene perso dopo il riferimento alla tabella pivot|Insetto|
|CELLSNET-47777|Errori di formattazione nel codice HTML convertito|Insetto|
|CELLSNET-47824|Problema con la formula PPMT che fornisce risultati errati|Insetto|
|CELLSNET-47847| Riferimento alla formula errato dopo l'eliminazione delle righe|Insetto|
|CELLSNET-47818|Shape.ToImage non esegue il rendering del testo nell'ambiente docker|Insetto|
|CELLSNET-47820|Mancano i bordi in Aspose EMF/OfficeCompatibleEMF convertito da XLSX|Insetto|
|CELLSNET-47844| Conversione errata della cella formattata della contabilità con doppia sottolineatura durante il salvataggio in PDF|Insetto|
|CELLSNET-47819|Le etichette dati non vengono visualizzate correttamente durante il salvataggio|Insetto|
|CELLSNET-47821|Etichette dati non corrette|Insetto|
|CELLSNET-47813| Strano comportamento (e differenze) con il grafico Treemap (e altri grafici avanzati)|Insetto|
|CELLSNET-47815|I commenti in thread non vengono trasferiti con la forma di inclusione|Insetto|
|CELLSNET-47816|Le dimensioni del file e MaxColumn della cartella di lavoro vengono aumentate dopo aver impostato il bordo del contorno|Insetto|
|CELLSNET-47828|Flusso Ctls aggiuntivo nel file XLS dopo l'aggiornamento a Aspose.Cells for .NET 21.1|Insetto|
|CELLSNET-47838|La tavolozza dei colori del grafico nativo non viene conservata|Insetto|
|CELLSNET-47845| Bordi rimossi in modo imprevisto dopo aver incollato con il tipo di incolla DefaultExceptBorders|Insetto|
|CELLSNET-47848|Problema con la rimozione del filtro automatico di ListObject o del flag Aggiungi pulsante filtro per esso|Insetto|
|CELLSNET-47840|Eccezione sollevata durante l'apertura del file Excel generato da un HTML|Eccezione|
|CELLSNET-47841|StackOverflowException con file xlsx|Eccezione|
|CELLSNET-47854|Cells.Find genera un'eccezione quando il file viene aperto tramite stream|Eccezione|
|CELLSNET-47825| Aspose.Cells 21.01 Eccezione documento di apertura|Eccezione|
|CELLSNET-47831|La nuova cartella di lavoro fallisce|Eccezione|
|


## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Modifica il comportamento di Cells.DeleteBlankRows()/Cells.DeleteBlankRows(DeleteOptions)**

Nelle vecchie versioni, eliminiamo tutte le impostazioni della colonna mentre eliminiamo le righe vuote se il foglio di lavoro è vuoto (nessun dato di celle). Ciò rende impossibile per l'utente eliminare solo le righe vuote e mantenere tutte le impostazioni della colonna. Dalla versione 21.2 non cancelliamo più le impostazioni delle colonne. Se l'utente deve eliminare le impostazioni della colonna per un foglio di lavoro vuoto, deve controllare che non ci siano dati nel foglio e quindi cancellare manualmente ColumnCollection.
Nelle vecchie versioni, non eliminiamo le righe vuote sotto forma. Ciò rende impossibile per l'utente eliminare tutte le righe vuote come previsto. Da 12.2, eliminiamo quelle righe vuote sotto forma insieme ad altre righe vuote comuni.

### **Proprietà Range.CellCount obsoleta.**

Utilizzare invece Range.RowCount e Range.ColumnCount per ottenere il conteggio totale delle celle.

### **Aggiunge la proprietà AutoFilter.ShowFilterButton.**

Indica se mostrare il pulsante filtro del filtro automatico.

### **Elimina la proprietà SeriesCollection.SecondCatergoryData obsoleta.**

Utilizzare invece la proprietà SeriesCollection.SecondCategoryData.

### **Elimina l'enumerazione StyleModifyFlag.Spacing.**

Non è usato.

