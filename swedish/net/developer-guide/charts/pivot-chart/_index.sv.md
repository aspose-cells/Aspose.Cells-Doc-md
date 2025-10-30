---
title: Hur man lägger till ett PivotChart med hjälp av Aspose.Cells
linktitle: Pivotdiagram
type: docs
weight: 100
url: /sv/net/how-to-add-pivot-chart/
description: Hur man lägger till ett PivotChart med hjälp av Aspose.Cells.
keywords: PivotChart
---
## Vad är PivotChart

Ett pivotdiagram är en visuell representation av datan i en pivottabell. Pivotdiagram ger ett sätt att sammanfatta, analysera, utforska och presentera summerad data. Här är några nyckelfunktioner och aspekter av pivotdiagram:

1. Datan ändras dynamiskt: Pivotdiagram uppdateras automatiskt för att återspegla ändringar i pivottabellen. Om du lägger till eller tar bort fält i pivottabellen, uppdateras pivotdiagrammet därefter.

1. Interaktiv: Pivotdiagram är interaktiva, vilket gör att användare kan filtrera, sortera och gräva ner i data. Detta gör det enkelt att utforska olika aspekter av datamängden.

1. Flexibelt Layout: Användare kan ändra layouten på pivotdiagrammet genom att dra och släppa fält, vilket ger flexibilitet i hur data visualiseras.

1. Olika Diagramtyper: Pivotdiagram kan skapas med olika diagramtyper som stapeldiagram, linjediagram, pie-diagram och mer, beroende på datans natur och insikterna du vill få.

1. Sammanfattning: Pivotdiagram sammanfattar stora mängder data och kan visa totalsummor, genomsnitt, antal eller andra sammanfattande statistik.

1. Filtrering: De erbjuder filtreringsmöjligheter, vilket gör att du kan visa endast de data som uppfyller vissa kriterier.

<br>
Pivotdiagram används ofta inom affärsintelligens och dataanalys för att ge en tydlig och koncis visuell sammanfattning av komplexa datamängder. De är ett kraftfullt verktyg för datadrivna beslut.

## Hur man lägger till en PivotChart med hjälp av Aspose.Cells

För att skapa en PivotChart med Aspose.Cells:

1. Ladda en [mallfil](pivotchart_data.xlsx) som redan är ifylld med data. Data kommer att användas som datakälla till pivottabellen.
1. Lägg till en pivot tabell till arbetsbladet genom att anropa PivotTables -samlingens add-metod (inkapslad i Worksheet-objektet).
1. Få åtkomst till det nya PivotTable-objektet från PivotTables-samlingen genom att skicka dess index. 
1. Använd något av pivot tabellens objekt som är inkapslade i PivotTable-objektet för att hantera tabellen.
1. Lägg till en graf.
1. Ange grafens PivotSource så att den hänvisar till en befintlig pivot tabell i kalkylarket.
1. Ange andra attribut.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
