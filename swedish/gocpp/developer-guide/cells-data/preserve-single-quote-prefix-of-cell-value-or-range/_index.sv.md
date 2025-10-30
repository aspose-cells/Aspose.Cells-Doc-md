---
title: Bevara enkel citattecken prefix av cellvärde eller område med Golang via C++
linktitle: Bevara Enkelkavot Prefix of Cell Value or Range
type: docs
weight: 310
url: /sv/go-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Lär dig hur du behåller enkel CITAT prefekt för cellvärde eller område via API et Aspose.Cells for C++.
keywords: Bevara enkla citattecken eller en räckesprefix, Göm ledande apostrof eller enkla citattecken, Visa ledande apostrof eller enkla citattecken
---

## **Möjliga användningsscenario**

När du sätter ett värde i cellen som börjar med ett apostrof eller enkelt citattecken, döljer Microsoft Excel det, men när du markerar cellen visas det ledande apostrofen eller citattecknet i formelfältet som visas i följande skärmdump.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells döljer också det ledande apostrofen eller citattecknet som Microsoft Excel men det sätter [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) till **true** för den cellen. Om du sätter ett tomt stil för cellen blir [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) återigen **false**. För att hantera detta problem tillhandahåller Aspose.Cells [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/getquoteprefix/)-egenskapen, när den är inställd på **false**, ändras inte [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/) och dess gamla värde bevaras. Det betyder att om det gamla värdet av [**Style.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/style/getquoteprefix/)-egenskapen var **true**, förblir det **true** och om det gamla värdet var **false**, förblir det **false**.

## **Bevara enskild citattecken prefiks av cellvärde eller område**

Följande exempel kod förklarar användningen av [**StyleFlag.GetQuotePrefix()**](https://reference.aspose.com/cells/go-cpp/styleflag/getquoteprefix/)-egenskapen som beskrivs tidigare. Läs kommentarerna i koden och se konsolutmatningen av koden nedan för mer hjälp.

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PreserveSingleQuotePrefixOfCellValueOrRange.go" >}}
## **Konsoloutput**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
