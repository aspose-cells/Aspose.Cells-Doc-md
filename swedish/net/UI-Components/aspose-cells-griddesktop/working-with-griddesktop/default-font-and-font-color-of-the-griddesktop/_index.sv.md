---
title: Standardtypsnitt och typsnittsfärg för GridDesktop
type: docs
weight: 70
url: /sv/net/aspose-cells-griddesktop/default-font-and-font-color-of-the-griddesktop/
keywords: GridDesktop, font, färg
description: Den här artikeln introducerar standardtypsnitt och typsnittsfärg i GridDesktop.
---

## **Möjliga användningsscenario**
Ibland vill man ändra standardtypsnittet och färgen för GridDesktop. Använd följande två egenskaper för detta ändamål. Du kan få åtkomst till dessa egenskaper vid designtid eller körtid beroende på dina behov.

- GridDesktop.DefaultCellFont
- GridDesktop.DefaultCellFontColor
## **Ändra standardtypsnitt och typsnittsfärg vid designtid**
Följande skärmbild visar hur man ändrar standardtypsnitt och typsnittsfärg för GridDesktop vid design

![todo:image_alt_text](default-font-and-font-color-of-the-griddesktop_1.png)
## **Ändra standardtypsnitt och typsnittsfärg vid körning**
Följande exempelkod förklarar hur man ändrar standardtypsnitt och typsnittsfärg för GridDesktop vid körning.

{{< highlight java >}}

 //Assign your desired Font object to DefaultCellFont property

System.Drawing.Font fnt = new System.Drawing.Font("Arial Black", 18);

this.gridDesktop1.DefaultCellFont = fnt;

//Assign your desired Font color to DefaultCellFontColor property

this.gridDesktop1.DefaultCellFontColor = System.Drawing.Color.Blue;

{{< /highlight >}}
