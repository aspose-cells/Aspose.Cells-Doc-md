---
title: Lavorare con i formati di visualizzazione dei dati del campo dati nella tabella pivot
type: docs
weight: 150
url: /it/java/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

Aspose.Cells supporta tutti i formati di visualizzazione dei dati del DataField.

{{% /alert %}}

## **Opzione di formato di visualizzazione "Classifica dal più piccolo al più grande" e "Classifica dal più grande al più piccolo"**

Aspose.Cells fornisce la possibilità di impostare l'opzione di formato di visualizzazione per i campi pivot. A tal scopo, l'API fornisce la proprietà [**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat). Per classificare dal più grande al più piccolo, è possibile impostare la proprietà [**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat) su [**PivotFieldDataDisplayFormat.RANK_LARGEST_TO_SMALLEST**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfielddatadisplayformat#RANK-LARGEST-TO-SMALLEST). Il seguente snippet di codice illustra come impostare le opzioni di formato di visualizzazione.

Il file di origine e i file di output di esempio possono essere scaricati da qui per testare il codice di esempio.

[File Excel di origine](PivotTableSample.xlsx)

[File Excel di output](PivotTableDataDisplayFormatRanking_out.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-PivotTableDataDisplayFormatRanking-1.java" >}}
{{< app/cells/assistant language="java" >}}
