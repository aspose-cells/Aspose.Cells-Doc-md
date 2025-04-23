---
title: Arbeiten mit Hintergrund in ODS Dateien
type: docs
weight: 170
url: /de/java/working-with-background-in-ods-files/
---

## **Hintergrund in ODS-Dateien**

Hintergrund kann in Tabellenblättern in ODS-Dateien hinzugefügt werden. Der Hintergrund kann entweder eine Farb- oder Grafikhintergrund sein. Der Hintergrund ist nicht sichtbar, wenn die Datei geöffnet ist, aber wenn die Datei als PDF gedruckt wird, ist der Hintergrund in der generierten PDF sichtbar. Der Hintergrund ist auch in der Druckvorschau sichtbar.

Aspose.Cells bietet die Möglichkeit, die Hintergrundinformationen zu lesen und Hintergrund in ODS-Dateien hinzuzufügen.

## **Lese Hintergrundinformationen aus OSD-Datei**

Aspose.Cells bietet die Klasse [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) zur Verwaltung des Hintergrunds in ODS-Dateien. Der folgende Code-Auszug zeigt die Verwendung der Klasse [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) durch das Laden der [Quell-ODS-Datei](GraphicBackground.ods) und das Auslesen der Hintergrundinformationen. Bitte beachten Sie die vom Code generierte Konsolenausgabe zur Referenz.

### **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-ReadODSBackground-1.java" >}}

### **Konsolenausgabe**

{{< highlight java >}}

Background Type: GRAPHIC

Backgorund Position: CENTER_CENTER

{{< /highlight >}}

## **Farbigen Hintergrund zu ODS-Datei hinzufügen**

Aspose.Cells bietet die Klasse [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) zur Verwaltung des Hintergrunds in ODS-Dateien. Der folgende Code-Auszug zeigt die Verwendung der Eigenschaft [**ODSPageBackground.Color**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#Color) zum Hinzufügen eines farbigen Hintergrunds zur ODS-Datei. Bitte sehen Sie sich die [ausgegebene ODS-Datei](ColoredBackground.ods) zur Referenz an.

### **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSColoredBackground-1.java" >}}

## **Grafischen Hintergrund zu ODS-Datei hinzufügen**

Aspose.Cells bietet die Klasse [**ODSPageBackground**](https://reference.aspose.com/cells/java/com.aspose.cells/ODSPageBackground) zur Verwaltung des Hintergrunds in ODS-Dateien. Der folgende Code-Auszug zeigt die Verwendung der Eigenschaft [**ODSPageBackground.GraphicData**](https://reference.aspose.com/cells/java/com.aspose.cells/odspagebackground#GraphicData) zum Hinzufügen eines grafischen Hintergrunds zur ODS-Datei. Bitte sehen Sie sich die [ausgegebene ODS-Datei](GraphicBackground.ods) zur Referenz an.

### **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-SetODSGraphicBackground-1.java" >}}
{{< app/cells/assistant language="java" >}}
