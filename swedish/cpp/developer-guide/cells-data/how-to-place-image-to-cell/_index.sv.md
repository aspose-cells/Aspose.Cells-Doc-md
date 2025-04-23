---
title: Hur man infogar bild i cell med C++
linktitle: Hur man infogar bild i cell
type: docs
weight: 130
url: /sv/cpp/how-to-insert-picture-in-cell/
description: Lär dig hur du infogar en bild i en cell med Aspose.Cells med C++.
keywords: Hur man infogar bild i cell, Infoga bild över celler, Placera bild i cell, Placera bild över celler, Hur man placerar bild i cell, Hur man placerar bild över celler, Växla mellan bild i cell och bild över celler, Växla mellan Plats i cell och Plats över celler
---

## **Möjliga användningsscenario**
 Bilden tillför ett ljus till ditt arbetsblad och ger en visuell representation av innehållet. De gör det också lättare för dig att förstå datan och komma med insikter. Även om du har kunnat använda bilder i Excel i många år, har Excel först nyligen möjliggjort att bilder blir faktiska cellvärden. Även om layouten på teckningen ändras, förblir den kopplad till datan. Du kan använda den i tabeller, sortera, filtrera, inkludera i formler, och så vidare!

## **Hur man infogar bild i cell med Excel**
Om hur man infogar en bild i en cell i Excel, följ dessa steg:

1. Gå till fliken Infoga och klicka på alternativet Bilder.
2. Välj **Plats i cell**. Välj en av följande källor från rullgardinsmenyn Infoga bild från (**Den här enheten**, **Lagerbilder** och **Onlinebilder**). Den här enheten för att infoga bild från din enhet. Lagerbilder för att infoga bild från lagerbilder. Onlinebilder för att infoga bild från webben.
<br>
<img src="1.png" width=60% />
3. Välj bild och infoga bild i en cell.
<br>
<img src="8.png" width=60% />

## **Hur man infogar bild över celler med Excel**
Om hur man infogar en bild över celler i Excel, följ dessa steg:

1. Gå till fliken Infoga och klicka på alternativet Bilder.
2. Välj **Plats över celler**. Välj en av följande källor från rullgardinsmenyn Infoga bild från (**Den här enheten**, **Lagerbilder** och **Onlinebilder**). Den här enheten för att infoga bild från din enhet. Lagerbilder för att infoga bild från lagerbilder. Onlinebilder för att infoga bild från webben.
<br>
<img src="2.png" width=60% />
3. Välj bild och infoga bild över celler.
<br>
<img src="3.png" width=60% />

## **Hur man växlar mellan bild i cell och bild över celler med Excel**
Du kan enkelt växla från **Bild i cell** till **Bild över celler**. Följ dessa steg:
1. Högerklicka på cellen och välj **Bild i cell** > **Placera över celler**. 
<br>
<img src="4.png" width=60% />
2. Resultatet efter växlingen är följande:
<br>
<img src="5.png" width=60% />

## **Hur man växlar från Bild över celler till Bild i cell med hjälp av Excel**
Du kan enkelt växla från **Bild över celler** till **Bild i cell**. Följ dessa steg:
1. Högerklicka på bilden och välj **Placera i cell**. 
<br>
<img src="6.png" width=60% />
2. Resultatet efter växlingen är följande:
<br>
<img src="7.png" width=60% />

## ** Hur man infogar bild i cell med C++**
Infoga bild i cell med hjälp av Aspose.Cells. Se följande exempelkod. Efter att ha utfört exempelkoden infogas en bild i en cell.
 1. Skapa ett Workbook-objekt. 
2. Hämta cellen där du vill infoga bilden.
3. Ange Cell.EmbeddedImage-egenskapen. 
4. Slutligen sparas arbetsboken i [utdata XLSX](ut.xlsx)-format. 

## **Exempelkod**

```c++
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get cell D8
    Cell d8 = worksheet.GetCells().Get(u"D8");

    // Read image file into byte vector
    std::ifstream file("aspose.png", std::ios::binary);
    std::vector<uint8_t> imageData((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());

    // Convert to Aspose's Vector and set embedded image in cell D8
    d8.SetEmbeddedImage(Vector<uint8_t>(imageData.data(), imageData.size()));

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
