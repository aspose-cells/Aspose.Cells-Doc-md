---
title: Kopiera intervall för Excel
linktitle: Kopiera intervall
type: docs
weight: 105
url: /sv/net/copy-ranges-of-Excel/
---
## **Introduktion**

I Excel kan du välja ett intervall, kopiera intervallet och sedan klistra in det med specifika alternativ i samma kalkylblad, andra kalkylblad eller andra filer.

## **Kopiera intervall med Aspose.Cells**

 Aspose.Cells ger viss överbelastning[Range.Copy](https://reference.aspose.com/cells/net/aspose.cells/range/copy/#copy) metoder för att kopiera intervallet.
 Och[Range.CopyStyle](https://reference.aspose.com/cells/net/aspose.cells/range/copystyle/) endast kopieringsstilen för serien;[Range.CopyData](https://reference.aspose.com/cells/net/aspose.cells/range/copydata/) endast kopieringsvärdet för intervallet

## **Kopiera intervall**

Skapa två intervall: källintervallet, målintervallet, kopiera sedan källintervallet till målintervallet med metoden Range.Copy.

Se följande kod:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range.cs" >}}

## **Klistra in intervall med alternativ**

Aspose.Cells stöder inklistring av intervallet med specifik typ.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Paste-Range.cs" >}}

## **Kopiera endast data från intervallet.**
Du kan också kopiera data med Range.CopyData-metoden som följande koder:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range-Data.cs" >}}

## **Förhandsämnen**
- [Kopiera radhöjder för källintervall till destinationsintervall](/cells/sv/net/copy-row-heights-of-source-range-to-destination-range/)


