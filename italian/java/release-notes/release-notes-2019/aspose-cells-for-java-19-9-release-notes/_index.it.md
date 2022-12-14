---
title: Aspose.Cells for Java 19.9 Note di rilascio
type: docs
weight: 40
url: /it/java/aspose-cells-for-java-19-9-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Java 19.9.

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42990|Le righe nascoste vengono visualizzate durante la conversione del file Excel in HTML quando esiste il filtro automatico|Insetto|
|CELLSJAVA-42997|CalculateFormula() ha esito negativo con stringhe di formule di grandi dimensioni|Insetto|
|CELLSJAVA-43000|CalculateFormula() corrompe il file Excel|Insetto|
|CELLSJAVA-42987|Problemi di formattazione durante la conversione di file Excel in PDF|Insetto|
|CELLSJAVA-42986|Sovrapposizione di testo dopo la conversione del file XLSX cinese in PDF|Insetto|
|CELLSJAVA-43012|Workbook.setRecalculateOnOpen(false) non funziona per le versioni di Excel più recenti|Insetto|
|CELLSJAVA-42996|Le etichette dati basate su formule non vengono visualizzate correttamente in PDF|Insetto|
|CELLSJAVA-42992|Eccezione sollevata durante la conversione di XLSM in immagine|Eccezione|
|CELLSJAVA-42991|Eccezione "La larghezza della colonna deve essere compresa tra 0 e 255" durante la conversione di Excel in PDF in macOS|Eccezione|
|CELLSJAVA-43004|Eccezione java.lang.NumberFormatException: per la stringa di input: "0.0" durante la conversione di Excel in HTML|Eccezione|
|CELLSJAVA-43010|IllegalArgumentException durante l'esecuzione di deleteBlankColumns()|Eccezione|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
### **Rimuove la proprietà Chart.Rotation obsoleta**
Usare invece la proprietà Chart.RotationAngle.
### **Rimuove la proprietà Chart.IsDataTableShown obsoleta**
Usare invece la proprietà Chart.ShowDataTable.
### **Rimuove la proprietà Chart.IsLegendShown obsoleta**
Usare invece la proprietà Chart.ShowLegend.
### **Rimuove la proprietà obsoleta Axis.Crosses**
Utilizzare invece la proprietà Axis.Crosses.
### **Aggiunge le proprietà enum OoxmlCompressionType e XlsbSaveOptions.CompressionType,OoxmlSaveOptions.CompressionType.**
Rappresenta il tipo di compressione per i file OOXML.
