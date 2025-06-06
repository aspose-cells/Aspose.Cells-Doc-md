---
title: Hur man lägger till ett PivotDiagram med Aspose.Cells för Python via .NET
linktitle: Pivotdiagram
type: docs
weight: 100
url: /sv/python-net/how-to-add-pivot-chart/
description: Hur man lägger till ett PivotDiagram med Aspose.Cells för Python via .NET.
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

## Hur man lägger till ett PivotDiagram med Aspose.Cells för Python Excel bibliotek

### **Lägga till en pivottabell**

För att skapa en pivottabell med Aspose.Cells för Python via .NET:

1. Lägg till lite data till arbetsbladsceller med hjälp av en Cell-objekts PutValue/setValue-metod. Du kan också använda en mallfil som redan är ifylld med data. Data kommer att användas som pivot tabellens datakälla.
1. Lägg till en pivot tabell till arbetsbladet genom att anropa PivotTables -samlingens add-metod (inkapslad i Worksheet-objektet).
1. Hämta det nya PivotTable-objektet från PivotTables-samlingen genom att ange dess index. # Använd något av de pivottabellobjekt som är inkapslade i PivotTable-objektet för att hantera tabellen.

Kodexempel ges nedan.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreatePivotTable-1.py" >}}

### **Lägga till en PivotChart**

För att skapa ett pivotdiagram med Aspose.Cells för Python via .NET:

1. Lägg till en graf.
1. Ange grafens PivotSource så att den hänvisar till en befintlig pivot tabell i kalkylarket.
1. Ange andra attribut.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreatePivotChart-1.py" >}}

