---
title: Arbeitsblatt in Bild mithilfe von Bild oder Druckoptionen konvertieren
type: docs
weight: 90
url: /de/python-net/converting-worksheet-to-image-using-imageorprint-options/
---

{{% alert color="primary" %}}

Dieses Dokument ist darauf ausgelegt, ein detailliertes Verständnis dafür zu vermitteln, wie man ein Arbeitsblatt in eine Bilddatei konvertiert und verschiedene Bilddruckoptionen für das Bild anwendet, Optionen wie Auflösung, TIFF-Komprimierung, Bildformat und Seitenqualität.

{{% /alert %}}

## **Arbeitsblätter als Bilder speichern - Unterschiedliche Ansätze**

Manchmal möchten Sie Ihre Worksheets als bildliche Darstellung präsentieren. Sie möchten die Worksheet-Bilder in Ihren Anwendungen oder auf Webseiten einfügen. Möglicherweise müssen Sie die Bilder in ein Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation oder in ein anderes Szenario einfügen. Einfach gesagt, Sie wollen ein Worksheet als Bild rendern, um es anderweitig verwenden zu können. Aspose.Cells für Python via .NET unterstützt die Konvertierung von Worksheets in Excel-Dateien in Bilder. Außerdem erlaubt Aspose.Cells für Python via .NET das Festlegen verschiedener Optionen wie Bildformat, Auflösung (vertikal und horizontal), Bildqualität sowie weitere Bild- und Druckeinstellungen.

Sie könnten Office-Automatisierung ausprobieren, aber Office-Automatisierung hat ihre eigenen Nachteile. Es gibt mehrere Gründe und Probleme, wie zum Beispiel Sicherheit, Stabilität, Skalierbarkeit und Geschwindigkeit, Preis und Funktionen. Kurz gesagt gibt es viele Gründe, wobei der Hauptgrund darin besteht, dass Microsoft selbst stark von der Office-Automatisierung bei Softwarelösungen abrät.

Dieser Artikel zeigt, wie man eine Konsolenanwendung in Visual Studio .NET erstellt, die Konvertierung eines Worksheets in ein Bild mithilfe verschiedener Bild- und Druckoptionen mit wenigen und einfachen Codezeilen unter Verwendung der Aspose.Cells für Python via .NET API durchführt.

Sie müssen den Namespace [**aspose.cells.rendering**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering) in Ihr Programm/Projekt importieren. Es hat mehrere wertvolle Klassen, zum Beispiel [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/workbookrender) usw.

Die Klasse [**SheetRender**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender) stellt ein Arbeitsblatt dar, um Bilder für das Arbeitsblatt zu rendern. Sie verfügt über eine überladene Methode [**to_image**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/sheetrender/to_image/#int-str), die ein Arbeitsblatt direkt in Bilddatei(en) mit den gewünschten Attributen oder Optionen konvertieren kann. Sie kann ein System.Drawing.Bitmap-Objekt zurückgeben und Sie können eine Bilddatei auf die Festplatte/den Stream speichern. Es werden mehrere Bildformate unterstützt, z.B. BMP, PNG, GIF, JPEG, TIFF, EMF und so weiter.

## **Verwendung von Aspose.Cells zum Konvertieren des Worksheets in ein Bild unter Verwendung von ImageOrPrint-Optionen**

### **Erstellen einer Vorlagenarbeitsmappe in Microsoft Excel**

Ich habe eine neue Arbeitsmappe in MS Excel erstellt und einige Daten im ersten Arbeitsblatt hinzugefügt. Jetzt werde ich das Arbeitsblatt der Vorlagendatei "Sheet1" in eine Bilddatei "SheetImage.tiff" konvertieren und verschiedene Bilddateiloptionen wie horizontale und vertikale Auflösungen, Tiff-Kompression usw. anwenden.

### **Arbeitsblatt in eine Bilddatei konvertieren**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-WorksheetToAnImage-1.py" >}}


## **Bildkonvertierung mit WorkbookRender**

Ein TIFF-Bild kann mehr als einen Frame enthalten. Sie können die gesamte Arbeitsmappe in ein einzelnes TIFF-Bild mit mehreren Frames oder Seiten speichern:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-UseWorkbookRenderForImageConversion-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
