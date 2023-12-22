---
title: Extrahieren von OLE-Objekten aus dem Arbeitsblatt
type: docs
weight: 10
url: /de/cpp/extracting-ole-objects-from-worksheet/
---
##  **Mögliche Nutzungsszenarien**
 Aspose.Cells ermöglicht Ihnen das Extrahieren aller Arten von OLE-Objekten aus dem Arbeitsblatt. Benutzen Sie bitte[Arbeitsblatt->GetOleObjects()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getoleobjects/) Methode für den Zugriff auf alle OLE-Objekte im Arbeitsblatt. Jedes OLE-Objekt hat[ProgID](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getprogid/) Und[ObjectData](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/)Eigenschaften, die Ihnen helfen können, den Typ des OLE-Objekts zu identifizieren und es erfolgreich zu extrahieren.
##  **Extrahieren von OLE-Objekten aus dem Arbeitsblatt**
 Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](66519077.xlsx) das über drei OLE-Objekte verfügt. Der Code identifiziert die Typen von OLE-Objekten und extrahiert sie einzeln als die folgenden Dateien.

- [AusgabeExtractOleObject.pptx](66519080.pptx)
- [AusgabeExtractOleObject.pdf](66519079.pdf)
- [AusgabeExtractOleObject.docx](66519078.docx)
##  **Beispielcode**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet-new.cpp" >}}
