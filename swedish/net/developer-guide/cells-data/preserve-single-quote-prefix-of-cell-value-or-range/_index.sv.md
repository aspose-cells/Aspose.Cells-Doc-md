---
title: Bevara Enkelkavot Prefix of Cell Value or Range
type: docs
weight: 310
url: /sv/net/preserve-single-quote-prefix-of-cell-value-or-range/
description: Lär dig hur man bevarar enkla citattecken eller en räckesprefix genom Aspose.Cells for .NET API.
keywords: Bevara enkla citattecken eller en räckesprefix, Göm ledande apostrof eller enkla citattecken, Visa ledande apostrof eller enkla citattecken
---

## **Möjliga användningsscenario**

När du sätter ett värde i cellen som har ledande apostrof eller citattecken, döljer sedan Microsoft Excel det, men när du väljer cellen visas den ledande apostrof eller citattecken i en formlerad som visas i följande skärmbild.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells gömmer också det ledande apostrofen eller enkla citattecknet som Microsoft Excel, men det sätter [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) som **true** för den cellen. Om du ställer in en tom stil för cellen blir [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) **false** igen. För att hantera detta problem tillhandahåller Aspose.Cells egendomen [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix), när den är inställd på **false**, uppdateras inte [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) alls och dess gamla värde bevaras. Det betyder att om det gamla värdet för egenskapen [**Style.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) var **true**, kommer det förbli **true** och om det gamla värdet var **false**, kommer det förbli **false**.

## **Bevara enskild citattecken prefiks av cellvärde eller område**

Följande exempelkod förklarar användningen av egenskapen [**StyleFlag.QuotePrefix**](https://reference.aspose.com/cells/net/aspose.cells/styleflag/properties/quoteprefix) som tidigare beskrivits. Läs kommentarerna inne i koden och se konsolresultatet för koden nedan för mer hjälp.

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-PreserveSingleQuotePrefixOfCellValueOrRange.cs" >}}

## **Konsoloutput**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.

Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
