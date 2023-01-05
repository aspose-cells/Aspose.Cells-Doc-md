---
title: Aspose.Cells for .NET 21.9 Note di rilascio
type: docs
weight: 4
url: /it/net/aspose-cells-for-net-21-9-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 21.9](https://www.nuget.org/packages/Aspose.Cells/21.9.0).

{{% /alert %}}

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSNET-48134|Supporta il rendering del grafico Box & Whisker Excel 2016 all'immagine|Nuova caratteristica|
|CELLSNET-48683|Elimina la tabella pivot conservando i dati|Aumento|
|CELLSNET-48624|Supporta l'intervallo denominato dell'intera riga/colonna per i file .ods|Aumento|
|CELLSNET-49052|Supporta l'impostazione della trasparenza dell'immagine per i file xlsx.|Aumento|
|CELLSNETCORE-233|Miglioramento per la modifica dell'autore del commento in thread|Aumento|
|CELLSNET-49011|Velocizza l'accesso dell'iteratore delle celle per il rendering per GridDesktop|Prestazione|
|CELLSNET-48915|Eccezione di memoria esaurita durante il rendering del foglio di lavoro nell'immagine|Prestazione|
|CELLSNET-47663|Il documento Excel non viene convertito in html|Prestazione|
|CELLSNET-48506|Migliora le prestazioni per la scrittura di file .ods.|Prestazione|
|CELLSNET-48645| Il testo all'interno di una forma a freccia ha ottenuto la posizione errata|Insetto|
|CELLSNET-48475|L'aggiornamento della tabella pivot non funziona correttamente|Insetto|
|CELLSNET-48711|Esporta l'xlsx ingrandito in html.|Insetto|
|CELLSNET-48998|Le modifiche alle proprietà vengono perse o lo fanno scomparire per l'oggetto Slicer|Insetto|
|CELLSNET-48614|La funzione di filtro di Excel non sembra funzionare correttamente|Insetto|
|CELLSNETCORE-136|Arrowhead non appare in ambiente Linux|Insetto|
|CELLSNETCORE-137|Freccia mancante durante la conversione di Excel in SVG|Insetto|
|CELLSNET-49045|Altezza celle errata osservata in GridWeb durante il caricamento del file allegato|Insetto|
|CELLSNET-49069|Aspose.Cells.GridWeb SessionMode non funzionante|Insetto|
|CELLSNET-40974| Conversione da Excel a Xps: il link non è cliccabile dopo la conversione effettuata .NET|Insetto|
|CELLSNET-48540| Le linee sono diventate tratteggiate sulle barre dei dati in Emf/OfficeCompatibleEmf|Insetto|
|CELLSNET-48609|Problema di differenza dei caratteri durante il confronto con l'immagine ExcelInterop|Insetto|
|CELLSNET-48983| Sheet to Emf lascia i bordi del bordo disegnati in modo errato|Insetto|
|CELLSNET-49049|Il carattere è distorto durante la conversione del foglio in un'immagine Emf con l'opzione EmfOnly|Insetto|
|CELLSNET-48049|Diversa spaziatura degli assi durante la conversione da cartella di lavoro xlsx a emf|Insetto|
|CELLSNET-48509|Il grafico a volte non viene visualizzato in base alla posizione della legenda|Insetto|
|CELLSNET-48580| Voce Miss Legend nell'output SVG del grafico Excel|Insetto|
|CELLSNET-48696|Errore nella modifica del colore dell'etichetta dati|Insetto|
|CELLSNET-48698|Problema relativo al colore del grafico durante l'esportazione in PDF|Insetto|
|CELLSNET-48797|Il valore medio del marker è un errore durante la lettura da xlsx|Insetto|
|CELLSNET-48455|Problema relativo all'altezza della riga di adattamento automatico|Insetto|
|CELLSNET-48473|La colonna AutoFit non funziona correttamente|Insetto|
|CELLSNET-48605|L'aggiunta di codice VBA alla cartella di lavoro ha prodotto risultati danneggiati|Insetto|
|CELLSNET-48644|Perdere righe e filigrana durante la conversione da XLSX a HTML per interruzioni di pagina|Insetto|
|CELLSNET-48669|L'intervallo denominato del file .ods viene letto come Table .|Insetto|
|CELLSNET-48718|Ottieni un nome oggetto incorporato errato|Insetto|
|CELLSNET-48966| Dopo aver copiato l'intervallo di celle, le formule vengono perse|Insetto|
|CELLSNET-49055| Le colonne AutoFit per la cella unita non funzionano|Insetto|
|CELLSNET-49100|In alcune celle mancano le linee della griglia durante l'esportazione in HTML|Insetto|
|CELLSNETCORE-149|La copia degli stili dopo la copia dei valori cancella i valori delle celle nel formato Excel 97|Insetto|
|CELLSNETCORE-152|I dati dell'immagine EMF non possono essere letti dal file XLS|Insetto|
|CELLSNET-48444|Errore di parametro non valido durante la conversione di file xlsb in xls|Eccezione|
|CELLSNET-48607|Errore da forma a immagine|Eccezione|
|CELLSNET-48866|Impossibile aprire il file Excel XLSX specifico nel controllo GridDesktop|Eccezione|
|CELLSNET-48956| Eccezione dopo aver impostato lo stile delle celle utilizzando Cell.SetStyle|Eccezione|
|CELLSNET-48712|Array fuori limite durante il rendering del grafico Box&Whisker|Eccezione|
|CELLSNET-48910|Eccezione generata durante il rendering di box&Whisker Chart in immagine|Eccezione|
|CELLSNET-48648| Indice di colonna non valido durante la copia di un intervallo|Eccezione|
|


## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Aggiunge la proprietà AutoFitterOptions.FormatStrategy.**

Ottiene e imposta la strategia formattata per l'adattamento automatico.

### **Aggiunge la proprietà MsoFormatPicture.Transparency.**

 Restituisce o imposta il grado di trasparenza dell'area come valore compreso tra 0,0 (opaco) e 1,0 (trasparente).

### **Aggiunge metodi PivotTableCollection.Remove() in overload.**

Elimina la tabella pivot specificata e controlla se conservare i dati delle celle.

### **Aggiunge la proprietà ImageOrPrintOptions.IsOptimized.**

 Indica se ottimizzare gli elementi di output. Il valore predefinito è false. Attualmente solo le linee di confine sono ottimizzate quando questa proprietà è impostata su true.

