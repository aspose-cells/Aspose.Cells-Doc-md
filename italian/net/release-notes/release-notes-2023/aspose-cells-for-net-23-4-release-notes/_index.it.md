---
title: Aspose.Cells for .NET 23.4 Note di rilascio
type: docs
weight: 9
url: /it/net/aspose-cells-for-net-23-4-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 23.4](https://www.nuget.org/packages/Aspose.Cells/23.4.0).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
| :- | :- | :- |
|CELLSNET-52860|Supporto al calcolo della funzione ENCODEURL|
|CELLSNET-53092|Supporto per salvare file xlsb in modalità LightCells|
|CELLSNET-53098|CalculateFormula() moltiplica l'array|
|CELLSNET-53136|Supporta il controllo del rendering activex e il controllo del modulo per la casella di controllo in GridWeb|
|CELLSNET-53151|Supporta il controllo di rendering activex per la casella di testo in GridWeb|
|CELLSNET-53152|Supporta il controllo del rendering activex e il controllo del modulo per il pulsante di opzione in GridWeb|
|CELLSNET-53059|Aggiungi API per controllare se il font è installato o disponibile|
|CELLSNET-53064|Supporto per impostare la formula sulla cella specificata in ListObject|
|CELLSNET-52903|La funzione CODICE restituisce valori diversi n Excel e Aspose.Cells|
|CELLSNET-53128|Migliora il testo allineato al centro durante l'esportazione in html|
|CELLSNET-53135|Salva il nome del foglio come nome del nodo quando converti excel in xml|
|CELLSNET-53079|Danneggiamento della forma durante il salvataggio del file in pdf|
|CELLSNET-52982|Si verifica un errore durante l'impostazione della formula LET per la cella|
|CELLSNET-53009|1.36 diventa 1.3599999999999999 dopo la lettura dal file modello xlsx|
|CELLSNET-53132|Il metodo Worksheet.CalculateFormula calcola la formula non valida in modo errato|
|CELLSNET-53139|Problema lettura decimali più di 15 caratteri|
|CELLSNET-53049|La griglia non è coerente con Excel nell'output PDF|
|CELLSNET-53078|GetPrintingPageBreaks restituisce valori non corretti|
|CELLSNET-53123| L'immagine copriva il testo in pdf convertito|
|CELLSNET-53103|Le tabelle vengono unite e tagliate durante la conversione in Html|
|CELLSNET-52661|La conversione di particolari Xlsx in Pptx produce risultati interrotti|
|CELLSNET-52953| L'allineamento Cell in Excel HTML è errato|
|CELLSNET-52968|Le colonne adattate automaticamente non possono contenere tutto il contenuto|
|CELLSNET-52993|Aspose.Cells non rileva correttamente il formato del file|
|CELLSNET-53035|AutoFitRows non funziona in combinazione con celle e bordi uniti|
|CELLSNET-53048| Il file generato è danneggiato Se Module.Name continua in giapponese|
|CELLSNET-53063|Cells.InsertRows non copia la formula impostata per una colonna della tabella|
|CELLSNET-53065|La sottolineatura dello stile del carattere non si applica a WordArt|
|CELLSNET-53082|Il problema con il popup del contenuto appare dopo aver salvato il file .xlsb|
|CELLSNET-53089|Visualizza il messaggio Impostazioni di calcolo quando si apre il file ods generato in MS Excel|
|CELLSNET-53104|La copia di fogli di lavoro o cartelle di lavoro non conserva l'ordinamento delle tabelle|
|CELLSNET-53111|Giustifica l'allineamento distribuito mancante durante il salvataggio del file in xls|
|CELLSNET-53115|Grafico sparkline mancante durante la conversione del file in ODS|
|CELLSNET-53117|Il file dei risultati si arresta in modo anomalo durante la conversione del file con la tabella pivot in ODS|
|CELLSNET-53118|Visualizza il grafico durante la conversione del file in ODS|
|CELLSNET-53119|Molteplici perdite di grafici durante la conversione del file in ODS|
|CELLSNET-53120|Grafico azionario mancante nel file di output ODS da un file XLSX|
|CELLSNET-53125|Gli intervalli denominati scompaiono dalla cartella di lavoro con attivazione macro quando vengono riaperti dopo il salvataggio|
|CELLSNET-53138|La tabella pivot non viene più visualizzata nelle connessioni ai report|
|CELLSNET-53157|Un collegamento interno tra i fogli in una cartella di lavoro non funziona durante la conversione di mht in excel|
|CELLSNET-53108|Si è verificata un'eccezione durante il caricamento di html|

##  **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

###  **Aggiunge la proprietà XlsbSaveOptions.LightCellsDataProvider**

Consente all'utente di salvare il file xlsb in modalità LightCell.

###  **Aggiunge i metodi Worksheet.CalculateArrayFormula(...).**

Consente all'utente di calcolare dinamicamente una formula come formula di matrice senza impostarla inizialmente su una cella.

###  **Aggiunge la proprietà CalculationOptions.CharacterEncoding**

Consente all'utente di specificare la codifica utilizzata per la codifica/decodifica dei caratteri durante il calcolo di formule come la funzione CHAR e CODE.

###  **Aggiunge lo spazio dei nomi Aspose.Cells.Drawing.Equations**

Consente agli utenti di completare la costruzione di una forma di equazione inserendo i nodi pertinenti passo dopo passo.

###  **Aggiunge le enumerazioni FileFormatType.XHtml e FileFormat.OneNote**

Rappresenta il tipo di formato file xhtml e One Note.

###  **Aggiunge il metodo FontConfigs.IsFontAvailable()**

Restituisce se il font è disponibile.

###  **Aggiunge la proprietà LoadOptions.IgnoreUselessShapes**

Indica se ignorare le forme inutili nei file xlsx.

###  **Aggiunge le proprietà PivotArea.OnlyData e OnlyLabel.**

Indica se selezionare solo i dati o l'etichetta per l'area pivot.

###  **Aggiunge l'enumerazione SaveFormat.XHtml.**

Rappresenta il formato di salvataggio.

###  **Aggiunge il metodo ListObject.PutCellFormula()**

Inserisce la formula nelle celle della tabella.

###  **Aggiunge la proprietà VbaProject.Encoding**

Ottiene e imposta la codifica del progetto VBA nei file Excel.

###  **Aggiunge la proprietà XmlSaveOptions.SheetNameAsElementName.**

Indica se salvare il nome del foglio come nome dell'elemento durante la conversione di dati excel in xml.

###  **Aggiunge la proprietà XmlSaveOptions.DataAsAttribute.**

Indica se salvare i dati come attributo del nodo durante la conversione di dati excel in dati xml.

