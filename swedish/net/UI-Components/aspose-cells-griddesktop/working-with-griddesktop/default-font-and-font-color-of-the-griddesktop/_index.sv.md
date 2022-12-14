---
title: Standardteckensnitt och teckensnittsfärg för GridDesktop
type: docs
weight: 70
url: /sv/net/default-font-and-font-color-of-the-griddesktop/
---
## **Möjliga användningsscenarier**
Ibland vill du ändra standardteckensnittet och teckensnittsfärgen för GridDesktop. Använd följande två egenskaper för detta ändamål. Du kan komma åt dessa egenskaper vid Design Time eller Runtime beroende på dina behov.

- GridDesktop.DefaultCellFont
- GridDesktop.DefaultCellFontColor
## **Ändra standardteckensnitt och teckensnittsfärg vid designtid**
Följande skärmdump visar hur du ändrar standardteckensnitt och teckensnittsfärg för GridDesktop vid designtid.

![todo:image_alt_text](default-font-and-font-color-of-the-griddesktop_1.png)
## **Ändra standardteckensnitt och teckensnittsfärg vid körning**
Följande exempelkod förklarar hur du ändrar standardteckensnitt och teckensnittsfärg för GridDesktop vid körning.

{{< highlight "java" >}}

 //Assign your desired Font object to DefaultCellFont property

System.Drawing.Font fnt = new System.Drawing.Font("Arial Black", 18);

this.gridDesktop1.DefaultCellFont = fnt;

//Assign your desired Font color to DefaultCellFontColor property

this.gridDesktop1.DefaultCellFontColor = System.Drawing.Color.Blue;

{{< /highlight >}}
