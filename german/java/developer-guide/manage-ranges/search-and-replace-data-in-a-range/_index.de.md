---
title: Suchen und Ersetzen von Daten in einem Bereich
type: docs
weight: 60
url: /de/java/search-and-replace-data-in-a-range/
description: Dieser Artikel zeigt, wie Sie Daten in einem Bereich in Excel mithilfe des Codes Java suchen und ersetzen.
keywords: java search and replace data in excel, java search data in excel, java search and replace data in a range, java search data in a range, java searching data in a range, java searching data in range, java searching data in excel, java search data in range, search and replace data in excel with java, search and replace data in a range with java, search and replace data in range with java
---
{{% alert color="primary" %}}

Manchmal müssen Sie nach bestimmten Daten in einem Bereich suchen und diese ersetzen, wobei Sie alle Zellwerte außerhalb des gewünschten Bereichs ignorieren. Aspose.Cells ermöglicht es Ihnen, eine Suche auf einen bestimmten Bereich einzuschränken. Dieser Artikel erklärt, wie.

{{% /alert %}}

Aspose.Cells bietet die[**FindOptions.setRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#setRange(com.aspose.cells.CellArea)) Methode zur Angabe eines Bereichs bei der Suche nach Daten.

 Angenommen, Sie möchten nach der Zeichenfolge suchen**"Suche"** und ersetzen Sie es durch**"ersetzen"** im Sortiment**E3:H6**. Im Screenshot unten ist die Zeichenfolge „search“ in mehreren Zellen zu sehen, aber wir wollen sie nur in einem bestimmten Bereich ersetzen, hier gelb hervorgehoben.

**Eingabedatei**

![todo: Bild_alt_Text](search-and-replace-data-in-a-range_1.png)

Nach der Ausführung des Codes sieht die Ausgabedatei wie folgt aus. Alle „Such“-Strings innerhalb des Bereichs wurden durch „Ersetzen“ ersetzt.

**Ausgabedatei**

![todo: Bild_alt_Text](search-and-replace-data-in-a-range_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SearchReplaceDataInRange-SearchReplaceDataInRange.java" >}}

## In Verbindung stehende Artikel

- [Daten finden oder suchen](/cells/de/java/find-or-search-data/)
