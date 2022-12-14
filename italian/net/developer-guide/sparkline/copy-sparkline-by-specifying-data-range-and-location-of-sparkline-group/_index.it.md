---
title: Copia sparkline specificando l'intervallo di dati e la posizione del gruppo sparkline
type: docs
weight: 300
url: /it/net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---
{{% alert color="primary" %}}

Microsoft Excel consente di copiare un grafico sparkline specificando l'intervallo di dati e la posizione di un gruppo di grafici sparkline. Aspose.Cells supporta questa funzione.

{{% /alert %}}

Per copiare un grafico sparkline in altre celle in Microsoft Excel:

1. Selezionare la cella contenente il grafico sparkline.
1.  Selezionare**Modifica dati** dal**Scintilla** sezione del**Disegno** scheda.
1.  Selezionare**Modifica la posizione e i dati del gruppo**.
1. Specificare l'intervallo di dati e la posizione.
1.  Clic**OK**.

Aspose.Cells fornisce il metodo SparklineCollection.Add(dataRange, row, column) per specificare l'intervallo di dati e la posizione di un gruppo sparkline. Il seguente codice di esempio carica il file Excel di origine come mostrato nello screenshot precedente, quindi accede al primo gruppo sparkline e aggiunge intervalli di dati e posizioni nel gruppo sparkline. Infine, scrive il file Excel di output su disco, mostrato anche nello screenshot qui sopra.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopySparkline-1.cs" >}}
