---
title: Hur man skapar ett tornadodiagram
type: docs
weight: 73
url: /sv/net/create-tornado-chart/
description: Lär dig hur du skapar ett tornadodiagram med Aspose.Cells for .NET API.
keywords: C# create a tornado chart, add a tornado chart, insert a tornado chart
---
##  **Introduktion**
Ett tornadodiagram, även känt som ett tornadodiagram eller tornadograf, är en typ av datavisualisering som ofta används för känslighetsanalys i Excel. Det hjälper dig att förstå effekten av att ändra variabler på ett visst resultat eller resultat.

##  **Hur man skapar ett tornadodiagram i Excel**
Du kan skapa ett tornadodiagram i Excel genom att följa dessa steg:
1. Välj data och gå till Infoga --> Diagram --> Infoga kolumn eller stapeldiagram --> Staplat stapeldiagram. Klicka på det.
<br>
<img src="1.png" width=70% />
2. Ändra Y-axeln: Högerklicka på y-axeln. Klicka på formataxeln. I etiketter klickar du på rullgardinsmenyn för etikettposition och väljer Låg objekt.
<br>
<img src="2.png" width=70% />
3. Välj valfri stapel och gå till formatering. Ställ in en lämplig spaltbredd.
<br>
<img src="3.png" width=70% />
4. Låt oss ta bort minustecknet (-) från tornadodiagrammet. Välj x-axeln. Gå till formatering. Klicka på numret i axelalternativen. I kategori, välj anpassad. Skriv ###0,###0 i formatkoden. Klicka på lägg till.
<br>
<img src="4.png" width=70% />
5. klicka på y-axeln och gå till axelalternativen. I Axis-alternativen, markera Kategorier i omvänd ordning.
<br>
<img src="5.png" width=70% />

##  **Hur man lägger till ett tornadodiagram i Aspose.Cells**
 Se följande exempelkod. Den laddar[exempel på Excel-fil](sample.xlsx) som innehåller några exempeldata. Den skapar sedan det staplade stapeldiagrammet baserat på de ursprungliga data och ställer in relevanta egenskaper. Slutligen sparar den arbetsboken till[utgång XLSX format](out.xlsx). Följande skärmdump visar tornadodiagrammet skapat av Aspose.Cells i utdata Excel-filen.
<br>
<img src="6.png" width=70% />

###  **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-tornado-chart.cs" >}}