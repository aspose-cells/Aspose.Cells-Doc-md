---
title: Bevara enstaka citatprefix för Cell värde eller intervall
type: docs
weight: 1900
url: /sv/java/preserve-single-quote-prefix-of-cell-value-or-range/
---
## **Möjliga användningsscenarier**

När du sätter ett värde inuti cellen som har inledande apostrof eller enstaka citattecken, döljer Microsoft Excel det, men när du markerar cellen visar den den inledande apostrof eller enstaka citattecken i en formelfält som visas i följande skärmdump.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells döljer också den ledande apostrof eller enstaka citat som Microsoft Excel men det anger[**Style.CitatPrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) som**Sann** för den cellen. Om du ställer in en tom stil för cellen, då[**Style.CitatPrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) blir**falsk** om igen. För att hantera denna fråga tillhandahåller Aspose.Cells[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) egenskap, när den är inställd**falsk**, då[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix)uppdateras inte alls och dess gamla värde bevaras. Det betyder om det gamla värdet av[**Style.CitatPrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix)egendom var**Sann**, kommer det att förbli sant och om det gamla värdet var falskt förblir det falskt.

## **Bevara enstaka citatprefix för Cell värde eller intervall**

Följande exempelkod förklarar användningen av[**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix)egendom som beskrivits tidigare. Vänligen läs kommentarerna i koden och se konsolutgången för koden nedan för mer hjälp.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.java" >}}

## **Konsolutgång**

{{< highlight "java" >}}

Quote Prefix of Cell A1: false

Quote Prefix of Cell A1: true

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: true

Quote Prefix of Cell A1: false

{{< /highlight >}}
