---
title: Hur man skapar en Gantt diagram
linktitle: Hur man skapar en Gantt diagram
type: docs
weight: 72
url: /sv/net/how-to-create-gantt-chart/
description: Lär dig hur du skapar ett Gantt diagram med Aspose.Cells for .NET API.
keywords: C# skapa ett Gantt diagram, lägg till ett Gantt diagram, infoga ett Gantt diagram
---

## **Vad är Gantt-diagram**

Ett Gantt-diagram är en typ av stapeldiagram som illustrerar ett projektschema. Det visar start- och slutdatum för olika delar av ett projekt. Varje uppgift eller aktivitet representeras av en stapel, där längden motsvarar dess varaktighet. Gantt-diagram indikerar också beroenden mellan uppgifter, vilket gör det möjligt för projektledare att visualisera sekvensen i vilken uppgifter måste slutföras. De används mycket inom projektledning för att planera, schemalägga och spåra projekt effektivt.

## **Hur man skapar ett Gantt-diagram i Excel**

Du kan skapa ett Gantt-diagram i Excel genom att följa dessa steg:
1. Lägg till lite data för Gantt-diagram. 
<br>
<img src="00.png" width=50% />
1. Välj datan och gå till Infoga --> Diagram --> Infoga stapel- eller stapeldiagram --> Staplad stapeldiagram. I vårt exempel är det B1:B7, och sedan Infoga **Staplad stapeldiagram**.
<br>
<img src="1.png" width=50% />

1. Välj diagrammet, **Välj data**->**Lägg till**, ange **Serie namn** och **Serie värden** enligt följande.
<br>
<img src="2.png" width=50% />

1. Välj diagrammet, redigera **Horisontell(Kategories) Axel Etiketter**.
<br>
<img src="3.png" width=50% />

1. **Formatera axel** Y-axeln, välj **Kategorier i omvänd ordning**.
1. Välj **Blå Serie** och ange **Fyllnad->Ingen fyllnad**.
1. **Formatera axel** X-axeln, ange **Minimum och Maxinum**(1/5/2019:43470,1/30/2019:43494).
<br>
<img src="4.png" width=50% />

1. **Lägg till datamarkörer** för diagrammet, nu får du en gantt-diagram.
<br>
<img src="0.png" width=50% />


## **Så här lägger du till ett Gantt-diagram i Aspose.Cells**
Se följande exempelkod. Den laddar den [exempel Excel-filen](sample.xlsx) som innehåller lite exempeldata. Den skapar sedan stapeldiagram baserat på den inledande datan och ställer in relevanta egenskaper. Slutligen sparar den arbetsboken till [utdata XLSX-formatet](result.xlsx). På följande skärmdump visas Gantt-diagrammet skapat av Aspose.Cells i utdata Excel-filen.
<br>
<img src="5.png" width=60% />

### **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-gantt-chart.cs" >}}

