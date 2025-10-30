---
title: Unisci file con Golang via C++
linktitle: Unire file
type: docs
weight: 20
url: /it/go-cpp/merge-files/
description: Impara come unire file Excel in modo efficiente usando Aspose.Cells for C++.
---

## **Introduzione**

Aspose.Cells fornisce diversi metodi per unire file. Per file semplici con dati, formattazione e formule, si può usare il metodo [**Workbook.Combine()**](https://reference.aspose.com/cells/go-cpp/workbook/combine/) per combinare diversi libri di lavoro, e il metodo [**Worksheet.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/copy/) per copiare fogli di lavoro in un nuovo libro. Questi metodi sono facili da usare ed efficienti, ma se hai molti file da unire, potresti trovare che richiedono molte risorse di sistema. Per evitarlo, usa il metodo statico [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/), un modo più efficiente per unire diversi file.

## **Unire file utilizzando Aspose.Cells**

Il seguente esempio di codice illustra come unire grandi file usando il metodo [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/go-cpp/cellshelper/mergefiles/). Prende due file semplici ma grandi, Book1.xls e Book2.xls. I file contengono solo dati formattati e formule.

{{% alert color="primary" %}}

Il metodo [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/go-cpp/cellshelper/mergefiles/) supporta solo l'unione di dati, stili, formattazione e formule. Oggetti come grafici, immagini, commenti o altri oggetti potrebbero non essere uniti usando questo metodo. Inoltre, viene utilizzato un file cache per memorizzare dati temporanei per il processo.

{{% /alert %}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MergeFiles.go" >}}
