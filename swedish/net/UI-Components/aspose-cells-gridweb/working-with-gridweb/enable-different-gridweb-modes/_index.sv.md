---
title: Aktivera olika GridWeb lägen
type: docs
weight: 60
url: /sv/net/aspose-cells-gridweb/enable-different-gridweb-modes/
keywords: GridWeb,EditMode,SessionMode
description: Den här artikeln introducerar hur man arbetar med EditMode och SessionMode i GridWeb.
---

{{% alert color="primary" %}} 

Den här artikeln beskriver olika lägen för Aspose.Cells.GridWeb. Dessa lägen är logiskt differentierade på grund av sina olika funktioner och beteenden. Vi har identifierat flera typer av lägen:

- Redigeringsläge
- Visa läge
- Session Mode
- Sessionlöst läge

Alla dessa lägen har sina egna egenskaper. Utvecklare kan arbeta med Aspose.Cells.GridWeb i vilket läge de än vill enligt sina behov. Vi kommer att titta på varje läge nedan.

{{% /alert %}} 
## **Redigeringsläge**
Som standard är Aspose.Cells.GridWeb-kontrollen i redigeringsläge. I redigeringsläge kan du fullständigt redigera eller modifiera rutinnehållet med alla funktioner som erbjuds av Aspose.Cells.GridWeb-kontrollen. Dessa funktioner inkluderar:

- Spara rutinnehållet i Microsoft Excel-filer.
- Skicka data till en server.
- Beräkna formler.
- Ångra eller kassera tidigare åtgärder.
- Hantera rader och kolumner.
- Klippa, kopiera eller klistra in data.
- Formatera celler etc.

**GridWeb-kontroll i redigeringsläge** 

![todo:image_alt_text](enable-different-gridweb-modes_1.png)

Utvecklare kan också växla till redigeringsläge programmässigt genom att ställa in Egenskapen EditMode för GridWeb-kontrollen till true.

Nedan visas ett exempel på hur man aktiverar redigeringsläget programmatiskt.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyEditMode.cs" >}}

{{% alert color="primary" %}} 

När en användare klickar på **Ångra**-knappen återgår GridWeb till sitt tidigare tillstånd (tillståndet före den senaste återkopplingen till servern). Den avbryter inte tidigare åtgärder en efter en.

{{% /alert %}} 
## **Visningsläge**
När GridWeb-kontrollen är i Visningsläge kan användare inte redigera eller ändra rutinens innehåll, vilket innebär att användare endast kan se rutinens innehåll. Därför kallas det här läget Visningsläge. I Visningsläge är några knappar (**Skicka**, **Spara** och **Ångra**) dolda och menyn som visas när du högerklickar innehåller endast alternativet **Kopiera**.

**GridWeb-kontroll i visningsläge** 

![todo:image_alt_text](enable-different-gridweb-modes_1.png)

Om utvecklare vill att deras användare endast ska se data kan de växla till Visningsläge programmatiskt genom att ange GridWeb-kontrollens EditMode-egenskap till false.

Nedan visas ett exempel på hur man aktiverar visningsläget programmatiskt



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyViewMode.cs" >}}

{{% alert color="primary" %}} 

Även i visningsläge kan användare ändra höjd och bredd på rader och kolumner.

{{% /alert %}} 
## **Session-läge**
Aspose.Cells.GridWeb-kontrollen håller kalkyldata i webbserverns användarsession mellan varje begäran från en webbanvändare. Det innebär att GridWeb-kontrollen alltid fungerar i Session-läge som standard. Om du inte arbetar i Session-läge, aktivera det genom att ange GridWeb-kontrollens SessionMode-egenskap till SessionMode.Session.

Nedan visas ett exempel på hur man aktiverar sessionläge programmatiskt



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionMode.cs" >}}
## **Sessionlöst läge**
Vi har redan diskuterat att Session-läge ger bäst prestanda genom att använda en användarsession för att ladda och lagra kalkyldata. Det förbrukar dock servers minne. Så om det finns ett stort antal samtidiga användare kan minnesproblem uppstå. För att spara serverminne och stödja stort antal samtidiga användare, överväg Sessionlöst läge.

Sessionlöst läge kan aktiveras genom att ange GridWeb-kontrollens SessionMode-egenskap till SessionMode.ViewState.

Nedan visas ett exempel på hur man aktiverar sessionlöst läge programmatiskt



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionlessMode.cs" >}}

{{% alert color="primary" %}} 

VIKTIGT: När SessionMode-egenskapen för GridWeb är satt till SessionMode.ViewState, lagrar rutinen data i sidans ViewState. Det innebär att den renderade sidan är större och kräver mer nätverkstrafik.

{{% /alert %}} {{% alert color="primary" %}} 

Om du vill använda SQL Server eller StateServer för att lagra sessioner, använd sessionsläget. GridWeb-kontrollen stöder att serialisera sina data till SQL Server eller StateServer.

Var god kontrollera följande artikel för mer hjälp.

- [Arbete med GridWeb när ASP.NET Session state mode är SQL Server](/cells/sv/net/aspose-cells-gridweb/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/)

{{% /alert %}}
