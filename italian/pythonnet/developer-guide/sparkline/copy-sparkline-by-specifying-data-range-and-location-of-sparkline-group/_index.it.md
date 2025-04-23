---
title: Copia Sparkline specificando intervallo dati e posizione del gruppo di Sparkline
type: docs
weight: 300
url: /it/python-net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

{{% alert color="primary" %}}

Microsoft Excel consente di copiare una sparkline specificando l'intervallo dati e la posizione di un gruppo di sparklines. Aspose.Cells per Python via .NET supporta questa funzione.

{{% /alert %}}

Per copiare una linea di tendenza in altre celle in Microsoft Excel

1. Selezionare la cella contenente la linea di tendenza
1. Selezionare **Modifica dati** dalla sezione **Linee di tendenza** della scheda **Progettazione**
1. Selezionare **Modifica posizione gruppo e dati**
1. Specificare l'intervallo di dati e la posizione
1. Fai clic su **OK**.

Aspose.Cells per Python via .NET fornisce il metodo SparklineCollection.Add(dataRange, row, column) per specificare l'intervallo dati e la posizione di un gruppo di sparklines. Il seguente esempio di codice carica il file Excel di origine come mostrato nello screenshot sopra, quindi accede al primo gruppo di sparklines e aggiunge intervalli dati e posizioni nel gruppo. Infine, scrive il file Excel di output sul disco, il quale è anche mostrato nello screenshot sopra.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Sparklines-CopySparkline-1.py" >}}

