---
title: Bevara Enkelkavot Prefix of Cell Value or Range
type: docs
weight: 310
url: /sv/python-net/preserve-single-quote-prefix-of-cell-value-or-range/
description: Lär dig hur man bevarar enkla citattecken som prefix för cellvärde eller omfång genom Aspose.Cells för Python via .NET API.
keywords: Python Excel bibliotek, Bevara enkla citattecken som prefix för cellvärde eller omfång med Python, Döljande inledande apostrof eller enkelt citattecken med Python, Visa inledande apostrof eller enkelt citattecken med Python
---

## **Möjliga användningsscenario**

När du sätter ett värde i cellen som har ledande apostrof eller citattecken, döljer sedan Microsoft Excel det, men när du väljer cellen visas den ledande apostrof eller citattecken i en formlerad som visas i följande skärmbild.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells för Python via .NET döljer också det inledande apostrofen eller enkla citattecknet som Microsoft Excel men ställer in [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) som **true** för den cellen. Om du ställer in en tom stil för cellen blir [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) igen **false**. För att hantera detta problem, tillhandahåller Aspose.Cells för Python via .NET egenskapen [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix), när den är inställd som **false**, då [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) uppdateras inte alls och dess gamla värde bevaras. Det betyder om det gamla värdet för [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) var **true**, kommer det förbli **true** och om det gamla värdet var **false**, kommer det förbli **false**.

## **Bevara enskild citattecken prefiks av cellvärde eller område**

Följande exempelkod förklarar användningen av egenskapen [**Style.quote_prefix**](https://reference.aspose.com/cells/python-net/aspose.cells/style/quote_prefix) som tidigare beskrivits. Läs kommentarerna inne i koden och se konsolresultatet för koden nedan för mer hjälp.

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-PreserveSingleQuotePrefixOfCellValueOrRange.py" >}}

## **Konsoloutput**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quote_prefix is False, it means, do not update the value of Cell.Style.quote_prefix.

Similarly, when StyleFlag.quote_prefix is True, it means, update the value of Cell.Style.quote_prefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
