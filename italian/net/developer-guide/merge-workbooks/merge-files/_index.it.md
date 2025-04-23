---
title: Unire file
type: docs
weight: 20
url: /it/net/merge-files/
---

## **Introduzione**

Aspose.Cells fornisce diverse modalità per unire i file. Per file semplici con dati, formattazione e formule, può essere utilizzato il metodo [**Workbook.Combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine) per combinare diversi diari di lavoro e il metodo [**Worksheet.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/copy/index) per copiare i fogli di lavoro in un nuovo diario di lavoro. Questi metodi sono facili da usare ed efficaci, ma se hai molti file da unire, potresti scoprire che richiedono molte risorse di sistema. Per evitare ciò, utilizza il metodo statico [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles), un modo più efficiente per unire diversi file.

## **Unire file utilizzando Aspose.Cells**

Il seguente esempio di codice illustra come unire file di grandi dimensioni utilizzando il metodo [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles). Prende due file semplici ma di grandi dimensioni, Book1.xls e Book2.xls. I file contengono solo dati formattati e formule.

{{% alert color="primary" %}}

Il metodo [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/methods/mergefiles) supporta solo la combinazione di dati, stili, formattazioni e formule. Gli oggetti come grafici, immagini, commenti o altri oggetti potrebbero non essere uniti utilizzando questo metodo. Inoltre, viene utilizzato un file memorizzato nella cache per memorizzare i dati temporanei per il processo.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-MergeFiles-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
