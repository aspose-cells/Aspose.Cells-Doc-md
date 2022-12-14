---
title: Rufen Sie eine Liste der Schriftarten ab, die in einer Tabelle oder Arbeitsmappe verwendet werden
type: docs
weight: 20
url: /de/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---
## **Mögliche Nutzungsszenarien**

 Häufig ist es erforderlich, die Schriftarten zu kennen, die in Ihrer Arbeitsmappe zum Rendern verwendet werden. Wenn Sie Ihre Arbeitsmappe in PDF oder Bild konvertieren, erfordert Aspose.Cells, dass alle erforderlichen Schriftarten auf Ihrem System installiert oder in Ihrem vorhanden sind**Fonts-Verzeichnis**Wenn Aspose.Cells die benötigte Schriftart nicht finden kann, versucht es, sie durch eine andere geeignete Schriftart zu ersetzen, die auf Ihrem System oder in Ihrem Schriftartenverzeichnis vorhanden ist und Ihre tatsächliche Schriftart ersetzen kann. Dies führt nicht nur zur ungewollten Wiedergabe von PDFs oder Bildern, sondern kostet auch Rechenzeit, um geeignete Schriftarten zu finden.

Um mit solchen Fällen fertig zu werden, sollten Sie wissen, welche Schriftarten von Ihrer Arbeitsmappe verwendet werden, und diese Schriftarten dann entweder auf Ihrem System im Falle einer Windows-Umgebung installieren oder sie in Ihrem Schriftartenverzeichnis im Falle einer Windows- oder Linux-Umgebung platzieren.

 Aspose.Cells bietet die[Workbook.getFonts()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#getFonts())-Methode, die die Liste aller Schriftarten zurückgibt, die in Ihrer Arbeitsmappe oder Tabelle verwendet werden.

## **Rufen Sie eine Liste der Schriftarten ab, die in einer Tabelle oder Arbeitsmappe verwendet werden**

 Der folgende Beispielcode lädt die Excel-Quelldatei und ruft die Liste der darin verwendeten Schriftarten ab. Es hat ein Dummy-Arbeitsblatt, dem einige Dummy-Schriftarten zur Veranschaulichung hinzugefügt wurden. Wenn der Code alle Schriftarten in der Arbeitsmappe druckt, werden auch diese Dummy-Schriftarten gedruckt. Der folgende Screenshot zeigt die[Excel-Beispieldatei](sampleGetFonts.xlsx)und wie die Dummy-Fonts aufgelistet werden.

![todo: Bild_alt_Text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetFontsUsedinWorkbook-GetFontsUsedinWorkbook.java" >}}

## **Konsolenausgabe**

 Hier ist die Konsolenausgabe des obigen Beispielcodes, wenn er mit dem angegebenen ausgeführt wird[Excel-Beispieldatei](sampleGetFonts.xlsx).

{{< highlight "java" >}}

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Arial; 10.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 10.0; Bold; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff808080 ]Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ffffffff ]Aspose.Cells.Font [ Calibri; 36.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 20.0; Bold; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]Aspose.Cells.Font [ Calibri; 11.0; Italic; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 12.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff294a4e ]Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]Aspose.Cells.Font [ Dummy-Arial-X; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Arial-Y; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Arial-Z; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Times-I; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Times-II; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Dummy-Times-III; 11.0; Regular; com.aspose.cells.Color@ff000000 ]Aspose.Cells.Font [ Calibri; 10.5; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 20.0; Regular; com.aspose.cells.Color@ff376268 ]Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]{{< /highlight >}}
