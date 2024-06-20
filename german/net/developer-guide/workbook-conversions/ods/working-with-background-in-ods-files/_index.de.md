---
title: Arbeiten mit Hintergrund in ODS Dateien
type: docs
weight: 150
url: /de/net/working-with-background-in-ods-files/
---

## **Hintergrund in ODS-Dateien**

Hintergrund kann zu Blättern in ODS-Dateien hinzugefügt werden. Der Hintergrund kann entweder ein farbiger Hintergrund oder ein grafischer Hintergrund sein. Der Hintergrund ist nicht sichtbar, wenn die Datei geöffnet ist, aber wenn die Datei als PDF gedruckt wird, ist der Hintergrund im generierten PDF sichtbar. Der Hintergrund ist auch in der Druckvorschau sichtbar.

Aspose.Cells bietet die Möglichkeit, die Hintergrundinformationen zu lesen und den Hintergrund in ODS-Dateien hinzuzufügen.

## **Hintergrundinformationen aus ODS-Datei lesen**

Aspose.Cells bietet die Klasse [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground), um Hintergründe in ODS-Dateien zu verwalten. Das folgende Codebeispiel zeigt die Verwendung der Klasse [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground), indem die [Quell-ODS](90112030.ods)-Datei geladen und die Hintergrundinformationen gelesen werden. Bitte beachten Sie die Konsolenausgabe, die vom Code erstellt wurde, als Referenz.

### **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadODSBackground-1.cs" >}}

### **Konsolenausgabe**

{{< highlight java >}}

Background Type: Graphic

Backgorund Position: CenterCenter

{{< /highlight >}}

## **Farbigen Hintergrund zu ODS-Datei hinzufügen**

Aspose.Cells bietet die Klasse [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground), um Hintergründe in ODS-Dateien zu verwalten. Das folgende Codebeispiel zeigt die Verwendung der Eigenschaft [**OdsPageBackground.Color**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/color) zum Hinzufügen eines farbigen Hintergrunds zur ODS-Datei. Bitte beachten Sie die [Ausgabedatei im ODS-Format](90112031.ods), die vom Code erstellt wurde, als Referenz.

### **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSColoredBackground-1.cs" >}}

## **Grafischen Hintergrund zu ODS-Datei hinzufügen**

Aspose.Cells bietet die Klasse [**OdsPageBackground**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground) zur Verwaltung des Hintergrunds in ODS-Dateien. Das folgende Codebeispiel demonstriert die Verwendung der Eigenschaft [**OdsPageBackground.GraphicData**](https://reference.aspose.com/cells/net/aspose.cells.ods/odspagebackground/properties/graphicdata), um einen grafischen Hintergrund zur ODS-Datei hinzuzufügen. Bitte beachten Sie die generierte Ausgabedatei ODS (90112030.ods) im Code als Referenz.

### **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-SetODSGraphicBackground-1.cs" >}}
