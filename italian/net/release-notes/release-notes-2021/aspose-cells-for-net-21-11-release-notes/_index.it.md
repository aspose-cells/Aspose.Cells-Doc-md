---
title: Aspose.Cells for .NET Note sulla versione 21.11
type: docs
weight: 2
url: /it/net/aspose-cells-for-net-21-11-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 21.11](https://www.nuget.org/packages/Aspose.Cells/21.11.0).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-48141|Supporta la formula/funzione XLookup|Nuova caratteristica|
|CELLSNET-49614|Supporta il salvataggio delle immagini con il metodo workbook.Save().|Nuova caratteristica|
|CELLSNET-49651|Supporta il salvataggio come file json.|Nuova caratteristica|
|CELLSNET-48499|Recupera i valori delle celle formattate rispetto a determinate celle|Aumento|
|CELLSNET-49523|Cancella i nomi definiti durante la cancellazione dei fogli di lavoro.|Aumento|
|CELLSNET-48646|Eccezione StackOverflow durante la conversione da Excel a PDF|Prestazione|
|CELLSNET-49378|Problema con le prestazioni di conversione da Excel a HTML e le celle vuote|Prestazione|
|CELLSNET-49453|Migliora le prestazioni durante la conversione di Excel in HTML|Prestazione|
|CELLSNET-48095|3D, la forma della nuvola è cambiata|Insetto|
|CELLSNET-49544|Errore nel salvataggio di NamedRange esterno che fa riferimento a un intervallo di più fogli|Insetto|
|CELLSNET-49588|Dati di tipo singolo salvati in modo diverso rispetto al valore originale|Insetto|
|CELLSNET-49667|Il risultato della formattazione condizionale ColorScale non è corretto|Insetto|
|CELLSNET-49043|La posizione della linea disegnata non è corretta nell'immagine|Insetto|
|CELLSNET-49068|PDF errato generato dal file Excel|Insetto|
|CELLSNET-49179|Il riferimento al titolo dell'asse viene rimosso in modo imprevisto|Insetto|
|CELLSNET-49294|Gli assi di alcuni grafici sono diversi da quelli dei file excel|Insetto|
|CELLSNET-49495|Sovrapposizione del rendering delle formule|Insetto|
|CELLSNET-49542|L'asse orizzontale del grafico scompare|Insetto|
|CELLSNETCORE-148|Il grafico a torta non viene visualizzato correttamente|Insetto|
|CELLSNET-49193|GridDesktop non funziona correttamente|Insetto|
|CELLSNET-49642|Aspose.Cells.GridWeb ha una dipendenza non dichiarata da Newtonsoft.Json|Insetto|
|CELLSNET-49452|Il testo multilinea non viene riprodotto bene|Insetto|
|CELLSNET-49498|Flusso HTML in Excel che solleva un'eccezione con le versioni più recenti|Insetto|
|CELLSNET-49610|Xml Import perdendo la formattazione del modello|Insetto|
|CELLSNET-49671|Il testo con caratteri Windings non viene visualizzato correttamente in immagini/HTML|Insetto|
|CELLSNETCORE-278|I risultati della conversione da XLSX a PDF non sono apribili quando la cultura è impostata su norvegese|Insetto|
|CELLSNET-49560|Differenze in XML|Insetto|
|CELLSNET-49598|Regressione: differenze in XML dopo il salvataggio|Insetto|
|CELLSNET-49630|Segni di graduazione errati sulla conversione in EMF|Insetto|
|CELLSNET-49673|Alcune parti delle linee tratteggiate sono diventate linee continue durante la conversione dei grafici in immagini|Insetto|
|CELLSNET-49545|I tipi HtmlCrossType.Default e HtmlCrossType.FitToCell sono interrotti|Insetto|
|CELLSNET-49654|Le macro non funzionano dopo aver convertito XLS in XLSM|Insetto|
|CELLSNET-49727|Le immagini dei file Mht non sono visibili in IE.|Insetto|
|CELLSNET-49609|"Errore da forma a immagine" durante la conversione di file Excel in PDF|Eccezione|
|CELLSNET-49608|Aspose.Cells dà errori quando si tenta di aggiungere determinati nomi di intervalli|Eccezione|
|CELLSNET-49697|Da XLSX a PDF: la stringa di input non era in un formato corretto.|Eccezione|
|CELLSNETCORE-287|NullPointerException durante il calcolo della formula|Eccezione|
|CELLSNET-49497|ExportXml con XML Map genera "NullReferenceException"|Eccezione|
|CELLSNET-49595|ExportXml con XML Map genera "NullReferenceException" per file Excel complessi|Eccezione|
|CELLSNET-49471|Regressione: GetRanges() restituisce Null|Regressione|
|


## **API pubblica e modifiche non compatibili con le versioni precedenti**

Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.

### **Aggiunge enum CellValueFormatStrategy.DisplayString.**

Con questa strategia, Cell.GetStringValue(CellValueFormatStrategy) prenderà in considerazione il limite della larghezza della colonna durante la formattazione dei valori della cella con lo stile di visualizzazione. Se il risultato formattato supera la larghezza disponibile, possono essere restituiti uno o più "#", proprio come mostra ms excel per questo tipo di celle.

### **Aggiunge la proprietà WorksheetCollection.ActiveSheetName.**

Ottiene e imposta il nome del foglio attivo della cartella di lavoro.

### **Aggiunge le classi JsonLoadOptions e JsonSaveOptions.**

Rappresenta le opzioni di caricamento o salvataggio dei file.

### **Aggiunge la proprietà ImageSaveOptions.StreamProvider.**

Fornisci gli stream se sono presenti due o più pagine.

### **Aggiunge l'enumerazione LoadFormat.Image e LoadFormat.Json.**

Rappresenta l'immagine e il tipo json.

### **Aggiunge SaveFormat.Bmp, SaveFormat.Emf, SaveFormat.Gif, SaveFormat.Jpg, SaveFormat.Json e SaveFormat.Png enum**

Nuovi formati di salvataggio supportati.

### **Aggiunge FileFormatType.Emf,FileFormatType.Gif,FileFormatType.Jpg,FileFormatType.Json,FileFormatType.Png,FileFormatType.Wmf enum**

Nuovi tipi di formati di file supportati.

