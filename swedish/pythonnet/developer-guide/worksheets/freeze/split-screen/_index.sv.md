---
title: Uppdelad skärm av Excel ark
linktitle: Dela skärm
type: docs
weight: 190
url: /sv/python-net/how-to-split-screen-of-excel-worksheet
description: I den här artikeln lär du dig hur man visar vissa rader och/eller kolumner i separata paneler genom att dela arbetsbladet i två eller fyra delar programmässigt med hjälp av Aspose.Cells för Python via .NET API er.
keywords: Python Excel bibliotek, Python lås översta rader, Python lås topprad, Python dela arbetsblad vertikalt på kolumner, Python dela arbetsblad horisontellt på rader, Python dela arbetsblad i fyra delar, Python ta bort delning.
---

## **Introduktion**

I den här artikeln kommer vi att lära oss hur man visar vissa rader och/eller kolumner i separata delar genom att dela upp arket i två eller fyra delar. När du arbetar med stora datamängder behöver du se ett par områden av samma kalkylblad samtidigt för att jämföra olika delar av data. Den uppdelade skärmfunktionen kan uppfylla dina behov.

## **Hur man delar skärmen i Excel**
För att dela upp ett arbetsblad i två eller fyra delar, gör följande:

1. Välj rad/kolumn/cell innan vilken du vill placera uppdelningen.
2. På fliken Visa, i gruppen Fönster, klicka på knappen Dela.

**![Dela skärm](Split-Screen.png)**

## **Hur man delar arbetsblad vertikalt på kolumner**

För att separera två områden av kalkylarket vertikalt, välj kolumnen till höger om den kolumn där du vill att uppdelningen ska visas och klicka på Split-knappen i Excel.

Det är enkelt att dela arbetsblad vertikalt på kolumner programmässigt med Aspose.Cells för Python via .NET, vi behöver bara välja en cell i översta raden som aktiv cell, sedan
dela med [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/)-metoden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Vertically-Split.py" >}}

## **Hur man delar arbetsblad horisontellt på rader**
För att separera ditt Excel-fönster horisontellt, välj raden under den rad där du vill att uppdelningen ska ske i Excel.

Det är enkelt att dela arbetsblad horisontellt på rader programmässigt med Aspose.Cells för Python via .NET, vi behöver bara välja en cell i vänstra kolumnen som aktiv cell, sedan
dela med [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/)-metoden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Horizontally-Split.py" >}}

## **Hur man delar arbetsblad i fyra delar**
För att visa fyra olika sektioner av samma arbetsblad samtidigt, dela upp skärmen både vertikalt och horisontellt i Excel.

Det är enkelt att dela arbetsblad vertikalt på kolumner programmässigt med Aspose.Cells för Python via .NET, vi behöver bara välja en cell som inte är i första raden och kolumnen som aktiv cell, sedan
dela med [**Worksheet.split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split/)-metoden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Split-Four.py" >}}

## **Hur man tar bort delning**
För att ta bort arbetsbladets uppdelning, klicka bara på Split-knappen igen.

Aspose.Cells för Python via .NET tillhandahåller en [**Worksheet.remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split/) metod för att ta bort dela inställningen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Remove-Split.py" >}}
