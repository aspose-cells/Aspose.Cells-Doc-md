---
title: Använda Sparklines och inställningar 3D-format
type: docs
weight: 40
url: /sv/net/using-sparklines-and-settings-3d-format/
---
## **Använder Sparklines**
Microsoft Excel 2010 kan analysera information på fler sätt än någonsin tidigare. Det låter användare spåra och lyfta fram viktiga datatrender med nya verktyg för dataanalys och visualisering. Sparklines är minidiagram som du kan placera inuti celler så att du kan se data och diagram på samma tabell. När sparklines används på rätt sätt går dataanalysen snabbare och mer rakt på sak. De ger också en enkel bild av information, och undviker överfulla kalkylblad med många upptagna diagram.

Aspose.Cells tillhandahåller ett API för att manipulera sparklines i kalkylblad.
### **Sparklines i Microsoft Excel**
Så här infogar du sparklines i Microsoft Excel 2010:

1. Markera cellerna där du vill att gnistlinjerna ska visas. För att göra dem enkla att se, markera celler vid sidan av data.
1.  Klick**Föra in** på bandet och välj sedan**kolumn** i**Sparklines** grupp.
1. Välj eller ange cellintervallet i kalkylbladet som innehåller källdata. Diagrammen kommer att visas.

Sparklines hjälper dig att se trender, till exempel vinst- eller förlustrekord för en softballliga. Sparklines kan till och med summera hela säsongen för varje lag i ligan.
### **Sparklines med Aspose.Cells**
 Utvecklare kan skapa, ta bort eller läsa sparklines (i mallfilen) med API:et som tillhandahålls av Aspose.Cells. Klasserna som hanterar sparklines finns i[Aspose.Cells.Charts](https://reference.aspose.com/cells/net/aspose.cells.charts)namnutrymme så du måste importera detta namnutrymme innan du använder dessa funktioner.

Genom att lägga till anpassad grafik för ett givet dataintervall har utvecklarna friheten att lägga till olika typer av små diagram till utvalda cellområden.

Exemplet nedan visar Sparklines-funktionen. Exemplet visar hur man:

1. Öppna en enkel mallfil.
1. Läs sparklines-information för ett kalkylblad.
1. Lägg till nya sparklines för ett givet dataintervall till ett cellområde.
1. Spara Excel-filen på disk.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-UsingSparklines-1.cs" >}}
## **Ställa in 3D-format**
Du kanske behöver 3D-diagramstilar så att du kan få precis resultaten för ditt scenario. Aspose.Cells tillhandahåller relevant API för att tillämpa Microsoft Excel 2007 3D-formatering.

Ett komplett exempel ges nedan för att visa hur man skapar ett diagram och använder Microsoft Excel 2007 3D-formatering. Efter exekvering av exempelkoden kommer ett kolumndiagram (med 3D-effekter) att läggas till i kalkylbladet.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-Applying3DFormat-1.cs" >}}
