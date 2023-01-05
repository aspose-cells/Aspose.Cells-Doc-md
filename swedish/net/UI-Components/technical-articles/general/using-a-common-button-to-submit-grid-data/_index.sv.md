---
title: Använda en gemensam knapp för att skicka rutdata
type: docs
weight: 20
url: /sv/net/using-a-common-button-to-submit-grid-data/
---
{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb tillhandahåller några inbyggda kommandoknappar som**Skicka in** och**Spara**. Använd dessa knappar för att utföra relaterade uppgifter.

Den här artikeln visar hur man skickar data till en server inte bara genom att klicka på GridWebs inbyggda**Spara** kommandoknapp, men genom att klicka på en vanlig ASP.NET-knapp (webbkontroll). Syftet med den här artikeln är att visa flexibiliteten hos Aspose.Cells.GridWeb. Dessutom använder den här artikeln också speciella funktioner som exponeras av Aspose.Cells.GridWeb för att användas i klientsideskriptet.

{{% /alert %}} 
## **Skicka rutnätsdata med en ASP.NET-knapp**
Aspose.Cells.GridWeb har tre inbyggda knappar (**Skicka in**, **Spara** och**Ångra** ). Efter redigering i GridWeb kan en användare klicka på**Skicka in** eller**Spara** knappen i flikfältet för att låta GridWeb skicka data till servern. Om användaren klickar på en arkflik utför GridWeb-kontrollen samma uppgift som de inbyggda kommandoknapparna. Aspose.Cells.GridWeb stöder också att lägga till denna funktionalitet till en vanlig ASP.NET-knappkontroll, men du måste lägga till lite extra kod till applikationen.
### **1. Skapa en testapplikation**
Öppna din Visual Studio.NET IDE och skapa ett nytt ASP.NET webbapplikationsprojekt. När applikationen har skapats kommer en standardsida för WebForm1.aspx att läggas till ditt projekt. Dra och släpp GridWeb-kontrollen från din verktygslåda till webbformuläret. Om du inte kan hitta GridWeb-kontrollen i din verktygslåda, gå till denna sida:[Integrera Aspose.Cells Grid Controls med Visual Studio.NET](/cells/sv/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/) för att lära dig mer om det. När GridWeb-kontrollen har lagts till i ditt webbformulär, lägg även till en Button-webbkontroll från Toolbox till ditt webbformulär.
### **2. Lägga till kod till Page_Load-händelse**
Nu är det dags att lägga till lite kod på sidan_Ladda händelse av webbformuläret. Du kan dubbelklicka på webbformuläret i designvyn och VS.NET IDE tar dig automatiskt till sidan_Ladda händelsehanterare där du skulle behöva använda Attributes-samlingen för knappen för att åsidosätta dess OnClick-händelse.

{{% alert color="primary" %}} 

ASP.NET Knappkontroll är en kontroll på serversidan. Närhelst den klickas utlöses en händelse på serversidan, men om du vill använda denna knappkontroll för att exekvera kod på klientsidan (normalt med javascript) måste du ändra dess onclick-attribut under Page_Load-händelse. Aspose.Cells.GridWeb tillhandahåller några funktioner som kan anropas i javascript för att hantera GridWeb-kontroll från klientsidan. I exemplet nedan har vi använt updateData & validateAll-funktioner (som är funktioner på klientsidan) i GridWeb för att uppdatera och validera Grid-data.

{{% /alert %}} 
#### **Kodexempel**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-UsingCommonSubmitButton.aspx-UsingCommonSubmitButton.cs" >}}
### **3. Kör programmet**
Nu kan du kompilera och köra din applikation genom att trycka på Ctrl+F5 och sidan kommer att öppnas i ett nytt webbläsarfönster. Låt oss lägga till några värden till GridWeb och trycka på knappen Skicka rutnätsdata till servern och du skulle se en återsändning för att uppdatera och validera GridWeb-data.
## **Slutsats**
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb erbjuder stor flexibilitet för att arbeta med GridWeb-kontroller från antingen server- eller klientsidan. Utvecklare har ett stort antal alternativ att använda GridWeb-kontroll i olika typer av scenarier för att ge bättre lösningar till sina kunder.

{{% /alert %}}
