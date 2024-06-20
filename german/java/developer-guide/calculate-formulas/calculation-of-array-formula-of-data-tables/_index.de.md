---
title: Berechnung der Array Formel von DatenTabellen
type: docs
weight: 550
url: /de/java/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}} 

Sie können eine Daten-Tabelle in Microsoft Excel über Daten > Was-wäre-wenn-Analyse > Daten-Tabelle... erstellen. Aspose.Cells ermöglicht es Ihnen jetzt, die Array-Formel der Daten-Tabelle zu berechnen. Verwenden Sie bitte [Workbook.calculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\)) wie üblich, um alle Arten von Formeln zu berechnen.

{{% /alert %}} 
## **Berechnung der Arrayformel von Datenblättern**
Im folgenden Beispielscode verwendeten wir diese [Quell-Excel-Datei](5472579.xlsx), die auch im folgenden Bild gezeigt wird.

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

Wenn Sie den Wert der Zelle B1 auf 100 ändern, werden die Werte der Daten-Tabelle, die mit gelber Farbe gefüllt sind, zu 120. Der Beispielscode generiert die [Ausgabedatei im PDF-Format](5472577.pdf), die in diesem Bild 120 als Werte in der Daten-Tabelle zeigt.

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Hier ist der Beispielcode, der verwendet wird, um das [Ausgabepdf](5472577.pdf) aus der [Quellexceldatei](5472579.xlsx) zu generieren. Bitte lesen Sie die Kommentare für weitere Informationen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculationOfArrayFormula-CalculationOfArrayFormula.java" >}}
