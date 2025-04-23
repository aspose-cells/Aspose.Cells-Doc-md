---
title: Wie drucke ich Excel auf zugeschnittenen Seiten breit und hoch
type: docs
weight: 200
url: /de/net/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Dieser Artikel zeigt Ihnen Code, der erklärt, wie man mit Aspose.Cells die Einstellung FitToPagesWide und FitToPagesTall setzt.
keywords: C# Wie man FitToPagesWide und FitToPagesTall festlegt, wie man FitToPagesWide und FitToPagesTall in C# hinzufügt, wie man FitToPagesWide und FitToPagesTall in Excel einstellt, wie man FitToPagesWide und FitToPagesTall in Excel löscht, wie man Excel so druckt, dass es auf Seite passt, wie man Arbeitsblätter auf eine Seite druckt, wie man alle Spalten eines Arbeitsblatts auf eine Seite druckt.
---

## **Einführung**

Die Einstellungen FitToPagesWide und FitToPagesTall werden in Tabellenkalkulationsanwendungen (wie Microsoft Excel) verwendet, um die Skalierung eines Tabellenblatts beim Drucken zu steuern. Diese Einstellungen helfen sicherzustellen, dass Ihre gedruckte Ausgabe innerhalb einer festgelegten Anzahl von Seiten passt, sowohl horizontal als auch vertikal. Hier eine Aufschlüsselung: 

1. FitToPagesWide: Diese Einstellung gibt die Anzahl der Seiten an, in die die gedruckte Ausgabe horizontal passt. Zum Beispiel bedeutet das Setzen von FitToPagesWide auf 1, dass der Inhalt auf die Breite einer Seite skaliert wird, egal wie breit das Tabellenblatt ist.
1. FitToPagesTall: Diese Einstellung gibt die Anzahl der Seiten an, in die die gedruckte Ausgabe vertikal passt. Zum Beispiel bedeutet das Setzen von FitToPagesTall auf 1, dass der Inhalt auf die Höhe einer Seite skaliert wird, unabhängig von der Anzahl der Zeilen.

## **Warum FitToPagesWide und FitToPagesTall verwenden**
Hier sind einige Gründe, warum Sie FitToPagesWide und FitToPagesTall einstellen sollten:
1. Kontrolle über das gedruckte Layout: Durch die Angabe der Anzahl der Seiten in der Breite und Höhe können Sie sicherstellen, dass Ihr gedrucktes Dokument leicht lesbar und gut organisiert ist, ohne dass Spalten oder Zeilen ungünstig auf mehrere Seiten aufgeteilt werden.
1. Konsistenz: Wenn Sie mehrere Blätter oder Berichte drucken, tragen diese Einstellungen dazu bei, ein einheitliches Format beizubehalten, was das Vergleichen und Analysieren gedruckter Dokumente erleichtert.
1. Professionelle Präsentation: Das richtige Skalieren und Anpassen des Inhalts an eine festgelegte Seitenzahl kann zu einer professionelleren und gepflegteren Präsentation Ihrer Daten führen.

## **So drucken Sie eine Datei als angepasste Seiten breit und hoch in Excel**

Um die Einstellungen FitToPagesWide und FitToPagesTall in Microsoft Excel festzulegen, befolgen Sie diese Schritte:

1. Öffnen Sie Ihre Excel-Arbeitsmappe und wechseln Sie auf das Blatt, das Sie drucken möchten.
1. Gehen Sie auf die Registerkarte Seitenlayout im Menüband.
1. Klicken Sie im Bereich Seite einrichten auf den kleinen Pfeil in der unteren rechten Ecke, um das Dialogfeld Seite einrichten zu öffnen.
1. Gehen Sie im Dialogfeld Seite einrichten auf die Registerkarte Seite.
1. Unter Skalierung wählen Sie die Option "Anpassen an" aus und geben Sie dann die Anzahl der Seiten in der Breite und Höhe an, die Sie möchten: Geben Sie die Anzahl der Seiten in der ersten Box (Anpassen an x Seiten breits) ein. Geben Sie die Anzahl der Seiten in der zweiten Box (Anpassen an y Seiten hoch) ein.
<br>
<img src="2.png" width=60% />

1. Klicken Sie auf OK, um die Einstellungen zu übernehmen.


## **So drucken Sie Excel als angepasste Seiten breit und hoch mit Aspose.Cells**

Um FitToPagesWide und FitToPagesTall in einem bestimmten Arbeitsblatt festzulegen: Laden Sie zuerst die [Beispieldatei](input.xlsx), und passen Sie dann die Eigenschaften [**Worksheet.PageSetup.FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/fittopagestall/) und [**Worksheet.PageSetup.FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/fittopageswide/) des [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/)-Objekts für das gewünschte Arbeitsblatt an. Hier ist ein Beispiel in C#:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-set-FitToPagesWide-FitToPagesTall.cs" >}}

Das Ausgabenergebnis:
<br>
<img src="1.png" width=60% />


## **So drucken Sie ein Blatt als eine Seite mit Aspose.Cells**

Um das Arbeitsblatt auf eine Seite zu drucken: Laden Sie zuerst die [Beispieldatei](sample.xlsx), und setzen Sie dann die Eigenschaft [**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/onepagepersheet/) des [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/)-Objekts. Hier ist ein Beispiel in C#:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-OnePagePerSheet.cs" >}}

Das Ausgabenergebnis:
<br>
<img src="3.png" width=60% />


## **So drucken Sie alle Spalten eines Arbeitsblatts auf einer Seite mit Aspose.Cells**

Um alle Spalten des Arbeitsblatts auf eine Seite zu drucken: Laden Sie zuerst die [Beispieldatei](sample.xlsx), und setzen Sie dann die Eigenschaft [**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/allcolumnsinonepagepersheet/) des [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/)-Objekts. Hier ist ein Beispiel in C#:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-AllColumnsInOnePagePerSheet.cs" >}}

Das Ausgabenergebnis:
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="csharp" >}}
