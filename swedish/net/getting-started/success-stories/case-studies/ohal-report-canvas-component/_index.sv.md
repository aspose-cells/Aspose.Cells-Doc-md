---
title: Ohal Rapport Canvas komponent
type: docs
weight: 30
url: /sv/net/ohal-report-canvas-component/
---

{{% alert color="primary" %}}

[Rapport PDF](https://blog.aspose.com/2008/03/17/complete-excel-export-capabilities-using-apis/)

**Användning av Aspose.Cells i Rapport Canvas Component**

Robert Chilvers, 17 mars 2008

{{% /alert %}}

## **Produktbakgrund**

Rapport Canvas Component låter användaren skapa visuella rapporter baserade på en förinställd dataset. Användaren kan lägga till olika komponenter på sin canvas, inklusive bilder, text rutor, diagram och tabeller, de specificerar sedan datan och hur den ska aggregeras. Användaren kan sedan omarrangera och ändra storlek på objekten för att passa deras sida. Användaren kan specificera färgpaletter och spara av mallar för framtida användning. Aspose.Cells används för att exportera alla objekt på canvasen till Excel med rätt data. Komponenten är skriven med VB.Net i Visual Studio 2008.

## **Kravscenario**

Vi valde Aspose.Cells på grund av dess näst intill kompletta Microsoft Excel exportmöjligheter. Det viktigaste för oss är förmågan att exportera diagram och tabeller särskilt i Microsoft Excel 2007 – dessa saknades i andra tredjepartskomponenter.

## **Lösningsimplementering**

Varje objekt på rapportens canvas har en funktion som överförs en instans av Aspose.Cells arbetsblad och lägger till sig själv på arbetsbladet. När användaren begär en export initieras arbetsboken och arbetsbladen och varje objekt på rapportens canvas har denna funktion anropad.

## **Fördelar**

Aspose.Cells tillät oss att bygga upp Excel arbetsboken helt oberoende av Excel och sedan spara arbetsboken i det format som valts av användaren. Detta sparade timmar av felsökning av interaktionen vid användning av Excel interop och implementera olika rutiner för att spara till varierande versioner av Excel.

## **Framtida implementering**

Vi tänker troligtvis använda Aspose.Cells för all inläsning och sparning av Excel-filer. Detta kommer att inkludera inläsning av datamallar och export av resultat.

## **Slutsats**

{{% alert color="primary" %}}

Hittills har vi inte haft några problem med att använda Aspose.Cells-komponenterna och komponenten borde spara oss utvecklingstid både på kort och lång sikt. Support- och försäljningsförfrågningar har besvarats snabbt och hjälpsamt.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
