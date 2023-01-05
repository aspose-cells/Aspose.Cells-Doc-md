---
title: Aspose.Cells for .NET 20.12 Note di rilascio
type: docs
weight: 1
url: /it/net/aspose-cells-for-net-20-12-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 20.12](https://www.nuget.org/packages/Aspose.Cells/20.12.0).

{{% /alert %}}

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSNET-47309|Le formule IFS vengono racchiuse tra parentesi graffe dopo il salvataggio con ASPOSE|Nuova caratteristica|
|CELLSNET-47710|Supporta la formula con la funzione Foglio()|Nuova caratteristica|
|CELLSNET-47672|Riduci le dimensioni dell'output durante la conversione in HTML|Aumento|
|CELLSNET-47674|Visualizza colonne aggiuntive quando il testo si sovrappone alle celle successive|Aumento|
|CELLSNET-47749|Rimuovi la macro ods in Workbook.RemoveMacro|Aumento|
|CELLSNET-47759|Supporto tag h1 quando si imposta Cell.HtmlString|Aumento|
|CELLSNET-47771|Manca il nuovo foglio di lavoro mc:Ignorable="x14ac xr xr2 xr3"|Aumento|
|CELLSNET-47758| Il complesso di conversione da XLSM a HTML richiede molto tempo|Prestazione|
|CELLSNET-47578|Markup non valido con tag SPAN di chiusura non aperto viene prodotto durante la conversione del documento Cells in HTML|Insetto|
|CELLSNET-47776|DirectoryNotFoundException durante il tentativo di aprire HTML|Insetto|
|CELLSNET-47643|Alcune colonne extra nel nuovo output in Excel per il rendering HTML|Insetto|
|CELLSNET-47688|Alcuni TD causeranno errori di carattere per il carattere Wingdings nel rendering da HTML a PDF|Insetto|
|CELLSNET-47690|La conversione di Html in Xlsx non rispetta lo stile della tabella html|Insetto|
|CELLSNET-47718|Le immagini sono allineate in modo errato durante l'importazione del file in html|Insetto|
|CELLSNET-47729|Le immagini si sovrappongono al testo durante l'importazione di HTML in Excel|Insetto|
|CELLSNET-47746|Virgolette non codificate nei valori degli attributi HTML|Insetto|
|CELLSNET-47747|Differenze durante la conversione di Excel in HTML|Insetto|
|CELLSNET-47763|Il valore della serie non è corretto dopo l'aggiornamento dei dati pivot.|Insetto|
|CELLSNET-47731|Risultato dell'esecuzione della formula PPMT errato|Insetto|
|CELLSNET-47734|L'inserimento di una colonna e la modifica della formula elimina le altre formule|Insetto|
|CELLSNET-47738|il filtro automatico non funziona come excel|Insetto|
|CELLSNET-47764|Numero convertito in scientifico durante la conversione da XLSX a CSV|Insetto|
|CELLSNET-47740| Il testo viene ritagliato (la prima riga non viene visualizzata) con il carattere personalizzato durante l'adattamento automatico delle righe|Insetto|
|CELLSNET-47753|Bordo attorno all'icona durante la conversione di Excel in PDF|Insetto|
|CELLSNETCORE-88|SetFontFolders non funziona correttamente con le etichette delle serie di dati|Insetto|
|CELLSNET-47739|La legenda mostra il nome della serie invece del testo dell'etichetta|Insetto|
|CELLSNET-47713|Problema con la copia dei fogli quando esiste una "definizione del nome nascosta" nel file Excel|Insetto|
|CELLSNET-47733|Diverso comportamento tra la versione 20.3 e 20.11|Insetto|
|CELLSNET-47752|Etichetta oggetto vecchio non recuperata nel foglio Excel|Insetto|
|CELLSNET-47761|Il file è danneggiato dopo aver cancellato il titolo del grafico.|Insetto|
|CELLSNETCORE-89|L'eliminazione di colonne vuote rimuove i commenti nelle colonne dopo la colonna eliminata|Insetto|
|CELLSNET-47732|RefreshPivotData genera un'eccezione|Eccezione|
|CELLSNET-47745|Eccezione sollevata durante l'importazione di file di esempio|Eccezione|
|CELLSNET-47711|Eccezione all'apertura del file ODS|Eccezione|
|CELLSNET-47712|Viene generata un'eccezione quando si tenta di caricare il documento allegato|Eccezione|
|CELLSNET-47715|Impossibile caricare il file Xltx|Eccezione|
|CELLSNET-47735|Eccezione all'apertura di XLSB|Eccezione|
|CELLSNET-47741|L'indice della colonna non deve trovarsi all'interno dell'eccezione del rapporto pivot quando si chiama DeleteBlankColumns|Eccezione|
|CELLSNET-47750|Impossibile aprire XLSX|Eccezione|
|CELLSNET-47751|Impossibile convertire XLSX in XLSM|Eccezione|
|CELLSNET-47773|ArgumentOutOfRangeException durante la conversione del foglio di lavoro in immagine|Eccezione|
|


## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Aggiunge il metodo Cell.SetDynamicArrayFormula(string arrayFormula, Opzioni FormulaParseOptions, bool calcola).**

Supporta l'impostazione della formula dell'array dinamico e la diffusione nelle celle adiacenti, se possibile.

### **Aggiunge il metodo Workbook.RefreshDynamicArrayFormulas(boolcalculate).**

Supporta l'aggiornamento delle formule di matrice dinamica e la diffusione nelle celle adiacenti in base ai dati correnti.

### **Aggiunge la proprietà Cell.Comment.**

Ottiene il commento della cella.

### **Aggiunge la proprietà HtmlSaveOptions.ExportExtraHeadings**

Indica se esportare intestazioni aggiuntive quando la lunghezza del testo è maggiore della colonna di visualizzazione massima.
Il valore predefinito è falso. Se desideri importare il file html in Excel, mantieni il valore predefinito.

### **Aggiunge la proprietà HtmlSaveOptions.ExportFormula**

Indica se esportare la formula durante il salvataggio del file in html. Il valore predefinito è vero.
Se desideri importare l'output html in Excel, mantieni il valore predefinito.


### **Aggiunge la proprietà HtmlSaveOptions.MergeEmptyTdForcely**

Indica se l'unione forzata dell'elemento TD vuoto durante l'esportazione del file in html.
La dimensione del file html verrà ridotta in modo significativo dopo aver impostato il valore su true. Il valore predefinito è falso.
Se vuoi importare il file html per eccellere o esportare le linee della griglia perfette quando salvi il file in html,
si prega di mantenere il valore predefinito.

### **Aggiunge la proprietà LoadOptions.AutoFilter**

Indica se filtrare automaticamente i dati durante il caricamento dei file.
volte, sebbene sia impostato il filtro automatico, le righe corrispondenti non sono nascoste nel file. Ora funziona solo per il file SpreadSheetML.

### **Aggiunge la proprietà WorkbookSettings.Author**

Ottiene e imposta l'autore della cartella di lavoro.

### **Aggiunge il metodo MultipleFilterCollection.Add().**

Aggiunge la stringa del filtro del filtro automatico.

