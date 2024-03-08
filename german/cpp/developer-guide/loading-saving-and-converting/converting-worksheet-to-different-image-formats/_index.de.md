---
title: Arbeitsblatt in verschiedene Bildformate konvertieren
type: docs
weight: 90
url: /de/cpp/converting-worksheet-to-different-image-formats/
---
{{% alert color="primary" %}} 

Mit Aspose.Cells können Sie ein Arbeitsblatt aus einer Arbeitsmappe exportieren und in verschiedene Bildformate konvertieren. In diesem Artikel wird erläutert, wie Sie ein Arbeitsblatt in verschiedene Bildformate konvertieren.

{{% /alert %}} 
##  **Konvertieren eines Arbeitsblatts in ein Bild**
Arbeitsblätter enthalten Daten, die Sie analysieren möchten. Ein Arbeitsblatt kann beispielsweise Parameter, Summen, Prozentsätze, Ausnahmen und Berechnungen enthalten.

Als Entwickler müssen Sie möglicherweise Arbeitsblätter als Bilder präsentieren. Beispielsweise müssen Sie möglicherweise ein Bild eines Arbeitsblatts in einer Anwendung oder Webseite verwenden. Möglicherweise möchten Sie ein Bild in ein Word-Dokument Microsoft, eine Datei PDF, eine Präsentation PowerPoint oder einen anderen Dokumenttyp einfügen. Einfach ausgedrückt: Sie möchten, dass ein Arbeitsblatt als Bild gerendert wird, damit Sie es woanders verwenden können.

Aspose.Cells unterstützt die Konvertierung von Excel-Arbeitsblättern in Bilder. Um diese Funktion nutzen zu können, müssen Sie die importieren[Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/)Namensraum für Ihr Programm oder Projekt. Es verfügt über mehrere wertvolle Klassen zum Rendern und Drucken, zum Beispiel:[SheetRender](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [ImageOrPrintOptions](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)und andere.

Die Klasse `Aspose.Cells.Rendering.ISheetRender` stellt ein Arbeitsblatt dar, das als Bilder gerendert werden soll. Es hat eine überladene Methode,[Vorstellen](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/), das ein Arbeitsblatt in Bilddateien mit unterschiedlichen Attributen oder Optionen konvertieren kann. Es werden mehrere Bildformate unterstützt, zum Beispiel BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Der folgende Codeausschnitt zeigt, wie ein Arbeitsblatt in einer Excel-Datei in eine Bilddatei konvertiert wird.
###  **PNG Format**
 Bitte sehen Sie sich den folgenden Beispielcode an:[Beispiel-Excel-Datei](67338402.xlsx) , und das[Ausgabe PNG Bilder](67338401.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_PNG-new.cpp" >}}

###  **TIFF Format**
 Bitte sehen Sie sich den folgenden Beispielcode an:[Beispiel-Excel-Datei](67338402.xlsx) , und das[Ausgabe TIFF Bild](67338419.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_TIFF-new.cpp" >}}

##  **Konvertieren des Arbeitsblatts in SVG**
SVG steht für Scalable Vector Graphics. SVG ist eine auf XML-Standards basierende Spezifikation für zweidimensionale Vektorgrafiken. Es handelt sich um einen offenen Standard, der seit 1999 vom World Wide Web Consortium (W3C) entwickelt wird.

Aspose.Cells for C++ kann seit Version 18.5.0 Arbeitsblätter in das Bild SVG konvertieren.

Um diese Funktion zu nutzen, importieren Sie den Namespace `Aspose.Cells.Rendering` in Ihr Programm oder Projekt. Es verfügt über mehrere wertvolle Klassen zum Rendern und Drucken, zum Beispiel `ISheetRender`, `IImageOrPrintOptions` und andere.

Die Klasse `Aspose.Cells.Rendering.IImageOrPrintOptions` gibt an, dass das Arbeitsblatt im Format SVG gespeichert wird. Der folgende Codeausschnitt zeigt, wie ein Arbeitsblatt in einer Excel-Datei in eine SVG-Bilddatei konvertiert wird

 Bitte sehen Sie sich den folgenden Beispielcode an:[Beispiel-Excel-Datei](67338402.xlsx) , und das[Ausgabe SVG Bilder](67338403.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_SVG-new.cpp" >}}
