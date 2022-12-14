---
title: Aspose.Cells for .NET 21.3 Note di rilascio
type: docs
weight: 28
url: /it/net/aspose-cells-for-net-21-3-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 21.3](https://www.nuget.org/packages/Aspose.Cells/21.3.0).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-47857|Cancella tutte le aree di unione sul foglio|Nuova caratteristica|
|CELLSNET-47892| Firma digitalmente Microsoft Riga della firma nel foglio di calcolo Excel|Aumento|
|CELLSNET-47905|Implementa l'algoritmo Digest di BouncyCastel's API|Aumento|
|CELLSNET-47838|La tavolozza dei colori del grafico nativo non viene conservata|Aumento|
|CELLSNET-47877|Workbook.Settings.RemovePersonalInformation non è efficace|Aumento|
|CELLSNET-47879|Il file generato è danneggiato durante il salvataggio del file xls con il file doc word6.0 incorporato come xlsx.|Aumento|
|CELLSNET-47893|Converti la linea della firma in immagine.|Aumento|
|CELLSNET-47899|Supporta la copia di QueryTable durante la copia della cartella di lavoro.|Aumento|
|CELLSNET-47842|Prestazioni lente durante l'aggiornamento di una grande tabella pivot|Prestazione|
|CELLSNET-42846|L'equazione viene persa al nuovo salvataggio del file ODS|Insetto|
|CELLSNET-47794|Le dimensioni e la posizione della forma della freccia non sono corrette|Insetto|
|CELLSNET-46469|Chart.RefreshPivotData() rimuove il formato del numero dell'asse|Insetto|
|CELLSNET-47871|Intestazioni errate durante il rendering dell'area di stampa|Insetto|
|CELLSNET-47875| MS Excel deve riparare il file dopo averlo salvato nuovamente tramite Aspose.Cells|Insetto|
|CELLSNET-47829| Il calcolo della formula risulta diverso quando si implementano riferimenti circolari e iterazioni|Insetto|
|CELLSNET-47865|Aspose.Cells presenta in modo errato la data in formato giapponese|Insetto|
|CELLSNET-47872|MS Excel richiede un messaggio di errore quando si apre un file XLTM risalvato da Aspose.Cells|Insetto|
|CELLSNET-47897|La selezione degli elementi dell'elenco non funziona quando viene caricata nell'applicazione ASP.NET|Insetto|
|CELLSNET-47862|Excel Accounting La sottolineatura viene tagliata durante l'esportazione in PDF|Insetto|
|CELLSNET-47881|La larghezza della colonna è inferiore al previsto durante l'importazione/mappatura del file XML nella cartella di lavoro|Insetto|
|CELLSNET-47804|Il testo della legenda del grafico non viene visualizzato correttamente|Insetto|
|CELLSNET-47834|Chart.Calculate() nei grafici modifica la formattazione del grafico|Insetto|
|CELLSNET-47856|Problema di conversione da XLSX a PDF con tabelle pivot|Insetto|
|CELLSNET-41275|I grafici che fanno riferimento ad altri fogli non vengono visualizzati|Insetto|
|CELLSNET-42847|Il grafico viene perso al nuovo salvataggio del file ODS|Insetto|
|CELLSNET-47861|Differenza nel calcolo dell'altezza della riga|Insetto|
|CELLSNET-47876|Le righe di adattamento automatico e l'altezza standard non funzionano correttamente per le celle unite|Insetto|
|CELLSNET-47903|L'inserimento di una colonna in una tabella provoca il danneggiamento della cartella di lavoro|Insetto|
|CELLSNET-47906|Problema con InsertCutCells API che interessa i riferimenti alle formule tra fogli di lavoro|Insetto|
|CELLSNET-47908|ForceFullCalculation ritorna a false dopo il nuovo salvataggio|Insetto|
|CELLSNET-47909|La rimozione delle righe vuote non aggiorna di conseguenza le forme dei commenti|Insetto|
|CELLSNET-47913|Shape.UpdateSelectedValue() causa un aggiornamento della forma improprio|Insetto|
|CELLSNET-47866|Eccezione durante il caricamento di un file Html|Eccezione|
|CELLSNET-47882|Eccezione sollevata durante l'importazione di html nel file excel|Eccezione|
|CELLSNET-47863|L'aggiunta di tag HTML alla cella genera System.FormatException|Eccezione|
|CELLSNET-47868|Eccezione dell'indice di fine riga non valida durante l'apertura del file XLS di Office 2000|Eccezione|
|CELLSNET-47869|Cells Errore di caricamento della cartella di lavoro con eccezione|Eccezione|
|CELLSNET-47870|Eccezione sollevata durante il caricamento del file XLS|Eccezione|
|


## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Aggiunge la proprietà SignatureLine.Id.**

Ottiene o imposta l'identificatore per questa riga della firma.

### **Aggiunge la proprietà DigitalSignature.Id.**

Specifica un GUID che può essere incrociato con il GUID della riga della firma archiviata nel contenuto del documento.

### **Aggiunge la proprietà DigitalSignature.ProviderId.**

Specifica l'ID classe del provider della firma.

### **Aggiunge la proprietà DigitalSignature.Image.**

Specifica un'immagine per la firma digitale.

### **Aggiunge la proprietà DigitalSignature.Text.**

Specifica il testo della firma effettiva nella firma digitale.

### **Aggiunge il metodo Cells.ClearMergedCells().**

Rimuove tutte le celle unite.

### **Aggiunge il metodo Workbook.RemovePersonalInformation().**

Rimuove tutte le informazioni personali.

### **Aggiunge la proprietà WorkbookSettings.ForceFullCalculate.**

 
Calcola completamente ogni volta che viene attivato un calcolo.

### **Aggiunge il costruttore DocxSaveOptions(Boolean).**

 Rappresenta le opzioni di salvataggio dei file .docx.

### **Elimina la proprietà WorkbookSettings.IsWriteProtected obsoleta.**

Usare invece la proprietà WorkbookSettings.WriteProtection.IsWriteProtected.

### **Elimina la proprietà WorkbookSettings.RecommendReadOnly obsoleta.**

Usare invece la proprietà WorkbookSettings.WriteProtection.RecommendReadOnly.

### **Elimina la proprietà WorkbookSettings.WriteProtectedPassword obsoleta.**

Usare invece la proprietà WorkbookSettings.WriteProtection.Password.

