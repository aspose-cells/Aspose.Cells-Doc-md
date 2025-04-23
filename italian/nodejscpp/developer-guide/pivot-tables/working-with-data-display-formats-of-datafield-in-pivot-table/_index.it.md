---
title: Lavorare con i formati di visualizzazione dei dati del campo dati nella tabella pivot
type: docs
weight: 140
url: /it/nodejs-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ supporta tutti i formati di visualizzazione dei dati di DataField.

{{% /alert %}}

## **Opzione di formato di visualizzazione "Classifica dal più piccolo al più grande" e "Classifica dal più grande al più piccolo"**

Aspose.Cells fornisce la possibilità di impostare l'opzione di formato di visualizzazione per i campi pivot. A questo scopo, l'API fornisce la proprietà [**PivotShowValuesSetting.setCalculationType**](https://reference.aspose.com/cells/nodejs-cpp/pivotshowvaluessetting/#setCalculationType-pivotfielddatadisplayformat-). Per classificare dal più grande al più piccolo, è possibile impostare la proprietà [**PivotShowValuesSetting.setCalculationType**](https://reference.aspose.com/cells/nodejs-cpp/pivotshowvaluessetting/#setCalculationType-pivotfielddatadisplayformat-) a [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/nodejs-cpp/pivotfielddatadisplayformat/). Il seguente frammento di codice dimostra come impostare le opzioni di formato di visualizzazione.

Il file di origine e i file di output di esempio possono essere scaricati da qui per testare il codice di esempio.

[File Excel di origine](101089332.xlsx)

[File Excel di output](101089333.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-PivotTableDataDisplayFormatRanking-1.js" >}}

