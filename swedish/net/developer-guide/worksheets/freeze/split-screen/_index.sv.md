---
title: Delad skärm av Excel-kalkylblad
linktitle: Delad skärm
type: docs
weight: 190
url: /sv/net/how-to-split-screen-of-excel-worksheet
description: I den här artikeln kommer du att lära dig hur du visar vissa rader och/eller kolumner i separata rutor genom att dela upp kalkylbladet i två eller fyra delar programmatiskt med hjälp av C# Library med .NET API.
keywords: Freeze top rows, Feeze top row.
---
{{% alert color="primary" %}}

den här artikeln kommer vi att lära oss hur du visar vissa rader och/eller kolumner i separata rutor genom att dela upp kalkylbladet i två eller fyra delar .
När vi arbetar med stora datamängder behöver vi se några områden i samma kalkylblad åt gången för att jämföra olika delmängder av data.
Funktionen med delad skärm kan möta dina behov.

{{% /alert %}}

##  **Hur man delar skärm i Excel**
Gör så här för att dela upp ett kalkylblad i två eller fyra delar:

1. Välj den rad/kolumn/cell innan du vill placera uppdelningen.
2. På fliken Visa, i gruppen Windows, klicka på knappen Dela.

**![Delad skärm](Split-Screen.png)**

##  **Dela kalkylblad vertikalt på kolumner**

För att separera två delar av kalkylarket vertikalt, välj kolumnen till höger om kolumnen där du vill att uppdelningen ska visas och klicka på knappen Dela i Excel.

Det är lätt att dela kalkylblad vertikalt på kolumner programmatiskt med Aspose.Cells för .Net, vi behöver bara välja en cell i den översta raden som aktiv cell, sedan
dela med[**Arbetsblad.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) metod.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Vertically-Split.cs" >}}

##  **Dela kalkylbladet horisontellt på rader**
För att separera ditt Excel-fönster horisontellt, välj raden under raden där du vill att uppdelningen ska ske i Excel.

Det är lätt att dela kalkylblad horisontellt på rader programmatiskt med Aspose.Cells för .Net, vi behöver bara välja en cell i den vänstra kolumnen som aktiv cell, sedan
dela med[**Arbetsblad.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) metod.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Horizontally-Split.cs" >}}

##  **Dela upp arbetsbladet i fyra delar**
För att se fyra olika delar av samma kalkylblad samtidigt, dela skärmen både vertikalt och horisontellt i Excel.

Det är lätt att dela kalkylblad vertikalt på kolumner programmatiskt med Aspose.Cells för .Net, vi behöver bara välja en cell inte i den första raden och kolumnen som aktiv cell, sedan
dela med[**Arbetsblad.Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/split/) metod.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Split-Four.cs" >}}

##  **Hur man tar bort split**
För att ta bort kalkylbladsdelningen klickar du bara på knappen Dela igen.

 Aspose.Cells för .Net ger en[**Worksheet.RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/removesplit/) metod för att ta bort delad inställning.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Remove-Split.cs" >}}