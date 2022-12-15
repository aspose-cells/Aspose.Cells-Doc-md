---
title: Ta bort Pivot Connection
type: docs
weight: 30
url: /sv/java/remove-pivot-connection/
description: Lär dig hur du tar bort pivotkoppling med Aspose.Cells Java bibliotek.
keywords: Remove pivot connection without office 2013, office 2016, office 2019 and office 365.
---
## **Möjliga användningsscenarier**

Om du vill ta bort slicer- och pivottabellen i Excel måste du högerklicka på slicer och välja "Rapportera anslutningar...". I alternativlistan kan du använda kryssrutan. På samma sätt, om du vill ta bort slicer- och pivottabellen med Aspose.Cells API programmatiskt, använd[**Slicer.removePivotConnection(pivottabell)**](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#removePivotConnection(com.aspose.cells.PivotTable)) metod. Det kommer att ta isär slicer och pivottabell.

## **Ta bort Slicer**

Följande exempelkod laddar[exempel på Excel-fil](remove-pivot-connection.xlsx)som innehåller en befintlig skivare. Den får åtkomst till skivorna och kopplar sedan bort skivan och pivottabellen. Slutligen sparar den arbetsboken som[utdata Excel-fil](remove-pivot-connection-out.xlsx). 


## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-Removing-Pivot-Connection.java" >}}