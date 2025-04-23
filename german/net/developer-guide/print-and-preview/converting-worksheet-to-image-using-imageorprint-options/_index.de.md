---
title: Arbeitsblatt in Bild mithilfe von Bild oder Druckoptionen konvertieren
type: docs
weight: 90
url: /de/net/converting-worksheet-to-image-using-imageorprint-options/
---

{{% alert color="primary" %}}

Dieses Dokument ist darauf ausgelegt, ein detailliertes Verständnis dafür zu vermitteln, wie man ein Arbeitsblatt in eine Bilddatei konvertiert und verschiedene Bilddruckoptionen für das Bild anwendet, Optionen wie Auflösung, TIFF-Komprimierung, Bildformat und Seitenqualität.

{{% /alert %}}

## **Arbeitsblätter als Bilder speichern - Unterschiedliche Ansätze**

Manchmal müssen Sie Ihre Arbeitsblätter als bildliche Darstellung präsentieren. Möglicherweise müssen Sie die Arbeitsblattbilder in Ihre Anwendungen oder Webseiten einfügen. Sie müssen möglicherweise die Bilder in ein Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation einfügen oder sie in einem anderen Szenario verwenden. Sie möchten einfach ein Arbeitsblatt als Bild gerendert haben, um es anderswo verwenden zu können. Aspose.Cells unterstützt die Konvertierung von Arbeitsblättern in Excel-Dateien in Bilder. Außerdem unterstützt Aspose.Cells das Festlegen unterschiedlicher Optionen wie Bildformat, Auflösung (sowohl vertikal als auch horizontal), Bildqualität und weitere Bild- und Druckoptionen.

Sie könnten Office-Automatisierung ausprobieren, aber Office-Automatisierung hat ihre eigenen Nachteile. Es gibt mehrere Gründe und Probleme, wie zum Beispiel Sicherheit, Stabilität, Skalierbarkeit und Geschwindigkeit, Preis und Funktionen. Kurz gesagt gibt es viele Gründe, wobei der Hauptgrund darin besteht, dass Microsoft selbst stark von der Office-Automatisierung bei Softwarelösungen abrät.

Dieser Artikel zeigt, wie man eine Konsolenanwendung in Visual Studio .NET erstellt, die Konvertierung eines Arbeitsblatts in ein Bild mithilfe verschiedener Bild- und Druckoptionen mit wenigen und einfachsten Codezeilen mithilfe der Aspose.Cells-API durchführt.

Sie müssen den Namespace [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering) in Ihr Programm/Projekt importieren. Es hat mehrere wertvolle Klassen, zum Beispiel [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender) usw.

Die Klasse [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) stellt ein Arbeitsblatt dar, um Bilder für das Arbeitsblatt zu rendern. Sie verfügt über eine überladene Methode [**ToImage**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index), die ein Arbeitsblatt direkt in Bilddatei(en) mit den gewünschten Attributen oder Optionen konvertieren kann. Sie kann ein System.Drawing.Bitmap-Objekt zurückgeben und Sie können eine Bilddatei auf die Festplatte/den Stream speichern. Es werden mehrere Bildformate unterstützt, z.B. BMP, PNG, GIF, JPEG, TIFF, EMF und so weiter.

## **Verwenden von Aspose.Cells zur Konvertierung von Arbeitsblättern in Bilder unter Verwendung von Bild- oder Druckoptionen.**

### **Erstellen einer Vorlagenarbeitsmappe in Microsoft Excel**

Ich habe eine neue Arbeitsmappe in MS Excel erstellt und einige Daten im ersten Arbeitsblatt hinzugefügt. Jetzt werde ich das Arbeitsblatt der Vorlagendatei "Sheet1" in eine Bilddatei "SheetImage.tiff" konvertieren und verschiedene Bilddateiloptionen wie horizontale und vertikale Auflösungen, Tiff-Kompression usw. anwenden.

### **Aspose.Cells herunterladen und installieren**

Zunächst müssen Sie [Aspose.Cells für .NET](https://downloads.aspose.com/cells/net) herunterladen. Installieren Sie es auf Ihrem Entwicklungssystem. Alle [Aspose](http://www.aspose.com/)-Komponenten funktionieren im Installationsfall im Evaluierungsmodus. Der Evaluierungsmodus hat keine zeitliche Begrenzung und fügt nur Wasserzeichen in erstellte Dokumente ein.

### **Ein Projekt erstellen**

Starten Sie Visual Studio .NET und erstellen Sie eine neue Konsolenanwendung. Dieses Beispiel zeigt eine C# Konsolenanwendung, aber Sie können auch VB.NET verwenden.

### **Referenzen hinzufügen**

Dieses Projekt wird Aspose.Cells verwenden. Sie müssen also eine Referenz zur Aspose.Cells-Komponente in Ihr Projekt hinzufügen. Fügen Sie zum Beispiel eine Referenz zu ....\Program Files\Aspose\Aspose.Cells for .NET\Bin\Net1.0\Aspose.Cells.dll hinzu.

### **Arbeitsblatt in eine Bilddatei konvertieren**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-WorksheetToAnImage-1.cs" >}}

## **Konversionsoptionen**

Es ist möglich, bestimmte Seiten als Bild zu speichern. Der folgende Code konvertiert die ersten und zweiten Arbeitsblätter in einer Arbeitsmappe in JPG-Bilder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-SpecificPagesToImage-1.cs" >}}

## **Bildkonvertierung mit WorkbookRender**

Ein TIFF-Bild kann mehr als einen Frame enthalten. Sie können die gesamte Arbeitsmappe in ein einzelnes TIFF-Bild mit mehreren Frames oder Seiten speichern:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-UseWorkbookRenderForImageConversion-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
