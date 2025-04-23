---
title: Ändra formatet på en cell
linktitle: Ändra formatet på en cell
description: Hur man använder Aspose.Cells biblioteket i Node.js via C++ för att ändra cellformatering, inklusive teckensnitt, färg, kant osv. Genom att justera dessa egenskaper får du mer kontroll över hur cellerna ser ut och uppträder.
keywords: Aspose.Cells, cellformatering, Node.js via C++, teckensnitt, färg, kant
type: docs
weight: 20
url: /sv/nodejs-cpp/how-to-change-format-of-cell/
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


## **Hur man ändrar formatet på en cell med Node.js**

För att ändra formatet på en cell med Aspose.Cells kan du använda följande metoder:
1. [Cell.setStyle(Style)](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-)
2. [Cell.setStyle(Style, explicitFlag)](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-boolean-)
3. [Cell.setStyle(Style, StyleFlag)](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-styleflag-)


## **Exempelkod**
I detta exempel skapar vi en Excel-arbetsbok, lägger till några exempeldata, får tillgång till det första kalkbladet, och hämtar två celler ("A2" och "B3"). Sedan hämtar vi cellens stil, ställer in olika formateringsalternativ (t.ex. teckensnitts färg, fetstil), och ändrar formatet till cellen. Slutligen sparar vi arbetsboken till en ny fil.
![todo:image_alt_text](change-format.png)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ChangeFormat.js" >}}
