---
title: Konvertieren von Arbeitsblatt in Bild und Arbeitsblatt in Bild für Seite
type: docs
weight: 210
url: /de/java/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---
{{% alert color="primary" %}}

Dieses Dokument soll den Entwicklern ein detailliertes Verständnis dafür vermitteln, wie ein Arbeitsblatt in eine Bilddatei und ein Arbeitsblatt mit mehreren Seiten in eine Bilddatei pro Seite konvertiert wird.

Manchmal müssen Sie Arbeitsblätter möglicherweise als Bilder darstellen, um sie beispielsweise in Anwendungen oder Webseiten zu verwenden. Möglicherweise müssen Sie die Bilder in ein Word-Dokument, eine PDF-Datei oder eine PowerPoint-Präsentation einfügen oder sie in einem anderen Szenario verwenden. Sie möchten das Arbeitsblatt einfach als Bild rendern. Aspose.Cells APIs unterstützen die Konvertierung von Arbeitsblättern in Microsoft Excel-Dateien in Bilder. Außerdem unterstützt Aspose.Cells das Konvertieren einer Arbeitsmappe in mehrere Bilddateien, eine pro Seite.

{{% /alert %}}

## **Verwenden von Aspose.Cells zum Konvertieren eines Arbeitsblatts in eine Bilddatei**

Dieser Artikel zeigt, wie Sie Aspose.Cells for Java API verwenden, um ein Arbeitsblatt in ein Bild zu konvertieren. Die API bietet mehrere wertvolle Klassen, wie z[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions), [**WorkbookRender**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookRender) , usw. Das[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender) -Klasse stellt ein Arbeitsblatt zum Rendern von Bildern für das Arbeitsblatt dar und ist überladen[**vorstellen**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toImage(int,%20java.io.OutputStream))-Methode, die ein Arbeitsblatt direkt in Bilddateien konvertieren kann, wobei alle Attribute oder Optionen festgelegt sind.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheettoImageFile-1.java" >}}

### **Ergebnis**

Nach dem Ausführen des obigen Codes wird das Arbeitsblatt mit dem Namen Sheet1 in eine Bilddatei SheetImage.jpg konvertiert.

**Die Ausgabe JPG**

![todo: Bild_alt_Text](converting-worksheet-to-image-and-worksheet-to-image-by-page_1.png)

## **Verwenden von Aspose.Cells, um ein Arbeitsblatt seitenweise in eine Bilddatei zu konvertieren**

Dieses Beispiel zeigt, wie Sie Aspose.Cells verwenden, um ein Arbeitsblatt aus einer Vorlagenarbeitsmappe mit mehreren Seiten in eine Bilddatei pro Seite zu konvertieren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ConvertWorksheetToImageByPage-1.java" >}}

### **Ergebnis**

Nachdem der obige Code ausgeführt wurde, wird das Arbeitsblatt mit dem Namen Sheet1 in zwei Bilddateien (1 pro Seite) Sheet 1 Page 1.Tiff und Sheet 1 Page 2.Tiff konvertiert.

**Generierte Bilddatei (Blatt 1 Seite 1.Tiff)**

![todo: Bild_alt_Text](converting-worksheet-to-image-and-worksheet-to-image-by-page_2.png)

**Generierte Bilddatei (Blatt 1 Seite 2.Tiff)**

![todo: Bild_alt_Text](converting-worksheet-to-image-and-worksheet-to-image-by-page_3.png)

{{% alert color="primary" %}}

Dieser Artikel zeigt, wie Sie mit Aspose.Cells ein Arbeitsblatt in eine Bilddatei konvertieren und Arbeitsblätter mit mehreren Seiten in mehrere Bilddateien (eine pro Seite) konvertieren. Aspose.Cells bietet mehr Flexibilität als andere Komponenten und bietet herausragende Geschwindigkeit, Effizienz und Zuverlässigkeit. Die Ergebnisse zeigen, dass Aspose.Cells von jahrelanger Forschung, Design und sorgfältiger Abstimmung profitiert hat.

{{% /alert %}}

## In Verbindung stehende Artikel

- [Konvertieren von Arbeitsblättern in verschiedene Bildformate](/cells/de/java/converting-worksheet-to-different-image-formats/)
- [Arbeitsblatt oder Diagramm in Bild mit gewünschter Breite und Höhe exportieren](/cells/de/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
