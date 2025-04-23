---
title: Quellenbereichszeilenhöhen in Zielbereich kopieren
type: docs
weight: 590
url: /de/net/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}}

Manchmal muss der Benutzer die Zeilenhöhen des Quellbereichs in den Zielbereich kopieren. Aspose.Cells bietet hierfür die [**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype)-Enumeration. Wenn Sie die Eigenschaft [**PasteOptions.PasteType**](https://reference.aspose.com/cells/net/aspose.cells/pasteoptions/properties/pastetype) mit der [**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype)-Enumeration setzen, werden die Höhen aller Zeilen im Quellbereich in den Zielbereich kopiert.

{{% /alert %}}

Der folgende Beispielcode erläutert die Verwendung der [**PasteType.RowHeights**](https://reference.aspose.com/cells/net/aspose.cells/pastetype)-Enumeration, um die Zeilenhöhen des Quellbereichs in den Zielbereich zu kopieren. Sobald Sie die mit diesem Code generierte Ausgabedatei in Microsoft Excel öffnen, werden Sie feststellen, dass die Zeilenhöhen des Zielbereichs genau den Zeilenhöhen des Quellbereichs entsprechen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetRowHeights-GetRowHeightsOfSourceRangeToDestinationRange.cs" >}}
{{< app/cells/assistant language="csharp" >}}
