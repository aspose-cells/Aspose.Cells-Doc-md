---
title: Aspose.Cells for Java 19.6 Note di rilascio
type: docs
weight: 70
url: /it/java/aspose-cells-for-java-19-6-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Java 19.6.

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42914|I formati condizionali di grandi dimensioni causano un'eccezione OOM|Aumento|
|CELLSJAVA-42916|Problema relativo al formato dei dati dopo Workbook.save()|Aumento|
|CELLSJAVA-42930|Errore di caricamento di Excel95|Aumento|
|CELLSJAVA-42927|Il file salvato si apre lentamente in Excel dopo aver eliminato le colonne|Aumento|
|CELLSJAVA-42932|Errore di formattazione condizionale con il metodo Style.getDisplayStyle|Insetto|
|CELLSJAVA-42928|Alcune righe non si riflettono nella conversione da XLSX a PDF|Insetto|
|CELLSJAVA-42904|L'immagine dell'intestazione sembra corrompere il file|Insetto|
|CELLSJAVA-42907|Filtro perso dopo aver salvato la cartella di lavoro|Insetto|
|CELLSJAVA-42915|I filtri vengono modificati dopo aver aggiunto un foglio alla cartella di lavoro|Insetto|
|CELLSJAVA-42918|Grafico del file convertito appiattito (conversione da XLS a XLSX)|Insetto|
|CELLSJAVA-42938|Il caricamento del file XLSX interrompe l'applicazione|Insetto|
|CELLSJAVA-42859|CellsException per il caricamento del nome dal file ODS|Eccezione|
|CELLSJAVA-42908|Eccezione durante la chiamata a Name.getRefersTo()|Eccezione|
|CELLSJAVA-42926|IllegalStateException durante il caricamento della cartella di lavoro|Eccezione|

## **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.
### **Aggiunge enum FileFormatType.FODS,FileFormatType.SXC,LoadFormat.FODS,LoadFormat.SXC,SaveFormat.FODS e SaveFormat.SXC**
Rappresenta i tipi di formato file .FODS e .SXC.
### **Aggiunge enum WarningType.UnsupportedFileFormat**
Rappresenta il formato di file non supportato per i tipi di avviso.
### **Aggiunge enum ODSGeneratorType**
Rappresenta il tipo di generatore di od.
### **OoxmlSaveOptions.EmbedOoxmlAsOleObject**
Indica se incorporare il file OOXML come OleObject.
### **Aggiunge Row.CopySettings(Aspose.Cells.Row,System.Boolean)**
Copia le impostazioni della riga, come stile, altezza, visibilità, ...ecc.
