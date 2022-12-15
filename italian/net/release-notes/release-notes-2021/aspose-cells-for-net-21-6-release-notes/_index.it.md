---
title: Aspose.Cells for .NET 21.6 Note di rilascio
type: docs
weight: 7
url: /it/net/aspose-cells-for-net-21-6-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 21.6](https://www.nuget.org/packages/Aspose.Cells/21.6.0).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-48104|Ottieni il valore di SlicerCacheItem nella raccolta Slicer.SlicerCache.SlicerCacheItems|Nuova caratteristica|
|CELLSNET-48121|Supporta lo stile personalizzato di Slicer in Xlsb|Nuova caratteristica|
|CELLSNET-48053|Imposta le formule definite dall'utente come formule di matrice e allo stesso tempo fornisci valori come risultati calcolati per tali formule|Nuova caratteristica|
|CELLSNET-43532|Possibilità di incorporare i caratteri con codifica ANSI|Nuova caratteristica|
|CELLSNET-48042|I valori delle celle formattate recuperate sono errati nel foglio di lavoro di Excel|Aumento|
|CELLSNET-48078|Copia completa della cartella di lavoro dopo il calcolo con l'impostazione CreateCalcChain|Aumento|
|CELLSNET-48079| Come verificare se un foglio di lavoro è vuoto|Aumento|
|CELLSNET-48135| Problema con cartella di lavoro protetta (con password) generata da Aspose.Cells|Aumento|
|CELLSNET-48050| la cpu si blocca sulla cartella di lavoro aperta|Prestazione|
|CELLSNET-48063|Tme costo quando si chiama l'API Cells.GetRowRawHeightPoint|Prestazione|
|CELLSNET-48046|L'offset del testo della forma non è corretto (freccia: quad).|Insetto|
|CELLSNET-48064|La disposizione del testo del carattere predefinito nella casella di testo non è corretta|Insetto|
|CELLSNET-48088|La parte sovrapposta della curva viene tagliata.|Insetto|
|CELLSNET-48089|Le curve sinistra e destra sono ridotte|Insetto|
|CELLSNET-48060|Errore durante l'utilizzo della funzione RemoveUnusedStyles con stili personalizzati|Insetto|
|CELLSNET-48080|La tabella pivot non può utilizzare "值" o "Valori" come nome di colonna durante la creazione della tabella pivot|Insetto|
|CELLSNET-48085| Viene eseguito il rendering dell'intestazione di colonna nascosta|Insetto|
|CELLSNET-48105|Il posizionamento della casella di testo viene modificato durante la conversione di Excel in HTML|Insetto|
|CELLSNET-48048| Eccezione durante il salvataggio di XLSX con commenti in formato PDF|Insetto|
|CELLSNET-48082|L'aggiunta di righe superiori a 30 utilizzando ImportCustomObjects genera un file danneggiato|Insetto|
|CELLSNET-48086|L'intervallo denominato non è stato creato correttamente in 21.5 ma ha funzionato in 21.4|Insetto|
|CELLSNET-48118|Supporto per aggiornare le formule di matrice dinamica in base all'intervallo versato aggiornato|Insetto|
|CELLSNET-48081|L'immagine non viene mostrata in GridWeb|Insetto|
|CELLSNET-48117|Aggiungere GridCell.GetValidation() per GridDesktop|Insetto|
|CELLSNET-47627|Problemi durante l'accesso/modifica dell'asse X di un grafico Excel utilizzando Aspose.Cells|Insetto|
|CELLSNET-48041| Il grafico estratto è distorto nel rendering del grafico rispetto all'immagine/PDF|Insetto|
|CELLSNET-48049|Diversa spaziatura degli assi durante la conversione da cartella di lavoro xlsx a emf|Insetto|
|CELLSNET-48101|I caratteri Chinse vengono visualizzati come Rectagle Linux Docker|Insetto|
|CELLSNET-48061|PowerQuery che scompaiono dopo la sostituzione della query|Insetto|
|CELLSNET-48065|Il file salvato nuovamente con un valore di intervallo denominato specifico causa il danneggiamento di Excel|Insetto|
|CELLSNET-48067|SetChartDataRange non ha riconosciuto le celle unite|Insetto|
|CELLSNET-48072|Leggi grafico vuoto otterrà un tipo di grafico errato|Insetto|
|CELLSNET-48133|Errore generato da MS Excel durante l'apertura del file XLSX di output|Insetto|
|CELLSNET-48045|Viene generata un'eccezione durante la conversione di svg in immagine|Eccezione|
|CELLSNET-48062|Eccezione sollevata durante la conversione da XLS a XLSX|Eccezione|
|CELLSNET-48074|Il valore non può essere nullo quando si apre il file dei numeri Apple|Eccezione|
|


## **API pubblica e modifiche non compatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.

### **Modifica il comportamento della proprietà Cell.IsErrorValue.**

Nelle versioni precedenti, questa proprietà si applica solo alle celle della formula. Per renderlo coerente con altre proprietà, da 21.6 controlliamo anche le celle non formula e se il suo valore è un valore di errore, restituiamo anche true. L'utente può controllare prima la proprietà Cell.IsFormula se ha solo bisogno di controllare il valore di errore per le celle della formula.

### **Modifica il comportamento della proprietà Cell.Value.**

Nelle vecchie versioni, questa proprietà restituisce sempre l'oggetto DateTime se la cella è formattata come data ora e il suo valore è numerico. A partire da 21.6, questa proprietà restituisce il valore numerico stesso se supera il valore DateTime massimo valido. Con questa modifica l'oggetto restituito è coerente con quanto mostrato nella barra della formula di ms excel.

### **Aggiunge la proprietà Cell.IsNumericValue.**

Fornisce all'utente un modo comodo ed efficiente per verificare se il valore di una cella è un valore numerico (int, double, datetime).

### **Aggiunge metodi sovraccaricati di Cell.SetSharedFormula()/SetArrayFormula()/SetDynamicArrayFormula().**

Supporto per impostare formule di matrice e formule condivise con valori predefiniti.

### **Aggiunge enum PdfFontEncoding.**

Rappresenta la codifica dei caratteri incorporati in pdf.

### **Aggiunge la proprietà PdfSaveOptions.FontEncoding.**

Ottiene o imposta la codifica dei caratteri incorporati in pdf.

### **Aggiunge la proprietà SlicerCacheItem.Value.**

Restituisce il testo dell'etichetta per l'elemento slicer. Sola lettura.

### **Aggiunge il metodo GlobalizationSettings.GetProtectionNameOfPivotTable().**

Ottiene il nome della protezione nella tabella pivot.

### **Aggiunge il metodo FileFormatUtil.FileFormatToSaveFormat.**

Converte il formato del file in formato di salvataggio.

