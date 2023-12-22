---
title: Rufen Sie eine Liste der in einer Tabelle oder Arbeitsmappe verwendeten Schriftarten ab
description: Aspose.Cells ist eine .NET-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien. Es unterstützt das Abrufen einer Liste der in einer Tabelle oder Arbeitsmappe verwendeten Schriftarten, sodass Benutzer die in einem Dokument verwendeten Schriftarteninformationen abrufen können. In diesem Artikel erfahren Sie, wie Sie mit der Bibliothek Aspose.Cells eine Liste von Schriftarten erhalten.
keywords: Aspose.Cells, Spreadsheet, Workbook, Font, List
type: docs
weight: 20
url: /de/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---
##  **Mögliche Nutzungsszenarien**

Für Rendering-Zwecke ist es häufig erforderlich, die in Ihrer Arbeitsmappe verwendeten Schriftarten zu kennen. Wenn Sie Ihre Arbeitsmappe in PDF oder ein Bild konvertieren, erfordert Aspose.Cells, dass alle benötigten Schriftarten auf Ihrem System installiert oder in Ihrem *Schriftartenverzeichnis** vorhanden sind. Wenn Aspose.Cells die benötigte Schriftart nicht finden kann, versucht es, sie durch eine andere geeignete Schriftart zu ersetzen, die auf Ihrem System oder in Ihrem Schriftartenverzeichnis vorhanden ist und Ihre tatsächliche Schriftart ersetzen kann. Dies führt nicht nur zur unerwünschten Darstellung von PDF oder Bildern, sondern erfordert auch Verarbeitungszeit für die Suche nach geeigneten Schriftarten.

Um solche Fälle zu bewältigen, sollten Sie wissen, welche Schriftarten von Ihrer Arbeitsmappe verwendet werden, und diese Schriftarten dann entweder auf Ihrem System installieren (bei einer Windows-Umgebung) oder sie in Ihrem Schriftartenverzeichnis ablegen (bei einer Windows- oder Linux-Umgebung).

 Aspose.Cells bietet die**[Workbook.GetFonts](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getfonts)**Methode, die die Liste aller in Ihrer Arbeitsmappe oder Tabelle verwendeten Schriftarten zurückgibt.

##  **Rufen Sie eine Liste der in einer Tabelle oder Arbeitsmappe verwendeten Schriftarten ab**

 Der folgende Beispielcode lädt die Excel-Quelldatei und ruft die Liste der darin verwendeten Schriftarten ab. Es gibt ein Dummy-Arbeitsblatt, dem zur Veranschaulichung einige Dummy-Schriftarten hinzugefügt wurden. Wenn der Code alle Schriftarten in der Arbeitsmappe druckt, werden auch diese Dummy-Schriftarten gedruckt. Der folgende Screenshot zeigt die[Beispiel-Excel-Datei](25395211.xlsx) und wie die Dummy-Schriftarten aufgelistet werden.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

##  **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-GetListOfFontsUsedInSpreadsheetOrWorkbook.cs" >}}

##  **Konsolenausgabe**

 Hier ist die Konsolenausgabe des obigen Beispielcodes, wenn er mit dem angegebenen ausgeführt wird[Beispiel-Excel-Datei](25395211.xlsx).

{{< highlight "java" >}}

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
