---
title: Einzelnes Anführungszeichen an Zellwert oder Bereich mit Golang über C++ beibehalten
linktitle: Behalten Sie das einfache Anführungszeichenpräfix des Zellwerts oder bereichs bei
type: docs
weight: 310
url: /de/go-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Lernen Sie, wie man das Einzelnen Anführungszeichenpräfix eines Zellwerts oder Bereichs mit der API Aspose.Cells for C++ bewahrt.
keywords: Präfix eines Zellenwerts oder Bereichs mit einfachem Anführungszeichen beibehalten, Anführende Apostrophe oder einfaches Anführungszeichen ausblenden, Anführende Apostrophe oder einfaches Anführungszeichen anzeigen
---

## **Mögliche Verwendungsszenarien**

Wenn Sie einen Wert in die Zelle eingeben, der ein führendes Apostroph oder einzelnes Anführungszeichen hat, blendet Microsoft Excel diese aus, aber wenn Sie die Zelle auswählen, wird das führende Apostroph oder einzelne Anführungszeichen in der Formelleiste angezeigt, wie im folgenden Screenshot.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells blendet das führende Apostroph oder einzelne Anführungszeichen genauso aus wie Microsoft Excel, setzt aber [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) für diese Zelle auf **true**. Wenn Sie einen leeren Stil der Zelle setzen, wird [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) wieder auf **false** gesetzt. Um dieses Problem zu lösen, bietet Aspose.Cells die Eigenschaft [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getquoteprefix/) an, die bei Einstellung auf **false** bewirkt, dass [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) überhaupt nicht aktualisiert wird und sein alter Wert beibehalten wird. Das bedeutet, wenn der alte Wert der Eigenschaft [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) **true** war, bleibt er **true**, und wenn der alte Wert **false** war, bleibt er **false**.

## **Einzelnes Anführungszeichen-Prefix des Zellenwerts oder -bereichs beibehalten**

Der folgende Beispielcode erklärt die Verwendung der Eigenschaft [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/styleflag/getquoteprefix/), wie zuvor beschrieben. Bitte lesen Sie die Kommentare im Code und sehen Sie sich die Konsolenausgabe an, die unten für weitere Hilfe gezeigt wird.

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PreserveSingleQuotePrefixOfCellValueOrRange.go" >}}
## **Konsolenausgabe**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
