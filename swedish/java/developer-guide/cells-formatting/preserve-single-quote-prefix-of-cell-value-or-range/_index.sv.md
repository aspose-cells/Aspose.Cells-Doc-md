---
title: Bevara Enkelkavot Prefix of Cell Value or Range
type: docs
weight: 1900
url: /sv/java/preserve-single-quote-prefix-of-cell-value-or-range/
---

## **Möjliga användningsscenario**

När du sätter ett värde i cellen som har ledande apostrof eller citattecken, döljer sedan Microsoft Excel det, men när du väljer cellen visas den ledande apostrof eller citattecken i en formlerad som visas i följande skärmbild.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells döljer också den ledande apostrofen eller citattecknet som Microsoft Excel men det ställer [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) till **true** för den cellen. Om du ställer in en tom stil på cellen, blir [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) igen **false**. För att hantera detta problem tillhandahåller Aspose.Cells egenskapen [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix). När den är inställd till **false** uppdateras [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) inte alls och dess gamla värde bevaras. Det betyder om det gamla värdet för egenskapen [**Style.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/style#QuotePrefix) var **true**, kommer det att förbli sant och om det gamla värdet var falskt, kommer det att förbli falskt.

## **Bevara enskild citattecken prefiks av cellvärde eller område**

Den följande exempelkoden förklarar användningen av egenskapen [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/styleflag#QuotePrefix) enligt tidigare beskrivning. Läs kommentarerna inne i koden och se konsolens utmatning av koden nedan för mer hjälp.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.java" >}}

## **Konsoloutput**

{{< highlight java >}}

Quote Prefix of Cell A1: false

Quote Prefix of Cell A1: true

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: true

Quote Prefix of Cell A1: false

{{< /highlight >}}
