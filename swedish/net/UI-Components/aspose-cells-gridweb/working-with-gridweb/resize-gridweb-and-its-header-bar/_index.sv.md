---
title: Ändra storlek på GridWeb och dess rubrikfält
type: docs
weight: 30
url: /sv/net/resize-gridweb-and-its-header-bar/
---
{{% alert color="primary" %}} 

[Lägg till GridWeb till webbformulär](/cells/sv/net/add-gridweb-to-web-form/), diskuterade storleksändring av Aspose.Cells.GridWeb-kontrollen med WYSIWYG. Den här artikeln förklarar hur man gör samma sak men vid körning med Aspose.Cells.GridWeb API. Den förklarar också hur man ändrar storlek på rubrikfälten för Aspose.Cells.GridWeb-kontrollen för att göra deras data lättare att läsa.

{{% /alert %}} 
## **Ändra bredd och höjd på Aspose.Cells.GridWeb**
Ändra bredd och höjd på Aspose.Cells. GridWeb-kontroll är en enkel men viktig funktion. Aspose.Cells.GridWeb-kontrollen representeras av GridWeb-klassen i API:t. För att ändra storlek på bredden och höjden på GridWeb-kontrollen, använd helt enkelt dess egenskaper för bredd och höjd.

{{% alert color="primary" %}} 

Kontrollens bredd och höjd kan definieras i pixlar eller punkter.

{{% /alert %}} 

Utdata från kodavsnittet som följer visas nedan.

**Ändrad bredd och höjd på GridWeb-kontrollen** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeGridWeb.aspx-ResizeGridWeb.cs" >}}
### **Ändra bredd och höjd på sidhuvudet**
Aspose.Cells.GridWeb-kontrollen innehåller två huvudfält enligt följande:

- Översta rubrikfältet, detta rubrikfält representerar kolumner som A , B , C , D etc.
- Vänster rubrikfält, denna rubrikstapel representerar rader som 1 , 2 , 3 , 4 osv.

Båda dessa rubrikfält visas nedan.

**Rubriker** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_2.png)

Ändra höjden på den översta rubriken och bredden på den vänstra rubriken med hjälp av GridWeb-kontrollens HeaderBarHeight respektive HeaderBarWidth egenskaper. Bilden nedan visar resultatet av kodexemplet som följer.

**Ändrad rubrikstavs bredd och höjd** 

![todo:image_alt_text](resize-gridweb-and-its-header-bar_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeHeaderBar.aspx-ResizeHeaderBar.cs" >}}
