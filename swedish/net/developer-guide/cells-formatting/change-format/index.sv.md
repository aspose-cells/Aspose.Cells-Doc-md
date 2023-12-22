---
title: Ändra formatet på en cell
description: Så här använder du Aspose.Cells-biblioteket i C# för att ändra formateringen av celler, inklusive teckensnitt, färg, ram, etc. Genom att justera dessa egenskaper har du mer kontroll över hur celler ser ut och visas.
keywords: Aspose.Cells, cell formatting, C#, font, color, border
type: docs
weight: 105
url: /sv/net/how-to-change-format-of-cell/
---
##  **Möjliga användningsscenarier**
När du vill markera vissa data kan du ändra stilen på cellerna.

##  **Hur man ändrar formatet på en cell i Excel**

För att ändra formatet för en enskild cell i Excel, följ dessa steg:

1. Öppna Excel och öppna arbetsboken som innehåller cellen du vill formatera.

2. Leta upp cellen du vill formatera.

3. Högerklicka på cellen och välj "Format Cells" från snabbmenyn. Alternativt kan du välja cellen och gå till fliken Hem i Excel-bandet, klicka på rullgardinsmenyn "Format" i gruppen "Cells" och välj "Format Cells".

4. Dialogrutan "Format Cells" visas. Här kan du välja olika formateringsalternativ att tillämpa på den valda cellen. Du kan till exempel ändra teckensnittsstil, teckenstorlek, teckensnittsfärg, nummerformat, ramar, bakgrundsfärg etc. Utforska de olika flikarna i dialogrutan för att komma åt olika formateringsalternativ.

5. När du har gjort de önskade formateringsändringarna klickar du på knappen "OK" för att tillämpa formateringen på den valda cellen.


##  **Hur man ändrar formatet på en cell med C#**

För att ändra formatet på en cell med Aspose.Cells kan du använda Du kan använda följande metoder:
1. [Cell.SetStyle(Style style)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle)
2. [Cell.SetStyle(Style style, bool explicitFlagga)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle_2)
3. [Cell.SetStyle(Style style, StyleFlag flagga)](https://reference.aspose.com/cells/net/aspose.cells/cell/setstyle/#setstyle_1)


##  **Exempelkod**
I det här exemplet skapar vi en Excel-arbetsbok, lägger till några exempeldata, kommer åt det första kalkylbladet och får två celler ("A2" och "B3"). Sedan får vi cellens stil, ställer in olika formateringsalternativ (t.ex. teckensnittsfärg, fetstil) och ändrar formatet till cellen. Slutligen sparar vi arbetsboken till en ny fil.
![todo:image_alt_text](change-format.png)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-change-format.cs" >}}
