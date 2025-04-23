---
title: Ändra formatet på en cell
description: Hur man använder Aspose.Cells bibliotek i C# för att ändra formateringen av celler, inklusive typsnitt, färg, kant, etc. Genom att justera dessa egenskaper har du mer kontroll över hur celler ser ut och visas.
keywords: Aspose.Cells, cellformatering, C#, typsnitt, färg, kant
type: docs
weight: 20
url: /sv/net/how-to-change-format-of-cell/
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

För att ändra formatet på en cell med hjälp av Aspose.Cells kan du använda följande metoder:
1. [Cell.SetStyle(Style style)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle)
2. [Cell.SetStyle(Style style, bool explicitFlag)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle_2)
3. [Cell.SetStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle_1)


## **Exempelkod**
I det här exemplet skapar vi en Exceldatabok, lägger till lite provdata, får åtkomst till det första kalkylarket och får två celler ("A2" och "B3"). Sedan får vi stilen på cellen, ställer in olika formateringsalternativ (t.ex. typsnittsfärg, fetstil) och ändrar formatet på cellen. Slutligen sparar vi arbetsboken till en ny fil.
![todo:image_alt_text](change-format.png)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-change-format.cs" >}}
{{< app/cells/assistant language="csharp" >}}
