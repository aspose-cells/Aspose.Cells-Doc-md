---
title: Lägg till pivottabellanslutning
type: docs
weight: 30
url: /sv/java/add-pivot-connection/
description: Lär dig hur man lägger till pivottabellanslutning med Aspose.Cells Java bibliotek.
keywords: Lägg till pivottabellanslutning utan Office 2013, Office 2016, Office 2019 och Office 365.
---

## **Möjliga användningsscenario**

Om du vill associera slicer och pivottabell i Excel måste du högerklicka på slicern och välja "Rapportanslutningar..."-objektet. I alternativlistan kan du klicka i kryssrutan. På liknande sätt, om du vill associera slicer och pivottabell med Aspose.Cells Java API programmatiskt, använd [**Slicer.addPivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#addPivotConnection-com.aspose.cells.PivotTable-) -metoden. Den kommer att associera slicer och pivottabell.

## **Associera slicer och Pivottabell**

Följande exempelkod laddar in den [exempel-Excel-filen](add-pivot-connection.xlsx) som innehåller en befintlig slicer. Den får åtkomst till slicern och associerar sedan slicer och pivottabell. Slutligen sparar den arbetsboken som [utdata-Excel-fil](add-pivot-connection-out.xlsx). 


## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-Adding-Pivot-Connection.java" >}}
{{< app/cells/assistant language="java" >}}
