---
title: Führenden Apostroph in Zellen anzeigen
type: docs
weight: 70
url: /de/net/show-leading-apostrophe-in-cells/
---
 In Microsoft Excel ist der führende Apostroph im Wert der Zelle ausgeblendet. Aspose.Cells bietet die Funktion zum standardmäßigen Anzeigen des Apostrophs. Dafür sorgt die API[Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle) Eigentum. Diese Eigenschaft gibt an, ob festgelegt werden soll[ZitatPräfix](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)-Eigenschaft, wenn Sie einen Zeichenfolgenwert eingeben, der mit einem einfachen Anführungszeichen in die Zelle beginnt. Einstellung der[Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle) Eigentum zu**FALSCH**zeigt den führenden Apostroph in der Excel-Ausgabedatei an.

Der folgende Screenshot zeigt die ausgegebene Excel-Datei mit dem sichtbaren Apostroph.

![todo: Bild_alt_Text](show-leading-apostrophe-in-cells_1.jpg)

Das folgende Code-Snippet demonstriert dies durch Hinzufügen von Daten mit Smart Markers in der Excel-Quelldatei. Die Quell- und Ausgabe-Excel-Dateien sind als Referenz beigefügt.

[Quelldatei](98107425.xlsx)

[Ausgabedatei](98107426.xlsx)
## **Beispielcode**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-1.cs" >}}

Die Implementierung von*Datenobjekt*Klasse ist unten angegeben

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-2.cs" >}}
