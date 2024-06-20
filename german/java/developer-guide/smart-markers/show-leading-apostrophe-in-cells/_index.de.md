---
title: Führende Apostroph in Zellen anzeigen
type: docs
weight: 20
url: /de/java/show-leading-apostrophe-in-cells/
---

## **Führende Apostrophzeichen in Zellen anzeigen**

In Microsoft Excel wird der führende Apostroph im Zellwert ausgeblendet. Aspose.Cells bietet die Funktion, den Apostroph standardmäßig anzuzeigen. Dafür stellt die API die [**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle)-Eigenschaft bereit. Diese Eigenschaft gibt an, ob die [**QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/Style#QuotePrefix)-Eigenschaft festgelegt werden soll, wenn ein Zeichenfolgenwert mit einem einzelnen Anführungszeichen in die Zelle eingegeben wird. Das Festlegen der [**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle)-Eigenschaft auf **false** zeigt den führenden Apostroph in der Ausgabedatei an.

Der folgende Screenshot zeigt die Ausgabedatei mit dem sichtbaren Apostroph.

![todo:image_alt_text](show-leading-apostrophe-in-cells_1.jpg)

Der folgende Code-Ausschnitt zeigt dies, indem Daten mit Smart Markern in der Quell-Excel-Datei hinzugefügt werden. Die Quell- und Ausgabedateien für Referenzzwecke sind angehängt.

[Quelldatei](AllowLeadingApostropheSample.xlsx)

[Ausgabedatei](AllowLeadingApostropheSample_out.xlsx)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AllowLeadingApostrophe-1.java" >}}

Die Implementierung der *DataObject* Klasse ist unten angegeben

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HelperClasses-DataObject-1.java" >}}
