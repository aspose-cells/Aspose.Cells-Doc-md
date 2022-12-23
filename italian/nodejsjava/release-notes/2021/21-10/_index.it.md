---
title: Aspose.Cells for Node.js via Java 21.10 Note di rilascio
type: docs
weight: 3
url: /it/nodejs-java/aspose-cells-for-node-js-via-java-21-10-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Node.js via Java 21.10](https://downloads.aspose.com/cells/nodejs/new-releases/aspose.cells-for-node.js-via-java-21.10/).

{{% /alert %}}

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-43768|Java Viene osservato un problema di spazio nell'heap durante la conversione del file XLSX in PDF|
|CELLSJAVA-43875|Eccezione "Invalid FontUnderlineType string val" durante il caricamento del file XLSX|
|CELLSJAVA-43876|Eccezione "java.lang.ArrayIndexOutOfBoundsException" al caricamento di un file XLSX|
|CELLSJAVA-43646|L'effetto ombra del testo non è reso correttamente|
|CELLSJAVA-43760|L'orientamento del triangolo isoscele non è corretto|
|CELLSJAVA-43786|Durante la conversione del file XLS in XLSX, alcune parti relative alle forme non vengono visualizzate correttamente|
|CELLSJAVA-43838|Dopo l'esecuzione di XlsToXlsx, la forma si perde|
|CELLSJAVA-43839|Dopo l'esecuzione di XlsToXlsx, LeftBracket viene perso|
|CELLSJAVA-43842|Dopo aver eseguito XlsToXlsx, la forma di LeftBracket è diversa dall'originale|
|CELLSJAVA-43848|Conversione da Excel a PDF: alcuni caratteri WordArt non vengono racchiusi nello stesso modo del file Excel|
|CELLSJAVA-43880|Angoli arrotondati errati della casella di testo dopo la conversione da xls a xlsx|
|CELLSJAVA-43867|L'icona del formato condizionale è diversa quando si esporta in html|
|CELLSJAVA-43812|excelToHtml: l'offset della posizione della forma non è corretto|
|CELLSJAVA-43871|Prisma 9 Oggetti OLE non visualizzati sull'output PDF|
|CELLSJAVA-43883|Dimensioni della pagina visualizzate errate|
|CELLSJAVA-43881|L'unione dei file causa la mancanza dell'impostazione del colore di sfondo dei fogli|
|CELLSJAVA-43892|Mancano i bordi di Excel convertiti in HTML|
|CELLSJAVA-43787|Eccezione "IllegalArgumentException: lunghezza trattino tutto zero ..." in Excel per il rendering HTML|
|CELLSJAVA-43885|IllegalArgumentException durante la conversione di excel|
|CELLSJAVA-43874|Workbook.save genera un'eccezione su un file specifico entro Aspose.Cells solo quando viene applicata la licenza Aspose|

## **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

### **Aggiunge il metodo di overload Name.GetRefersTo().**

Ottiene l'espressione della formula basata sulla cella specificata.

### **Aggiunge il metodo di overload Range.AutoFill().**

Riempi automaticamente l'intervallo target con il tipo di riempimento.

### **Aggiunge la proprietà Comment.IsThreadedComment.**

Indica se questo commento è un commento con thread.

### **Aggiunge la proprietà HtmlSaveOptions.IgnoreInvisibleShapes.**

Indica se inserire forme invisibili durante il salvataggio di html.

### **Aggiunge la proprietà Range.CurrentRegion.**

Restituisce un intervallo delimitato da qualsiasi combinazione di righe e colonne vuote.

### **Aggiunge la classe AxisBins.**

 Rappresenta i contenitori degli assi per i grafici a istogramma.

### **Metodo obsoleto SheetRender.GetPageSize(int pageIndex)**

Usare invece SheetRender.GetPageSizeInch(int pageIndex).

### **Aggiunge il metodo SheetRender.GetPageSizeInch(int pageIndex)**

Ottieni la dimensione della pagina dell'immagine di output? in unità di pollice.

### **Aggiunge il metodo WorkbookRender.GetPageSizeInch(int pageIndex)**

Ottieni l'immagine di output delle dimensioni della pagina? in unità di pollici.

