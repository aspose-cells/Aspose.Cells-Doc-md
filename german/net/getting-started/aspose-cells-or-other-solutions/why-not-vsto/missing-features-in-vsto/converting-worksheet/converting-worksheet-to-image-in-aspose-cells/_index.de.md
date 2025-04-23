---
title: Arbeitsblatt in Bild in Aspose.Cells konvertieren
type: docs
weight: 20
url: /de/net/converting-worksheet-to-image-in-aspose-cells/
---

Dieses Dokument soll den Entwicklern ein detailliertes Verständnis darüber vermitteln, wie man ein Arbeitsblatt in eine Bilddatei und ein Arbeitsblatt mit mehreren Seiten in eine Bilddatei pro Seite konvertiert.
Manchmal müssen Tabellenblätter als Bilder präsentiert werden, z.B. um sie in Anwendungen oder Webseiten zu verwenden. Sie müssen die Bilder möglicherweise in ein Word-Dokument, eine **PDF**-Datei, eine PowerPoint-Präsentation einfügen oder sie in einem anderen Szenario verwenden. Kurz gesagt, Sie möchten das Tabellenblatt als Bild rendern. Aspose.Cells unterstützt die Konvertierung von Tabellenblättern in Microsoft Excel-Dateien in Bilder. Außerdem unterstützt **Aspose.Cells** die Konvertierung eines Arbeitsmappen in mehrere Bilddateien, eine pro Seite.

Möglicherweise verwenden Sie Office Automation, um dies zu erreichen, aber Office-Automation hat ihre eigenen Nachteile. Es gibt mehrere Gründe und Probleme, beispielsweise Sicherheit, Stabilität, Skalierbarkeit/Geschwindigkeit, Preis und Funktionen. Kurz gesagt, es gibt viele Gründe, aber der Hauptgrund ist, dass Microsoft selbst dringend von der Verwendung von Office-Automation abrät.

In diesem Artikel wird gezeigt, wie man eine Konsolenanwendung in Visual Studio .Net erstellt, ein Arbeitsblatt in ein Bild umwandelt und ein Arbeitsblatt mit wenigen und einfachsten Codezeilen mithilfe der Aspose.Cells API in ein Bild für jedes Arbeitsblatt umwandelt. Sie müssen den Namespace Aspose.Cells.Rendering in Ihr Programm/Projekt importieren. Er enthält mehrere wertvolle Klassen, z.B. SheetRender, ImageOrPrintOptions, WorkbookRender usw. Die Klasse Aspose.Cells.Rendering.SheetRender repräsentiert ein Arbeitsblatt, um Bilder für das Arbeitsblatt zu rendern. Sie verfügt über eine überladene **ToImage**-Methode, die ein Arbeitsblatt direkt in die gewünschte Bilddatei(-en) mit Ihren gewünschten Attributen oder Optionen konvertieren kann. Sie kann ein Objekt des Typs **System.Drawing.Bitmap** zurückgeben und Sie können eine Bilddatei auf die Festplatte/den Stream speichern. Es werden verschiedene Bildformate unterstützt, z.B. .bmp, .png, .gif, .jpg, .jpeg, .tiff, .emf usw.

{{< highlight csharp >}}

//Create a new Workbook object

//Open a template excel file

Workbook book = new Workbook("Sheet to Image.xls");

//Get the first worksheet.

Worksheet sheet = book.Worksheets[0];

//Define ImageOrPrintOptions

ImageOrPrintOptions imgOptions = new ImageOrPrintOptions();

//Specify the image type

imgOptions.ImageType = ImageType.Jpeg;

//Render the sheet with respect to specified image/print options

SheetRender sr = new SheetRender(sheet, imgOptions);

//Render the image for the sheet

Bitmap bitmap = sr.ToImage(0);

//Save the image file

bitmap.Save("SheetImage.jpg");

{{< /highlight >}}
## **Beispielcode herunterladen**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Cells1.0/Worksheet.to.Image.Aspose.Cells.zip)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Worksheet%20to%20Image%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
