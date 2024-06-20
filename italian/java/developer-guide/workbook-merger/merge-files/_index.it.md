---
title: Unire file
type: docs
weight: 10
url: /it/java/merge-files/
---

## **Introduzione**

Aspose.Cells fornisce modi diversi per unire file. Per file semplici con dati, formattazione e formule, è possibile utilizzare il metodo [**Workbook.combine()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#combine(com.aspose.cells.Workbook)) per combinare diversi fogli di lavoro, e il metodo [**Worksheet.copy(**)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)) può essere utilizzato per copiare i fogli di lavoro in una nuova cartella di lavoro. Questi metodi sono facili da usare ed efficaci, ma se hai molti file da unire, potresti scoprire che richiedono molte risorse di sistema. Per evitare ciò, utilizza il metodo statico CellsHelper.mergeFiles, un modo più efficiente per unergi file vari.

## **Unire file utilizzando Aspose.Cells**

Il seguente codice di esempio illustra come unire file di grandi dimensioni utilizzando il metodo CellsHelper.mergeFiles. Prende due file semplici ma di grandi dimensioni, MyBook1.xls e MyBook2.xls. I file contengono solo dati formattati e formule.

{{% alert color="primary" %}}

Il metodo CellsHelper.mergeFiles supporta solo l'unione di dati, stili, formattazione e formule. Gli oggetti come grafici, immagini, commenti o altri oggetti potrebbero non essere uniti utilizzando questo metodo. Inoltre, viene utilizzato un file in cache per memorizzare dati temporanei per il processo.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-MergeFiles-MergeFiles.java" >}}
