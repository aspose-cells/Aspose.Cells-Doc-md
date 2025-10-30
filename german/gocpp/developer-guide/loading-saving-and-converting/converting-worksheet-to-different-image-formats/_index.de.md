---
title: Konvertieren von Arbeitsblättern in verschiedene Bildformate
type: docs
weight: 90
url: /de/go-cpp/converting-worksheet-to-different-image-formats/
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, ein Arbeitsblatt aus einer Arbeitsmappe zu exportieren und in verschiedene Bildformate zu konvertieren. In diesem Artikel wird erläutert, wie ein Arbeitsblatt in verschiedene Bildformate konvertiert werden kann.

{{% /alert %}}

## **Arbeitsblatt in Bild konvertieren**

Arbeitsblätter enthalten Daten, die Sie analysieren möchten. Zum Beispiel kann ein Arbeitsblatt Parameter, Summen, Prozentsätze, Ausnahmen und Berechnungen enthalten.

Als Entwickler müssen Sie möglicherweise Arbeitsblätter als Bilder darstellen. Zum Beispiel könnten Sie ein Bild eines Arbeitsblatts in einer Anwendung oder Webseite verwenden wollen. Möglicherweise möchten Sie ein Bild in ein Microsoft Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation oder einen anderen Dokumenttyp einfügen. Kurz gesagt, Sie möchten ein Arbeitsblatt als Bild gerendert haben, um es anderweitig verwenden zu können.

Aspose.Cells unterstützt die Konvertierung von Excel-Arbeitsblättern in Bilder. Um diese Funktion zu nutzen, müssen Sie den Namespace [Aspose.Cells.Rendering](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) in Ihr Programm oder Projekt importieren. Es enthält mehrere nützliche Klassen für Rendering und Druck, z.B. [SheetRender](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [ImageOrPrintOptions](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), und andere.

Die Klasse [Aspose.Cells.Rendering.ISheetRender](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) repräsentiert ein Arbeitsblatt, das als Bild gerendert werden soll. Sie verfügt über eine überladene Methode, [ToImage](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/), die ein Arbeitsblatt in Bilddateien mit unterschiedlichen Attributen oder Optionen umwandeln kann. Mehrere Bildformate werden unterstützt, z.B. BMP, PNG, GIF, JPG, JPEG, TIFF und EMF.

Der folgende Codeausschnitt zeigt, wie man ein Arbeitsblatt in einer Excel-Datei in eine Bilddatei konvertiert.

### **Excel/Tabellendokument in PNG mit GoLang konvertieren**

Bitte werfen Sie einen Blick auf den folgenden Beispielcode, die [Beispiel-Excel-Datei](67338402.xlsx) und die [Ausgabebilder im PNG-Format](67338401.zip).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Png.go" >}}

### **Excel/Tabellendokument in TIFF mit GoLang konvertieren**

Bitte werfen Sie einen Blick auf den folgenden Beispielcode, die [Beispiel-Excel-Datei](67338402.xlsx) und das [Ausgabe-TIFF-Bild](67338419.zip).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Tiff.go" >}}

## **Excel/Tabellendokument in SVG mit GoLang konvertieren**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_Svg.go" >}}

SVG steht für Skalierbare Vektorgrafiken. SVG ist eine Spezifikation auf der Grundlage von XML-Standards für zweidimensionale Vektorgrafiken. Es ist ein offener Standard, der vom World Wide Web Consortium (W3C) seit 1999 entwickelt wird.

Aspose.Cells for Go via C++ konnte seit Version 24.12.0 Arbeitsblätter in SVG-Bilder umwandeln.

Um diese Funktion zu verwenden, importieren Sie den `Aspose.Cells.Rendering`-Namespace in Ihr Programm oder Projekt. Es verfügt über mehrere wertvolle Klassen für das Rendern und Drucken, wie z. B. `ISheetRender`, `IImageOrPrintOptions` und andere.

Die Klasse `Aspose.Cells.Rendering.IImageOrPrintOptions` gibt an, dass das Arbeitsblatt im SVG-Format gespeichert wird. Der folgende Codeausschnitt zeigt, wie man ein Arbeitsblatt in einer Excel-Datei in eine SVG-Bilddatei konvertiert.

Bitte werfen Sie einen Blick auf den folgenden Beispielcode, die [Beispiel-Excel-Datei](67338402.xlsx) und die [Ausgabe-SVG-Bilder](67338403.zip).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertWorksheetToImage_SVG.go" >}}
