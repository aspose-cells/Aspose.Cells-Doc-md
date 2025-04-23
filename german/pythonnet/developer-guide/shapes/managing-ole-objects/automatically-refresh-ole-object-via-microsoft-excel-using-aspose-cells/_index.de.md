---
title: OLE Objekt automatisch aktualisieren
type: docs
weight: 270
url: /de/python-net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells für Python via .NET bietet die Eigenschaft [**OleObject.auto_load**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/auto_load), um das OLE-Objekt beim Öffnen der Excel-Datei in Microsoft Excel zu aktualisieren. Durch diese Eigenschaft wird das OLE-Objekt das korrekte OLE-Bild anzeigen, das von Microsoft Excel erzeugt wurde.

{{% /alert %}}

Der folgende Beispielcode lädt die [Beispieldatei Excel](5115231.xlsx), die ein nicht-reales OLE-Bild enthält. Das OLE-Objekt ist tatsächlich ein Microsoft-Word-Dokument, aber die Beispieldatei Excel zeigt stattdessen das Tierbild an. Wenn Sie jedoch die [Ausgabedatei Excel](5115225.xlsx) öffnen, sehen Sie, dass Microsoft Excel das korrekte OLE-Bild anzeigt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-RefreshOLEObjects-1.py" >}}
