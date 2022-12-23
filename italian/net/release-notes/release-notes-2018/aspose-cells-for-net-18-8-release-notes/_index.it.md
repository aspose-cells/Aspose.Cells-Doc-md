---
title: Aspose.Cells for .NET 18.8 Note di rilascio
type: docs
weight: 50
url: /it/net/aspose-cells-for-net-18-8-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 18.8](https://www.nuget.org/packages/Aspose.Cells/18.8.0).

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSNET-42992|Applica l'allineamento del testo al testo parziale all'interno di TextBox|Nuova caratteristica|
|CELLSNET-44155|Connessioni di lettura/scrittura del file XLSB|Nuova caratteristica|
|CELLSNET-46123|Supporta l'analisi delle formule dei registri di revisione nell'array binario|Nuova caratteristica|
|CELLSNET-46220|Imposta l'opzione ContentCopyForAccessibility durante la conversione del foglio di calcolo nel formato file PDF|Nuova caratteristica|
|CELLSNET-43560|Crittografare un file ODS|Nuova caratteristica|
|CELLSNET-43556|Apri il file ODS crittografato|Nuova caratteristica|
|CELLSNET-46209|Supporta la lettura e la scrittura DConn del file XLS|Nuova caratteristica|
|CELLSNET-43326|Aggiungi overload a CopyRows e CopyColumns con le opzioni Incolla speciale|Nuova caratteristica|
|CELLSNET-41637|Recupera le impostazioni dei totali parziali|Nuova caratteristica|
|CELLSNET-46252|Argomento per saltare riga/righe come intestazioni di dati nell'esportazione dell'intervallo in datatable|Aumento|
|CELLSNET-46226|Le annotazioni a penna diventano immagini normali dopo la conversione|Aumento|
|CELLSNET-41693|È incluso il miglioramento delle colonne di adattamento automatico|Aumento|
|CELLSNET-46263|L'applicazione si blocca durante la conversione da XLS a PDF|Prestazione|
|CELLSNET-46262|Cell lo sfondo è errato quando l'orientamento del testo della cella è inclinato nell'output PDF|Insetto|
|CELLSNET-44761|Il testo in una forma non è stato visualizzato correttamente in PDF|Insetto|
|CELLSNET-43916|Manca l'ombreggiatura della forma durante la conversione del foglio di calcolo in HTML|Insetto|
|CELLSNET-46251|L'applicazione si blocca durante la conversione da XLSX a HTML|Insetto|
|CELLSNET-46241|Problema con le multilinee in HTML|Insetto|
|CELLSNET-46219|La larghezza dal tag HTML non viene seguita durante la conversione da HTML a XLSX|Insetto|
|CELLSNET-46280|Eccezione sollevata durante l'importazione dei dati nel file Excel con SmartMarkers|Insetto|
|CELLSNET-46267|Problema con i dati che filtrano le prime righe|Insetto|
|CELLSNET-46264|La proprietà R1C1Formula ha cambiato il suo comportamento|Insetto|
|CELLSNET-46258|Problema di calcolo della formula di matrice VLOOKUP inversa|Insetto|
|CELLSNET-46197|Problema di convalida dei dati: se l'inserimento di un valore errato e il clic su un'altra cella non ripristinano automaticamente la cella di convalida al valore precedente|Insetto|
|CELLSNET-46276|Conversione da Excel a PDF: viene aggiunta una pagina vuota|Insetto|
|CELLSNET-46275|Grande PDF creato da XLS|Insetto|
|CELLSNET-46259|La conversione di Excel in PDF aggiunge una linea retta|Insetto|
|CELLSNET-46255|Problema del numero di pagina (nel piè di pagina) in Excel per il rendering PDF|Insetto|
|CELLSNET-46238|Caricamento del file crittografato ODS non riuscito|Insetto|
|CELLSNET-46231|Il testo nelle celle della colonna A non viene visualizzato correttamente nell'output PDF|Insetto|
|CELLSNET-46165|Aspose.Cells smette di rispondere quando si tenta di convertire un file Excel nel formato di file PDF|Insetto|
|CELLSNET-46236|File MS Excel danneggiato dopo l'anonimizzazione|Insetto|
|CELLSNET-45192|Il file XLS salvato viene mostrato in visualizzazione protetta|Insetto|
|CELLSNET-46235|L'immagine non può essere visualizzata durante il salvataggio nel formato XLS|Insetto|
|CELLSNET-46225|Gestione del ritorno a capo con virgolette doppie|Insetto|
|CELLSNET-46218|Dopo aver eseguito AutoFitColumns, le parole della colonna non sono ancora completamente rese|Insetto|
|CELLSNET-46139|Workbook.DataConnections non mostra le informazioni di connessione del file XLS|Insetto|
|CELLSNET-46042|Le barre vengono convertite in barre rovesciate dopo aver modificato i collegamenti esterni|Insetto|
|CELLSNET-45377|Connessioni dati non trovate nel documento XLS|Insetto|
|CELLSNET-44487|La connessione dati viene persa durante la conversione da XLT a XLSM|Insetto|
|CELLSNET-44486|La connessione dati viene persa durante la conversione da XLS a XLSM|Insetto|
|CELLSNET-43563|I grafici vengono persi quando XLSX viene convertito in ODS|Insetto|
|CELLSNET-41002|L'equazione scompare durante la conversione del formato (XLSX -> XLS)|Insetto|
|CELLSNET-46277|Eccezione durante il calcolo delle formule|Eccezione|
|CELLSNET-46249|L'eccezione viene generata durante la lettura del file HTML|Eccezione|
|CELLSNET-46246|L'eccezione viene generata durante l'aggiunta della firma digitale sul server della piattaforma cloud di GroupDocs|Eccezione|
|CELLSNET-46232|Eccezione nome cella non valido durante il caricamento del file XLSX|Eccezione|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Aggiunge la proprietà PdfSecurityOptions.AccessibilityExtractContent**
Autorizzazione a copiare o estrarre contenuti (a supporto dell'accessibilità agli utenti disabili o per altri scopi).
#### **Aggiunge il costruttore DigitalSignature(System.Byte[],System.String,System.String,System.DateTime)**
Costruttore di firma digitale.
#### **Aggiunge la classe SubtotalSetting**
Rappresenta l'impostazione del subtotale.
#### **Aggiunge il metodo Cells.RetrieveSubtotalSetting(CellArea)**
Recupera l'impostazione del subtotale.
#### **Aggiunge il metodo di sovraccarico Range.ExportDataTable(Aspose.Cells.ExportTableOptions).**
Supporta le opzioni di esportazione dell'intervallo.
#### **Aggiunge la proprietà WebQueryConnection.IsSameSetting ed elimina la proprietà WebQueryConnection.IsFirstRow**
Utilizzare invece la proprietà WebQueryConnection.IsSameSetting.
#### **Aggiunge la proprietà WebQueryConnection.IsXmlSourceData ed elimina la proprietà WebQueryConnection.IsSourceData**
Utilizzare invece la proprietà WebQueryConnection.IsXmlSourceData.
#### **Aggiunge la proprietà Shape.IsEquation**
Indica se la forma contiene un'equazione.
#### **Aggiunge l'overload Cells.CopyColumns(Int32,Int32,PasteOptions) e il metodo Cels.CopyRows(Int32,Int32,PasteOptions)**
Supporta le opzioni di incolla durante la copia di righe e colonne.
#### **Aggiunge la proprietà Axis.IsAutoTickLabelSpacing**
Indica se la spaziatura dell'etichetta del segno di spunta è automatica.
