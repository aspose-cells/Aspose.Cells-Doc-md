---
title: Cellformatering
type: docs
weight: 50
url: /sv/cpp/cells-formatting/
---

## **Formatera cell eller cellområde**
Om du vill formatera en cell eller cellområde, då tillhandahåller Aspose.Cells klassen [Style](https://reference.aspose.com/cells/cpp/aspose.cells/style/). Du kan uppnå all formatering av cell eller cellområde med hjälp av denna klass. Några av de saker som kan åstadkommas med IStyle klassen rörande formatering är följande

- Ange fyllfärg i cellen
- Ange textradbrytning i cellen
- Ange cellernas ramar som topp-, vänster-, botten- och högerramar, etc.
- Ange fontfärg, fontstorlek, fontnamn, överstrykning, fetstil, kursiv, understrykning, etc.
- Ange textens horisontella eller vertikala justering till höger, vänster, topp, botten, mitten, etc.

Om du vill ange stilen för en enskild cell, använd då metoden [Cell->SetStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setstyle/) och om du vill ange stilen för en cellmängd, använd då metoden [Range->ApplyStyle()](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/).
## **Exempelkod**
Följande exempel på kod formaterar cell C4 i arbetsbladet på olika sätt och skärmdumpen visar den [utdata excelfilen](21266438.xlsx) som genererats för din referens.

![todo:image_alt_text](cells-formatting_1.png)



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CellsFormatting-FormatCellOrRangeOfCells-new.cpp" >}}
