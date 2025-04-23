---
title: Kopiera områden av Excel
linktitle: Kopiera områden
type: docs
weight: 105
url: /sv/net/copy-ranges-of-Excel/
---

## **Introduktion**

I Excel kan du markera ett område, kopiera området och sedan klistra in det med specifika alternativ på samma arbetsblad, andra arbetsblad eller andra filer.

## **Kopiera områden med hjälp av Aspose.Cells**

Aspose.Cells tillhandahåller några överbelastnings [Range.Copy](https://reference.aspose.com/cells/net/aspose.cells/range/copy/#copy) metoder för att kopiera området.
Och [Range.CopyStyle](https://reference.aspose.com/cells/net/aspose.cells/range/copystyle/) endast kopiera stil från området; [Range.CopyData](https://reference.aspose.com/cells/net/aspose.cells/range/copydata/) endast kopiera värde från området

## **Kopiera område**

Skapa två områden: källområdet, målområdet, sedan kopiera källområdet till målområdet med Range.Copy-metoden.

Se följande kod:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range.cs" >}}

## **Klistra in område med alternativ**

Aspose.Cells stöder att klistra in området med specifik typ.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Paste-Range.cs" >}}

## **Endast kopiera data för området**
Du kan också kopiera data med Range.CopyData-metoden enligt följande koder:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range-Data.cs" >}}

## **Fortsatta ämnen**
- [Kopiera radhöjder från källspann till destinationspann](/cells/sv/net/copy-row-heights-of-source-range-to-destination-range/)


{{< app/cells/assistant language="csharp" >}}
