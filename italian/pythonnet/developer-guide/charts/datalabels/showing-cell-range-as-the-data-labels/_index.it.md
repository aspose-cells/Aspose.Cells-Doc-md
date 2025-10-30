---
title: Mostrare l intervallo di celle come etichette dati
description: Impara come mostrare un intervallo di celle come etichette dei dati nei grafici usando Aspose.Cells per Python via .NET. La nostra guida dimostrerà come collegare le etichette alla tua fonte di dati e formattarle per fornire informazioni accurate e significative nei tuoi grafici.
keywords: Aspose.Cells per Python via .NET, creazione di grafici, etichette dei dati, intervallo di celle, fonte dei dati, formattazione, precisione, informazioni significative.
type: docs
weight: 130
url: /it/python-net/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}

In Microsoft Excel 2013, puoi mostrare un intervallo di celle per le etichette dei dati. Aspose.Cells per Python via .NET supporta questa funzione.

{{% /alert %}}

## **Casella di controllo per mostrare l'intervallo di celle come etichette dati**

Per mostrare l'intervallo di celle come etichette dati in Microsoft Excel:

1. Seleziona le etichette dati della serie e fai clic con il tasto destro per aprire il menu contestuale.
1. Seleziona **Formatta etichette dati**. Le opzioni di etichettatura vengono visualizzate.
1. Seleziona o deseleziona l'opzione **L'etichetta contiene - Valore dalle celle**.

Il codice di esempio qui sotto accede alle etichette dati di una serie del grafico e imposta la proprietà [**DataLabels.show_cell_range**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/datalabels/show_cell_range) su **true** per selezionare l'opzione **L'etichetta contiene - Valore dalle celle**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ShowCellRangeAsDataLabels.py" >}}
{{< app/cells/assistant language="python-net" >}}
