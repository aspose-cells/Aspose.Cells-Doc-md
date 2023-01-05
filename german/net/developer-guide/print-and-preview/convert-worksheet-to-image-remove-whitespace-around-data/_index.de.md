---
title: Arbeitsblatt in Bild konvertieren - Entfernen Sie Leerzeichen um Daten
type: docs
weight: 40
url: /de/net/convert-worksheet-to-image-remove-whitespace-around-data/
---
{{% alert color="primary" %}}

Manchmal müssen Sie Arbeitsblattbilder in Anwendungen oder Webseiten präsentieren. Beispielsweise müssen Sie möglicherweise Bilder in ein Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation oder ein anderes Dokument einfügen. Grundsätzlich möchten Sie ein Arbeitsblatt als Bild rendern, damit es in andere Anwendungen eingefügt werden kann. Mit Aspose.Cells können Sie Microsoft Excel-Arbeitsblätter in Bilder konvertieren.

{{% /alert %}}

## **Entfernen Sie Leerzeichen um Daten**

 Das[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender)API konvertiert ein Arbeitsblatt in eine Bilddatei mit beliebigen angegebenen Attributen, z. B. Bildformat, paginierte Blätter usw. Mehrere Bildformate werden unterstützt, darunter BMP, GIF, JPG, TIFF und EMF.

 Wenn Sie die Blatt-zu-Bild-Funktion verwenden, hat das Ausgabebild standardmäßig Leerzeichen, d. h. einen Rand. Sie können dies entfernen, indem Sie die oberen, unteren, linken und rechten Seiteneinrichtungsränder für das Quellarbeitsblatt auf 0 setzen und angeben[**Aspose.Cells.Rendering.ImageOrPrintOptions**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions)Attribute entsprechend.

Das folgende Code-Snippet entfernt den Leerraum um die Daten im Ausgabebild.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveWhitespaceAroundData-1.cs" >}}

