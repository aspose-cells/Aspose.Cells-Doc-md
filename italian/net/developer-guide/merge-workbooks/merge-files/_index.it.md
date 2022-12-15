---
title: Unisci file
type: docs
weight: 20
url: /it/net/merge-files/
---
## **introduzione**

 Aspose.Cells offre diversi modi per unire i file. Per file semplici con dati, formattazione e formule, il file[**Cartella di lavoro.Combina()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine) metodo può essere utilizzato per combinare più cartelle di lavoro e il file[**Foglio di lavoro.Copia()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index)metodo può essere utilizzato per copiare i fogli di lavoro in una nuova cartella di lavoro. Questi metodi sono facili da usare ed efficaci, ma se hai molti file da unire, potresti scoprire che richiedono molte risorse di sistema. Per evitare ciò, utilizzare il[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)metodo statico, un modo più efficiente per unire più file.

## **Unisci file utilizzando Aspose.Cells**

 Il codice di esempio seguente illustra come unire file di grandi dimensioni utilizzando l'estensione[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)metodo. Richiede due file semplici ma di grandi dimensioni, Book1.xls e Book2.xls. I file contengono solo dati formattati e formule.

{{% alert color="primary" %}}

 Il[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles)Il metodo supporta solo l'unione di dati, stili, formattazione e formule. Oggetti come grafici, immagini, commenti o altri oggetti potrebbero non essere uniti utilizzando questo metodo. Inoltre, un file memorizzato nella cache viene utilizzato per archiviare dati temporanei per il processo.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-MergeFiles-1.cs" >}}
