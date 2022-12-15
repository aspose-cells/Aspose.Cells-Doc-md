---
title: Aspose.Cells for .NET Note sulla versione 18.11
type: docs
weight: 20
url: /it/net/aspose-cells-for-net-18-11-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 18.11](https://www.nuget.org/packages/Aspose.Cells/18.11.0).

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-46377|Controlla se una cella ha una formula circolare|Nuova caratteristica|
|CELLSNET-46399|Si è verificata un'eccezione durante la chiamata a PivotTable.RefreshData()|Nuova caratteristica|
|CELLSNET-46394|Recupera la data di aggiornamento della tabella pivot simile a Interop.Excel|Nuova caratteristica|
|CELLSNET-46261|La sostituzione dei testi in SmartArt non funziona|Nuova caratteristica|
|CELLSNET-46435|GetValidationValue restituisce un valore errato per numeri grandi|Aumento|
|CELLSNET-46117|La posizione del testo cambia leggermente separando la forma|Aumento|
|CELLSNET-46400|Si blocca durante la chiamata a PivotTable.RefreshData|Prestazione|
|CELLSNET-46441|Cell.GetDisplayStyle() si blocca per una cella|Prestazione|
|CELLSNET-46423|Problemi di formattazione durante la conversione di XLSX in PDF|Insetto|
|CELLSNET-46410|Il formato della tabella pivot viene incasinato dopo l'aggiornamento|Insetto|
|CELLSNET-46404|Elaborazione dei diagrammi allo stesso modo delle immagini durante il salvataggio dell'HTML|Insetto|
|CELLSNET-46388|Il file è corrotto dopo aver caricato e salvato nuovamente un formato di file XLSX|Insetto|
|CELLSNET-46387|Tabella pivot per l'ordinamento dei problemi|Insetto|
|CELLSNET-46366|Mancano bordi e colori di sfondo durante la conversione dell'HTML in XLSX|Insetto|
|CELLSNET-46365|Fogli di stile CSS di riferimento ignorati durante l'apertura di HTML|Insetto|
|CELLSNET-46431|Il risultato della formula VLookup è diverso dal risultato di MS Excel|Insetto|
|CELLSNET-46430|La formula dell'array non funziona dopo Workbook.Combine nella conversione da XLSX a XLSB|Insetto|
|CELLSNET-46428|Name.RefersTo non recupera il valore corretto|Insetto|
|CELLSNET-46413|La creazione di XLSX con la formattazione condizionale produce un file danneggiato|Insetto|
|CELLSNET-46403|La formula di matrice non funziona dopo Workbook.Combine per salvare nel formato di file XLSB|Insetto|
|CELLSNET-46396|La cartella di lavoro salvata come SVG è danneggiata poiché in realtà è un file TIFF|Insetto|
|CELLSNET-46420|Grafico in PDF che riceve problemi di picco|Insetto|
|CELLSNET-46411|Si blocca durante la conversione di XLSX in PDF|Insetto|
|CELLSNET-46408|Gli indicatori di dati non sono presenti nell'immagine del grafico di output dal file MS Excel|Insetto|
|CELLSNET-46393|Etichette degli assi disallineate dopo la conversione del grafico MS Excel nel formato immagine PNG|Insetto|
|CELLSNET-46359|Variazione della dimensione del carattere per le etichette nel grafico nel file SVG di output|Insetto|
|CELLSNET-46433|La formattazione condizionale viene eliminata durante l'eliminazione dell'intervallo denominato|Insetto|
|CELLSNET-46427|MS Excel segnala un problema dopo l'apertura/salvataggio con Aspose.Cells|Insetto|
|CELLSNET-46421|La proprietà CreatedTime del documento cambia dopo essere stata salvata nello stream|Insetto|
|CELLSNET-46417|Il testo a capo non funziona insieme a una riga vuota sopra il testo|Insetto|
|CELLSNET-46416|Grafici dati persi durante il caricamento e il salvataggio del file XLSX|Insetto|
|CELLSNET-46409|Problema con l'elenco a discesa dopo la conversione da XML|Insetto|
|CELLSNET-46407|L'inizializzazione della cartella di lavoro richiede troppo tempo durante il caricamento di un formato di file XLSM|Insetto|
|CELLSNET-46397|Il titolo del grafico viene perso durante la conversione da XLS a XLSM|Insetto|
|CELLSNET-46401|ArgumentException mentre si lavora con il file HTML generato|Eccezione|
|CELLSNET-46426|Eccezione durante la chiamata di AutoFitColumns()|Eccezione|
|CELLSNET-46415|Eccezione CellsException durante il salvataggio quando ParsingFormulaOnOpen è false|Eccezione|
|CELLSNET-46422|Eccezione durante l'elaborazione di smart tag|Eccezione|
### **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.
#### **Aggiunge la proprietà PivotTable.RefreshedByWho**
Ottiene il nome dell'utente che ha aggiornato la tabella pivot l'ultima volta.
#### **Aggiunge la proprietà PivotTable.RefreshDate**
Ottiene la data dell'ultimo aggiornamento della tabella pivot.
#### **Aggiunge le proprietà CalculationData.CellRow/CellColumn**
Fornisce all'utente un modo efficiente per ottenere gli indici di riga e colonna della cella invece di recuperare l'oggetto Cell.
#### **Aggiunge la classe CalculationCell**
Rappresenta i dati di calcolo relativi a una cella calcolata.
#### **Aggiunge il metodo AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData).**
Fornisce all'utente un metodo per raccogliere ed elaborare i riferimenti circolari.
#### **Aggiunge la proprietà TxtLoadOptions.TreatConsecutiveDelimitersAsOne**
Consente all'utente di scegliere se i delimitatori consecutivi devono essere presi come uno solo durante l'importazione del file CSV.
#### **Aggiunge il metodo FormatCondition.SetFormulas(string formula1, string formula2, bool isR1C1, bool isLocal)**
Fornisce un modo efficiente e conveniente per l'utente di impostare le formule per FormatCondition.
#### **Aggiunge il metodo Validation.GetListValue(int row, int column).**
Consente all'utente di ottenere il valore per produrre l'elenco per la convalida di una cella specifica.
#### **Metodo obsoleto ValidationCollection.Add(Validation validation).**
Usare invece il metodo ValidationCollection.Add(CellArea).
#### **Aggiunge il metodo Validation.Copy(Aspose.Cells.Validation,Aspose.Cells.CopyOptions)**
Convalida delle copie.
#### **Aggiunge le proprietà CreatedUniversalTime ,LastPrintedUniversalTime e LastSavedUniversalTime di BuiltInDocumentPropertyCollection**
Restituisce l'ora UTC relativa alle proprietà incorporate.
#### **Aggiunge la proprietà OoxmlSaveOptions.UpdateSmartArt**
Indica se aggiornare la smart art.
#### **Aggiunge la classe SmartArtShape**
Rappresenta la forma artistica intelligente.
