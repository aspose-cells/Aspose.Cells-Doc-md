---
title: Zugriff auf die Anzeige kennzeichnung des verknüpften Ole Objekts mit Golang via C++ und Änderung
linktitle: Auf das Anzeigen des verknüpften Ole Objekts zugreifen und es ändern
type: docs
weight: 100
url: /de/go-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: Lernen Sie, wie Sie den Anzeige Label verbundener OLE Objekte in Excel Dateien mit Aspose.Cells for C++ zugreifen und diesen ändern.
---

## **Mögliche Verwendungsszenarien**

Microsoft Excel erlaubt es, das Anzeige-Label des OLE-Objekts zu ändern, wie im folgenden Screenshot gezeigt. Sie können auch das Anzeige-Label des OLE-Objekts mit den APIs von Aspose.Cells und den Methoden [**GetLabel()**](https://reference.aspose.com/cells/go-cpp/oleobject/getlabel/) und [**SetLabel(const U16String\& value)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/setlabel/) zugreifen oder ändern.

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **Auf das Anzeigen des verknüpften Ole-Objekts zugreifen und es ändern**

Bitte sehen Sie sich den folgenden Beispielcode an. Es lädt die [Beispieldatei Excel](64716810.xlsx), die das Ole-Objekt enthält. Der Code ruft das Ole-Objekt auf und ändert sein Label von 'Sample APIs' in 'Aspose APIs'. Bitte sehen Sie sich die unten angezeigte Konsolenausgabe an, die die Auswirkung des Beispielcodes auf die Beispieldatei Excel zeigt.

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AccessAndModifyTheDisplayLabelOfTheLinkedOleObject.go" >}}
## **Konsolenausgabe**

{{< highlight java >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
