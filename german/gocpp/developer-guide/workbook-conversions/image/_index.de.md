---
title: Excel in Bild konvertieren mit Golang über C++
linktitle: Excel in Bild konvertieren
type: docs
weight: 300
url: /de/go-cpp/convert-excel-to-image/
description: Erfahren Sie, wie Sie Excel Arbeitsblätter mit Aspose.Cells for C++ in Bilder, einschließlich TIFF und SVG, umwandeln.
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, ein Arbeitsblatt aus der Arbeitsmappe zu exportieren und in verschiedene Formate zu konvertieren. Dieser Artikel erklärt, wie man ein Arbeitsblatt in verschiedene Formate konvertiert.

{{% /alert %}}

## Arbeitsmappe in TIFF konvertieren

Eine Excel-Datei kann mehrere Blätter und Seiten enthalten. [**WorkbookRender**](https://reference.aspose.com/cells/go-cpp/workbookrender/) ermöglicht die Konvertierung von Excel in TIFF mit mehreren Seiten. Außerdem können Sie mehrere Optionen für TIFF steuern, wie [Kompression](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/), [GetTiffColorDepth()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettiffcolordepth/), Auflösung ([GetHorizontalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/), [GetVerticalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/)).

Der folgende Code zeigt, wie Excel in TIFF mit mehreren Seiten konvertiert wird. Die [Quell-Excel-Datei](workbook-to-tiff-with-mulitiple-pages.xlsx) und das generierte TIFF-Bild (workbook-to-tiff-with-mulitiple-pages.tiff) sind als Referenz angehängt.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image.go" >}}
## **Arbeitsblatt in Bild konvertieren**

Arbeitsblätter enthalten Daten, die Sie analysieren möchten. Zum Beispiel kann ein Arbeitsblatt Parameter, Summen, Prozentsätze, Ausnahmen und Berechnungen enthalten.

Als Entwickler müssen Sie möglicherweise Arbeitsblätter als Bilder präsentieren. Möglicherweise müssen Sie beispielsweise ein Bild eines Arbeitsblatts in einer Anwendung oder auf einer Webseite verwenden. Sie möchten möglicherweise ein Bild in ein Microsoft Word-Dokument, eine PDF-Datei, eine PowerPoint-Präsentation oder einen anderen Dokumententyp einfügen. Kurz gesagt, Sie möchten ein Arbeitsblatt als Bild gerendert haben, damit Sie es an anderer Stelle verwenden können.

Aspose.Cells unterstützt die Konvertierung von Excel-Arbeitsblättern in Bilder. Um diese Funktion zu nutzen, müssen Sie den [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/go-cpp/)-Namensraum in Ihr Programm oder Projekt importieren. Es verfügt über mehrere wertvolle Klassen zum Rendern und Drucken, zum Beispiel [**SheetRender**](https://reference.aspose.com/cells/go-cpp/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/go-cpp/workbookrender/) und andere.

Die [**SheetRender**](https://reference.aspose.com/cells/go-cpp/sheetrender/)-Klasse repräsentiert ein Arbeitsblatt, das als Bild gerendert werden soll. Sie hat eine überladene Methode, [**ToImage**](https://reference.aspose.com/cells/go-cpp/sheetrender/toimage/), die ein Arbeitsblatt mit verschiedenen Attributen oder Optionen in Bilddateien umwandeln kann. Es gibt ein `System.Drawing.Bitmap`-Objekt zurück und Sie können eine Bilddatei auf Festplatte oder Stream speichern. Verschiedene Bildformate werden unterstützt, zum Beispiel BMP, PNG, GIF, JPG, JPEG, TIFF, EMF.

Der folgende Codeausschnitt zeigt, wie man ein Arbeitsblatt in einer Excel-Datei in eine Bilddatei konvertiert.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image-1.go" >}}
{{% alert color="primary" %}}

Zum jetzigen Zeitpunkt unterstützt die API zur Konvertierung von Arbeitsblättern in Bilder keine 3D-Bubble-Diagramme.

{{% /alert %}}

## **Arbeitsblatt in SVG konvertieren**

SVG steht für Skalierbare Vektorgrafiken. SVG ist eine Spezifikation auf der Grundlage von XML-Standards für zweidimensionale Vektorgrafiken. Es ist ein offener Standard, der vom World Wide Web Consortium (W3C) seit 1999 entwickelt wird.

Aspose.Cells for C++ konnte seit Version 7.1.0 Arbeitsblätter in SVG-Bilder umwandeln. Das folgende Codebeispiel zeigt, wie man ein Arbeitsblatt in einer Excel-Datei in eine SVG-Bilddatei konvertiert.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Image-2.go" >}}
## **Erweiterte Themen**
- [Konvertieren Sie ein Excel-Diagramm in ein Bild](/cells/de/cpp/convert-an-excel-chart-to-image/)
- [Konvertieren eines Diagramms in ein Bild im SVG-Format](/cells/de/cpp/converting-chart-to-image-in-svg-format/)
- [Diagramm in SVG mit viewBox-Attribut exportieren](/cells/de/cpp/export-chart-to-svg-with-viewbox-attribute/)
- [Konvertierungsvorgang von Excel nach TIFF verfolgen](/cells/de/cpp/track-conversion-progress-of-excel-to-tiff/)
