---
title: Lavorare con i formati di visualizzazione dei dati di DataField nella tabella pivot con Golang tramite C++
linktitle: Lavorare con i formati di visualizzazione dei dati di DataField nella Pivot Table
type: docs
weight: 140
url: /it/go-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
description: Impara come lavorare con i formati di visualizzazione dei dati di DataField nella Pivot Table usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells supporta tutti i formati di visualizzazione dei dati del DataField.

{{% /alert %}}

## **Opzione di visualizzazione "Classifica dal più piccolo al più grande" e "Classifica dal più grande al più piccolo"**

Aspose.Cells consente di impostare l'opzione di formato di visualizzazione per i campi pivot. Per questo, l'API fornisce la proprietà [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/go-cpp/pivotshowvaluessetting/getcalculationtype/). Per ordinare dal più grande al più piccolo, puoi impostare la proprietà [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/go-cpp/pivotshowvaluessetting/getcalculationtype/) su [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfielddatadisplayformat/). Il seguente frammento di codice mostra come impostare le opzioni di formato di visualizzazione.

Il file di origine e i file di output di esempio possono essere scaricati da qui per testare il codice di esempio.

[File Excel di origine](101089332.xlsx)

[File Excel di output](101089333.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithDataDisplayFormatsOfDatafieldInPivotTable.go" >}}
