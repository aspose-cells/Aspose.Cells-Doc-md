---
title: Konvertieren des Arbeitsblatts in ein Bild mit ImageOrPrint-Optionen
type: docs
weight: 90
url: /de/net/converting-worksheet-to-image-using-imageorprint-options/
---
{{% alert color="primary" %}}

Dieses Dokument soll ein detailliertes Verständnis dafür vermitteln, wie Sie ein Arbeitsblatt in eine Bilddatei konvertieren und verschiedene Bild- und Druckoptionen für das Bild anwenden, Optionen wie Auflösung, TIFF-Komprimierung, Bildformat und Seitenqualität.

{{% /alert %}}

## **Speichern von Arbeitsblättern in Bildern - verschiedene Ansätze**

Manchmal müssen Sie Ihre Arbeitsblätter möglicherweise als bildliche Darstellung präsentieren. Sie müssen die Arbeitsblattbilder in Ihren Anwendungen oder Webseiten präsentieren. Möglicherweise müssen Sie die Bilder in ein Word-Dokument, eine PDF-Datei oder eine PowerPoint-Präsentation einfügen oder sie in einem anderen Szenario verwenden. Sie möchten einfach, dass ein Arbeitsblatt als Bild gerendert wird, damit Sie es an anderer Stelle verwenden können. Aspose.Cells unterstützt die Konvertierung von Arbeitsblättern in Excel-Dateien in Bilder. Außerdem unterstützt Aspose.Cells die Einstellung verschiedener Optionen wie Bildformat, Auflösung (sowohl vertikal als auch horizontal), Bildqualität und andere Bild- und Druckoptionen.

Sie können die Office-Automatisierung ausprobieren, aber die Office-Automatisierung hat ihre eigenen Nachteile. Es gibt mehrere Gründe und Probleme: zum Beispiel Sicherheit, Stabilität, Skalierbarkeit und Geschwindigkeit, Preis und Funktionen. Kurz gesagt, es gibt viele Gründe, wobei der wichtigste darin besteht, dass Microsoft selbst dringend von der Office-Automatisierung durch Softwarelösungen abrät.

Dieser Artikel zeigt, wie Sie eine Konsolenanwendung in Visual Studio .NET erstellen, die Konvertierung eines Arbeitsblatts in ein Bild mit verschiedenen Bild- und Druckoptionen mit wenigen und einfachsten Codezeilen unter Verwendung von Aspose.Cells API durchführen.

 Sie müssen importieren[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering)Namensraum zu Ihrem Programm/Projekt. Es hat mehrere wertvolle Klassen, zum Beispiel[**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)usw.

Das[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) Klasse stellt ein Arbeitsblatt dar, um Bilder für das Arbeitsblatt zu rendern, es hat eine überladene[**Vorstellen**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)Methode, die ein Arbeitsblatt direkt in Bilddatei(en) konvertieren kann, die mit Ihren gewünschten Attributen oder Optionen angegeben sind. Es kann ein System.Drawing.Bitmap-Objekt zurückgeben und Sie können eine Bilddatei auf dem Datenträger/Stream speichern. Es werden mehrere Bildformate unterstützt, zB BMP, PNG, GIFF, JPEG, TIFF, EMF und so weiter.

## **Verwenden von Aspose.Cells zum Konvertieren eines Arbeitsblatts in ein Bild mithilfe von ImageOrPrint-Optionen.**

### **Erstellen einer Vorlagenarbeitsmappe in Microsoft Excel**

Ich habe eine neue Arbeitsmappe in MS Excel erstellt und einige Daten im ersten Arbeitsblatt hinzugefügt. Jetzt werde ich das Arbeitsblatt „Sheet1“ der Vorlagendatei in eine Bilddatei „SheetImage.tiff“ konvertieren und verschiedene Bildoptionen wie horizontale und vertikale Auflösungen, TiffCompression usw. anwenden.

### **Laden Sie Aspose.Cells herunter und installieren Sie es**

 Zuerst müssen Sie[Download](https://downloads.aspose.com/cells/net) Aspose.Cells für .Net. Installieren Sie es auf Ihrem Entwicklungscomputer. Alles[Aspose](http://www.aspose.com/) Komponenten arbeiten, wenn sie installiert sind, im Evaluierungsmodus. Der Bewertungsmodus ist zeitlich unbegrenzt und fügt nur Wasserzeichen in die produzierten Dokumente ein.

### **Erstellen Sie ein Projekt**

Starten Sie Visual Studio. Net und erstellen Sie eine neue Konsolenanwendung. Dieses Beispiel zeigt eine C#-Konsolenanwendung, aber Sie können auch VB.NET verwenden.

### **Referenzen hinzufügen**

Dieses Projekt verwendet Aspose.Cells. Sie müssen also in Ihrem Projekt einen Verweis auf die Komponente Aspose.Cells hinzufügen. Fügen Sie beispielsweise einen Verweis auf ….\Program Files\Aspose\Aspose.Cells for .NET\Bin\Net1.0\Aspose.Cells.dll hinzu

### **Arbeitsblatt in eine Bilddatei konvertieren**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-WorksheetToAnImage-1.cs" >}}

## **Konvertierungsoptionen**

Es ist möglich, bestimmte Seiten als Bild zu speichern. Der folgende Code konvertiert das erste und zweite Arbeitsblatt in einer Arbeitsmappe in JPG-Bilder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-SpecificPagesToImage-1.cs" >}}

## **Bildkonvertierung mit WorkbookRender**

Sie können die Arbeitsmappe durchlaufen und jedes darin enthaltene Arbeitsblatt in ein separates Bild rendern:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-UseWorkbookRenderForImageConversion-1.cs" >}}

