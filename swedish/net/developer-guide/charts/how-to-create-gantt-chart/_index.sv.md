---
title: Hur skapar man Gantt diagram
linktitle: Hur skapar man Gantt diagram
type: docs
weight: 72
url: /sv/net/how-to-create-gantt-chart/
description: Hur man skapar Gantt diagram i Aspose.Cells.
keywords: skapa/infoga Gantt diagram Excel Aspose
---
## Vad är Gantt-diagram

Ett Gantt-diagram hjälper dig att schemalägga dina projektuppgifter och sedan hjälper dig att följa din framsteg.

## Lägg till Gantt-diagram i Excel

Behöver du visa status för en enkel projektschema med ett Gantt-diagram? Även om Excel inte har en fördefinierad Gantt-diagramtyp kan du simulera en genom att anpassa ett stapeldiagram för att visa start- och slutförancedatum för uppgifter, som så här:

![todo:image_alt_text](00.png)

![todo:image_alt_text](0.png)

## Hur man skapar

- Välj data du vill rita. I vårt exempel är det B1:B7, och sedan infoga **Stapeldiagram**.

![todo:image_alt_text](1.png)

- Välj diagrammet, **Välj data**->**Lägg till**, ange **Serienamn** och **Serievärden** enligt följande

![todo:image_alt_text](2.png)

- Välj diagrammet, Redigera **Horisontella (Kategorier) axel etiketter**

![todo:image_alt_text](3.png)

- **Formatera axeln** Y-axel, välj **Kategorier i omvänd ordning**
- Välj **Blå Serie** och ange **Fyllning->Ingen fyllning**
- **Formatera axeln** X-axeln, ställ in **Mininum och Maxinum**(1/5/2019:43470,1/30/2019:43494)

![todo:image_alt_text](4.png)

- **Lägg till Dataetiketter** för diagrammet
Nu har du fått ett gantt-diagram.

## Lägg till Gantt-diagram i Aspose.Cells

Följande exemplarkod skapar ett Gantt-diagram genom att öppna en [exempelfil](sample.xlsx)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-gantt-chart.cs" >}}

Du får en fil liknande [resultatfil](result.xlsx). I filen ser du följande:

![todo:image_alt_text](5.png)

