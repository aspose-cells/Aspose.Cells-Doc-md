---
title: Bevara enstaka citatprefix för Cell värde eller intervall
type: docs
weight: 310
url: /sv/net/preserve-single-quote-prefix-of-cell-value-or-range/
---
## **Möjliga användningsscenarier**

När du sätter ett värde inuti cellen som har inledande apostrof eller enstaka citattecken, döljer Microsoft Excel det, men när du markerar cellen visar den den inledande apostrof eller enstaka citattecken i en formelrad som visas i följande skärmdump.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells döljer också den ledande apostrof eller enstaka citat som Microsoft Excel men det ställer in[**Style.CitatPrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) som**Sann** för den cellen. Om du ställer in en tom stil för cellen, då[**Style.CitatPrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) blir**falsk** igen. För att hantera denna fråga tillhandahåller Aspose.Cells[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix) egenskap, när den är inställd**falsk** , då[**Style.CitatPrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)uppdateras inte alls och dess gamla värde bevaras. Det betyder om det gamla värdet av[**Style.CitatPrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)egendom var**Sann** , det kommer att finnas kvar**Sann** och om det gamla värdet var**falsk** , det kommer att finnas kvar**falsk**.

## **Bevara enstaka citatprefix för Cell värde eller intervall**

 Följande exempelkod förklarar användningen av[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix)egendom som beskrivits tidigare. Vänligen läs kommentarerna i koden och se konsolutgången för koden nedan för mer hjälp.

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.cs" >}}

## **Konsolutgång**

{{< highlight "java" >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
