---
title: Arbeitsblatt in Bild umwandeln in Aspose.Cells
type: docs
weight: 20
url: /de/net/converting-worksheet-to-image-in-aspose-cells/
---
Dieses Dokument soll den Entwicklern ein detailliertes Verständnis dafür vermitteln, wie ein Arbeitsblatt in eine Bilddatei und ein Arbeitsblatt mit mehreren Seiten in eine Bilddatei pro Seite konvertiert wird.
 Manchmal müssen Sie Arbeitsblätter möglicherweise als Bilder darstellen, um sie beispielsweise in Anwendungen oder Webseiten zu verwenden. Möglicherweise müssen Sie die Bilder in ein Word-Dokument einfügen, a**Pdf** Datei, eine PowerPoint-Präsentation oder verwenden Sie sie in einem anderen Szenario. Sie möchten das Arbeitsblatt einfach als Bild rendern. Aspose.Cells unterstützt die Konvertierung von Arbeitsblättern in Microsoft Excel-Dateien in Bilder. Ebenfalls,**Aspose.Cells** unterstützt das Konvertieren einer Arbeitsmappe in mehrere Bilddateien, eine pro Seite.

Sie können Office-Automatisierung verwenden, um dies zu erreichen, aber die Office-Automatisierung hat ihre eigenen Nachteile. Es gibt mehrere Gründe und Probleme: zum Beispiel Sicherheit, Stabilität, Skalierbarkeit/Geschwindigkeit, Preis und Funktionen. Kurz gesagt, es gibt viele Gründe, aber der Hauptgrund ist, dass Microsoft selbst dringend von Office-Automatisierung abrät.

Dieser Artikel zeigt, wie Sie mit Aspose.Cells API eine Konsolenanwendung in Visual Studio.Net erstellen, ein Arbeitsblatt in ein Bild konvertieren und ein Arbeitsblatt in ein Bild für jedes Arbeitsblatt in ein Bild umwandeln Namensraum zu Ihrem Programm/Projekt. Es hat mehrere wertvolle Klassen, z. B. SheetRender, ImageOrPrintOptions, WorkbookRender usw. Aspose.Cells. Die Klasse Rendering.SheetRender stellt ein Arbeitsblatt dar, um Bilder für das Arbeitsblatt zu rendern, es ist überladen**Vorstellen** Methode, die ein Arbeitsblatt direkt in Bilddatei(en) konvertieren kann, die mit Ihren gewünschten Attributen oder Optionen angegeben sind. Es kann zurückkehren**System.Zeichnung.Bitmap** Objekt und Sie können eine Bilddatei auf der Festplatte/im Stream speichern. Es werden mehrere Bildformate unterstützt, z. B. .bmp, .png, .gif, .jpg, .jpeg, .tiff, .emf usw.

{{< highlight "csharp" >}}

 //Create a new Workbook object

//Open a template excel file

Workbook book = new Workbook("Sheet to Image.xls");

//Get the first worksheet.

Worksheet sheet = book.Worksheets[0];

//Define ImageOrPrintOptions

ImageOrPrintOptions imgOptions = new ImageOrPrintOptions();

//Specify the image format

imgOptions.ImageFormat = System.Drawing.Imaging.ImageFormat.Jpeg;

//Render the sheet with respect to specified image/print options

SheetRender sr = new SheetRender(sheet, imgOptions);

//Render the image for the sheet

Bitmap bitmap = sr.ToImage(0);

//Save the image file

bitmap.Save("SheetImage.jpg");

{{< /highlight >}}
## **Beispielcode herunterladen**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.Image.Aspose.Cells.zip)
- [Bit Bucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20Image%20%28Aspose.Cells%29.zip)
