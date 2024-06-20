---
title: Ändra storlek på GridWeb och dess huvudfält
type: docs
weight: 30
url: /sv/net/aspose-cells-gridweb/resize-gridweb-and-its-header-bar/
keywords: GridWeb, ändra storlek
description: Denna artikel introducerar hur man ändrar storlek i GridWeb.
---

{{% alert color="primary" %}} 

[Lägg till GridWeb till webbformulär](/cells/sv/net/aspose-cells-gridweb/add-gridweb-to-web-form/), diskuterade att ändra storleken på Aspose.Cells.GridWeb-kontrollen med WYSIWYG. Den här artikeln förklarar hur man gör samma sak, men vid körning med hjälp av Aspose.Cells.GridWeb API. Den förklarar också hur man ändrar storleken på huvudfälten för Aspose.Cells.GridWeb-kontrollen för att göra deras data lättare att läsa.

{{% /alert %}} 
## **Ändra bredd och höjd på Aspose.Cells.GridWeb**
Ändra bredden och höjden på Aspose.Cells.GridWeb-kontrollen är en enkel men viktig funktion. Aspose.Cells.GridWeb-kontrollen representeras av GridWeb-klassen i API:et. För att ändra bredd och höjd på GridWeb-kontrollen, använd dess bredd- och höjdegenskaper.

{{% alert color="primary" %}} 

Kontrollens bredd och höjd kan definieras i pixlar eller punkter.

{{% /alert %}} 

Utmatningen av kodsnutten som följer visas nedan.

Ändrad bredd och höjd på GridWeb-kontrollen 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeGridWeb.aspx-ResizeGridWeb.cs" >}}
### **Ändra bredd och höjd på sidhuvuden**
Aspose.Cells.GridWeb-kontrollen innehåller två sidhuvuden enligt följande:

- Övre huvudfält, detta huvudfält representerar kolumner som A, B, C, D etc.
- Vänster huvudfält, detta huvudfält representerar rader som 1, 2, 3, 4 etc.

Båda dessa sidhuvuden visas nedan.

Sidhuvuden 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_2.png)

Ändra höjden på det övre sidhuvudet och bredden på det vänstra sidhuvudet med hjälp av GridWeb-kontrollens HeaderBarHeight- respektive HeaderBarWidth-egenskaper. Figuren nedan visar utmatningen av kodexemplet som följer.

Ändrad sidhuvudsbredd och höjd 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeHeaderBar.aspx-ResizeHeaderBar.cs" >}}
