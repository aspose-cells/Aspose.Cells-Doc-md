---
title: Extrahieren von OLE-Objekten aus dem Arbeitsblatt
type: docs
weight: 10
url: /de/cpp/extracting-ole-objects-from-worksheet/
---
## **Mögliche Nutzungsszenarien**
 Aspose.Cells ermöglicht es Ihnen, alle Arten von OLE-Objekten aus dem Arbeitsblatt zu extrahieren. Bitte verwende[IWorksheet->GetIOleObjects()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a4c59d95cdd871ecfe18274480831a728) -Methode, um auf alle OLE-Objekte im Arbeitsblatt zuzugreifen. Jedes OLE-Objekt hat[ProgID](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object#abb2ea6872025fe4724d9613cd6b81752) und[Objektdaten](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object#a4a200a03478d3553798360cd6a911d70)Eigenschaften, die Ihnen helfen können, den Typ des OLE-Objekts zu identifizieren und erfolgreich zu extrahieren.
## **Extrahieren von OLE-Objekten aus dem Arbeitsblatt**
 Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](66519077.xlsx) die drei OLE-Objekte hat. Der Code identifiziert die Typen von OLE-Objekten und extrahiert sie nacheinander als die folgenden Dateien.

- [outputExtractOleObject.pptx](66519080.pptx)
- [outputExtractOleObject.pdf](66519079.pdf)
- [outputExtractOleObject.docx](66519078.docx)
## **Beispielcode**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet.cpp" >}}
