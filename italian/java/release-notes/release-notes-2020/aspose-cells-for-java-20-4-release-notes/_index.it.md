---
title: Aspose.Cells for Java 20.4 Note di rilascio
type: docs
weight: 30
url: /it/java/aspose-cells-for-java-20-4-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 20.4](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.4/).

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43153|Visualizza la legenda del grafico a cascata in turco simile a MS Excel|Aumento|
|CELLSJAVA-43142|Rendering da Excel a HTML: alcune celle non sono allineate dopo la conversione|Insetto|
|CELLSJAVA-43155|Il testo ruotato viene impostato fuori dalla cella quando viene visualizzato come HTML|Insetto|
|CELLSJAVA-43161|Rappresentazione errata dell'equazione|Insetto|
|CELLSJAVA-43130|Problema di trasparenza del grafico a cascata|Insetto|
|CELLSJAVA-43131|Excel a PDF - Forme con testo non convertito correttamente|Insetto|
|CELLSJAVA-43133|Chart.toImage non include etichette di dati nell'immagine di output|Insetto|
|CELLSJAVA-43138|Immagine generata con problemi di rendering.|Insetto|
|CELLSJAVA-43151|Modifiche di stile dopo la conversione del file XLS|Insetto|
|CELLSJAVA-43158|IllegalArgumentException: Map size(0) deve essere >= 1|Eccezione|
|CELLSJAVA-43149|Eccezione sollevata durante il salvataggio di XLSM dopo la rimozione del foglio di lavoro|Eccezione|
|CELLSJAVA-43150|Eccezione "java.lang.NumberFormatException" al caricamento del file|Eccezione|
## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
### **Aggiunge la proprietà ChartTextFrame.DirectionType.**
Ottiene e imposta la direzione del testo nel grafico.
### **Aggiunge ChartTextFrame.ReadingOrder e rende obsoleta la proprietà ChartTextFrame.TextDirection.**
Usare invece la proprietà ChartTextFrame.ReadingOrder.
### **Aggiunge classi per la funzionalità avanzata di Revisioni.**
Ottiene le informazioni sulla revisione.
### **Modifica il valore predefinito della proprietà TxtSaveOptions.TrimLeadingBlankRowAndColumn.**
Per rendere il comportamento predefinito del salvataggio di CSV lo stesso con ms excel, abbiamo modificato il valore predefinito e il comportamento di questa proprietà. Per le vecchie versioni, il suo valore predefinito era "false". Dalla 20.4, il suo valore predefinito diventa "true".
### **Modifica il comportamento per il rilevamento di righe/colonne vuote per il salvataggio di CSV.**
Per le vecchie versioni, abbiamo preso quelle righe/colonne che non hanno dati ma hanno impostazioni personalizzate (visibilità, formattazione, ... ecc.) come vuote. Dalla 20.4 non li prendiamo più come vuoti, il nuovo comportamento è lo stesso con ms excel.
### **Aggiunge la proprietà TxtSaveOptions.ExportArea.**
Specifica l'intervallo di dati delle celle da esportare. Gli utenti possono utilizzare questa opzione per ottenere lo stesso risultato con le versioni precedenti per il comportamento modificato di TxtSaveOptions.TrimLeadingBlankRowAndColumn e righe/colonne vuote.
### **Aggiunge la classe UnionRange.**
Rappresenta l'intervallo di unione.
### **Elimina la proprietà DrawObject.Image obsoleta.**
Usare invece la proprietà DrawObject.ImageBytes.
### **Aggiunge la proprietà Bullet.FontName**
Ottiene e imposta il nome del carattere del punto elenco.
### **Aggiunge il metodo WorksheetCollection.CreateUnionRange().**
Crea un intervallo di unione.
### **Elimina l'enumerazione SaveType obsoleta.**
È inutilizzato.
### **Elimina le proprietà OleObject.ImageFormat e Picture.ImageFormat obsolete.**
Usare invece le proprietà OleObject.ImageType e Picture.ImageType.
