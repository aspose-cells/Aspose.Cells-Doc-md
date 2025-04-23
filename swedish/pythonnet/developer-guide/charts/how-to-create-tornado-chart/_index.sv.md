---
title: Hur man skapar ett tornado diagram
type: docs
weight: 73
url: /sv/python-net/create-tornado-chart/
description: Lär dig hur man skapar ett tornadodiagram med Aspose.Cells för Python via .NET API.
keywords: Python skapa ett tornadodiagram, lägg till ett tornadodiagram, infoga ett tornadodiagram
---

## **Introduktion**
Ett tornado diagram, även känt som en tornado graf eller tornado diagram, är en typ av datavisualisering som ofta används för känslighetsanalys i Excel. Det hjälper dig att förstå effekten av förändrande variabler på ett visst resultat eller en viss effekt.

## **Hur man skapar ett tornado diagram i Excel**
Du kan skapa ett tornado diagram i Excel genom att följa dessa steg:
1. Välj datan och gå till Infoga --> Diagram --> Infoga kolumn- eller stapeldiagram --> Staplad stolpdiagram. Klicka på det.
<br>
<img src="1.png" width=70% />
2. Ändra Y-axeln: Högerklicka på y-axeln. Klicka på formatera axeln. I etiketter, klicka på etikettposition nedrullningsalternativ och välj Låg element.
<br>
<img src="2.png" width=70% />
3. Välj vilken som helst stapel och gå till formatering. Ange en lämplig luckbredd.
<br>
<img src="3.png" width=70% />
4. Låt oss ta bort minustecknet (-) från tornado diagrammet. Välj x-axeln. Gå till formatering. I axelalternativ, klicka på nummer. I kategori, välj anpassad. I formatkoden skriv ###0,###0. Klicka på lägg till.
<br>
<img src="4.png" width=70% />
5. Klicka på y-axeln och gå till axelalternativen. I axelalternativen, kryssa i kategorier i omvänd ordning.
<br>
<img src="5.png" width=70% />

## **Hur man lägger till ett tornadodiagram i Aspose.Cells för Python Excel-biblioteket**
Se följande exempel. Den laddar den [exempel-Excelfil](sample.xlsx) som innehåller några exempeldata. Den skapar sedan ett stapeldiagram baserat på initialdata och ställer in relevanta egenskaper. Slutligen sparar den arbetsboken i [utdata XLSX-format](out.xlsx). Följande skärmklipp visar tornadodiagrammet som skapas av Aspose.Cells för Python via .NET i utdatafilen.
<br>
<img src="6.png" width=70% />

### **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-create-tornado-chart.py" >}}
