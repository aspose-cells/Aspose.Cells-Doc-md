---
title: Aspose.Cells for PHP via Java 23.4 Note di rilascio
type: docs
weight: 9
url: /it/php-java/aspose-cells-for-php-via-java-23-4-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for PHP via Java 23.4](https://downloads.aspose.com/cells/php/new-releases/aspose.cells-for-php-via-java-23.4/).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
| :- | :- | :- |
|CELLSJAVA-45255|Visualizza il testo dall'alto verso il basso con la "modalità di scrittura" CSS|
|CELLSJAVA-45227|Aspose.Cells si blocca salvando il file come XLSB|
|CELLSJAVA-45241|Il risultato calcolato di MIRR non è corretto|
|CELLSJAVA-45296|Aspose Cells non ricalcola la formula per alcuni valori|
|CELLSJAVA-45223|Dal grafico all'immagine: l'altezza dei caratteri e della legenda non è visualizzata correttamente|
|CELLSJAVA-45257| Le scale del grafico mancano nel rendering da Excel a PDF|
|CELLSJAVA-45054|impossibile cambiare foglio di lavoro per il file specificato dal cliente|
|CELLSJAVA-45229|impossibile caricare il file in GridWeb per il file test.xlsx|
|CELLSJAVA-45231|setRowHeightForCSV non ha effetto dopo aver cambiato foglio di lavoro, l'altezza della riga del file csv è ancora piccola|
|CELLSJAVA-45251|Dopo aver regolato la larghezza della colonna, anche la posizione del pulsante del filtro deve essere regolata in posizione|
|CELLSJAVA-45082|Il riempimento della linea ondulata è diverso dopo aver salvato il file in pdf|
|CELLSJAVA-45237|Errore di visualizzazione della formula durante il salvataggio del file in SVG|
|CELLSJAVA-45236|Errore di posizione della riga durante il salvataggio del file in SVG|
|CELLSJAVA-45252|Rimozione errata delle pagine durante la conversione da Excel a PDF quando si utilizza l'opzione PrintingPageType.IGNORE_BLANK|
|CELLSJAVA-45273|Alcuni testi non sono visibili durante la conversione in svg|
|CELLSJAVA-45266|Cell errore di localizzazione del contenuto durante la conversione in html|
|CELLSJAVA-45279|Quando si esporta il file in HTML, viene visualizzato uno spazio vuoto aggiuntivo|
|CELLSJAVA-45248| HTML in Excel: non è possibile mantenere il formato multiplo contemporaneamente|
|CELLSJAVA-45304|Il grafico non è presente nei grafici a barre durante la conversione di xlsx in ods|
|CELLSJAVA-45305|La forma del sole viene convertita in una forma rettangolare quando si converte ods in xlsx|
|CELLSJAVA-45308|I valori Cell non sono visibili per le celle con cross-sheet durante la conversione di xlsx in od|
|CELLSJAVA-45259|Perdita di dati durante la conversione di HTML con elenchi in XLSX|
|CELLSJAVA-45260|HTML a XLSX: Allineamento non mantenuto|
|CELLSJAVA-45271| Il file dei risultati ha un uid diverso quando si salva una cartella di lavoro due volte|
|CELLSJAVA-45283|La selezione PivotArea supporta altri tipi di campi pivot rispetto a PivotFieldType.Data|
|CELLSJAVA-45298|I colori dei grafici a torta devono essere mantenuti durante la conversione di xlsx in ods|
|CELLSJAVA-45309|L'angolo della prima fetta del grafico a torta non è corretto quando si converte excel in ods|
|CELLSJAVA-45310|Aggiungere il formato OneNote a FileFormatUtil API per rilevare FileFormatType|

##  **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

###  **Aggiunge la proprietà XlsbSaveOptions.LightCellsDataProvider**

Consente all'utente di salvare il file xlsb in modalità LightCell.

###  **Aggiunge i metodi Worksheet.CalculateArrayFormula(...).**

Consente all'utente di calcolare dinamicamente una formula come formula di matrice senza impostarla inizialmente su una cella.

###  **Aggiunge la proprietà CalculationOptions.CharacterEncoding**

Consente all'utente di specificare la codifica utilizzata per la codifica/decodifica dei caratteri durante il calcolo di formule come la funzione CHAR e CODE.

###  **Aggiunge la classe EquationNode e le sue classi derivate**

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
