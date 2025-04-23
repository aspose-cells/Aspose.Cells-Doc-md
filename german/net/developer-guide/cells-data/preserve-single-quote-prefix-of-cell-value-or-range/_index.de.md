---
title: Behalten Sie das einfache Anführungszeichenpräfix des Zellwerts oder bereichs bei
type: docs
weight: 310
url: /de/net/preserve-single-quote-prefix-of-cell-value-or-range/
description: Erfahren Sie, wie Sie das Präfix eines Zellenwerts oder Bereichs mit einfachem Anführungszeichen durch die Aspose.Cells for .NET API beibehalten.
keywords: Präfix eines Zellenwerts oder Bereichs mit einfachem Anführungszeichen beibehalten, Anführende Apostrophe oder einfaches Anführungszeichen ausblenden, Anführende Apostrophe oder einfaches Anführungszeichen anzeigen
---

## **Mögliche Verwendungsszenarien**

Wenn Sie einen Wert in die Zelle einsetzen, der ein führendes Apostroph oder einfach Anführungszeichen hat, verbirgt es Microsoft Excel, aber wenn Sie die Zelle auswählen, zeigt es das führende Apostroph oder Anführungszeichen in einer Formelleiste an, wie im folgenden Screenshot gezeigt.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells blendet auch das führende Anführungszeichen oder das einfache Anführungszeichen wie Microsoft Excel aus, setzt aber [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) als **true** für diese Zelle. Wenn Sie einen leeren Stil der Zelle setzen, wird [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) wieder zu **false**. Um dieses Problem zu lösen, bietet Aspose.Cells die Eigenschaft [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix). Wenn es auf **false** gesetzt ist, wird [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) überhaupt nicht aktualisiert und sein alter Wert bleibt erhalten. Das bedeutet, wenn der alte Wert der Eigenschaft [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) **true** war, bleibt er **true**, und wenn der alte Wert **false** war, bleibt er **false**.

## **Einzelnes Anführungszeichen-Prefix des Zellenwerts oder -bereichs beibehalten**

Der folgende Beispielcode erläutert die Verwendung der [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix)-Eigenschaft, wie zuvor beschrieben. Bitte lesen Sie die Kommentare im Code und sehen Sie die Konsolenausgabe des folgenden Codes für weitere Hilfe.

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.cs" >}}

## **Konsolenausgabe**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
