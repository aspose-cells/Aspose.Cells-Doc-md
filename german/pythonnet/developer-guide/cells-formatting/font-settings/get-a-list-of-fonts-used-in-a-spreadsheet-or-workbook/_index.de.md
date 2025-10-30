---
title: Eine Liste der in einer Tabelle oder Arbeitsmappe verwendeten Schriftarten abrufen
description: Aspose.Cells ist eine Python Bibliothek zur Arbeit mit Tabellenkalkulationsdateien. Es unterstützt das Abrufen einer Liste der verwendeten Schriftarten in einer Tabelle oder Arbeitsmappe, sodass Nutzer die Schriftartinformationen des Dokuments ermitteln können. Dieser Artikel zeigt, wie man mit der Aspose.Cells für Python via .NET Bibliothek eine Schriftartenliste erhält.
keywords: Aspose.Cells für Python via .NET, Tabellenkalkulation, Arbeitsmappe, Schriftart, Liste
type: docs
weight: 20
url: /de/python-net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **Mögliche Verwendungsszenarien**

Es ist oft notwendig, die verwendeten Schriftarten in der Arbeitsmappe für Rendering-Zwecke zu kennen. Wenn Sie Ihre Arbeitsmappe in PDF oder Bild umwandeln, benötigt Aspose.Cells für Python via .NET, dass alle benötigten Schriftarten auf Ihrem System installiert oder im **Fonts-Verzeichnis** vorhanden sind. Wenn Aspose.Cells für Python via .NET die benötigte Schriftart nicht finden kann, versucht es, sie durch eine andere geeignete Schriftart zu ersetzen, die auf Ihrem System oder im Fonts-Verzeichnis vorhanden ist, um die tatsächliche Schrift zu substituieren. Dies führt nicht nur zu unerwünschtem Rendering von PDF oder Bildern, sondern kostet auch Verarbeitungszeit.

Um mit solchen Fällen umzugehen, sollten Sie wissen, welche Schriftarten von Ihrer Arbeitsmappe verwendet werden, dann entweder diese Schriftarten in Ihrem System installieren, falls es sich um eine Windows-Umgebung handelt, oder sie in Ihr Schriftartenverzeichnis legen, falls es sich um eine Windows- oder Linux-Umgebung handelt.

Aspose.Cells für Python via .NET bietet die [**Workbook.get_fonts**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/get_fonts) Methode, welche die Liste aller in Ihrer Arbeitsmappe verwendeten Schriftarten zurückgibt.

## **Eine Liste der in einer Arbeitsmappe oder einem Arbeitsblatt verwendeten Schriftarten abrufen**

Der folgende Beispielcode lädt die Quelldatei und ruft die Liste der darin verwendeten Schriftarten ab. Es hat ein Dummy-Arbeitsblatt, auf dem zu Illustrationszwecken einige Dummy-Schriftarten hinzugefügt sind. Wenn der Code alle Schriftarten in der Arbeitsmappe ausdruckt, werden auch diese Dummy-Schriftarten ausgedruckt. Der folgende Screenshot zeigt die [Beispiel-Excel-Datei](25395211.xlsx) und wie die Dummy-Schriftarten aufgelistet sind.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-GetListOfFontsUsedInSpreadsheetOrWorkbook.py" >}}

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

{{< app/cells/assistant language="python-net" >}}
