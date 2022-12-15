---
title: Lesen und Schreiben der Abfragetabelle des Arbeitsblatts
type: docs
weight: 560
url: /de/java/reading-and-writing-query-table-of-worksheet/
---
{{% alert color="primary" %}} 

 Aspose.Cells bietet[Worksheet.getQueryTables()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#QueryTables) Sammlung, die die zurückgibt[QueryTableCollection](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTableCollection) . Um eine bestimmte zu bekommen[Abfragetabelle](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) , verwenden Sie die[QueryTableCollection.get()](https://reference.aspose.com/cells/java/com.aspose.cells/querytablecollection#Item%20\(int\) )-Eigenschaft und übergeben Sie den Index der QueryTable. Das[Abfragetabelle](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) Die Klasse hat die folgenden beiden Eigenschaften zum Anpassen der QueryTable.

- [QueryTable.getAdjustColumnWidth()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#AdjustColumnWidth)
- [QueryTable.getPreserveFormatting()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting)

Dies sind beides boolesche Werte. Sie können sie in Microsoft Excel über Daten > Verbindungen > Eigenschaften anzeigen.

{{% /alert %}} 
## **Lesen und Schreiben der Abfragetabelle des Arbeitsblatts**
 Der folgende Beispielcode liest die erste[Abfragetabelle](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)des ersten Arbeitsblatts und druckt dann beide[Abfragetabelle](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) Eigenschaften. Dann setzt es die[QueryTable.PreserveFormatting](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting) zu**Stimmt**.

Der folgende Screenshot zeigt die[Excel-Quelldatei](5472578.xlsx) im Code und seinen Eigenschaften verwendet, die beide zeigen[Abfragetabelle](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)Werte.

![todo: Bild_alt_Text](reading-and-writing-query-table-of-worksheet_1.png)

Der folgende Screenshot zeigt die[Excel-Datei ausgeben](5472574.xlsx) generiert durch den Code und seine Eigenschaften, die beide zeigen[Abfragetabelle](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)Werte. Wie Sie sehen können, ist das Kontrollkästchen Beibehaltene Formatierung jetzt aktiviert.

![todo: Bild_alt_Text](reading-and-writing-query-table-of-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.java" >}}
## **Konsolenausgabe**
Hier ist die Konsolenausgabe des obigen Beispielcodes

{{< highlight "java" >}}

 Adjust Column Width: true

Preserve Formatting: false

{{< /highlight >}}
## **Abfragetabellen-Ergebnisbereich abrufen**
Aspose.Cells bietet die Möglichkeit, die Adresse, dh den Ergebnisbereich von Zellen für eine Abfragetabelle zu lesen. Der folgende Code demonstriert diese Funktion, indem er die Adresse des Ergebnisbereichs für eine Abfragetabelle liest. Die Beispieldatei kann heruntergeladen werden[hier](QueryTXT.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-RetrieveQueryTableResultRange.java" >}}
