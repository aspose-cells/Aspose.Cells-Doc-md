---
title: Daten finden oder suchen
type: docs
weight: 120
url: /de/java/find-or-search-data/
---
{{% alert color="primary" %}} 

 In Microsoft Excel können Benutzer nach Zellen suchen, die bestimmte Daten enthalten. Klicken zum Beispiel**Bearbeiten** und dann**Finden** öffnet den Suchdialog. Der Benutzer gibt einen Wert ein und klickt**OK** danach zu suchen. Excel hebt übereinstimmende Felder hervor.

**Verwenden des Dialogfelds „Suchen“, um Zellen zu finden, die einen bestimmten Wert enthalten** 

![todo: Bild_alt_Text](find-or-search-data_1.png)

In diesem Beispiel lautet der Suchwert „Orangen“.

Aspose.Cells ermöglicht es Entwicklern, die Zellen in einem Arbeitsblatt zu durchsuchen, um diejenigen zu finden, die einen bestimmten Wert enthalten.

{{% /alert %}} 
## **Suche nach Cells, die bestimmte Daten enthalten**
 Aspose.Cells bietet eine Klasse,[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) , die eine Excel-Datei darstellt. Das[Arbeitsmappe](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) Klasse enthält[Arbeitsblattsammlung](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) , eine Sammlung, die den Zugriff auf alle Arbeitsblätter in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)Klasse.

 Das[Arbeitsblatt](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Klasse bietet[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) , eine Sammlung, die alle Zellen im Arbeitsblatt darstellt[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)Die Sammlung bietet mehrere Methoden zum Suchen von Zellen in einem Arbeitsblatt, die benutzerdefinierte Daten enthalten. Einige dieser Verfahren werden nachstehend ausführlicher erörtert.

Alle Suchmethoden geben die Zellreferenzen für alle Zellen zurück, die den angegebenen Suchwert enthalten.
## **Finden, das eine Formel enthält**
 Entwickler können eine bestimmte Formel im Arbeitsblatt finden, indem sie die aufrufen[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung[finden](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\) )-Methode, die Einstellung der[FindOptions.setLookInType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookInType) zu[LookInType.FORMULAS](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#FORMULAS)und als Parameter an die übergeben[finden](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) Methode.

 Typischerweise die[finden](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\))-Methode akzeptiert zwei oder mehr Parameter:

- Zu suchendes Objekt: Stellt ein Objekt dar, das im Arbeitsblatt gefunden werden muss.
- Die vorherige Cell: stellt die vorherige Zelle mit derselben Formel dar. Dieser Parameter kann bei der Suche von Anfang an auf null gesetzt werden.
- Suchoptionen: stellt die Suchkriterien dar. In den folgenden Beispielen werden die folgenden Arbeitsblattdaten verwendet, um Findungsmethoden zu üben:

**Beispielarbeitsblattdaten** 

![todo: Bild_alt_Text](find-or-search-data_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsContainingFormula-FindingCellsContainingFormula.java" >}}
## **Suche nach Zeichenketten**
Die Suche nach Zellen, die einen Zeichenfolgenwert enthalten, ist einfach und flexibel. Es gibt verschiedene Suchmöglichkeiten, z. B. die Suche nach Zellen, die Zeichenfolgen enthalten, die mit einem bestimmten Zeichen oder einer Gruppe von Zeichen beginnen.
### **Suche nach Zeichenfolgen, die mit bestimmten Zeichen beginnen**
 Um nach dem ersten Zeichen in einer Zeichenfolge zu suchen, rufen Sie die auf[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung[finden](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\))-Methode, legen Sie die fest[FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) zu[LookAtType.START_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#START_WITH)und übergebe es als Parameter an die[finden](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) Methode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsWithStringOrNumber-FindingCellsWithStringOrNumber.java" >}}
### **Suche nach Zeichenfolgen, die mit bestimmten Zeichen enden**
 Aspose.Cells kann auch Zeichenfolgen finden, die mit bestimmten Zeichen enden. Um nach den letzten Zeichen in einer Zeichenfolge zu suchen, rufen Sie die auf[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) Sammlung[finden](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\))-Methode, legen Sie die fest[FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) zu[LookAtType.END_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#END_WITH)und übergebe es als Parameter an die[finden](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) Methode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsEndWithSpecificCharacters-FindingCellsEndWithSpecificCharacters.java" >}}
## **Suchen mit regulären Ausdrücken: die RegEx-Funktion**
Ein regulärer Ausdruck bietet ein prägnantes und flexibles Mittel zum Abgleichen (Angeben und Erkennen) von Textzeichenfolgen, z. B. bestimmten Zeichen, Wörtern oder Mustern.

Zum Beispiel das reguläre Ausdrucksmuster abc-* ~~xyz~~ findet die Zeichenfolgen "abc-123-xyz", "abc-985-xyz" und "abc-pony-xyz".* ist ein Platzhalter, sodass das Muster mit allen Zeichenfolgen übereinstimmt, die mit "abc" beginnen und mit "-xyz" enden, unabhängig davon, welche Zeichen sich in der Mitte befinden.

Aspose.Cells ermöglicht die Suche mit regulären Ausdrücken.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingwithRegularExpressions-FindingwithRegularExpressions.java" >}}

## **Themen vorantreiben**
- [Finden Sie Zellen mit einem bestimmten Stil](/cells/de/java/find-cells-with-specific-style/)
- [Suchen Sie Daten mit Originalwerten](/cells/de/java/search-data-using-original-values/)
