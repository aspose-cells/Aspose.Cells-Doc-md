---
title: Copiare Sparkline specificando l’intervallo di dati e la posizione del Gruppo di Sparkline con Golang tramite C++
linktitle: Copia Sparkline specificando l intervallo di dati e la posizione
type: docs
weight: 300
url: /it/go-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
description: Impara come copiare sparklines specificando l intervallo di dati e la posizione usando Aspose.Cells for C++.
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

Aspose.Cells fornisce il metodo `SparklineCollection.Add(dataRange, row, column)` per specificare l'intervallo di dati e la posizione di un gruppo di sparklines. Il codice di esempio carica il file Excel di origine come mostrato nello screenshot sopra, quindi accede al primo gruppo di sparklines e aggiunge intervalli di dati e posizioni nel gruppo. Infine, scrive il file Excel di output su disco, visualizzato anche nello screenshot sopra.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopySparklineBySpecifyingDataRangeAndLocationOfSparklineGroup.go" >}}
