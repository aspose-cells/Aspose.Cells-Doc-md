---
title: Konvertieren eines Arbeitsblatts in ein Bild mithilfe der ImageOrPrint-Optionen
type: docs
weight: 90
url: /de/net/converting-worksheet-to-image-using-imageorprint-options/
---
{{% alert color="primary" %}}

Dieses Dokument soll ein detailliertes Verständnis dafür vermitteln, wie man ein Arbeitsblatt in eine Bilddatei konvertiert und verschiedene Bild- und Druckoptionen für das Bild anwendet, Optionen wie Auflösung, Komprimierung, Bildformat und Seitenqualität.

{{% /alert %}}

##  **Arbeitsblätter in Bildern speichern – verschiedene Ansätze**

Manchmal kann es erforderlich sein, dass Sie Ihre Arbeitsblätter als bildliche Darstellung präsentieren. Sie müssen die Arbeitsblattbilder in Ihren Anwendungen oder Webseiten präsentieren. Möglicherweise müssen Sie die Bilder in ein Word-Dokument, eine PDF-Datei oder eine PowerPoint-Präsentation einfügen oder sie in einem anderen Szenario verwenden. Sie möchten lediglich, dass ein Arbeitsblatt als Bild gerendert wird, damit Sie es an anderer Stelle verwenden können. Aspose.Cells unterstützt die Konvertierung von Arbeitsblättern in Excel-Dateien in Bilder. Außerdem unterstützt Aspose.Cells das Festlegen verschiedener Optionen wie Bildformat, Auflösung (sowohl vertikal als auch horizontal), Bildqualität und andere Bild- und Druckoptionen.

Sie könnten es mit Office Automation versuchen, aber die Office-Automatisierung hat ihre eigenen Nachteile. Es gibt mehrere Gründe und Probleme: zum Beispiel Sicherheit, Stabilität, Skalierbarkeit und Geschwindigkeit, Preis und Funktionen. Kurz gesagt, es gibt viele Gründe, der wichtigste ist, dass Microsoft selbst dringend von der Office-Automatisierung durch Softwarelösungen abrät.

In diesem Artikel wird gezeigt, wie Sie eine Konsolenanwendung in Visual Studio .NET erstellen, die Konvertierung eines Arbeitsblatts in ein Bild mithilfe verschiedener Bild- und Druckoptionen mit wenigen und einfachsten Codezeilen mithilfe von Aspose.Cells API durchführen.

 Sie müssen importieren[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/net/aspose.cells.rendering)Namensraum für Ihr Programm/Projekt. Es verfügt über mehrere wertvolle Klassen, zum Beispiel:[**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions), [**WorkbookRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/workbookrender)usw.

Der[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) Die Klasse stellt ein Arbeitsblatt zum Rendern von Bildern für das Arbeitsblatt dar. Sie ist überladen[**Vorstellen**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender/methods/toimage/index)Methode, die ein Arbeitsblatt direkt in Bilddateien konvertieren kann, die mit Ihren gewünschten Attributen oder Optionen angegeben sind. Es kann ein System.Drawing.Bitmap-Objekt zurückgeben und Sie können eine Bilddatei auf der Festplatte/im Stream speichern. Es werden mehrere Bildformate unterstützt, z. B. BMP, PNG, GIFF, JPEG, TIFF, EMF und so weiter.

##  **Verwenden von Aspose.Cells zum Konvertieren eines Arbeitsblatts in ein Bild mithilfe der ImageOrPrint-Optionen.**

###  **Erstellen einer Vorlagenarbeitsmappe in Microsoft Excel**

Ich habe eine neue Arbeitsmappe in MS Excel erstellt und einige Daten in das erste Arbeitsblatt eingefügt. Jetzt werde ich das Arbeitsblatt „Sheet1“ der Vorlagendatei in eine Bilddatei „SheetImage.tiff“ konvertieren und verschiedene Bildoptionen wie horizontale und vertikale Auflösungen, TiffCompression usw. anwenden.

###  **Laden Sie Aspose.Cells herunter und installieren Sie es**

 Zuerst müssen Sie[herunterladen](https://downloads.aspose.com/cells/net) Aspose.Cells für .Net. Installieren Sie es auf Ihrem Entwicklungscomputer. Alle[Aspose](http://www.aspose.com/)Komponenten arbeiten nach der Installation im Evaluierungsmodus. Der Auswertungsmodus ist zeitlich unbegrenzt und fügt lediglich Wasserzeichen in erstellte Dokumente ein.

###  **Erstellen Sie ein Projekt**

Starten Sie Visual Studio. Net und erstellen Sie eine neue Konsolenanwendung. Dieses Beispiel zeigt eine Konsolenanwendung C#, Sie können aber auch VB.NET verwenden.

###  **Referenzen hinzufügen**

Dieses Projekt verwendet Aspose.Cells. Daher müssen Sie in Ihrem Projekt einen Verweis auf die Komponente Aspose.Cells hinzufügen. Fügen Sie beispielsweise einen Verweis auf ….\Programme\Aspose\Aspose.Cells for .NET\Bin\Net1.0\Aspose.Cells.dll hinzu

###  **Arbeitsblatt in eine Bilddatei konvertieren**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-WorksheetToAnImage-1.cs" >}}

##  **Konvertierungsoptionen**

Es ist möglich, bestimmte Seiten als Bild zu speichern. Der folgende Code konvertiert das erste und zweite Arbeitsblatt in einer Arbeitsmappe in JPG-Bilder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-SpecificPagesToImage-1.cs" >}}

##  **Bildkonvertierung mit WorkbookRender**

Ein TIFF-Bild kann aus mehr als einem Frame bestehen. Sie können die gesamte Arbeitsmappe in einem einzigen TIFF-Bild mit mehreren Frames oder Seiten speichern:

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageOrPrintOptions-UseWorkbookRenderForImageConversion-1.cs" >}}

