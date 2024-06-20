---
title: OLE Objekt automatisch über Microsoft Excel mit Aspose.Cells aktualisieren
type: docs
weight: 270
url: /de/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells bietet die Eigenschaft [**OleObject.AutoLoad**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/autoload), um das OLE-Objekt zu aktualisieren, wenn die Excel-Datei in Microsoft Excel geöffnet wird. Aufgrund dieser Eigenschaft wird das OLE-Objekt das korrekte OLE-Bild anzeigen, das von Microsoft Excel generiert wurde.

{{% /alert %}}

Der folgende Beispielcode lädt die [Beispieldatei Excel](5115231.xlsx), die ein nicht-reales OLE-Bild enthält. Das OLE-Objekt ist tatsächlich ein Microsoft-Word-Dokument, aber die Beispieldatei Excel zeigt stattdessen das Tierbild an. Wenn Sie jedoch die [Ausgabedatei Excel](5115225.xlsx) öffnen, sehen Sie, dass Microsoft Excel das korrekte OLE-Bild anzeigt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-RefreshOLEObjects-1.cs" >}}
