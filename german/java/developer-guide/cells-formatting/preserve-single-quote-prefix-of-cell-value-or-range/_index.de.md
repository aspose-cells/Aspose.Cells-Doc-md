---
title: Präfix für einfache Anführungszeichen von Cell Wert oder Bereich beibehalten
type: docs
weight: 1900
url: /de/java/preserve-single-quote-prefix-of-cell-value-or-range/
---
## **Mögliche Nutzungsszenarien**

Wenn Sie einen Wert in die Zelle einfügen, die einen führenden Apostroph oder ein einfaches Anführungszeichen enthält, blendet Microsoft Excel ihn aus, aber wenn Sie die Zelle auswählen, wird der führende Apostroph oder das einfache Anführungszeichen in einer Formelleiste angezeigt, wie im folgenden Screenshot gezeigt.

![todo: Bild_alt_Text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells verbirgt auch den führenden Apostroph oder das einfache Anführungszeichen wie Microsoft Excel, aber es setzt die[**Style.QuotePräfix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) wie**Stimmt** für diese Zelle. Wenn Sie einen leeren Stil der Zelle festlegen, dann[**Style.QuotePräfix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) wird**FALSCH** wieder. Um dieses Problem zu lösen, bietet Aspose.Cells[**StyleFlag.ZitatPräfix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) Eigenschaft, wenn sie gesetzt ist**FALSCH**, dann[**StyleFlag.ZitatPräfix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix)überhaupt nicht aktualisiert und der alte Wert bleibt erhalten. Es bedeutet, wenn der alte Wert von[**Style.QuotePräfix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix)Eigentum war**Stimmt**, bleibt er wahr, und wenn der alte Wert falsch war, bleibt er falsch.

## **Präfix für einfache Anführungszeichen von Cell Wert oder Bereich beibehalten**

Der folgende Beispielcode erläutert die Verwendung von[**StyleFlag.ZitatPräfix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix)Eigenschaft wie zuvor beschrieben. Bitte lesen Sie die Kommentare im Code und sehen Sie sich die Konsolenausgabe des unten angegebenen Codes an, um weitere Hilfe zu erhalten.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.java" >}}

## **Konsolenausgabe**

{{< highlight "java" >}}

Quote Prefix of Cell A1: false

Quote Prefix of Cell A1: true

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: true

Quote Prefix of Cell A1: false

{{< /highlight >}}
