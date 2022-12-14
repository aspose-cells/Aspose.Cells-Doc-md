---
title: Einfügen von OLE-Objekten in das Arbeitsblatt
type: docs
weight: 20
url: /de/cpp/inserting-ole-objects-into-the-worksheet/
---
## **Mögliche Nutzungsszenarien**
 Aspose.Cells ermöglicht das Einfügen eines OLE-Objekts in das Arbeitsblatt. Bitte verwende[IWorksheet->GetIOleObjects()->Add()](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object_collection#af230dd65a00cefabcc4b9f165b5dc7ba)Methode zu diesem Zweck. Sie benötigen ein Bild-Byte-Array, das verwendet wird, um das OLE-Objekt in das Arbeitsblatt einzufügen, und Ole-Objektdatenbytes, die Ihr eigentliches Objekt sein werden, um das Ole-Objekt in das Arbeitsblatt einzufügen.
## **Einfügen von OLE-Objekten in das Arbeitsblatt**
 Der folgende Beispielcode erstellt das Arbeitsmappenobjekt, fügt das Ole-Objekt in das erste Arbeitsblatt ein und speichert es unter[Excel-Datei ausgeben](66519074.xlsx) . Bitte sehen Sie sich ... an[Aspose Logo](66519075.png) als Bildbytes und verwendet[Excel-Datei eingeben](66519081.xlsx)als Ole-Objektdaten innerhalb des Codes als Referenz verwendet.
## **Beispielcode**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-InsertingOLEObjectsIntoWorksheet.cpp" >}}
