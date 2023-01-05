---
title: Aspose.Cells for Java 8.1.0 Note di rilascio
type: docs
weight: 50
url: /it/java/aspose-cells-for-java-8-1-0-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 8.1.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.1.0/)

{{% /alert %}} 

 Aspose.Cells for Java è stato aggiornato alla versione 8.1.0 e siamo lieti di annunciare che questa versione porta l'aggiunta di 10 nuovi utili miglioramenti.
Usando Aspose.Cells for Java puoi lavorare con XLS, SpreadsheetML, OOXML, XLSB, CSV, HTML, ODS, PDF, XPS e altri formati nelle tue applicazioni. Puoi anche generare, modificare, convertire, visualizzare e stampare cartelle di lavoro senza utilizzare Microsoft Excel.
Visita la documentazione per sapere come iniziare con Aspose.Cells for Java.
Nota che questo download contiene una versione completamente funzionante del prodotto, tuttavia senza un set di licenze funzionerà in modalità di valutazione con alcune limitazioni. Per testare Aspose.Cells senza queste limitazioni di valutazione è possibile richiedere una licenza temporanea gratuita di 30 giorni.
 Di seguito è riportato un elenco delle modifiche in questa versione di Aspose.Cells for Java.

Altri miglioramenti e modifiche

Miglioramenti

(CELLSJAVA-40823) - Limita API all'uso della directory dei caratteri specificata utilizzando il metodo CellsHelper.setFontDir
(CELLSJAVA-40716) - le linee del diagramma non sono nitide
(CELLSJAVA-40827) - Ottieni il colore del display definito nel formato numerico personalizzato

Insetti

(CELLSJAVA-40809) - Alcuni colori sono mostrati appena prima della colonna in una tabella
(CELLSJAVA-40814) - Le immagini mancano nel risultante PDF quando il foglio di calcolo viene convertito su Ubuntu
(CELLSJAVA-40826) - Nell'output HTML mancano le impostazioni della griglia e dei caratteri
(CELLSJAVA-40829) - Impossibile impostare la qualità di stampa dei fogli di lavoro
(CELLSJAVA-40838) - Le copie di stampa vengono conservate per il formato XLS ma non per il formato XLSX

Eccezioni

(CELLSJAVA-40739) - Salvataggio di Pivottable come mht
(CELLSJAVA-40531) - CellsException: la dimensione della mappa (0) deve essere >= 1


Pubblico API e modifiche incompatibili con le versioni precedenti

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

Proprietà obsolete BuiltInDocumentPropertyCollection.Bytes/Characters/CharactersWithSpaces/Lines/Paragraphs
Queste proprietà sono scritte per Word e PowerPoint, Excel le ometterà.

Aggiunge la proprietà Cell.StringValueWithoutFormat
Ottiene il valore della cella come stringa senza alcun formato.

Aggiunge la proprietà HtmlSaveOptions.ExportHiddenWorksheet
Indica se esportare il contenuto del foglio di lavoro nascosto durante il salvataggio del file html. Il valore predefinito è vero.

Nota
Poiché la base di codice di Aspose.Cells for Java corrisponde al codice della versione .NET pertinente, la maggior parte delle modifiche, miglioramenti e correzioni inclusi in Aspose.Cells for .NET v8.1.0 sono inclusi anche in questo Aspose.Cells for Java v8.1.0.
