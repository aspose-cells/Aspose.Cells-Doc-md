---
title: Daten finden oder suchen
type: docs
weight: 120
url: /de/java/find-or-search-data/
---

{{% alert color="primary" %}} 

In Microsoft Excel können Benutzer nach Zellen suchen, die spezifische Daten enthalten. Wenn beispielsweise auf **Bearbeiten** und dann **Suchen** geklickt wird, wird der Suchdialog geöffnet. Benutzer geben einen Wert ein und klicken auf **OK**, um danach zu suchen. Excel hebt übereinstimmende Felder hervor.

**Verwenden des Suchdialogs, um Zellen zu finden, die einen bestimmten Wert enthalten** 

![todo:image_alt_text](find-or-search-data_1.png)

In diesem Beispiel ist der Suchwert "Orangen".

Aspose.Cells ermöglicht Entwicklern, in den Zellen eines Arbeitsblatts nach solchen zu suchen, die einen bestimmten Wert enthalten.

{{% /alert %}} 
## **Zellen finden, die bestimmte Daten enthalten**
Aspose.Cells bietet eine Klasse, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), die eine Excel-Datei repräsentiert. Die [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)-Klasse enthält [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), eine Sammlung, die den Zugriff auf jedes der Arbeitsblätter in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) repräsentiert.

Die [Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-Klasse stellt die [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung bereit, die alle Zellen im Arbeitsblatt repräsentiert. Die [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlung bietet verschiedene Methoden zum Auffinden von Zellen in einem Arbeitsblatt, die benutzerspezifische Daten enthalten. Einige dieser Methoden werden im Folgenden näher erläutert.

Alle Suchmethoden geben die Zellreferenzen für Zellen zurück, die den angegebenen Suchwert enthalten.
## **Suchen nach einer Formel**
Entwickler können eine angegebene Formel im Arbeitsblatt finden, indem sie die [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlungsmethode [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\))aufrufen, die [FindOptions.setLookInType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookInType)auf [LookInType.FORMULAS](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#FORMULAS)setzen und sie als Parameter an die [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\))-Methode übergeben.

In der Regel akzeptiert die [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\))-Methode zwei oder mehr Parameter:

- Zu suchendes Objekt: stellt ein Objekt dar, das im Arbeitsblatt gefunden werden muss.
- Die vorherige Zelle: stellt die vorherige Zelle mit derselben Formel dar. Dieser Parameter kann auf null gesetzt werden, wenn von Anfang an gesucht wird.
- Suchoptionen: stellt die Suchkriterien dar. In den folgenden Beispielen wird die folgende Arbeitsblattdaten verwendet, um die Suchmethoden zu üben:

**Beispielarbeitsblattdaten** 

![todo:image_alt_text](find-or-search-data_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsContainingFormula-FindingCellsContainingFormula.java" >}}
## **Suche nach Zeichenfolgen**
Die Suche nach Zellen, die einen Zeichenfolgenwert enthalten, ist einfach und flexibel. Es gibt verschiedene Möglichkeiten der Suche, z. B. die Suche nach Zellen, die Zeichenfolgen enthalten, die mit einem bestimmten Zeichen oder einer bestimmten Zeichenfolge beginnen.
### **Suche nach Zeichenfolgen, die mit bestimmten Zeichen beginnen**
Um nach dem ersten Zeichen in einer Zeichenfolge zu suchen, rufen Sie die [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlungsmethode [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\))auf, setzen Sie [FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType)auf [LookAtType.START_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#START_WITH)und übergeben Sie sie als Parameter an die [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\))-Methode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsWithStringOrNumber-FindingCellsWithStringOrNumber.java" >}}
### **Suche nach Zeichenfolgen, die mit bestimmten Zeichen enden**
Aspose.Cells kann auch Zeichenfolgen finden, die mit bestimmten Zeichen enden. Um nach den letzten Zeichen in einer Zeichenfolge zu suchen, rufen Sie die [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-Sammlungsmethode [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\))auf, setzen Sie [FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType)auf [LookAtType.END_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#END_WITH)und übergeben Sie sie als Parameter an die [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\))-Methode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsEndWithSpecificCharacters-FindingCellsEndWithSpecificCharacters.java" >}}
## **Suchen mit regulären Ausdrücken: die Regex-Funktion**
Ein regulärer Ausdruck bietet eine präzise und flexible Möglichkeit, Zeichenketten abzugleichen (zu spezifizieren und zu erkennen), wie bestimmte Zeichen, Wörter oder Muster.

Zum Beispiel passt das reguläre Ausdrucksmuster abc-*~~xyz~~ zu den Zeichenketten "abc-123-xyz", "abc-985-xyz" und "abc-pony-xyz". * ist ein Platzhalter, so dass das Muster zu allen Zeichenketten passt, die mit "abc" beginnen und mit "-xyz" enden, unabhängig von den Zeichen in der Mitte.

Aspose.Cells ermöglicht die Suche mit regulären Ausdrücken.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingwithRegularExpressions-FindingwithRegularExpressions.java" >}}

## **Erweiterte Themen**
- [Suchen Sie nach Zellen mit einem bestimmten Stil](/cells/de/java/find-cells-with-specific-style/)
- [Daten mithilfe der Originalwerte suchen](/cells/de/java/search-data-using-original-values/)
