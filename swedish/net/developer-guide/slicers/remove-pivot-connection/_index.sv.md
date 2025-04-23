---
title: Ta bort pivotkoppling
type: docs
weight: 30
url: /sv/net/remove-pivot-connection/
description: Lär dig hur du tar bort pivot anslutning med Aspose.Cells biblioteket.
keywords: Ta bort pivotkoppling utan Office 2013, Office 2016, Office 2019 och Office 365.
---

## **Möjliga användningsscenario**

Om du vill avassociera en slicer och en pivottabell i Excel, måste du högerklicka på slicern och välja "Rapportkopplingar...". I alternativlistan kan du använda kryssrutan. På liknande sätt om du vill avassociera en slicer och pivottabell med Aspose.Cells API programmatiskt, använd [**Slicer.RemovePivotConnection(PivotTable pivot)**](https://reference.aspose.com/cells/net/aspose.cells.slicers/slicer/removepivotconnection/)-metoden. Den kommer att avassosciera slicern och pivottabellen.

## **Bryt isär snitt och pivottabell**

Följande provkod laddar in [provmappen](remove-pivot-connection.xlsx) som innehåller en befintlig slicer. Den går igenom slicerna och sedan avassocierar den slicern och pivottabellen. Slutligen sparar den arbetsboken som [output Excel-fil](remove-pivot-connection-out.xlsx). 


## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Slicers-Removing-Pivot-Connection.cs" >}}
{{< app/cells/assistant language="csharp" >}}
