---  
title: Automatisches Aktualisieren des OLE Objekts über Microsoft Excel mit Aspose.Cells for Node.js via C++  
linktitle: OLE Objekt automatisch über Microsoft Excel mit Aspose.Cells aktualisieren  
type: docs  
weight: 270  
url: /de/nodejs-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/  
description: Lernen, wie man OLE Objekte in Excel mit Aspose.Cells for Node.js via C++ automatisch aktualisiert.  
---  

{{% alert color="primary" %}}  
Aspose.Cells bietet die Eigenschaft [**OleObject.getAutoLoad()**](https://reference.aspose.com/cells/nodejs-cpp/oleobject/#getAutoLoad--), um das OLE-Objekt zu aktualisieren, wenn die Excel-Datei in Microsoft Excel geöffnet wird. Aufgrund dieser Eigenschaft wird das OLE-Objekt das korrekte OLE-Bild anzeigen, das von Microsoft Excel generiert wurde.  
{{% /alert %}}  

Der folgende Beispielcode lädt die [Beispieldatei Excel](5115231.xlsx), die ein nicht-reales OLE-Bild enthält. Das OLE-Objekt ist tatsächlich ein Microsoft-Word-Dokument, aber die Beispieldatei Excel zeigt stattdessen das Tierbild an. Wenn Sie jedoch die [Ausgabedatei Excel](5115225.xlsx) öffnen, sehen Sie, dass Microsoft Excel das korrekte OLE-Bild anzeigt.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object from your sample excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample_oleobject.xlsx"));

// Access first worksheet
const sheet = workbook.getWorksheets().get(0);

// Set auto load property of first ole object to true
sheet.getOleObjects().get(0).setAutoLoad(true);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "RefreshOLEObjects_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  
