---
title: Lägg till GridWeb till webbformulär
type: docs
weight: 10
url: /sv/net/add-gridweb-to-web-form/
---
{{% alert color="primary" %}} 

Det här avsnittet ger en grundläggande steg-för-steg-guide för nybörjare som hjälper dem att skapa och använda Aspose.Cells.GridWeb-kontrollen i webbapplikationer.

{{% /alert %}} 
## **Skapa och använda Aspose.Cells.GridWeb Control**
### **Steg 1: Skapa ett webbapplikationsprojekt**
Skapa först ett webbapplikationsprojekt där du kan använda Aspose.Cells.GridWeb-kontrollen:

1. Öppna Visual Studio.
1.  Från**Fil** menyn, välj**Ny** följd av**Projekt**. 

![todo:image_alt_text](add-gridweb-to-web-form_1.png)



En dialogruta för nytt projekt visas.

1.  Välj**ASP.NET Webbapplikation** för önskat språk.

![todo:image_alt_text](add-gridweb-to-web-form_2.png)

1.  Välj**Webbformulär** mall.

![todo:image_alt_text](add-gridweb-to-web-form_3.png)

1. Lägg till ett nytt webbformulär till projektet.
### **Steg 2: Bädda in kontroll i webbformuläret**
 Dra och släpp Aspose.Cells.GridWeb-kontrollen från Visual Studio-verktygslådan till webbformuläret.

![todo:image_alt_text](add-gridweb-to-web-form_4.png)

{{% alert color="primary" %}} 

 För att lära dig hur du lägger till Aspose.Cells Grid-kontroller till Visual Studio Toolbox, läs[Integrera Aspose.Cells.Grid-kontroller med Visual Studio.NET](/cells/sv/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/).

{{% /alert %}} 

 När kontrollen har lagts till i formuläret renderas den så här:

![todo:image_alt_text](add-gridweb-to-web-form_5.png)
### **Steg 3: Ändra storlekskontroll**
Formuläret återges i en standardstorlek. Justera storleken genom att dra kanterna eller hörnen.

![todo:image_alt_text](add-gridweb-to-web-form_6.png)
### **Steg 4: Ställa in kontrollegenskaper**
 Aspose.Cells.GridWeb-kontroll kan också konfigureras med olika egenskaper.

![todo:image_alt_text](add-gridweb-to-web-form_7.png)

Det är möjligt att justera många egenskaper för kontrollen med dialogrutan Egenskaper. Grundläggande egenskaper inkluderar höjd, bredd, färg och visuella stilar. Avancerade egenskaper inkluderar redigeringsläge, sessionsläge och dubbelklicksläge. Dessutom är det möjligt att ställa in anpassade händelsehanterare i dialogrutan Egenskaper.

Det finns också några extra konfigurationsverktyg för Aspose.Cells.GridWeb som kan ses längst ner i dialogrutan Egenskaper som hyperlänkar, eller högerklicka på GridWeb-kontrollen för att hitta dem. Dessa konfigurationsverktyg inkluderar:

- Anpassade kommandoknappar
#### **Anpassade kommandoknappar**
Så här öppnar du redigeraren för anpassade kommandoknappar:
 Högerklicka på GridWeb-kontrollen och välj**Anpassade kommandoknappar**. 

![todo:image_alt_text](add-gridweb-to-web-form_8.png)



 Dialogrutan CustomCommandButton Collection Editor visas.

![todo:image_alt_text](add-gridweb-to-web-form_9.png)

Dialogrutan låter utvecklare lägga till och ta bort anpassade kommandoknappar i GridWeb-kontrollen.


### **Viktig**
Aspose.Cells.GridWeb tillhandahåller också sina resursfiler med kontrollen. Den "acw_client" är en mapp (@ din installationskatalog) som innehåller filer och Aspose.Cells. GridWeb använder denna mapp för att hantera sin interna konfiguration och andra funktioner, den har skriptfiler, bildfiler och andra filer för att specificera GridWebs beteende och ställa in andra operationer. config-filen används för att hantera de inbäddade klientresurserna (bilder, skript, etc.). Dessutom, när du behöver distribuera webbapplikationen med GridWeb-kontroll, skulle du också kopiera "acw_client"-katalogen till din projektmapp åtminstone kunde din webbapplikation (utplacerad över servern) inte hitta den. Du kan alltid ange resursmappen genom att lägga till följande kodrader i konfigurationssektionen (t.ex. i web.config-filen i din VS.NET Projekt):



|<p>{{< highlight "java" >}}</p><p> <appSettings></p><p>  <add key="aspose.cells.gridweb.acw_client_path" value="/grid/acw_client/"/> </p><p></appSettings></p><p>{{< /highlight >}}</p>|
|:- |


{{% alert color="primary" %}}

Sökvägen är alltid relaterad till projektets katalog. Du bör inte använda någon katalog som ligger utanför projektets katalog. Så det är nödvändigt att kopiera "acw_client"-katalogen (@ din GridWeb-installationsmapp) till projektets katalog/underkatalog.

{{% /alert %}}
### **Steg 5: Kör webbapplikation**
 Kör programmet genom att trycka på Ctrl+F5 eller klicka på**Start** knapp.

 När applikationen körs i en webbläsare visas sidan WebForm1.aspx, som nu innehåller en tom Aspose.Cells.GridWeb-kontroll. Lägg till värden i celler genom att klicka på dem. Det är också möjligt att utföra andra uppgifter som att ändra höjden på en rad eller bredden på en kolumn, kopiera (Ctrl+C) eller klippa (Ctrl+X) celldata till urklipp och klistra in (Ctrl+V) data i cell . För att utföra fler operationer, högerklicka på kontrollen för att se en fullständig lista med alternativ.

**Snabbmeny för GridWeb-kontroll** 

![todo:image_alt_text](add-gridweb-to-web-form_10.png)
