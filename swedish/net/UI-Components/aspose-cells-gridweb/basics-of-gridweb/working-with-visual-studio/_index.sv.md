---
title: Arbeta med Visual Studio
type: docs
weight: 20
url: /sv/net/aspose-cells-gridweb/work-with-visual-studio/
keywords: GridWeb,visualstudio
description: Den här artikeln introducerar hur man använder GridWeb i Visual Studio.
---

{{% alert color="primary" %}} 

Den här ämnet förklarar hur man använder Aspose.Cells.GridWeb i ASP.NET-applikationer med hjälp av Visual Studio.NET 2005. Det här ämnet är användbart för nybörjarnivåutvecklare som arbetar med Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Arbeta med Aspose.Cells.GridWeb med Visual Studio 2013**
Detta ämne visar hur man använder Aspose.Cells.GridWeb genom att skapa en provwebbplats i Visual Studio 2013. Processen har delats in i steg.
### **Steg 1: Skapa ny webbplats**
1. Öppna Visual Studio 2013.
1. Från menyn **File** väljer du **New Menu**, sedan **Web Site**. 

![todo:image_alt_text](working-with-visual-studio_1.png)


Dialogrutan för ny webbplats öppnas. 

1. Välj **ASP.NET Web Forms Site** från Visual Studio-installerade mallar.
1. Välj HTTP-läge för platsen för webbplatsen. 

![todo:image_alt_text](working-with-visual-studio_2.png)




1. Ange en plats där webbplatsens filer ska skapas och lagras. 
   1. Klicka på **Bläddra** i dialogrutan för ny webbplats. 

![todo:image_alt_text](working-with-visual-studio_3.png)



Dialogrutan Välj plats visas. 

1. Klicka på fliken **Local IIS**.
   Alla mappar och webbapplikationer som är lagrade i din IIS rotkatalog visas (till exempel: C:\Inetpub\wwwroot). 

![todo:image_alt_text](working-with-visual-studio_4.png)




1. Skapa nu en ny webbapplikation i din lokala IIS där webbplatsens filer kommer att lagras.
   Dialogrutan Välj plats låter dig skapa och ta bort webbapplikationer eller virtuella kataloger i din lokala IIS. För att skapa en webbapplikation, klicka på en knapp enligt visas nedan i figuren. 

![todo:image_alt_text](working-with-visual-studio_5.png)



En ny webbapplikation med standardnamnet WebSite skapas. 

1. Byt namn på webbapplikationen. Vi döpte den till GridWebOn2013.
1. Klicka på **Öppna**. 

![todo:image_alt_text](working-with-visual-studio_6.png)



You return to the New Web Site dialog. The path of web site location is set to <http://localhost/GridWebOn2013>. 

1. Klicka på **OK** för att låta Visual Studio skapa en webbplats. 

![todo:image_alt_text](working-with-visual-studio_7.png)
### **Steg 2: Kontrollera käll- och designvyer för en webbsida**
En standardwebbplats har skapats av Visual Studio 2013. Den innehåller en default.aspx-webbsida med lite dum text och markup. 

**Källvy av default.aspx-sida** 

![todo:image_alt_text](working-with-visual-studio_8.png)



Alla webbsidor (inklusive ASP.NET) kan öppnas i två lägen. Ett är källvy som låter utvecklare komma åt och modifiera källkoden. Det andra läget är designvy som kan användas för att utforma webbsidor på ett WYSIWYG-sätt. Ovanstående skärmbild visar en källvy av default.aspx-webbsidan. För att visa designvyn, klicka på **Design**. 

**Designvy av default.aspx-sida** 

![todo:image_alt_text](working-with-visual-studio_9.png)




Ta bort Default.aspx-sidan som lades till av Visual Studio och lägg till en ny tom Default.aspx-sida.

![todo:image_alt_text](working-with-visual-studio_10.png)
### **Steg 3: Lägga till Aspose.Cells.GridWeb till webbsida**
Du kan enkelt lägga till Aspose.Cells.GridWeb (eller GridWeb) kontroll till en webbsida genom att dra den från verktygsfältet. 

![todo:image_alt_text](working-with-visual-studio_11.png)




{{% alert color="primary" %}} 

Om du inte vet hur du lägger till Aspose.Cells.GridWeb i verktygsfältet, se [Integrera Aspose.Cells Grid Controls med Visual Studio.NET](/cells/sv/net/aspose-cells-gridweb/integrate-aspose-cells-grid-controls-with-visual-studio-net/). 

{{% /alert %}} 

När GridWeb-kontrollen släpps på webbsidan skulle den renderas så här: 

![todo:image_alt_text](working-with-visual-studio_12.png)



### **Step 4: Change the <!DOCTYPE> tag**
1. Switch to source view and find the following **<!DOCTYPE>** tag in the source code: 

**ASP.NET**

{{< highlight csharp >}}



<!DOCTYPE html>



{{< /highlight >}}

1. Välj den kompletta taggen. 

![todo:image_alt_text](working-with-visual-studio_13.png)




1. Retain, change or delete the <!DOCTYPE> tag.
1. Or modify the <!DOCTYPE> tag with the following one: 

{{< highlight csharp >}}



<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">



{{< /highlight >}}
### **Steg 5: Ändra storlek på Aspose.Cells.GridWeb Control**
Du kan ändra bredden och höjden på GridWeb-kontrollen efter att ha dragit den till webbplatsen. 

I designläge kan du ändra bredd och höjd på GridWeb. 

![todo:image_alt_text](working-with-visual-studio_14.png)



### **Steg 6: Konfigurera egenskaperna för Aspose.Cells.GridWeb**
Konfigurera egenskaperna för Aspose.Cells.GridWeb i WYSIWYG genom att klicka på **Egenskaper**-knappen på höger sida av Visual Studio 2013 IDE. 
En egenskapsdialog visas. 

![todo:image_alt_text](working-with-visual-studio_15.png)



Egenskapsrutan gör det möjligt att konfigurera utseendet och känslan hos GridWeb samt andra egenskaper för att styra GridWebs beteende.
### **Steg 7: Kör din första webbplats med Aspose.Cells.GridWeb**
Bygg och kör webbplatsen. 

1. Kör webbplatsen direkt från Visual Studio genom att trycka på Ctrl+F5 eller klicka på **Starta felsökning**. 

![todo:image_alt_text](working-with-visual-studio_16.png)

Nu kan du börja använda GridWeb-kontrollen. 

**GridWeb-kontroll i aktion** 

![todo:image_alt_text](working-with-visual-studio_17.png)
