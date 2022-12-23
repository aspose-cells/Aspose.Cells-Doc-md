---
title: Präfix für einfache Anführungszeichen von Cell Wert oder Bereich beibehalten
type: docs
weight: 310
url: /de/net/preserve-single-quote-prefix-of-cell-value-or-range/
---
## **Mögliche Nutzungsszenarien**

Wenn Sie einen Wert in die Zelle einfügen, die einen führenden Apostroph oder ein einfaches Anführungszeichen enthält, blendet Microsoft Excel ihn aus, aber wenn Sie die Zelle auswählen, wird der führende Apostroph oder das einfache Anführungszeichen in einer Formelleiste angezeigt, wie im folgenden Screenshot gezeigt.

![todo: Bild_alt_Text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells verbirgt auch den führenden Apostroph oder das einfache Anführungszeichen wie Microsoft Excel, aber es setzt die[**Style.QuotePräfix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) als**wahr** für diese Zelle. Wenn Sie einen leeren Stil der Zelle festlegen, dann[**Style.QuotePräfix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) wird**FALSCH** aufs Neue. Um dieses Problem zu lösen, bietet Aspose.Cells[**StyleFlag.ZitatPräfix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix) Eigenschaft, wenn sie gesetzt ist**FALSCH** , dann[**Style.QuotePräfix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)überhaupt nicht aktualisiert und der alte Wert bleibt erhalten. Es bedeutet, wenn der alte Wert von[**Style.QuotePräfix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)Eigentum war**wahr** , es wird bleiben**wahr** und ob der alte wert war**FALSCH** , es wird bleiben**FALSCH**.

## **Präfix für einfache Anführungszeichen von Cell Wert oder Bereich beibehalten**

 Der folgende Beispielcode erläutert die Verwendung von[**StyleFlag.ZitatPräfix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix)Eigenschaft wie zuvor beschrieben. Bitte lesen Sie die Kommentare im Code und sehen Sie sich die Konsolenausgabe des unten angegebenen Codes an, um weitere Hilfe zu erhalten.

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.cs" >}}

## **Konsolenausgabe**

{{< highlight "java" >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
