---
title: Arbeitsblatt in Bild und Arbeitsblatt in Bild pro Seite konvertieren
type: docs
weight: 210
url: /de/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

Dieses Dokument soll den Entwicklern ein detailliertes Verständnis vermitteln, wie man ein Arbeitsblatt in eine Bilddatei und ein Arbeitsblatt mit mehreren Seiten in eine Bilddatei pro Seite umwandelt.

Manchmal müssen Arbeitsblätter als Bilder präsentiert werden, zum Beispiel um sie in Anwendungen oder Webseiten zu verwenden. Möglicherweise müssen Sie die Bilder in ein Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation einfügen oder sie in einem anderen Szenario verwenden. Sie wollen das Arbeitsblatt einfach als Bild rendern. Aspose.Cells APIs unterstützen die Konvertierung von Arbeitsblättern in Microsoft Excel-Dateien in Bilder. Außerdem unterstützt Aspose.Cells die Konvertierung einer Arbeitsmappe in mehrere Bilddateien, eine pro Seite.

{{% /alert %}}

## **Verwendung von Aspose.Cells zum Konvertieren eines Arbeitsblatts in eine Bilddatei**

In diesem Artikel wird gezeigt, wie man die API Aspose.Cells for Java verwendet, um ein Arbeitsblatt in ein Bild zu konvertieren. Die API bietet verschiedene wertvolle Klassen wie [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) und so weiter. Die Klasse [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) repräsentiert ein Arbeitsblatt zur Darstellung von Bildern für das Arbeitsblatt und verfügt über eine überladene Methode [**toImage**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage-int-java.io.OutputStream-), die ein Arbeitsblatt direkt in Bilddateien mit beliebigen Attributen oder Optionen konvertieren kann.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImageFile-1.java" >}}

### **Ergebnis**

Nach Ausführen des obigen Codes wird das Arbeitsblatt namens Sheet1 in eine Bilddatei SheetImage.jpg konvertiert.

**Die Ausgabe JPG**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_1.png)

## **Verwendung von Aspose.Cells zur Konvertierung eines Arbeitsblatts in eine Bilddatei nach Seite**

Dieses Beispiel zeigt, wie man Aspose.Cells verwendet, um ein Arbeitsblatt aus einer Vorlagenarbeitsmappe, die mehrere Seiten hat, in eine Bilddatei pro Seite zu konvertieren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheetToImageByPage-1.java" >}}

### **Ergebnis**

Nach Ausführen des obigen Codes wird das Arbeitsblatt namens Sheet1 in zwei Bilddateien (eine pro Seite) Sheet 1 Page 1.Tiff und Sheet 1 Page 2.Tiff konvertiert.

**Generierte Bilddatei (Sheet 1 Page 1.Tiff)**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_2.png)

**Generierte Bilddatei (Sheet 1 Page 2.Tiff)**

![todo:image_alt_text](converting-worksheet-to-image-and-worksheet-to-image-by-page_3.png)

{{% alert color="primary" %}}

Dieser Artikel zeigt, wie man ein Arbeitsblatt in eine Bilddatei konvertiert und Arbeitsblätter mit mehreren Seiten in mehrere Bilddateien (eine pro Seite) mithilfe von Aspose.Cells exportiert. Aspose.Cells bietet mehr Flexibilität als andere Komponenten und bietet herausragende Geschwindigkeit, Effizienz und Zuverlässigkeit. Die Ergebnisse zeigen, dass Aspose.Cells von langjähriger Forschung, Gestaltung und sorgfältiger Abstimmung profitiert hat.

{{% /alert %}}

## Verwandte Artikel

- [Arbeitsblatt in verschiedene Bildformate konvertieren](/cells/de/java/converting-worksheet-to-different-image-formats/)
- [Arbeitsblatt oder Diagramm in Bild mit gewünschter Breite und Höhe exportieren](/cells/de/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
{{< app/cells/assistant language="java" >}}
