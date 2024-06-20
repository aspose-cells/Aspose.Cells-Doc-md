---
title: Führende Apostroph in Zellen anzeigen
type: docs
weight: 70
url: /de/net/show-leading-apostrophe-in-cells/
---

In Microsoft Excel wird der führende Apostroph im Zellenwert ausgeblendet. Aspose.Cells bietet die Funktion, den Apostroph standardmäßig anzuzeigen. Dafür bietet die API die Eigenschaft [Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle). Diese Eigenschaft gibt an, ob die Eigenschaft [QuotePrefix](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) gesetzt werden soll, wenn ein Zeichenfolgenwert, der mit einem einfachen Anführungszeichen beginnt, in die Zelle eingegeben wird. Wenn die Eigenschaft [Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle) auf **false** gesetzt wird, wird der führende Apostroph in der Ausgabedatei angezeigt.

Der folgende Screenshot zeigt die Ausgabedatei mit dem sichtbaren Apostroph.

![todo:image_alt_text](show-leading-apostrophe-in-cells_1.jpg)

Der folgende Code-Ausschnitt zeigt dies, indem Daten mit Smart Markern in der Quell-Excel-Datei hinzugefügt werden. Die Quell- und Ausgabedateien für Referenzzwecke sind angehängt.

[Quelldatei](98107425.xlsx)

[Ausgabedatei](98107426.xlsx)
## **Beispielcode**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-1.cs" >}}

Die Implementierung der *DataObject* Klasse ist unten angegeben

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-2.cs" >}}
