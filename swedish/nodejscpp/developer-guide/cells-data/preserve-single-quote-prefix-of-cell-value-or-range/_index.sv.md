---
title: Bevara Enkelkavot Prefix of Cell Value or Range
type: docs
weight: 310
url: /sv/nodejs-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Lär dig hur du behåller enkla citattecken prefixt för cellvärde eller område via Aspose.Cells for Node.js via C++ API.
keywords: Bevara Enkel tecken Prefix av Cellvärde eller Område Node.js via C++, Dölj ledande apostrof eller enkelsitattecken Node.js via C++, Visa ledande apostrof eller enkelsitattecken Node.js via C++
---

## **Möjliga användningsscenario**

När du sätter ett värde i cellen som har ledande apostrof eller citattecken, döljer sedan Microsoft Excel det, men när du väljer cellen visas den ledande apostrof eller citattecken i en formlerad som visas i följande skärmbild.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells for Node.js via C++ döljer också det ledande apostrofen eller enkelsitattecknet som Microsoft Excel, men den sätter [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-) som **true** för den cellen. Om du anger en tom stil för cellen blir [**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) **false** igen. För att hantera detta problem erbjuder Aspose.Cells for Node.js via C++ [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-)-metoden, när den är inställd på **false**, ändras inte [**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) och dess gamla värde bevaras. Det betyder att om det gamla värdet av [**Style.getQuotePrefix()**](https://reference.aspose.com/cells/nodejs-cpp/style/#getQuotePrefix--) var **true**, förblir det **true** och om det var **false** förblir det **false**.

## **Bevara enskild citattecken prefiks av cellvärde eller område**

Följande exempel kod förklarar användningen av [**Style.setQuotePrefix(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setQuotePrefix-boolean-)-metoden som beskrivits tidigare. Läs kommentarer inuti koden och se på utdata i konsolen nedan för mer hjälp.

## **Exempelkod**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-preserve-single-quote-prefix-of-cell-value-or-range.js" >}}



## **Konsoloutput**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quotePrefix is False, it means, do not update the value of Cell.Style.quotePrefix.

Similarly, when StyleFlag.quotePrefix is True, it means, update the value of Cell.Style.quotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
