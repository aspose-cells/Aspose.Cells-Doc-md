---
title: Zeilenhöhen des Quellbereichs in den Zielbereich kopieren mit Golang über C++
linktitle: Quellenbereichszeilenhöhen in Zielbereich kopieren
type: docs
weight: 590
url: /de/go-cpp/copy-row-heights-of-source-range-to-destination-range/
description: Lernen Sie, wie Sie Zeilenhöhen von einem Quellbereich auf einen Zielbereich mit Aspose.Cells for C++ kopieren.
---

{{% alert color="primary" %}}

Manchmal müssen Benutzer Zeilenhöhen von einem Quellbereich auf einen Zielbereich kopieren. Aspose.Cells bietet dafür den [**PasteType::RowHeights**](https://reference.aspose.com/cells/go-cpp/pastetype/)-Aufzählungstyp. Wenn Sie die Eigenschaft [**GetPasteType()**](https://reference.aspose.com/cells/cpp/aspose.cells/pasteoptions/getpastetype/) mit dem [**PasteType::RowHeights**](https://reference.aspose.com/cells/go-cpp/pastetype/)-Aufzählungstyp setzen, werden die Höhen aller Zeilen im Quellbereich in den Zielbereich kopiert.

{{% /alert %}}

 Das folgende Beispiel erklärt, wie man die [**PasteType::RowHeights**](https://reference.aspose.com/cells/go-cpp/pastetype/)-Aufzählung verwendet, um Zeilenhöhen von einem Quellbereich in einen Zielbereich zu kopieren. Wenn Sie die erzeugte Excel-Datei in Microsoft Excel öffnen, sehen Sie, dass die Zeilenhöhen im Zielbereich genau die gleichen sind wie im Quellbereich.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyRowHeightsOfSourceRangeToDestinationRange.go" >}}
