---
title: Använda sparklines och inställningar 3D format
type: docs
weight: 40
url: /sv/python-net/using-sparklines-and-settings-3d-format/
---

## **Användning av sparklines**
Microsoft Excel 2010 kan analysera information på fler sätt än någonsin tidigare. Det låter användarna spåra och markera viktiga datatrender med nya verktyg för dataanalys och visualisering. Sparklines är minidiagram som du kan placera i celler så att du kan se data och diagram på samma tabell. När sparklines används på rätt sätt blir dataanalys snabbare och mer fokuserad. De ger också en enkel vy av information och undviker överfyllda arbetsblad med många upptagna diagram.

Aspose.Cells för Python via .NET ger ett API för att manipulera sparklines i kalkylblad.
### **Sparklines i Microsoft Excel**
För att infoga sparklines i Microsoft Excel 2010:

1. Välj cellerna där du vill att sparklines ska visas. För att göra dem enkla att visa, välj celler bredvid datan.
1. Klicka på **Infoga** på menyn och välj sedan **kolumn** i **Sparklines** gruppen.
1. Välj eller ange cellområdet på arbetsbladet som innehåller källdata. Graferna kommer att visas.

Sparklines hjälper dig att se trender, till exempel vinst- eller förlustrekord för en softbolliga. Sparklines kan till och med summera hela säsongen för varje lag i ligan.
### **Sparklines med Aspose.Cells för Python via .NET**
Utvecklare kan skapa, ta bort eller läsa sparklines (i mallfilen) med API:et som Aspose.Cells för Python via .NET tillhandahåller. Klasserna som hanterar sparklines finns i [aspose.cells.charts](https://reference.aspose.com/cells/python-net/aspose.cells.charts)-namnrymden, så du måste importera denna innan du använder dessa funktioner.

Genom att lägga till anpassad grafik för ett givet dataområde har utvecklare friheten att lägga till olika typer av små diagram i utvalda cellområden.

Exemplet nedan demonstrerar funktionen Sparklines. Exemplet visar hur man:

1. Öppna en enkel mallfil.
1. Läs sparklinesinformation för ett arbetsblad.
1. Lägg till nya gnistrande linjer för ett givet datintervall till ett cellområde.
1. Spara Excel-filen på disk.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Sparklines-UsingSparklines-1.py" >}}
## **Inställning 3D-format**
Du kan behöva 3D-diagramstilar för att få just de resultat du vill ha i din scenariot. Aspose.Cells för Python via .NET erbjuder den relevanta API:et för att tillämpa Microsoft Excel 2007 3D-formatering.

Ett komplett exempel ges nedan för att visa hur man skapar ett diagram och tillämpar Microsoft Excel 2007 3D-formatering. Efter att ha exekverat exempelkoden kommer ett stapeldiagram (med 3D-effekter) att läggas till på arbetsbladet.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Sparklines-Applying3DFormat-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
