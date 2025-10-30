---
title: Ändra formatet på en cell
description: Hur du använder Aspose.Cells för Python via .NET biblioteket för att ändra formateringen av celler, inklusive teckensnitt, färg, border etc. Genom att justera dessa egenskaper får du mer kontroll över hur cellerna ser ut och framträder.
keywords: Aspose.Cells för Python via .NET biblioteket, cellformatering, Python, teckensnitt, färg, border
type: docs
weight: 20
url: /sv/python-net/how-to-change-format-of-cell/
---

## **Möjliga användningsscenario**
När du vill markera viss data kan du ändra stilen på cellerna.

## **Hur man ändrar formatet på en cell i Excel**

För att ändra formatet på en enda cell i Excel, följ dessa steg:

1. Öppna Excel och öppna arbetsboken som innehåller den cell du vill formatera.

2. Leta reda på den cell du vill formatera.

3. Högerklicka på cellen och välj "Formatera celler" från snabbmenyn. Alternativt kan du markera cellen och gå till fliken Hem i Excel-ribbonen, klicka på rullgardinsmenyn "Formatera" i gruppen "Celler" och välj "Formatera celler".

4. Dialogrutan "Formatera celler" visas. Här kan du välja olika formateringsalternativ att tillämpa på den valda cellen. Till exempel kan du ändra typsnittsstil, typsnittstorlek, typsnittsfärg, nummerformat, kanter, bakgrundsfärg, etc. Utforska de olika flikarna i dialogrutan för att komma åt olika formateringsalternativ.

5. Efter att ha gjort önskade formateringsändringar klickar du på "OK"-knappen för att tillämpa formateringen på den valda cellen.


## **Hur man ändrar formatet på en cell med C#**

För att ändra formatet på en cell med Aspose.Cells för Python via .NET kan du använda följande metoder:
1. [Cell.set_style(style)](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style/#aspose.cells.Style)
2. [Cell.set_style(style, explicit_flag)](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style/#aspose.cells.Style-bool)
3. [Cell.set_style(style, flag)](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style/#aspose.cells.Style-aspose.cells.StyleFlag)


## **Exempelkod**
I det här exemplet skapar vi en Exceldatabok, lägger till lite provdata, får åtkomst till det första kalkylarket och får två celler ("A2" och "B3"). Sedan får vi stilen på cellen, ställer in olika formateringsalternativ (t.ex. typsnittsfärg, fetstil) och ändrar formatet på cellen. Slutligen sparar vi arbetsboken till en ny fil.
![todo:image_alt_text](change-format.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-Cells-change-format.py" >}}

{{< app/cells/assistant language="python-net" >}}
