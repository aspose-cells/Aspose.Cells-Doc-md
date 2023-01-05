---
title: Aspose.Cells for .NET 8.7.1 Note di rilascio
type: docs
weight: 130
url: /it/net/aspose-cells-for-net-8-7-1-release-notes/
---
### **Altri miglioramenti e modifiche**

|**Chiave** |**Sommario** |**Categoria** |
|:- |:- |:- |
|CELLSNET-44154 |Supporta la lettura/scrittura della tabella delle query.|Nuova caratteristica|
|CELLSNET-43616 | Supporto Formula di matrice che coinvolge la funzione "TABELLA".|Nuova caratteristica|
|CELLSNET-44195 | Il file viene aperto in Visualizzazione protetta dopo la conversione nel formato file XLS| Aumento|
|CELLSNET-44182 | Cells find con formattazione personalizzata funziona nella versione precedente ma non nella versione più recente| Aumento|
|CELLSNET-44187 | I valori Cell vengono erroneamente sostituiti con # quando vengono convertiti in HTML| Insetto|
|CELLSNET-44161 | Aspose.Cells generato XLSX fa sì che Excel 2007 ripari il foglio di calcolo| Insetto|
|CELLSNET-44063 | La tabella pivot perde l'ordine dell'intestazione dopo aver lavorato con il file di input| Insetto|
|CELLSNET-44215 | Salva in pdf che mostra i dati estranei a destra della tabella| Insetto|
|CELLSNET-44201 | Problema relativo agli indici di caratteri non supportati nella formula CHAR| Insetto|
|CELLSNET-44193 | L'ombreggiatura delle celle inclinate non viene visualizzata correttamente in PDF| Insetto|
|CELLSNET-44213 | Il salvataggio dell'immagine dal foglio di lavoro produce un'immagine leggermente diversa| Insetto|
|CELLSNET-44192 | Le etichette delle categorie nella parte superiore del grafico sono allineate a destra invece che a sinistra| Insetto|
|CELLSNET-44240 | Problema con la ridenominazione di un intervallo denominato| Insetto|
|CELLSNET-44239 | Cell.ContainsExternalLink restituisce true se la formula è =WEEKNUM| Insetto|
|CELLSNET-44231 |Il nuovo salvataggio del foglio di calcolo corrompe il risultato| Insetto|
|CELLSNET-44222 | La cartella di lavoro con macro viene danneggiata con la versione 8.7.0| Insetto|
|CELLSNET-44220 | L'impostazione della proprietà WorkbookSettings.Password danneggia il foglio di calcolo risultante| Insetto|
|CELLSNET-44218 | Il nuovo salvataggio di XLSX rinomina il file xl\embeddings\oleObject1.bin| Insetto|
|CELLSNET-44214 | Copia intervallo non mantiene le impostazioni di ListObject| Insetto|
|CELLSNET-44203 | Il riferimento alle formule è diverso tra 8.6.2 e 8.7.0 per l'operazione Worksheet.Copy| Insetto|
|CELLSNET-44241 | System.IndexOutOfRangeException in Cells.ImportData| Eccezione|
|CELLSNET-44226 | System.ArgumentException in Workbook.Save durante il salvataggio nel formato ODS| Eccezione|
|CELLSNET-44225 | Eccezione: "Testo non valido del nome definito." verificato durante la copia del foglio di lavoro| Eccezione|
|CELLSNET-44223 | NullReferenceException durante il caricamento di un file XLSX specifico| Eccezione|
|CELLSNET-44212 | Eccezione NullReference all'apertura del file excel di origine| Eccezione|
|CELLSNET-44204 | CellsException: la dimensione del carattere non è compresa nell'intervallo, in Cartella di lavoro ctor| Eccezione|
|CELLSNET-44196 | Fornire la possibilità di rilevare quale colonna viene filtrata e quale valore filtrare sull'interfaccia GridWeb|Nuova caratteristica|
|CELLSNET-44232 |Problema GridDesktop con RemoveRow(index) dove index è "0"| Insetto|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Aggiunge la proprietà LookInType.OriginalValues.**
Trova solo l'oggetto dai valori originali senza formato.
