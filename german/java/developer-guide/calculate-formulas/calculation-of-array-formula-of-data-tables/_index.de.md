---
title: Berechnung der Array-Formel von Datentabellen
type: docs
weight: 550
url: /de/java/calculation-of-array-formula-of-data-tables/
---
{{% alert color="primary" %}} 

Sie können eine Datentabelle in Microsoft Excel erstellen, indem Sie Daten > Was-wäre-wenn-Analyse > Datentabelle ... verwenden. Mit Aspose.Cells können Sie jetzt die Matrixformel der Datentabelle berechnen. Bitte verwende[Workbook.calculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\)) wie gewohnt für die Berechnung beliebiger Formeln.

{{% /alert %}} 
## **Berechnung der Array-Formel von Datentabellen**
 Im folgenden Beispielcode haben wir dies verwendet[Excel-Quelldatei](5472579.xlsx) was auch im folgenden Bild zu sehen ist.

![todo: Bild_alt_Text](calculation-of-array-formula-of-data-tables_1.png)

 Wenn Sie den Wert der Zelle B1 in 100 ändern, werden die Werte der Datentabelle, die mit gelber Farbe gefüllt sind, zu 120. Der Beispielcode generiert die[Ausgang PDF](5472577.pdf) die 120 als Werte in der Datentabelle anzeigt, wie in diesem Bild gezeigt.

![todo: Bild_alt_Text](calculation-of-array-formula-of-data-tables_2.png)

 Hier ist der Beispielcode, der zum Generieren der[Ausgang PDF](5472577.pdf) von dem[Excel-Quelldatei](5472579.xlsx). Bitte lesen Sie die Kommentare für weitere Informationen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculationOfArrayFormula-CalculationOfArrayFormula.java" >}}
