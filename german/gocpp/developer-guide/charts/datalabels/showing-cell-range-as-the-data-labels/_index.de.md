---
title: Anzeigen des Zellbereichs als Datenbeschriftungen mit Golang über C++
linktitle: Anzeige des Zellenbereichs als Datenbeschriftungen
description: Erfahren Sie, wie Sie einen Zellbereich als Datenbeschriftungen in Diagrammen mit Aspose.Cells for C++ anzeigen. Unser Leitfaden zeigt, wie Sie die Beschriftungen mit Ihrer Datenquelle verknüpfen und formatieren, um genaue und aussagekräftige Informationen in Ihren Diagrammen bereitzustellen.
keywords: Aspose.Cells for C++, Diagrammerstellung, Datenbeschriftungen, Zellbereich, Datenquelle, Formatierung, Genauigkeit, aussagekräftige Informationen.
type: docs
weight: 130
url: /de/go-cpp/showing-cell-range-as-the-data-labels/
---

{{% alert color="primary" %}}

In Microsoft Excel 2013 können Sie einen Zellenbereich für Datenbeschriftungen anzeigen. Aspose.Cells unterstützt diese Funktion

{{% /alert %}}

## **Kontrollkästchen zum Anzeigen des Zellenbereichs als Datenbeschriftungen**

So zeigen Sie den Zellenbereich als Datenbeschriftungen in Microsoft Excel:

1. Wählen Sie die Seriendatenbeschriftungen aus und klicken Sie mit der rechten Maustaste, um das Kontextmenü zu öffnen.
1. Wählen Sie **Datenelemente formatieren** aus. Beschriftungsoptionen werden angezeigt.
1. Wählen oder deaktivieren Sie die Option **Beschriftung enthält - Wert aus Zellen**.

Der unten stehende Beispielcode greift auf die Beschriftungen von Diagrammserien zu und setzt die [**DataLabels.GetShowCellRange()**](https://reference.aspose.com/cells/go-cpp/datalabels/getshowcellrange/)-Eigenschaft auf **true**, um die Option **Beschriftung enthält - Wert aus Zellen** auszuwählen.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ShowingCellRangeAsTheDataLabels.go" >}}
