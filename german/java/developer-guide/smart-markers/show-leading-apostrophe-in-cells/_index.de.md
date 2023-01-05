---
title: Führenden Apostroph in Zellen anzeigen
type: docs
weight: 20
url: /de/java/show-leading-apostrophe-in-cells/
---
## **Führenden Apostroph in Zellen anzeigen**

In Microsoft Excel ist der führende Apostroph im Wert der Zelle ausgeblendet. Aspose.Cells bietet die Funktion zum standardmäßigen Anzeigen des Apostrophs. Dafür sorgt die API[**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle)Eigentum. Diese Eigenschaft gibt an, ob festgelegt werden soll[**ZitatPräfix**](https://reference.aspose.com/cells/java/com.aspose.cells/Style#QuotePrefix)-Eigenschaft, wenn Sie einen Zeichenfolgenwert eingeben, der mit einem einfachen Anführungszeichen in die Zelle beginnt. Einstellung der[**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle)Eigentum zu**FALSCH**zeigt den führenden Apostroph in der Excel-Ausgabedatei an.

Der folgende Screenshot zeigt die ausgegebene Excel-Datei mit dem sichtbaren Apostroph.

![todo: Bild_alt_Text](show-leading-apostrophe-in-cells_1.jpg)

Das folgende Code-Snippet demonstriert dies durch Hinzufügen von Daten mit Smart Markers in der Excel-Quelldatei. Die Quell- und Ausgabe-Excel-Dateien sind als Referenz beigefügt.

[Quelldatei](AllowLeadingApostropheSample.xlsx)

[Ausgabedatei](AllowLeadingApostropheSample_out.xlsx)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AllowLeadingApostrophe-1.java" >}}

Die Implementierung von*Datenobjekt*Klasse ist unten angegeben

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HelperClasses-DataObject-1.java" >}}
