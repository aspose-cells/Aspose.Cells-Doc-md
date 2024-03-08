---
title: Hur man lägger till ett pivotdiagram med Aspose.Cells
linktitle: Pivotdiagram
type: docs
weight: 100
url: /sv/java/how-to-add-pivot-chart/
description: Hur man lägger till ett pivotdiagram med Aspose.Cells.
keywords: PivotChart
---
##  Vad är PivotChart

Ett pivotdiagram i Excel är en grafisk representation av data som skapats från en pivottabell. Det tillåter användare att visualisera och analysera data dynamiskt genom att sammanfatta och visa information i diagramform. Pivotdiagram är interaktiva och kan enkelt modifieras för att visa olika perspektiv på data, vilket gör det till ett kraftfullt verktyg för dataanalys och presentation i Excel.

##  Hur man lägger till ett pivotdiagram med Aspose.Cells
###  **Skapa en pivottabell**

Så här skapar du en pivottabell med Aspose.Cells:

1. Lägg till några data i ett kalkylbladsceller med hjälp av ett Cell-objekts PutValue/setValue-metod. Du använder också en mallfil som redan är fylld med data. Data kommer att användas som pivottabellens datakälla.
1. Lägg till en pivottabell till kalkylbladet genom att anropa PivotTables-samlingens add-metod (inkapslad i Worksheet-objektet).
1. Få tillgång till det nya PivotTable-objektet från PivotTables-samlingen genom att skicka dess index.
1. Använd något av pivottabellobjekten som är inkapslade i PivotTable-objektet för att hantera tabellen.

Ett kodexempel ges nedan. När koden körs genereras en ny fil: pivotTable_test.xls.

**Indata** 

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_1.png)

**Utgångspivottabellen**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}

###  **Skapa ett pivotdiagram baserat på pivottabellen**

Så här skapar du ett pivotdiagram med Aspose.Cells:

1. Lägg till ett diagram.
1. Ställ in pivotkällan för diagrammet så att den refererar till en befintlig pivottabell i kalkylarket.
1. Ställ in andra attribut.

Nedan visas koden som används av komponenten för att utföra uppgiften. När koden körs genereras en ny fil: pivotChart_test.xls.

**Pivotdiagrambladet**

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}

{{% alert color="primary" %}}

Den här artikeln visar hur du skapar pivottabeller och pivotdiagram med Aspose.Cells. Förhoppningsvis kommer det att hjälpa dig att använda dessa funktioner i dina egna scenarier.

Aspose.Cells har dragit nytta av år av forskning, design och noggrann justering.

 Vi välkomnar dina frågor, kommentarer och förslag på[Aspose.Cells Forum](https://forum.aspose.com/c/cells/9). Vi garanterar ett snabbt svar.

{{% /alert %}}
