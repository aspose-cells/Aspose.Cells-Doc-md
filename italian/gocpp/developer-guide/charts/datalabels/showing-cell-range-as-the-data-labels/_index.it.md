---
title: Mostra l intervallo di celle come etichette dati con Golang via C++
linktitle: Mostrare l intervallo di celle come etichette dati
description: Impara come mostrare un intervallo di celle come etichette dati nei grafici usando Aspose.Cells for C++. La nostra guida dimostrerà come collegare le etichette alla fonte dati e formattarle per fornire informazioni accurate e significative nei tuoi grafici.
keywords: Aspose.Cells for C++, tracciamento, etichette dati, intervallo di celle, fonte dati, formattazione, precisione, informazioni significative.
type: docs
weight: 130
url: /it/go-cpp/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}

In Microsoft Excel 2013, puoi visualizzare un intervallo di celle per le etichette dati. Aspose.Cells supporta questa funzionalità.

{{% /alert %}}

## **Casella di controllo per mostrare l'intervallo di celle come etichette dati**

Per mostrare l'intervallo di celle come etichette dati in Microsoft Excel:

1. Seleziona le etichette dati della serie e fai clic con il tasto destro per aprire il menu contestuale.
1. Seleziona **Formatta etichette dati**. Le opzioni di etichettatura vengono visualizzate.
1. Seleziona o deseleziona l'opzione **L'etichetta contiene - Valore dalle celle**.

Il codice di esempio qui sotto accede alle etichette dati di una serie del grafico e imposta la proprietà [**DataLabels.GetShowCellRange()**](https://reference.aspose.com/cells/go-cpp/datalabels/getshowcellrange/) su **true** per selezionare l'opzione **L'etichetta contiene - Valore dalle celle**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShowingCellRangeAsTheDataLabels.go" >}}
