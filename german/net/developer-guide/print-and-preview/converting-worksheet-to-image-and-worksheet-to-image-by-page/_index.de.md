---
title: Konvertieren von Arbeitsblatt in Bild und Arbeitsblatt in Bild für Seite
type: docs
weight: 80
url: /de/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---
{{% alert color="primary" %}}

Dieses Dokument soll den Entwicklern ein detailliertes Verständnis dafür vermitteln, wie ein Arbeitsblatt in eine Bilddatei und ein Arbeitsblatt mit mehreren Seiten in eine Bilddatei pro Seite konvertiert wird.

Manchmal müssen Sie Arbeitsblätter möglicherweise als Bilder darstellen, um sie beispielsweise in Anwendungen oder Webseiten zu verwenden. Möglicherweise müssen Sie die Bilder in ein Word-Dokument, eine PDF-Datei oder eine PowerPoint-Präsentation einfügen oder sie in einem anderen Szenario verwenden. Sie möchten das Arbeitsblatt einfach als Bild rendern. Aspose.Cells unterstützt die Konvertierung von Arbeitsblättern in Microsoft Excel-Dateien in Bilder. Außerdem unterstützt Aspose.Cells das Konvertieren einer Arbeitsmappe in mehrere Bilddateien, eine pro Seite.

Sie können Office-Automatisierung verwenden, um dies zu erreichen, aber die Office-Automatisierung hat ihre eigenen Nachteile. Es gibt mehrere Gründe und Probleme: zum Beispiel Sicherheit, Stabilität, Skalierbarkeit/Geschwindigkeit, Preis und Funktionen. Kurz gesagt, es gibt viele Gründe, aber der Hauptgrund ist, dass Microsoft selbst dringend von Office-Automatisierung abrät.

{{% /alert %}}

## **Verwenden von Aspose.Cells zum Konvertieren eines Arbeitsblatts in eine Bilddatei**

Dieser Artikel zeigt, wie Sie eine Konsolenanwendung in Visual Studio erstellen, ein Arbeitsblatt in ein Bild konvertieren und ein Arbeitsblatt in ein Bild für jedes Arbeitsblatt mit wenigen und einfachsten Codezeilen mithilfe von Aspose.Cells API konvertieren.

 Sie müssen die importieren[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) Namensraum zu Ihrem Programm/Projekt. Es hat mehrere wertvolle Klassen, wie z[**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender), usw. Das[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) -Klasse stellt ein Arbeitsblatt zum Rendern von Bildern für das Arbeitsblatt dar und ist überladen[**Vorstellen**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)Methode, die ein Arbeitsblatt direkt in Bilddateien konvertieren kann, wobei alle Attribute oder Optionen festgelegt sind. Es kann ein System.Drawing.Bitmap-Objekt zurückgeben und Sie können eine Bilddatei auf dem Datenträger/Stream speichern. Mehrere Bildformate werden unterstützt, zum Beispiel BMP, PNG, GIF, JPG, JPEG, TIFF, EMF und andere.

In diesem Artikel wird erläutert, wie Sie:

- Konvertieren Sie ein Arbeitsblatt in ein Bild
- Konvertieren Sie jede Seite in einem Arbeitsblatt in ein Bild

Diese Aufgabe zeigt, wie Sie Aspose.Cells verwenden, um ein Arbeitsblatt aus einer Vorlagenarbeitsmappe in eine Bilddatei zu konvertieren.

### **Projekt einrichten**

1.  Zuerst,[herunterladen Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1.  Installieren Sie es auf Ihrem Entwicklungscomputer. Alle[Aspose](http://www.aspose.com/)Komponenten arbeiten, wenn sie installiert sind, im Evaluierungsmodus. Der Bewertungsmodus ist zeitlich unbegrenzt und fügt nur Wasserzeichen in die produzierten Dokumente ein. Starten Sie nun Visual Studio.Net und erstellen Sie eine neue Konsolenanwendung. Dieses Beispiel verwendet eine C#-Konsolenanwendung, aber Sie können auch VB.NET verwenden. Fügen Sie dem erstellten Projekt den Verweis auf Aspose.Cells hinzu.

### **Arbeitsblatt in Bilddatei konvertieren**

 Ich habe eine neue Arbeitsmappe in Microsoft Excel erstellt und einige Daten im ersten Arbeitsblatt hinzugefügt:**Testbook.xlsx** (1 Arbeitsblatt). Konvertieren Sie als Nächstes das Arbeitsblatt Sheet1 der Vorlagendatei in eine Bilddatei mit dem Namen SheetImage.jpg.

 Es folgt der Code, der von der Komponente verwendet wird, um die Aufgabe auszuführen. Es konvertiert Sheet1 in**Testbook.xlsx** zu einer Bilddatei, um zu erklären, wie einfach diese Konvertierung ist.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheettoImageFile-1.cs" >}}

## **Verwenden von Aspose.Cells, um ein Arbeitsblatt seitenweise in eine Bilddatei zu konvertieren**

Dieses Beispiel zeigt, wie Sie Aspose.Cells verwenden, um ein Arbeitsblatt aus einer Vorlagenarbeitsmappe mit mehreren Seiten in eine Bilddatei pro Seite zu konvertieren.

### **Arbeitsblatt seitenweise in Bild umwandeln**

 Ich habe eine neue Arbeitsmappe in Microsoft Excel erstellt und einige Daten im ersten Arbeitsblatt hinzugefügt:**Testbook2.xlsx** (1 Arbeitsblatt).

Konvertieren Sie nun das Arbeitsblatt Sheet1 der Vorlagendatei in Bilddateien (eine Datei pro Seite). Da ich die Konsolenanwendung bereits erstellt habe, um die Kopieraufgabe auszuführen, überspringe ich diese Schritte zum Erstellen der Konsolenanwendung und gehe direkt zu den Arbeitsblattkonvertierungsschritten.

Es folgt der Code, der von der Komponente verwendet wird, um die Aufgabe auszuführen. Es konvertiert Sheet1 in Testbook2.xls seitenweise in Bilddateien.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

