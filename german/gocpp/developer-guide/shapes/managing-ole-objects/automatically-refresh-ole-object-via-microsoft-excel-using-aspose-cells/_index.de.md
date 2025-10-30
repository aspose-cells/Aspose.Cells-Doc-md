---
title: Automatisches Aktualisieren des OLE Objekts in Microsoft Excel mit Golang via C++
linktitle: OLE Objekt automatisch aktualisieren
type: docs
weight: 270
url: /de/go-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: Lernen Sie, wie man OLE Objekte in Microsoft Excel automatisch aktualisiert mit Aspose.Cells mit Golang via C++.
---

{{% alert color="primary" %}}

Aspose.Cells stellt die Eigenschaft [**OleObject.GetAutoLoad()**](https://reference.aspose.com/cells/go-cpp/oleobject/getautoload/) bereit, um das OLE-Objekt beim Öffnen der Excel-Datei in Microsoft Excel zu aktualisieren. Aufgrund dieser Eigenschaft zeigt das OLE-Objekt das korrekte durch Microsoft Excel generierte OLE-Bild an.

{{% /alert %}}

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](5115231.xlsx), die ein nicht echtes OLE-Bild enthält. Das OLE-Objekt ist tatsächlich ein Microsoft Word-Dokument, aber die Beispiel-Excel-Datei zeigt das Tierbild anstelle des Microsoft Word-Bildes. Wenn Sie jedoch die [Ausgabedatei](5115225.xlsx) öffnen, sehen Sie, dass Microsoft Excel das richtige OLE-Bild anzeigt.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AutomaticallyRefreshOleObjectViaMicrosoftExcelUsingAsposeCells.go" >}}
