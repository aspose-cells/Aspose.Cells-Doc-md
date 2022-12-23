---
title: Utilizzo dei formati di visualizzazione dei dati di DataField nella tabella pivot
type: docs
weight: 150
url: /it/java/working-with-data-display-formats-of-datafield-in-pivot-table/
---
{{% alert color="primary" %}}

Aspose.Cells supporta tutti i formati di visualizzazione dei dati di DataField.

{{% /alert %}}

## **Opzione del formato di visualizzazione "Classifica dal più piccolo al più grande" e "Classifica dal più grande al più piccolo".**

Aspose.Cells offre la possibilità di impostare l'opzione del formato di visualizzazione per i campi pivot. Per questo, lo API fornisce il[**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat) proprietà. Per classificare dal più grande al più piccolo, puoi impostare il[**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat)proprietà a[**PivotFieldDataDisplayFormat.RANK_LARGEST_TO_SMALLEST**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfielddatadisplayformat#RANK_LARGEST_TO_SMALLEST). Il seguente frammento di codice illustra l'impostazione delle opzioni del formato di visualizzazione.

I file sorgente e di output di esempio possono essere scaricati da qui per testare il codice di esempio:

[File Excel di origine](PivotTableSample.xlsx)

[File Excel di output](PivotTableDataDisplayFormatRanking_out.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-PivotTableDataDisplayFormatRanking-1.java" >}}
