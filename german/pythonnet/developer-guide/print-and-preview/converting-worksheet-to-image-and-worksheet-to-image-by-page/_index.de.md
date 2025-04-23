---
title: Arbeitsblatt in Bild und Arbeitsblatt in Bild pro Seite konvertieren
type: docs
weight: 80
url: /de/python-net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

Dieses Dokument soll den Entwicklern ein detailliertes Verständnis vermitteln, wie man ein Arbeitsblatt in eine Bilddatei und ein Arbeitsblatt mit mehreren Seiten in eine Bilddatei pro Seite umwandelt.

Manchmal möchten Sie Worksheets als Bilder präsentieren, beispielsweise um sie in Anwendungen oder Webseiten zu verwenden. Sie könnten die Bilder in ein Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation einfügen oder sie in einem anderen Szenario verwenden wollen. Einfach gesagt, Sie möchten das Worksheet als Bild rendern. Aspose.Cells für Python via .NET unterstützt die Konvertierung von Worksheets in Excel-Dateien in Bilder. Außerdem unterstützt Aspose.Cells für Python via .NET die Umwandlung eines Workbooks in mehrere Bilddateien, eine pro Seite.

Möglicherweise verwenden Sie Office Automation, um dies zu erreichen, aber Office-Automation hat ihre eigenen Nachteile. Es gibt mehrere Gründe und Probleme, beispielsweise Sicherheit, Stabilität, Skalierbarkeit/Geschwindigkeit, Preis und Funktionen. Kurz gesagt, es gibt viele Gründe, aber der Hauptgrund ist, dass Microsoft selbst dringend von der Verwendung von Office-Automation abrät.

{{% /alert %}}

## **Verwendung von Aspose.Cells zum Konvertieren eines Arbeitsblatts in eine Bilddatei**

Dieser Artikel zeigt, wie man eine Konsolenanwendung in Visual Studio erstellt, ein Worksheet in ein Bild konvertiert und ein Worksheet in jeweils ein Bild pro Worksheet mit wenigen und einfachen Zeilen Code unter Verwendung der Aspose.Cells für Python via .NET API umwandelt.

Sie müssen den Namespace [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering) in Ihr Programm/Projekt importieren. Es hat mehrere wertvolle Klassen, wie [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) usw. Die Klasse [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) repräsentiert ein Arbeitsblatt zum Rendern von Bildern für das Arbeitsblatt und verfügt über eine überladene Methode [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str), die direkt ein Arbeitsblatt in Bilddateien mit beliebigen Attributen oder festgelegten Optionen umwandeln kann. Es kann ein System.Drawing.Bitmap-Objekt zurückgeben und Sie können eine Bilddatei auf die Festplatte/stream speichern. Es werden mehrere Bildformate unterstützt, zum Beispiel BMP, PNG, GIF, JPG, JPEG, TIFF, EMF und andere.

Dieser Artikel erklärt, wie man ein Worksheet in ein Bild konvertiert. Diese Aufgabe zeigt, wie man Aspose.Cells für Python via .NET benutzt, um ein Worksheet aus einer Vorlage-Arbeitsmappe in eine Bilddatei umzuwandeln.


### **Arbeitsblatt in Bilddatei konvertieren**

Ich habe eine neue Arbeitsmappe in Microsoft Excel erstellt und einige Daten im ersten Arbeitsblatt hinzugefügt: **Testbook.xlsx** (1 Arbeitsblatt). Konvertieren Sie als Nächstes das Arbeitsblatt Sheet1 der Vorlagendatei in eine Bilddatei namens SheetImage.jpg.

Nachfolgend ist der von der Komponente verwendete Code, um die Aufgabe zu erledigen. Es konvertiert Sheet1 in **Testbook.xlsx** in eine Bilddatei, um zu erklären, wie einfach diese Konvertierung ist.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ConvertWorksheettoImageFile-1.py" >}}

## **Verwendung von Aspose.Cells zur Konvertierung eines Arbeitsblatts in eine Bilddatei nach Seite**

Dieses Beispiel zeigt, wie man Aspose.Cells für Python via .NET benutzt, um ein Worksheet aus einer Vorlage-Arbeitsmappe, die mehrere Seiten enthält, in eine Bilddatei pro Seite zu konvertieren.

### **Arbeitsblatt nach Seite in Bild konvertieren**

Ich habe eine neue Arbeitsmappe in Microsoft Excel erstellt und einige Daten im ersten Arbeitsblatt hinzugefügt: **Testbook2.xlsx** (1 Arbeitsblatt).

Konvertieren Sie jetzt das Arbeitsblatt Sheet1 der Vorlagendatei in Bilddateien (eine Datei pro Seite). Da ich die Konsolenanwendung bereits erstellt habe, um die Kopieraufgabe auszuführen, werde ich diese Schritte zur Erstellung der Konsolenanwendung überspringen und direkt zu den Arbeitsblattkonvertierungsschritten übergehen.

Nachfolgend ist der von der Komponente verwendete Code, um die Aufgabe zu erledigen. Es konvertiert Sheet1 in Testbook2.xlsx in Bilddateien nach Seite.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-ConvertWorksheetToImageByPage-1.py" >}}

