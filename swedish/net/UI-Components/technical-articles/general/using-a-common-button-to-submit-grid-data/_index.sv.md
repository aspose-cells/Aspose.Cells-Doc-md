---
title: Att använda en vanlig knapp för att skicka in rutdata
type: docs
weight: 20
url: /sv/net/aspose-cells-gridweb/using-a-common-button-to-submit-grid-data/
keywords: GridWeb, skicka in, knapp, anpassad
description: Den här artikeln beskriver användningen av skickaknappen i GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb tillhandahåller några inbyggda kommandoknappar som **Skicka** och **Spara**. Använd dessa knappar för att utföra relaterade uppgifter.

Denna artikel visar hur man skickar in data till en server inte bara genom att klicka på GridWebs inbyggda **Spara** -kommandoknapp, utan genom att klicka på en vanlig ASP.NET-knapp (Webbkontroll). Syftet med denna artikel är att visa flexibiliteten hos Aspose.Cells.GridWeb. Dessutom används även specialfunktioner som exponeras av Aspose.Cells.GridWeb som ska användas i klientsidescriptet.

{{% /alert %}} 
## **Skicka in rutdata med hjälp av en ASP.NET-knapp**
Aspose.Cells.GridWeb tillhandahåller tre inbyggda knappar (**Skicka**, **Spara** och **Ångra**). Efter redigering i GridWeb kan en användare klicka på **Skicka** eller **Spara** -knappen i flikfältet för att låta GridWeb skicka data till servern. Om användaren klickar på en arkflik utför kontrollen GridWeb samma uppgift som hos de inbyggda kommandoknapparna. Aspose.Cells.GridWeb stödjer också att lägga till denna funktionalitet till en vanlig ASP.NET-knappkontroll, men du måste lägga till lite extra kod i applikationen.
### **1. Skapa en testapplikation**
Öppna din Visual Studio.NET IDE och skapa ett nytt ASP.NET webbapplikationsprojekt. När applikationen har skapats läggs en standardwebform (WebForm1.aspx) till ditt projekt. Dra och släpp GridWeb-kontrollen från verktygsfältet till webbformuläret. Om du inte kan hitta GridWeb-kontrollen i verktygsfältet, hänvisar du till den här sidan: [Integrera Aspose.Cells Grid-kontroller med Visual Studio.NET](/cells/sv/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/) för att lära dig mer om det. Efter att GridWeb-kontrollen har lagts till ditt webbformulär lägger du också till en knappkontroll från verktygsfältet till ditt webbformulär.
### **2. Lägga till kod i Page_Load-händelsen**
Nu är det dags att lägga till lite kod till Page_Load-händelsen för webbformuläret. Du kan dubbelklicka på webbformuläret i designvyn och VS.NET IDE tar automatiskt dig till Page_Load-händelsen där du skulle behöva använda knappens Attributkollektion för att övertrumfa dess OnClick-händelse.

{{% alert color="primary" %}} 

ASP.NET-knappkontrollen är en serversidekontroll. När den klickas utlöses en serversidehändelse, men om du vill använda denna knappkontroll för att köra lite kod på klientsidan (normalt med hjälp av javascript) måste du modifiera dess onclick-attribut under Page_Load-händelsen. Aspose.Cells.GridWeb tillhandahåller några funktioner som kan åberopas i javascript för att hantera GridWeb-kontrollen från klientsidan. I exemplet nedan har vi använt updateData & validateAll-funktioner (som är klientsidefunktioner) från GridWeb för att uppdatera och validera rutdata.

{{% /alert %}} 
#### **Kodexempel**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-UsingCommonSubmitButton.aspx-UsingCommonSubmitButton.cs" >}}
### **3. Körning av applikationen**
Nu kan du kompilera och köra din applikation genom att trycka på Ctrl+F5, och sidan öppnas i ett nytt webbläsarfönster. Lägg till några värden i GridWeb och tryck på Skicka in rutdata till server-knappen så ser du en postback för att uppdatera och validera GridWeb-data.
## **Slutsats**
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb erbjuder stor flexibilitet för att arbeta med GridWeb-kontroller från antingen serversidan eller klientsidan. Utvecklare har ett brett antal alternativ att använda GridWeb-kontrollen i olika typer av scenarier för att ge bättre lösningar till sina kunder.

{{% /alert %}}
