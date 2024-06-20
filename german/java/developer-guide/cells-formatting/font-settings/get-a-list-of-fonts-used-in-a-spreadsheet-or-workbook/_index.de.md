---
title: Eine Liste der in einer Tabelle oder Arbeitsmappe verwendeten Schriftarten abrufen
type: docs
weight: 20
url: /de/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **Mögliche Verwendungsszenarien**

Es ist oft notwendig zu wissen, welche Schriftarten in Ihrer Arbeitsmappe für die Wiedergabe verwendet werden. Wenn Sie Ihre Arbeitsmappe in PDF oder Bild umwandeln, benötigt Aspose.Cells alle benötigten Schriftarten auf Ihrem System oder in Ihrem **Schriftartenverzeichnis**. Wenn Aspose.Cells die benötigte Schriftart nicht finden kann, versucht es, sie durch eine andere geeignete Schriftart zu ersetzen, die auf Ihrem System oder in Ihrem Schriftartenverzeichnis vorhanden ist und Ihre tatsächliche Schriftart ersetzen kann. Dies führt nicht nur zu einer unerwünschten Darstellung von PDFs oder Bildern, sondern benötigt auch Zeit für die Suche nach geeigneten Schriftarten.

Um mit solchen Fällen umzugehen, sollten Sie wissen, welche Schriftarten von Ihrer Arbeitsmappe verwendet werden, dann entweder diese Schriftarten in Ihrer Windows-Umgebung installieren oder sie in Ihrem Schriftartenverzeichnis in Windows- oder Linux-Umgebung platzieren.

Aspose.Cells bietet die Methode [Workbook.getFonts()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#getFonts--) an, die die Liste aller im Arbeitsbuch oder Spreadsheet verwendeten Schriftarten zurückgibt.

## **Eine Liste der in einer Arbeitsmappe oder einem Arbeitsblatt verwendeten Schriftarten abrufen**

Der folgende Beispielcode lädt die Quelldatei und ruft die darin verwendeten Schriftarten ab. Es gibt ein fiktives Arbeitsblatt, auf dem zu Illustrationszwecken einige fiktive Schriftarten hinzugefügt wurden. Wenn der Code alle Schriftarten im Arbeitsbuch ausgibt, werden auch diese fiktiven Schriftarten aufgeführt. Der folgende Screenshot zeigt die [Beispiel-Excel-Datei](sampleGetFonts.xlsx) und wie die fiktiven Schriftarten aufgelistet sind.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetFontsUsedinWorkbook-GetFontsUsedinWorkbook.java" >}}

## **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Beispielcodes, wenn er mit der angegebenen [Beispiel-Excel-Datei](sampleGetFonts.xlsx) ausgeführt wird.

{{< highlight java >}}

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Arial; 10.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 10.0; Bold; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff808080 ]

Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ffffffff ]

Aspose.Cells.Font [ Calibri; 36.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 20.0; Bold; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]

Aspose.Cells.Font [ Calibri; 11.0; Italic; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 12.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]

Aspose.Cells.Font [ Dummy-Arial-X; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Arial-Y; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Arial-Z; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Times-I; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Times-II; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Times-III; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 10.5; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 20.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]

{{< /highlight >}}
