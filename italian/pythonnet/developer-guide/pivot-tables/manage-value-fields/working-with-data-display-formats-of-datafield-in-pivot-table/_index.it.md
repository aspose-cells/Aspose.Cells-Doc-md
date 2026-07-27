---
title: Lavorare con i formati di visualizzazione dei dati del campo dati nella tabella pivot
type: docs
weight: 140
url: /it/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/
description: Come lavorare con i formati di visualizzazione dei dati del campo dati nella tabella pivot con Aspose.Cells per Python via .NET.
keywords: Aspose.Cells per Excel Python, libreria Python Excel, Lavorare con i formati di visualizzazione dei dati del campo dati nella tabella pivot.
---

{{% alert color="primary" %}}

Aspose.Cells per Python via .NET supporta tutti i formati di visualizzazione dei dati del campo dati.

{{% /alert %}}

## **Come impostare l'opzione di formato di visualizzazione "Rank dal più piccolo al più grande" e "Rank dal più grande al più piccolo"**

Aspose.Cells for Python via .NET fornisce la possibilità di impostare l'opzione di formato di visualizzazione per i campi pivot. A questo scopo, l'API fornisce la proprietà [**PivotField.data_display_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/data_display_format/). Per classificare dal più grande al più piccolo, è possibile impostare la proprietà [**PivotField.data_display_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/data_display_format/) su [**PivotFieldDataDisplayFormat.RANK_LARGEST_TO_SMALLEST**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfielddatadisplayformat/). Il seguente frammento di codice dimostra come impostare le opzioni di formato di visualizzazione.

Il file di origine e i file di output di esempio possono essere scaricati da qui per testare il codice di esempio.

[File Excel di origine](101089332.xlsx)

[File Excel di output](101089333.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTableDataDisplayFormatRanking-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
