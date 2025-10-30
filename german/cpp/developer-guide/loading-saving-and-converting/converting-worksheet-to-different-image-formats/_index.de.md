---
title: Konvertieren von Arbeitsblättern in verschiedene Bildformate
type: docs
weight: 90
url: /de/cpp/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}} 

Aspose.Cells ermöglicht es Ihnen, ein Arbeitsblatt aus einer Arbeitsmappe zu exportieren und in verschiedene Bildformate zu konvertieren. In diesem Artikel wird erläutert, wie ein Arbeitsblatt in verschiedene Bildformate konvertiert werden kann.

{{% /alert %}} 
## **Arbeitsblatt in Bild konvertieren**
Arbeitsblätter enthalten Daten, die Sie analysieren möchten. Zum Beispiel kann ein Arbeitsblatt Parameter, Summen, Prozentsätze, Ausnahmen und Berechnungen enthalten.

Als Entwickler müssen Sie möglicherweise Arbeitsblätter als Bilder präsentieren. Möglicherweise müssen Sie beispielsweise ein Bild eines Arbeitsblatts in einer Anwendung oder auf einer Webseite verwenden. Sie möchten möglicherweise ein Bild in ein Microsoft Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation oder einen anderen Dokumententyp einfügen. Kurz gesagt, Sie möchten ein Arbeitsblatt als Bild gerendert haben, damit Sie es an anderer Stelle verwenden können.

Aspose.Cells unterstützt die Konvertierung von Excel-Arbeitsblättern in Bilder. Um diese Funktion zu verwenden, müssen Sie den [Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) Namespace in Ihr Programm oder Projekt importieren. Es verfügt über mehrere wertvolle Klassen für das Rendern und Drucken, wie z. B. [SheetRender](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [ImageOrPrintOptions](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) und andere.

Die Klasse `Aspose.Cells.Rendering.ISheetRender` stellt ein Arbeitsblatt dar, das als Bilder gerendert werden soll. Sie verfügt über eine überladene Methode, [ToImage](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/), die ein Arbeitsblatt in Bilddatei(en) mit verschiedenen Attributen oder Optionen konvertieren kann. Mehrere Bildformate werden unterstützt, wie z.B. BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Der folgende Codeausschnitt zeigt, wie man ein Arbeitsblatt in einer Excel-Datei in eine Bilddatei konvertiert.
### **PNG-Format**
Bitte werfen Sie einen Blick auf den folgenden Beispielcode, die [Beispiel-Excel-Datei](67338402.xlsx) und die [Ausgabebilder im PNG-Format](67338401.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_PNG-new.cpp" >}}

### **TIFF-Format**
Bitte werfen Sie einen Blick auf den folgenden Beispielcode, die [Beispiel-Excel-Datei](67338402.xlsx) und das [Ausgabe-TIFF-Bild](67338419.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_TIFF-new.cpp" >}}

## **Arbeitsblatt in SVG konvertieren**
SVG steht für Skalierbare Vektorgrafiken. SVG ist eine Spezifikation auf der Grundlage von XML-Standards für zweidimensionale Vektorgrafiken. Es ist ein offener Standard, der vom World Wide Web Consortium (W3C) seit 1999 entwickelt wird.

Aspose.Cells for C++ kann Arbeitsblätter seit der Version 18.5.0 in SVG-Bilder konvertieren.

Um diese Funktion zu verwenden, importieren Sie den `Aspose.Cells.Rendering`-Namespace in Ihr Programm oder Projekt. Es verfügt über mehrere wertvolle Klassen für das Rendern und Drucken, wie z. B. `ISheetRender`, `IImageOrPrintOptions` und andere.

Die Klasse `Aspose.Cells.Rendering.IImageOrPrintOptions` gibt an, dass das Arbeitsblatt im SVG-Format gespeichert wird. Der folgende Codeausschnitt zeigt, wie man ein Arbeitsblatt in einer Excel-Datei in eine SVG-Bilddatei konvertiert.

Bitte werfen Sie einen Blick auf den folgenden Beispielcode, die [Beispiel-Excel-Datei](67338402.xlsx) und die [Ausgabe-SVG-Bilder](67338403.zip).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadingSavingAndConverting-ConvertingWorksheetToImage_SVG-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
