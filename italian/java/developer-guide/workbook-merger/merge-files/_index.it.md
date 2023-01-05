---
title: Unisci file
type: docs
weight: 10
url: /it/java/merge-files/
---
## **introduzione**

 Aspose.Cells offre diversi modi per unire i file. Per file semplici con dati, formattazione e formule, il file[**Cartella di lavoro.combina()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#combine(com.aspose.cells.Workbook) può essere utilizzato per combinare più cartelle di lavoro e il metodo[**Foglio di lavoro.copia(**)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#copy(com.aspose.cells.Worksheet)) può essere utilizzato per copiare i fogli di lavoro in una nuova cartella di lavoro. Questi metodi sono facili da usare ed efficaci, ma se hai molti file da unire, potresti scoprire che richiedono molte risorse di sistema. Per evitare ciò, utilizzare il metodo statico CellsHelper.mergeFiles, un modo più efficiente per unire più file.

## **Unisci file utilizzando Aspose.Cells**

Il codice di esempio seguente illustra come unire file di grandi dimensioni utilizzando il metodo CellsHelper.mergeFiles. Richiede due file semplici ma di grandi dimensioni, MyBook1.xls e MyBook2.xls. I file contengono solo dati formattati e formule.

{{% alert color="primary" %}}

Il metodo CellsHelper.mergeFiles supporta solo l'unione di dati, stili, formattazione e formule. Oggetti come grafici, immagini, commenti o altri oggetti potrebbero non essere uniti utilizzando questo metodo. Inoltre, un file memorizzato nella cache viene utilizzato per archiviare dati temporanei per il processo.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-MergeFiles-MergeFiles.java" >}}
