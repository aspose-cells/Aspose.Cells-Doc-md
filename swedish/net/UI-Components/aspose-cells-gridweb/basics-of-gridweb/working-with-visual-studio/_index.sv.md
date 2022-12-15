---
title: Arbetar med Visual Studio
type: docs
weight: 20
url: /sv/net/working-with-visual-studio/
---
{{% alert color="primary" %}} 

Det här avsnittet förklarar hur man använder Aspose.Cells.GridWeb i ASP.NET-applikationer med Visual Studio.NET 2005. Det här ämnet är användbart för utvecklare på nybörjarnivå som arbetar med Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Arbeta med Aspose.Cells.GridWeb med Visual Studio 2013**
Det här avsnittet visar hur du använder Aspose.Cells.GridWeb genom att skapa en exempelwebbplats i Visual Studio 2013. Processen har delats upp i steg.
### **Steg 1: Skapa ny webbplats**
1. Öppna Visual Studio 2013.
1.  Från**Fil** menyn, välj**Ny meny** , då**Hemsida**. 

![todo:image_alt_text](working-with-visual-studio_1.png)


 Dialogrutan Ny webbplats öppnas.

1.  Välj**ASP.NET Webbformulär** från Visual Studio installerade mallar.
1.  Välj HTTP-läge för platsen för webbplatsen.

![todo:image_alt_text](working-with-visual-studio_2.png)




1.  Ange en plats där webbplatsfilerna ska skapas och lagras.
 1. Klicka**Bläddra** i dialogrutan Ny webbplats.

![todo:image_alt_text](working-with-visual-studio_3.png)



 Dialogrutan Välj plats visas.

1.  Klicka på**Lokal IIS** flik.
Alla mappar och webbapplikationer som är lagrade i din IIS-rotmapp visas (till exempel: C:\Inetpub\wwwroot).

![todo:image_alt_text](working-with-visual-studio_4.png)




1. Skapa nu en ny webbapplikation i din lokala IIS där webbplatsfilerna kommer att lagras.
 Dialogrutan Välj plats låter dig skapa och ta bort webbapplikationer eller virtuella kataloger i din lokala IIS. För att skapa en webbapplikation, klicka på en knapp som visas nedan i figuren.

![todo:image_alt_text](working-with-visual-studio_5.png)



 En ny webbapplikation med standardnamnet WebSite skapas.

1. Byt namn på webbapplikationen. Vi döpte om det till GridWebOn2013.
1.  Klick**Öppna**. 

![todo:image_alt_text](working-with-visual-studio_6.png)



 Du återgår till dialogrutan Ny webbplats. Sökvägen till webbplatsens plats är inställd på<http://localhost/GridWebOn2013>. 

1.  Klick**OK** för att låta Visual Studio skapa en webbplats.

![todo:image_alt_text](working-with-visual-studio_7.png)
### **Steg 2: Kontrollera käll- och designvyer för en webbsida**
 En standardwebbplats kommer att ha skapats av Visual Studio 2013. Den innehåller en default.aspx webbsida med lite dummytext och uppmärkning.

**Källvy för sidan default.aspx** 

![todo:image_alt_text](working-with-visual-studio_8.png)



Alla webbsidor (inklusive ASP.NET) kan öppnas i två lägen. En är källvyn som låter utvecklare komma åt och ändra källkoden. Det andra läget är designvy som kan användas för att designa webbsidor på ett WYSIWYG-sätt. Skärmbilden ovan visar en källvy av webbsidan default.aspx. Klicka på för att se designvyn**Design**. 

**Designvy av sidan default.aspx** 

![todo:image_alt_text](working-with-visual-studio_9.png)




Ta bort sidan Default.aspx som lagts till av Visual Studio och lägg till en ny tom sida Default.aspx.

![todo:image_alt_text](working-with-visual-studio_10.png)
### **Steg 3: Lägga till Aspose.Cells.GridWeb till webbsidan**
 Du kan helt enkelt lägga till Aspose.Cells.GridWeb (eller GridWeb) kontroll till en webbsida genom att dra den från verktygslådan.

![todo:image_alt_text](working-with-visual-studio_11.png)




{{% alert color="primary" %}} 

 Om du inte vet hur du lägger till Aspose.Cells.GridWeb i verktygslådan, se[Integrera Aspose.Cells Grid Controls med Visual Studio.NET](/cells/sv/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/). 

{{% /alert %}} 

 När GridWeb-kontrollen har släppts till webbsidan, skulle den återges så här:

![todo:image_alt_text](working-with-visual-studio_12.png)



### **Steg 4: Ändra taggen <!DOCTYPE>**
1.  Växla till källvy och hitta följande**<!DOCTYPE>** tag i källkoden:

**ASP.NET**

{{< highlight "csharp" >}}



<!DOCTYPE html>



{{< /highlight >}}

1.  Välj hela taggen.

![todo:image_alt_text](working-with-visual-studio_13.png)




1.  Behåll, ändra eller ta bort<!DOCTYPE>märka.
1.  Eller ändra<!DOCTYPE> tagga med följande:

{{< highlight "csharp" >}}



<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">



{{< /highlight >}}
### **Steg 5: Ändra storlek Aspose.Cells.GridWeb Control**
 Du kan ändra bredden och höjden på GridWeb-kontrollen efter att ha dragit den till webbplatsen.

 I designvyn kan du ändra storlek på bredden och höjden på GridWeb.

![todo:image_alt_text](working-with-visual-studio_14.png)



### **Steg 6: Konfigurera egenskaperna för Aspose.Cells.GridWeb**
 Konfigurera Aspose.Cells.GridWeb-egenskaperna i WYSIWYG genom att klicka på**Egenskaper** knappen på höger sida av Visual Studio 2013 IDE.
 En dialogruta för egenskaper visas.

![todo:image_alt_text](working-with-visual-studio_15.png)



Panelen Egenskaper gör det möjligt att konfigurera utseendet och känslan för GridWeb och vissa andra egenskaper för att kontrollera GridWebs beteende.
### **Steg 7: Kör din första webbplats som innehåller Aspose.Cells.GridWeb**
 Bygg och kör webbplatsen.

1.  Kör webbplatsen direkt från Visual Studio genom att trycka på Ctrl+F5 eller klicka**Börja felsöka**. 

![todo:image_alt_text](working-with-visual-studio_16.png)

 Nu kan du börja spela med GridWeb-kontroll.

**GridWeb-kontroll i aktion** 

![todo:image_alt_text](working-with-visual-studio_17.png)
