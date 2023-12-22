---
title: Hur man skapar Gantt-diagram
linktitle: Hur man skapar Gantt-diagram
type: docs
weight: 72
url: /sv/net/how-to-create-gantt-chart/
description: Hur man skapar Gantt-diagram i Aspose.Cells.
keywords: create/insert Gantt Chart Excel Aspose
---
##  Vad är Gantt-diagram

Ett Gantt-diagram hjälper dig att schemalägga dina projektuppgifter och hjälper dig sedan att spåra dina framsteg.

##  Lägg till Gantt-diagram i Excel

Behöver du visa status för ett enkelt projektschema med ett Gantt-diagram? Även om Excel inte har en fördefinierad Gantt-diagramtyp, kan du simulera en genom att anpassa ett staplat stapeldiagram för att visa start- och slutdatum för uppgifter, så här:

![todo:image_alt_text](00.png)

![todo:image_alt_text](0.png)

##  Hur man skapar

-  Välj de data du vill kartlägga. I vårt exempel är det B1:B7, och sedan Insert**Staplad bar** Diagram.

![todo:image_alt_text](1.png)

- Välj diagrammet,**Välj data**->**Lägg till**, ställ in **Serienamnet** och**Serievärden** enligt följande

![todo:image_alt_text](2.png)

-  Välj diagrammet, Redigera**Horisontella (kategori) axeletiketter**

![todo:image_alt_text](3.png)

- **Formatera axel** Y-axeln, välj**Kategorier i omvänd ordning**
-  Välj**Blå serie** och ställ in**Fyll->NEJ Fyll**
- **Formatera axel** X-axeln, ställ in *Mininum och Maxinum**(1/5/2019:43470,1/30/2019:43494)

![todo:image_alt_text](4.png)

- **Lägg till datafiler** för diagrammet
Nu får du ett gantt-diagram.

## Lägg till Gantt-diagram i Aspose.Cells

 Följande exempelkod skapar ett Gantt-diagram genom att öppna a[exempelfil](sample.xlsx)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "create-gantt-chart.cs" >}}

 Du kommer att få en fil som liknar[resultatfil](result.xlsx).I filen ser du följande:

![todo:image_alt_text](5.png)

