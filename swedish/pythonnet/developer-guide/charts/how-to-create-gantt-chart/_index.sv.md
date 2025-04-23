---
title: Hur man skapar ett Gantt diagram
linktitle: Hur man skapar ett Gantt diagram
type: docs
weight: 72
url: /sv/python-net/how-to-create-gantt-chart/
description: Lär dig hur du skapar ett Gantt diagram med Aspose.Cells för Python via .NET API.
keywords: Python skapar ett Gantt diagram, lägger till ett Gantt diagram, infogar ett Gantt diagram
---

## **Vad är Gantt-diagram**

Ett Gantt-diagram är en sorts stapeldiagram som illustrerar ett projektschema. Det visar start- och sluttider för olika delar av ett projekt. Varje uppgift eller aktivitet representeras av en stapel, vars längd motsvarar dess varaktighet. Gantt-diagram visar också beroenden mellan uppgifter, vilket gör det möjligt för projektledare att visualisera i vilken ordning uppgifter ska utföras. Det används ofta inom projektledning för att planera, schemalägga och följa upp projekt effektivt.

## **Hur man skapar ett Gantt-diagram i Excel**

Du kan skapa ett Gantt-diagram i Excel genom att följa dessa steg:
1. Lägg till några data för Gantt-diagrammet. 
<br>
<img src="00.png" width=50% />
1. Markera datan och gå till Infoga --> Diagram --> Infoga kolumn- eller stapeldiagram --> Staplat stapeldiagram. I vårt exempel är det B1:B7, och därefter Infoga **Staplat stapeldiagram**.
<br>
<img src="1.png" width=50% />

1. Välj diagrammet, **Välj data**->**Lägg till**, ställ in **Serienamn** och **Serievärden** som följer.
<br>
<img src="2.png" width=50% />

1. Välj diagrammet, redigera **Horisontell (Kategor) -axelrubriker**.
<br>
<img src="3.png" width=50% />

1. **Formatera axeln** på Y-axeln, välj **Kategorier i omvänd ordning**.
1. Välj **Blå serie** och ställ in **Fyllning->Ingen fyllning**.
1. **Formatera axeln** på X-axeln, ställ in **Minsta** och **Max** (1/5/2019:43470, 1/30/2019:43494).
<br>
<img src="4.png" width=50% />

1. **Lägg till datapunkter** för diagrammet, nu får du ett Gantt-diagram.
<br>
<img src="0.png" width=50% />


## **Hur man lägger till ett Gantt-diagram i Aspose.Cells för Python Excel-bibliotek**
Se följande exempel. Den laddar in [exempel Excel-fil](sample.xlsx) som innehåller vissa exempeldata. Den skapar sedan det staplade stapeldiagrammet baserat på data och ställer in relevanta egenskaper. Slutligen sparar den arbetsboken till [utdata XLSX-format](result.xlsx). Följande skärmbild visar Gantt-diagrammet som skapats av Aspose.Cells för Python via .NET i den utdata Excel-fil.
<br>
<img src="5.png" width=60% />

### **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-create-gantt-chart.py" >}}

