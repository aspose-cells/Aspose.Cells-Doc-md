---
title: Extrahieren von OLE Objekten aus dem Arbeitsblatt
type: docs
weight: 10
url: /de/cpp/extracting-ole-objects-from-worksheet/
---

## **Mögliche Verwendungsszenarien**
Aspose.Cells ermöglicht es Ihnen, alle Arten von OLE-Objekten aus dem Arbeitsblatt zu extrahieren. Bitte verwenden Sie die Methode [Worksheet->GetOleObjects()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getoleobjects/), um auf alle OLE-Objekte im Arbeitsblatt zuzugreifen. Jedes OLE-Objekt verfügt über die Eigenschaften [ProgID](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getprogid/) und [ObjectData](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/), die Ihnen helfen können, den Typ des OLE-Objekts zu identifizieren und erfolgreich zu extrahieren.
## **Extrahieren von OLE-Objekten aus dem Arbeitsblatt**
Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](66519077.xlsx), die drei OLE-Objekte enthält. Der Code identifiziert die Arten von OLE-Objekten und extrahiert sie nacheinander als die folgenden Dateien.

- [outputExtractOleObject.pptx](66519080.pptx)
- [outputExtractOleObject.pdf](66519079.pdf)
- [outputExtractOleObject.docx](66519078.docx)
## **Beispielcode**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
