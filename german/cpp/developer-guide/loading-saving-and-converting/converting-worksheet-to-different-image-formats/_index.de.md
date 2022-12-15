---
title: Konvertieren von Arbeitsblättern in verschiedene Bildformate
type: docs
weight: 90
url: /de/cpp/converting-worksheet-to-different-image-formats/
---
{{% alert color="primary" %}} 

Aspose.Cells ermöglicht es Ihnen, ein Arbeitsblatt aus einer Arbeitsmappe zu exportieren und es in verschiedene Bildformate zu konvertieren. In diesem Artikel wird erläutert, wie Sie ein Arbeitsblatt in andere Bildformate konvertieren.

{{% /alert %}} 
## **Arbeitsblatt in Bild umwandeln**
Arbeitsblätter enthalten Daten, die Sie analysieren möchten. Ein Arbeitsblatt kann beispielsweise Parameter, Summen, Prozentsätze, Ausnahmen und Berechnungen enthalten.

Als Entwickler müssen Sie möglicherweise Arbeitsblätter als Bilder präsentieren. Beispielsweise müssen Sie möglicherweise ein Bild eines Arbeitsblatts in einer Anwendung oder Webseite verwenden. Vielleicht möchten Sie ein Bild in ein Microsoft-Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation oder einen anderen Dokumenttyp einfügen. Einfach ausgedrückt, Sie möchten, dass ein Arbeitsblatt als Bild gerendert wird, damit Sie es an anderer Stelle verwenden können.

Aspose.Cells unterstützt die Konvertierung von Excel-Arbeitsblättern in Bilder. Um diese Funktion nutzen zu können, müssen Sie die[Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.rendering)Namensraum zu Ihrem Programm oder Projekt. Es hat mehrere wertvolle Klassen zum Rendern und Drucken, zum Beispiel[ISheetRender](https://reference.aspose.com/cells/cpp/class/aspose.cells.rendering.i_sheet_render), [IImageOrPrintOptions](https://reference.aspose.com/cells/cpp/class/aspose.cells.rendering.i_image_or_print_options)und andere.

Die Klasse `Aspose.Cells.Rendering.ISheetRender` stellt ein Arbeitsblatt dar, das als Bilder gerendert werden soll. Es hat eine überladene Methode,[Vorstellen](https://reference.aspose.com/cells/cpp/class/aspose.cells.rendering.i_sheet_render#ae508827a76d0c353ab0890024ec363c5), die ein Arbeitsblatt in Bilddatei(en) mit unterschiedlichen Attributen oder Optionen konvertieren kann. Mehrere Bildformate werden unterstützt, zum Beispiel BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Das folgende Code-Snippet zeigt, wie Sie ein Arbeitsblatt in einer Excel-Datei in eine Bilddatei konvertieren.
### **PNG-Format**
 Bitte sehen Sie sich den folgenden Beispielcode an, its[Beispiel-Excel-Datei](67338402.xlsx) , und die[PNG-Bilder ausgeben](67338401.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_PNG.cpp" >}}
### **TIFF-Format**
 Bitte sehen Sie sich den folgenden Beispielcode an, its[Beispiel-Excel-Datei](67338402.xlsx) , und die[TIFF-Bild ausgeben](67338419.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_TIFF.cpp" >}}
## **Arbeitsblatt in SVG konvertieren**
SVG steht für Scalable Vector Graphics. SVG ist eine auf XML-Standards basierende Spezifikation für zweidimensionale Vektorgrafiken. Es ist ein offener Standard, der seit 1999 vom World Wide Web Consortium (W3C) entwickelt wird.

Aspose.Cells for C++ kann seit Version 18.5.0 Arbeitsblätter in SVG-Bilder konvertieren.

Um diese Funktion zu verwenden, importieren Sie den Namespace `Aspose.Cells.Rendering` in Ihr Programm oder Projekt. Es hat mehrere wertvolle Klassen zum Rendern und Drucken, zum Beispiel `ISheetRender`, `IImageOrPrintOptions` und andere.

Die Klasse `Aspose.Cells.Rendering.IImageOrPrintOptions` gibt an, dass das Arbeitsblatt im SVG-Format gespeichert wird. Das folgende Code-Snippet zeigt, wie Sie ein Arbeitsblatt in einer Excel-Datei in eine SVG-Bilddatei konvertieren

 Bitte sehen Sie sich den folgenden Beispielcode an, its[Beispiel-Excel-Datei](67338402.xlsx) , und die[SVG-Bilder ausgeben](67338403.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_SVG.cpp" >}}
