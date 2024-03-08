---
title: Hur man lägger till ett pivotdiagram med Aspose.Cells
linktitle: Pivotdiagram
type: docs
weight: 100
url: /sv/net/how-to-add-pivot-chart/
description: Hur man lägger till ett pivotdiagram med Aspose.Cells.
keywords: PivotChart
---
##  Vad är PivotChart

Ett pivotdiagram i Excel är en grafisk representation av data som skapats från en pivottabell. Det tillåter användare att visualisera och analysera data dynamiskt genom att sammanfatta och visa information i diagramform. Pivotdiagram är interaktiva och kan enkelt modifieras för att visa olika perspektiv på data, vilket gör det till ett kraftfullt verktyg för dataanalys och presentation i Excel.

##  Hur man lägger till ett pivotdiagram med Aspose.Cells

###  **Lägga till en pivottabell**

Så här skapar du en pivottabell med Aspose.Cells:

1. Lägg till några data i ett kalkylbladsceller med hjälp av ett Cell-objekts PutValue/setValue-metod. Du använder också en mallfil som redan är fylld med data. Data kommer att användas som pivottabellens datakälla.
1. Lägg till en pivottabell till kalkylbladet genom att anropa PivotTables-samlingens add-metod (inkapslad i Worksheet-objektet).
1. Få tillgång till det nya PivotTable-objektet från PivotTables-samlingen genom att skicka dess index. # Använd något av pivottabellobjekten som är inkapslade i PivotTable-objektet för att hantera tabellen.

Kodexempel ges nedan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

###  **Lägga till ett pivotdiagram**

Så här skapar du ett pivotdiagram med Aspose.Cells:

1. Lägg till ett diagram.
1. Ställ in pivotkällan för diagrammet så att den refererar till en befintlig pivottabell i kalkylarket.
1. Ställ in andra attribut.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

