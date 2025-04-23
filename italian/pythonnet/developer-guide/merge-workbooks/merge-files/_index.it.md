---
title: Unire file
type: docs
weight: 20
url: /it/python-net/merge-files/
---

## **Introduzione**

Aspose.Cells for Python via .NET offre diversi modi per unire file. Per file semplici con dati, formattazione e formule, può essere usato il metodo [**Workbook.combine()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/combine) per combinare vari workbook, e il metodo [**Worksheet.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/copy) per copiare i fogli di lavoro in un nuovo workbook. Questi metodi sono facili da usare ed efficaci, ma se hai molti file da unire, potresti scoprire che consumano molte risorse di sistema. Per evitare questo, usa il metodo statico [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files), un modo più efficiente per unire diversi file.

## **Unisci file usando Aspose.Cells for Python via .NET**

Il seguente esempio di codice illustra come unire file di grandi dimensioni utilizzando il metodo [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files). Prende due file semplici ma di grandi dimensioni, Book1.xls e Book2.xls. I file contengono solo dati formattati e formule.

{{% alert color="primary" %}}

Il metodo [**CellsHelper.merge_files**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/merge_files) supporta solo la combinazione di dati, stili, formattazioni e formule. Gli oggetti come grafici, immagini, commenti o altri oggetti potrebbero non essere uniti utilizzando questo metodo. Inoltre, viene utilizzato un file memorizzato nella cache per memorizzare i dati temporanei per il processo.

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Merge-Workbooks-CellsHelperClass-MergeFiles-1.py" >}}

