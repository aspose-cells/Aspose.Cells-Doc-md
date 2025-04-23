---
title: Copia Sparkline specificando intervallo dati e posizione del gruppo di Sparkline
type: docs
weight: 300
url: /it/net/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

{{% alert color="primary" %}}

Microsoft Excel consente di copiare una linea di tendenza specificando l'intervallo di dati e la posizione di un gruppo di linee di tendenza. Aspose.Cells supporta questa funzionalità

{{% /alert %}}

Per copiare una linea di tendenza in altre celle in Microsoft Excel

1. Selezionare la cella contenente la linea di tendenza
1. Selezionare **Modifica dati** dalla sezione **Linee di tendenza** della scheda **Progettazione**
1. Selezionare **Modifica posizione gruppo e dati**
1. Specificare l'intervallo di dati e la posizione
1. Fai clic su **OK**.

Aspose.Cells fornisce il metodo SparklineCollection.Add(dataRange, riga, colonna) per specificare l'intervallo di dati e la posizione di un gruppo di linee di tendenza. Il codice di esempio seguente carica il file Excel di origine come mostrato nella schermata sopra, quindi accede al primo gruppo di linee di tendenza e aggiunge intervalli di dati e posizioni nel gruppo di linee di tendenza. Infine, scrive il file Excel di output su disco che è anche mostrato nella schermata sopra

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopySparkline-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
