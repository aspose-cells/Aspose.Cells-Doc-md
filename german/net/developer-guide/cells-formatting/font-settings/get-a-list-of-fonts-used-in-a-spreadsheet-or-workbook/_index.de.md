---
title: Eine Liste der in einer Tabelle oder Arbeitsmappe verwendeten Schriftarten abrufen
description: Aspose.Cells ist eine .NET Bibliothek zum Arbeiten mit Tabellendateien. Es unterstützt das Abrufen einer Liste der in einer Tabelle oder Arbeitsmappe verwendeten Schriftarten und ermöglicht Benutzern, Informationen über verwendete Schriftarten in einem Dokument zu erhalten. Dieser Artikel zeigt Ihnen, wie Sie die Aspose.Cells Bibliothek verwenden, um eine Liste der Schriftarten abzurufen.
keywords: Aspose.Cells, Tabelle, Arbeitsmappe, Schriftart, Liste
type: docs
weight: 20
url: /de/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **Mögliche Verwendungsszenarien**

Es ist oft notwendig zu wissen, welche Schriftarten in Ihrer Arbeitsmappe für die Darstellung verwendet werden. Wenn Sie Ihre Arbeitsmappe in PDF oder Bild konvertieren, erfordert Aspose.Cells, dass alle benötigten Schriftarten auf Ihrem System installiert oder in Ihrem **Schriftartenverzeichnis** vorhanden sind. Wenn Aspose.Cells die benötigte Schriftart nicht finden kann, versucht es, sie durch eine andere geeignete Schriftart zu ersetzen, die auf Ihrem System oder in Ihrem Schriftartenverzeichnis vorhanden ist und Ihre tatsächliche Schriftart ersetzen kann. Dies führt nicht nur zu einer unerwünschten Darstellung von PDF oder Bildern, sondern kostet auch Verarbeitungszeit, um geeignete Schriftarten zu finden.

Um mit solchen Fällen umzugehen, sollten Sie wissen, welche Schriftarten von Ihrer Arbeitsmappe verwendet werden, dann entweder diese Schriftarten in Ihrem System installieren, falls es sich um eine Windows-Umgebung handelt, oder sie in Ihr Schriftartenverzeichnis legen, falls es sich um eine Windows- oder Linux-Umgebung handelt.

Aspose.Cells bietet die [**Workbook.GetFonts**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getfonts)-Methode, die eine Liste aller im Workbook oder Spreadsheet verwendeten Schriften zurückgibt.

## **Eine Liste der in einer Arbeitsmappe oder einem Arbeitsblatt verwendeten Schriftarten abrufen**

Der folgende Beispielcode lädt die Quelldatei und ruft die Liste der darin verwendeten Schriftarten ab. Es hat ein Dummy-Arbeitsblatt, auf dem zu Illustrationszwecken einige Dummy-Schriftarten hinzugefügt sind. Wenn der Code alle Schriftarten in der Arbeitsmappe ausdruckt, werden auch diese Dummy-Schriftarten ausgedruckt. Der folgende Screenshot zeigt die [Beispiel-Excel-Datei](25395211.xlsx) und wie die Dummy-Schriftarten aufgelistet sind.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-GetListOfFontsUsedInSpreadsheetOrWorkbook.cs" >}}

## **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Beispielcodes, wenn er mit der angegebenen [Beispiel-Excel-Datei](25395211.xlsx) ausgeführt wird.

{{< highlight java >}}

Aspose.Cells.Font [ Calibri; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Arial; 10; Regular; Color [A=255, R=0, G=0, B=0] ]

Aspose.Cells.Font [ Calibri; 10; Bold; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=128, G=128, B=128] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 36; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 11; Italic; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 12; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Dummy-Arial-X; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Y; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Z; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-I; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-II; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-III; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10.5; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
