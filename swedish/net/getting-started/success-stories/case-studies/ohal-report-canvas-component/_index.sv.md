---
title: Ohal Report Canvas Component
type: docs
weight: 30
url: /sv/net/ohal-report-canvas-component/
---
{{% alert color="primary" %}}

[Rapportera PDF](https://blog.aspose.com/2008/03/17/complete-excel-export-capabilities-using-apis/)

**Användning av Aspose.Cells i Report Canvas Component**

Robert Chilvers, 17 mars 2008

{{% /alert %}}

## **Produktbakgrund**

Report Canvas-komponenten låter användaren skapa visuella rapporter baserade på en förladdad datauppsättning. Användaren kan lägga till olika komponenter till sin arbetsyta, inklusive bilder, textrutor, diagram och tabeller, de specificerar sedan data och hur den ska aggregeras. Användaren kan sedan ordna om och ändra storlek på objekten så att de passar deras sida. Användaren kan specificera färgpaletter och spara mallar för framtida bruk. Aspose.Cells används för att exportera alla objekt på arbetsytan till Excel med rätt data. Komponenten är skriven med VB.Net i Visual Studio 2008.

## **Kravscenario**

Vi valde Aspose.Cells på grund av dess nästan kompletta Microsoft Excel-exportmöjligheter. Viktigast för oss är möjligheten att exportera diagram och tabeller, särskilt i Microsoft Excel 2007 – dessa saknades i andra komponenter från tredje part.

## **Lösningsimplementering**

Varje objekt på rapportduken har en funktion som skickas till en instans av kalkylbladet Aspose.Cells och lägger till sig själv i kalkylbladet. När användaren begär en export initieras arbetsboken och kalkylbladen och varje objekt på rapportytan har den här funktionen anropad.

## **Fördelar**

Aspose.Cells tillät oss att bygga upp Excel-arbetsboken helt oberoende av Excel och sedan spara arbetsboken i det format som valts av användaren. Detta sparade timmar av felsökning av interaktionen vid användning av Excel-interop och implementering av olika rutiner för att spara till olika versioner av Excel.

## **Framtida implementering**

Vi kommer sannolikt att använda Aspose.Cells för all laddning och lagring av Excel-filer. Detta inkluderar att ladda datamallar och exportera resultat.

## **Slutsats**

{{% alert color="primary" %}}

Ännu har vi inte haft några problem med att använda Aspose.Cells-komponenterna och komponenten borde spara oss utvecklingstid på både kort och lång sikt. Support- och försäljningsfrågor har besvarats snabbt och hjälpsamt.

{{% /alert %}}
