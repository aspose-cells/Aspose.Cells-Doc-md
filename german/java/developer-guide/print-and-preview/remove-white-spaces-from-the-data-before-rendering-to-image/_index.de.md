---
title: Leerzeichen aus den Daten entfernen, bevor sie als Bild gerendert werden
type: docs
weight: 270
url: /de/java/remove-white-spaces-from-the-data-before-rendering-to-image/
---

{{% alert color="primary" %}}

Manchmal müssen Arbeitsblattbilder in Anwendungen oder Webseiten präsentiert werden. Sie müssen beispielsweise ein Bild in ein Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation oder ein anderes Dokument einfügen. Grundsätzlich möchten Sie ein Arbeitsblatt als Bild rendern, damit es in andere Anwendungen eingefügt werden kann. Die Aspose.Cells-APIs ermöglichen es Ihnen, Microsoft Excel-Arbeitsblätter in Bilder umzuwandeln.

{{% /alert %}}

Die [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)-Klasse kann ein Arbeitsblatt in eine Bilddatei mit beliebigen Attributen konvertieren, zum Beispiel Bildformat, paginierte Blätter usw. Mehrere Bildformate werden unterstützt, darunter BMP, GIF, JPG, TIFF und EMF.

Wenn Sie die Blatt-in-Bild-Funktion verwenden, hat das Ausgabebild standardmäßig einen weißen/leeren Bereich, d.h. einen Rand, um sich herum. Sie können dies entfernen. Legen Sie die oberen, linken, unteren und rechten Seiteneinrichtungsmargen für das Quellarbeitsblatt auf 0 fest und spezifizieren Sie entsprechende [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)-Attribute.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-RemoveWhitespaceAroundData-1.java" >}}
