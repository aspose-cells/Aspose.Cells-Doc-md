---
title: Einfügen von OLE Objekten in das Arbeitsblatt
type: docs
weight: 20
url: /de/cpp/inserting-ole-objects-into-the-worksheet/
---

## **Mögliche Verwendungsszenarien**
Aspose.Cells ermöglicht es Ihnen, ein OLE-Objekt im Arbeitsblatt einzufügen. Bitte verwenden Sie die Methode [Worksheet->GetOleObjects()->Add()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobjectcollection/add/) für diesen Zweck. Sie benötigen ein Bild-Byte-Array, das verwendet wird, um das OLE-Objekt im Arbeitsblatt einzufügen, und OLE-Objektdatenbytes, die Ihr tatsächliches Objekt darstellen, um das OLE-Objekt im Arbeitsblatt einzufügen. 
## **Einfügen von OLE-Objekten in das Arbeitsblatt**
The following sample code creates the workbook object and inserts the Ole object inside the first worksheet and saves it as [output Excel file](66519074.xlsx). Please see the <a href="66519075.png" download="66519075.png">Aspose-Logo</a> used as image bytes and [input Excel file](66519081.xlsx) used as Ole object data inside the code for reference.
## **Beispielcode**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-InsertingOLEObjectsIntoWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
