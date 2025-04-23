---
title: Arbeitsblatt in Bild und Arbeitsblatt in Bild pro Seite konvertieren
type: docs
weight: 80
url: /de/net/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}

Dieses Dokument soll den Entwicklern ein detailliertes Verständnis vermitteln, wie man ein Arbeitsblatt in eine Bilddatei und ein Arbeitsblatt mit mehreren Seiten in eine Bilddatei pro Seite umwandelt.

Manchmal müssen Arbeitsblätter als Bilder präsentiert werden, zum Beispiel um sie in Anwendungen oder Webseiten zu verwenden. Sie müssen die Bilder möglicherweise in ein Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation einfügen oder sie in einem anderen Szenario verwenden. Im Grunde genommen möchten Sie das Arbeitsblatt als Bild rendern. Aspose.Cells unterstützt die Umwandlung von Arbeitsblättern in Microsoft Excel-Dateien in Bilder. Außerdem unterstützt Aspose.Cells die Umwandlung eines Arbeitsmappen in mehrere Bilddateien, eine pro Seite.

Möglicherweise verwenden Sie Office Automation, um dies zu erreichen, aber Office-Automation hat ihre eigenen Nachteile. Es gibt mehrere Gründe und Probleme, beispielsweise Sicherheit, Stabilität, Skalierbarkeit/Geschwindigkeit, Preis und Funktionen. Kurz gesagt, es gibt viele Gründe, aber der Hauptgrund ist, dass Microsoft selbst dringend von der Verwendung von Office-Automation abrät.

{{% /alert %}}

## **Verwendung von Aspose.Cells zum Konvertieren eines Arbeitsblatts in eine Bilddatei**

In diesem Artikel wird gezeigt, wie man eine Konsolenanwendung in Visual Studio erstellt, ein Arbeitsblatt in ein Bild konvertiert und ein Arbeitsblatt mit wenigen und einfachsten Codezeilen in ein Bild pro Arbeitsblatt umwandelt, indem man die Aspose.Cells API verwendet.

Sie müssen den Namespace [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) in Ihr Programm/Projekt importieren. Es hat mehrere wertvolle Klassen, wie [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) usw. Die Klasse [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) repräsentiert ein Arbeitsblatt zum Rendern von Bildern für das Arbeitsblatt und verfügt über eine überladene Methode [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index), die direkt ein Arbeitsblatt in Bilddateien mit beliebigen Attributen oder festgelegten Optionen umwandeln kann. Es kann ein System.Drawing.Bitmap-Objekt zurückgeben und Sie können eine Bilddatei auf die Festplatte/stream speichern. Es werden mehrere Bildformate unterstützt, zum Beispiel BMP, PNG, GIF, JPG, JPEG, TIFF, EMF und andere.

Dieser Artikel erklärt, wie:

- Ein Arbeitsblatt in ein Bild konvertiert wird
- Jede Seite in einem Arbeitsblatt in ein Bild konvertiert wird

Diese Aufgabe zeigt, wie man Aspose.Cells verwendet, um ein Arbeitsblatt aus einer Vorlagenarbeitsmappe in eine Bilddatei zu konvertieren.

### **Setup-Projekt**

1. Zuerst [download Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1. Installieren Sie es auf Ihrem Entwicklungscomputer. Alle [Aspose](http://www.aspose.com/) -Komponenten, wenn sie installiert sind, arbeiten im Evaluierungsmodus. Der Evaluierungsmodus hat kein Zeitlimit und fügt nur Wasserzeichen in die erstellten Dokumente ein. Starten Sie nun Visual Studio.Net und erstellen Sie eine neue Konsolenanwendung. Dieses Beispiel verwendet eine C#-Konsolenanwendung, aber Sie können auch VB.NET verwenden. Fügen Sie dem erstellten Projekt einen Verweis auf Aspose.Cells hinzu.

### **Arbeitsblatt in Bilddatei konvertieren**

Ich habe eine neue Arbeitsmappe in Microsoft Excel erstellt und einige Daten im ersten Arbeitsblatt hinzugefügt: **Testbook.xlsx** (1 Arbeitsblatt). Konvertieren Sie als Nächstes das Arbeitsblatt Sheet1 der Vorlagendatei in eine Bilddatei namens SheetImage.jpg.

Nachfolgend ist der von der Komponente verwendete Code, um die Aufgabe zu erledigen. Es konvertiert Sheet1 in **Testbook.xlsx** in eine Bilddatei, um zu erklären, wie einfach diese Konvertierung ist.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheettoImageFile-1.cs" >}}

## **Verwendung von Aspose.Cells zur Konvertierung eines Arbeitsblatts in eine Bilddatei nach Seite**

Dieses Beispiel zeigt, wie man Aspose.Cells verwendet, um ein Arbeitsblatt aus einer Vorlagenarbeitsmappe, die mehrere Seiten hat, in eine Bilddatei pro Seite zu konvertieren.

### **Arbeitsblatt nach Seite in Bild konvertieren**

Ich habe eine neue Arbeitsmappe in Microsoft Excel erstellt und einige Daten im ersten Arbeitsblatt hinzugefügt: **Testbook2.xlsx** (1 Arbeitsblatt).

Konvertieren Sie jetzt das Arbeitsblatt Sheet1 der Vorlagendatei in Bilddateien (eine Datei pro Seite). Da ich die Konsolenanwendung bereits erstellt habe, um die Kopieraufgabe auszuführen, werde ich diese Schritte zur Erstellung der Konsolenanwendung überspringen und direkt zu den Arbeitsblattkonvertierungsschritten übergehen.

Nachfolgend ist der von der Komponente verwendete Code, um die Aufgabe zu erledigen. Es konvertiert Sheet1 in Testbook2.xlsx in Bilddateien nach Seite.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ConvertingWorksheetToImage-ConvertWorksheetToImageByPage-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
