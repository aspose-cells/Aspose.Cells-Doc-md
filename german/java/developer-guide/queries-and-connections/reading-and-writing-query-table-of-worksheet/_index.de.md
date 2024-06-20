---
title: Lesen und Schreiben von Abfrage Tabellen des Arbeitsblatts
type: docs
weight: 560
url: /de/java/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}} 

Aspose.Cells stellt die [Worksheet.getQueryTables()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#QueryTables)-Sammlung bereit, die die [QueryTableCollection](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTableCollection) zurückgibt. Um eine bestimmte [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) zu erhalten, verwenden Sie die Eigenschaft [QueryTableCollection.get()](https://reference.aspose.com/cells/java/com.aspose.cells/querytablecollection#Item%20\(int\)) und geben den Index der QueryTable an. Die [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)-Klasse verfügt über die folgenden beiden Eigenschaften zur Anpassung der Abfragetabelle.

- [QueryTable.getAdjustColumnWidth()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#AdjustColumnWidth)
- [QueryTable.getPreserveFormatting()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting)

Dies sind beide boolesche Werte. Sie können sie in Microsoft Excel über **Daten > Verbindungen > Eigenschaften** anzeigen.

{{% /alert %}} 
## **Lesen und Schreiben von Abfragetabellen des Arbeitsblatts**
Der folgende Beispielcode liest die erste [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) des ersten Arbeitsblatts und gibt dann beide Eigenschaften der [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) aus. Anschließend wird [QueryTable.PreserveFormatting](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting) auf **true** gesetzt.

Der folgende Screenshot zeigt die [Quelldatei Excel](5472578.xlsx), die im Code verwendet wird, und deren Eigenschaften, die beide Werte der [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) anzeigen.

![todo:image_alt_text](reading-and-writing-query-table-of-worksheet_1.png)

Der folgende Screenshot zeigt die [Ausgabedatei der Excel-Tabelle](5472574.xlsx), die durch den Code generiert wurde und ihre Eigenschaften, die beide Werte der [QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable) zeigen. Wie Sie sehen können, ist jetzt das Feld 'Formatierung beibehalten' aktiviert.

![todo:image_alt_text](reading-and-writing-query-table-of-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.java" >}}
## **Konsolenausgabe**
Hier ist die Konsolenausgabe des obigen Beispielscodes

{{< highlight java >}}

 Adjust Column Width: true

Preserve Formatting: false

{{< /highlight >}}

## **Abfragetabellenergebnisbereich abrufen**
Aspose.Cells bietet die Möglichkeit, die Adresse, d.h. den Ergebnisbereich der Zellen für eine Abfragetabelle, zu lesen. Der folgende Code demonstriert diese Funktion, indem er die Adresse des Ergebnisbereichs für eine Abfragetabelle liest. Die Beispieldatei kann [hier](QueryTXT.xlsx) heruntergeladen werden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-RetrieveQueryTableResultRange.java" >}}
