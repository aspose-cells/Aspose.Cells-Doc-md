---
title: Entfernen Sie Leerzeichen aus den Daten, bevor Sie das Bild rendern
type: docs
weight: 270
url: /de/java/remove-white-spaces-from-the-data-before-rendering-to-image/
---
{{% alert color="primary" %}}

Manchmal müssen Sie Arbeitsblattbilder in Anwendungen oder Webseiten präsentieren. Beispielsweise müssen Sie möglicherweise Bilder in ein Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation oder ein anderes Dokument einfügen. Grundsätzlich möchten Sie ein Arbeitsblatt als Bild rendern, damit es in andere Anwendungen eingefügt werden kann. Mit Aspose.Cells-APIs können Sie Microsoft-Excel-Arbeitsblätter in Bilder konvertieren.

{{% /alert %}}

 Das[**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)-Klasse kann ein Arbeitsblatt in eine Bilddatei mit beliebigen angegebenen Attributen konvertieren, z. B. Bildformat, paginierte Blätter usw. Mehrere Bildformate werden unterstützt, darunter BMP, GIF, JPG, TIFF und EMF.

 Wenn Sie die Blatt-zu-Bild-Funktion verwenden, hat das Ausgabebild standardmäßig einen weißen/leeren Bereich, d. h. einen Rand. Sie können dies entfernen. Legen Sie die oberen, linken, unteren und rechten Seiteneinrichtungsränder für das Quellarbeitsblatt auf 0 fest und geben Sie sie an[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)Attribute entsprechend.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-RemoveWhitespaceAroundData-1.java" >}}
