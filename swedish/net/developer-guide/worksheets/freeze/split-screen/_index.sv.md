---
title: Uppdelad skärm av Excel ark
linktitle: Dela skärm
type: docs
weight: 190
url: /sv/net/how-to-split-screen-of-excel-worksheet
description: I den här artikeln kommer du att lära dig hur man visar vissa rader och/eller kolumner i separata fönster genom att dela arbetsbladet i två eller fyra delar programmatiskt med C# biblioteket med .NET API.
keywords: Frys topprader, Frys översta raden.
---

## **Introduktion**

I den här artikeln kommer vi att lära oss hur man visar vissa rader och/eller kolumner i separata delar genom att dela upp arket i två eller fyra delar. När du arbetar med stora datamängder behöver du se ett par områden av samma kalkylblad samtidigt för att jämföra olika delar av data. Den uppdelade skärmfunktionen kan uppfylla dina behov.

## **Hur man delar skärmen i Excel**
För att dela upp ett arbetsblad i två eller fyra delar, gör följande:

1. Välj rad/kolumn/cell innan vilken du vill placera uppdelningen.
2. På fliken Visa, i gruppen Fönster, klicka på knappen Dela.

**![Dela skärm](Split-Screen.png)**

## **Dela arbetsblad vertikalt på kolumner**

För att separera två områden av kalkylarket vertikalt, välj kolumnen till höger om den kolumn där du vill att uppdelningen ska visas och klicka på Split-knappen i Excel.

Det är enkelt att dela arbetsblad vertikalt på kolumner programmatiskt med Aspose.Cells för .Net, vi behöver bara välja en cell i översta raden som aktiv cell, sedan
dela med [**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/)-metoden.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Vertically-Split.cs" >}}

## **Dela arbetsblad horisontellt på rader**
För att separera ditt Excel-fönster horisontellt, välj raden under den rad där du vill att uppdelningen ska ske i Excel.

Det är enkelt att dela arbetsblad horisontellt på rader programmatiskt med Aspose.Cells för .Net, vi behöver bara välja en cell i den vänstra kolumnen som aktiv cell, sedan
dela med [**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/)-metoden.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Horizontally-Split.cs" >}}

## **Dela arbetsblad i fyra delar**
För att visa fyra olika sektioner av samma arbetsblad samtidigt, dela upp skärmen både vertikalt och horisontellt i Excel.

Det är enkelt att dela arbetsblad vertikalt på kolumner programmatiskt med Aspose.Cells för .Net, vi behöver bara välja en cell som inte är i den första raden och kolumnen som aktiv cell, sedan
dela med [**Worksheet.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/)-metoden.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Split-Four.cs" >}}

## **Hur man tar bort uppdelning**
För att ta bort arbetsbladets uppdelning, klicka bara på Split-knappen igen.

Aspose.Cells för .Net tillhandahåller en [**Worksheet.RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/removesplit/)-metod för att ta bort uppdelningsinställningen.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Remove-Split.cs" >}}
{{< app/cells/assistant language="csharp" >}}
