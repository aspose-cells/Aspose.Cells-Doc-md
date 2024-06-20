---
title: Ta bort pivotkoppling
type: docs
weight: 30
url: /sv/java/remove-pivot-connection/
description: Lär dig hur du tar bort pivotkoppling med Aspose.Cells Java biblioteket.
keywords: Ta bort pivotkoppling utan Office 2013, Office 2016, Office 2019 och Office 365.
---

## **Möjliga användningsscenario**

Om du vill avassociera en slicer och en pivottabell i Excel, måste du högerklicka på slicern och välja "Rapportkopplingar...". I alternativlistan kan du använda kryssrutan. På liknande sätt om du vill avassociera en slicer och pivottabell med Aspose.Cells API programmatiskt, använd [**Slicer.removePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#removePivotConnection(com.aspose.cells.PivotTable))-metoden. Den kommer att avassosciera slicern och pivottabellen.

## **Ta bort slicer**

Följande provkod laddar in [provmappen](remove-pivot-connection.xlsx) som innehåller en befintlig slicer. Den går igenom slicerna och sedan avassocierar den slicern och pivottabellen. Slutligen sparar den arbetsboken som [output Excel-fil](remove-pivot-connection-out.xlsx). 


## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-Removing-Pivot-Connection.java" >}}
