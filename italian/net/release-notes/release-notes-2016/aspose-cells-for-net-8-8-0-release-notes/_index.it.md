---
title: Aspose.Cells for .NET 8.8.0 Note di rilascio
type: docs
weight: 110
url: /it/net/aspose-cells-for-net-8-8-0-release-notes/
---
### **1) Aspose.Cells**

|**Chiave** |**Riepilogo** |**Categoria** |
|:- |:- |:- |
|CELLSNET-44376 | Fornire la possibilità di vietare la conversione di valori numerici lunghi in notazione esponenziale durante l'importazione da HTML| Nuova caratteristica|
|CELLSNET-44360 | Rilevamento delle virgolette singole iniziali nella cella| Nuova caratteristica|
|CELLSNET-44356 | Ottieni l'indirizzo della cella di destinazione o di output per una connessione esterna| Nuova caratteristica|
|CELLSNET-44340 | Supporto per la localizzazione (tedesco) della convalida lato client| Nuova caratteristica|
|CELLSNET-44345 | La formula per WordArt non reagisce alla modifica dell'argomento durante la conversione da XLS a XLSB| Aumento|
|CELLSNET-44342 | Il processo sembra bloccarsi con l'utilizzo della CPU al 100% per la conversione di un foglio di calcolo a pagina singola in PDF| Prestazione|
|CELLSNET-44324 | XLSM viene danneggiato dopo aver ripopolato i dati e aggiornato la tabella pivot| Insetto|
|CELLSNET-44312 | Le interruzioni di riga vengono perse durante l'importazione di codice HTML e l'esportazione in un foglio di calcolo| Insetto|
|CELLSNET-44311 | I bordi vengono persi durante l'importazione di codice HTML e l'esportazione in un foglio di calcolo| Insetto|
|CELLSNET-44286 | Sample1.xlsx viene danneggiato dopo essere stato aperto e aggiornato| Insetto|
|CELLSNET-44375 | Codifica errata con il file di destinazione (CSV).| Insetto|
|CELLSNET-44368 |Problema di formattazione di milioni di numeri durante la conversione di Excel in PDF| Insetto|
|CELLSNET-44347 | L'API esegue il rendering di due pagine PDF per un foglio di lavoro indipendentemente dall'impostazione di OnePagePerSheet su true| Insetto|
|CELLSNET-44335 | Il testo viene tagliato durante il rendering del foglio di calcolo| Insetto|
|CELLSNET-44382 | Il grafico non viene generato correttamente nel file Excel di output| Insetto|
|CELLSNET-44373 | Problema di allineamento con l'elenco puntato (forma) nell'immagine di rendering| Insetto|
|CELLSNET-44337 | Lo stile dell'elenco puntato (forma) è diverso nell'immagine di output| Insetto|
|CELLSNET-44300 | Parte delle etichette dell'asse X viene visualizzata con orientamento orizzontale durante la conversione del grafico in immagine| Insetto|
|CELLSNET-44372 | Il file Excel con documenti incorporati viene danneggiato durante il salvataggio| Insetto|
|CELLSNET-44369 |# Rif! dopo aver copiato celle contenenti riferimenti a celle denominate da una cartella di lavoro a un'altra
| Insetto|
|CELLSNET-44359 | La rimozione della password da un foglio di calcolo protetto modifica il nome dell'oggetto incorporato| Insetto|
|CELLSNET-44348 | Il numero viene arrotondato quando si converte HTML in formato foglio di calcolo| Insetto|
|CELLSNET-44330 | Riferimento oggetto non impostato eccezione all'apertura di un file Excel| Eccezione|
|CELLSNET-44323 | Riferimento all'oggetto non impostato su un'istanza di un oggetto in PivotTable.RefreshData| Eccezione|
|CELLSNET-44355 |L'indice era al di fuori dei limiti dell'eccezione dell'array durante la conversione di Excel in PDF| Eccezione|
|CELLSNET-44354 | Da forma a immagine Errore durante la conversione di Excel in PDF| Eccezione|
|CELLSNET-44380 | "Formula non valida" durante il caricamento di un file Excel specifico tramite API Aspose.Cells| Eccezione|
|CELLSNET-44370 | "Invalid sectionId of Header Footer image" all'apertura del file Excel| Eccezione|
|CELLSNET-44357 | System.ArgumentException: l'elemento è già stato aggiunto, in Workbook ctor| Eccezione|
### **2) Aspose.Cells Griglia Suite**

|**Chiave** |**Riepilogo** |**Categoria** |
|:- |:- |:- |
|CELLSNET-44350 | Aggiungi avviso di timeout della sessione per GridWeb| Nuova caratteristica|
|CELLSNET-44339 | 500 Errore interno: "Errore in Cell: formula non valida" inserendo una formula non valida nell'interfaccia utente di GridWeb| Eccezione|
|CELLSNET-44326 | Facendo clic su una cella, il testo formattato viene modificato nella sua sorgente HTML| Insetto|
|CELLSNET-44325 | GridWeb modifica il contenuto dell'elenco/elenco a discesa di convalida dei dati| Insetto|
|CELLSNET-44321 | Il menu contestuale cresce quando vengono aggiunte righe o colonne attraverso di esso| Insetto|
|CELLSNET-44320 | L'aggiunta di righe e colonne tramite il menu contestuale non funziona| Insetto|
### **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.
#### **Aggiunge la proprietà HTMLLoadOptions.DeleteRedundantSpaces**
 Indica se eliminare gli spazi ridondanti quando il testo va a capo utilizzando le righe<br>etichetta.
#### **Rende obsoleta la proprietà LoadOptions.ConvertNumericData e aggiunge la proprietà TxtLoadOptions.ConvertNumericData.**
Utilizzare invece la proprietà TxtLoadOptions.ConvertNumericData o HTMLLoadOptions.ConvertNumericData.
#### **Aggiunge la proprietà Style.QuotePrefix.**
Indica se il valore della cella inizia con virgolette singole.
#### **Aggiunge la proprietà QueryTable.ConnectionId.**
Ottiene l'ID connessione della tabella di query.
#### **Aggiunge la proprietà ExternalConnection.Id.**
Ottiene l'id della connessione.
#### **Aggiunge la proprietà ListObject.QueryTable.**
Ottiene la QueryTable collegata della tabella.
#### **Aggiunge la proprietà HTMLLoadOptions.KeepPrecision.**
Indica se non analizzare un valore stringa se la lunghezza è 15.
