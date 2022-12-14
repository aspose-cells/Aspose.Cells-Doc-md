---
title: Aktivera olika GridWeb-lägen
type: docs
weight: 60
url: /sv/net/enable-different-gridweb-modes/
---
{{% alert color="primary" %}} 

Den här artikeln beskriver Aspose.Cells.GridWebs olika lägen. Dessa lägen är logiskt differentierade på grund av deras olika egenskaper och beteenden. Vi har identifierat flera typer av lägen:

- Redigeringsläge
- Visningsläge
- Sessionsläge
- Sessionslöst läge

Alla dessa lägen har sina egna egenskaper. Utvecklare kan arbeta med Aspose.Cells.GridWeb i alla lägen enligt deras krav. Vi kommer att titta på varje läge nedan.

{{% /alert %}} 
## **Redigeringsläge**
Som standard är Aspose.Cells.GridWeb-kontrollen i redigeringsläge. I redigeringsläge kan du helt redigera eller modifiera rutnätets innehåll med alla funktioner som erbjuds av Aspose.Cells.GridWeb-kontrollen. Dessa funktioner inkluderar:

- Spara rutnätsinnehållet till Microsoft Excel-filer.
- Skicka data till en server.
- Beräkna formler.
- Ångra eller kassera tidigare åtgärder.
- Hantera rader och kolumner.
- Klipp ut, kopiera eller klistra in data.
- Formatera celler etc.

**GridWeb-kontroll i redigeringsläge** 

![todo:image_alt_text](enable-different-gridweb-modes_1.png)

Utvecklare kan också byta till redigeringsläge programmatiskt genom att ställa in egenskapen EditMode för GridWeb-kontrollen till true.

Exemplet nedan visar hur du aktiverar redigeringsläge programmatiskt.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyEditMode.cs" >}}

{{% alert color="primary" %}} 

 Närhelst en användare klickar på**Ångra** knappen, för den GridWeb till sitt tidigare tillstånd (tillståndet före den senaste återsändningen till servern). Den avbryter inte tidigare åtgärder en efter en.

{{% /alert %}} 
## **Visningsläge**
När GridWeb-kontrollen är i visningsläge kan användare inte redigera eller ändra rutnätsinnehåll, vilket innebär att användare bara kan se rutnätsinnehåll. Det är därför detta läge kallas View mode. I visningsläge, några knappar (**Skicka in**, **Spara** och**Ångra** ) är dolda och menyn som visas när du högerklickar innehåller bara**Kopiera** alternativ.

**GridWeb-kontroll i View Mode** 

![todo:image_alt_text](enable-different-gridweb-modes_1.png)

Om utvecklare vill att deras användare endast ska se data kan de byta till visningsläge programmatiskt genom att ställa in GridWeb-kontrollens EditMode-egenskap till false.

Exemplet nedan visar hur du aktiverar visningsläget programmatiskt



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyViewMode.cs" >}}

{{% alert color="primary" %}} 

Även i vyläget kan användare ändra höjden och bredden på rader och kolumner.

{{% /alert %}} 
## **Sessionsläge**
Kontrollen Aspose.Cells.GridWeb håller arkdata i användarsessionen på webbservern mellan varje begäran från en webbanvändare. Det betyder att GridWeb-kontrollen alltid fungerar i sessionsläge som standard. Men om du inte arbetar i sessionsläge, slå på det genom att ställa in GridWEb control#s SessionMode-egenskap till SessionMode.Session.

Exemplet nedan visar hur du aktiverar sessionsläget programmatiskt



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionMode.cs" >}}
## **Sessionslöst läge**
Vi har redan diskuterat att sessionslägesmetod ger bästa prestanda genom att använda en användarsession för att ladda och lagra arkdata. Det förbrukar dock serverminne. Så om det finns ett stort antal samtidiga användare kan minnesproblem uppstå. För att spara serverminne och stödja ett stort antal samtidiga användare, överväg Sessionless-läget.

Sessionslöst läge kan aktiveras genom att ställa in GridWeb-kontrollens SessionMode-egenskap till SessionMode.ViewState.

Exemplet nedan visar hur man aktiverar sessionslöst läge programmatiskt



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionlessMode.cs" >}}

{{% alert color="primary" %}} 

VIKTIGT: När GridWebs SessionMode-egenskap är inställd på SessionMode.ViewState, lagrar rutnätet data i sidans ViewState. Det betyder att den renderade sidan är större och förbrukar mer nätverkstrafik.

{{% /alert %}} {{% alert color="primary" %}} 

Om du vill använda SQL Server eller StateServer för att hålla sessioner, använd sessionsläge. GridWeb-kontrollen stöder serialisering av dess data till SQL Server eller StateServer.

Läs följande artikel för mer hjälp.

- [Fungerar med GridWeb när ASP.NET Session tillståndsläge är SQL Server](/cells/sv/net/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/)

{{% /alert %}}
