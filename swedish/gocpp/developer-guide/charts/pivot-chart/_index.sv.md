---
title: Hur man lägger till en PivotDiagram med Golang via C++
linktitle: Pivotdiagram
type: docs
weight: 100
url: /sv/go-cpp/how-to-add-pivot-chart/
description: Hur man lägger till en PivotDiagram med Aspose.Cells med Golang via C++.
keywords: PivotChart
---

## Vad är PivotChart

Ett pivotdiagram är en visuell representation av datan i en pivottabell. Pivotdiagram ger ett sätt att sammanfatta, analysera, utforska och presentera summerad data. Här är några nyckelfunktioner och aspekter av pivotdiagram:

1. **Dynamisk datarapportering**: Pivotdiagram uppdateras automatiskt för att återspegla förändringar i pivottabellen. Om du lägger till eller tar bort fält i pivottabellen, uppdateras pivotdiagrammet därefter.

1. **Interaktiv**: Pivotdiagram är interaktiva, vilket tillåter användare att filtrera, sortera och fördjupa sig i data. Detta gör det enkelt att utforska olika aspekter av datamängden.

1. **Flexibelt layout**: Användare kan ändra layouten på pivotdiagrammet genom att dra och släppa fält, vilket ger flexibilitet i hur data visualiseras.

1. **Olika diagramtyper**: Pivotdiagram kan skapas med olika diagramtyper som stapeldiagram, linjediagram, cirkeldiagram och fler, beroende på datans natur och insseiten du vill få.

1. **Sammanfattning**: Pivotdiagram sammanfattar stora datamängder och kan visa totalsummor, medelvärden, antal eller andra sammanfattande statistik.

1. **Filtrering**: De erbjuder filtreringsmöjligheter, vilket gör att du kan visa endast den data som uppfyller vissa kriterier.

<br>
Pivotdiagram används ofta inom affärsintelligens och dataanalys för att ge en tydlig och koncis visuell sammanfattning av komplexa datamängder. De är ett kraftfullt verktyg för datadrivna beslut.

## Hur man lägger till en PivotChart med hjälp av Aspose.Cells

### **Lägga till en pivottabell**

För att skapa en pivot tabell med Aspose.Cells:

1. Lägg till data i ett kalkylblad med hjälp av `Cell`-objektets `PutValue` eller `SetValue` metod. Du kan också använda en mallfil som redan är ifylld med data. Data kommer att användas som datakälla för pivot-tabellen.
1. Lägg till en pivot-tabell i kalkylbladet genom att anropa `PivotTables`-samlingen `Add`-metod (inkapslad i `Worksheet`-objektet).
1. Få tillgång till det nya `PivotTable`-objektet från `PivotTables`-samlingen genom att ange dess index. Använd något av pivot-tabellobjekten som kapslas in i `PivotTable`-objektet för att hantera tabellen.

Kodexempel ges nedan.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PivotChart.go" >}}
### **Lägga till en PivotChart**

För att skapa en PivotChart med Aspose.Cells:

1. Lägg till en graf.
1. Ställ in `PivotSource` för diagrammet att hänvisa till en befintlig pivot-tabell i kalkylbladet.
1. Ange andra attribut.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PivotChart-1.go" >}}
