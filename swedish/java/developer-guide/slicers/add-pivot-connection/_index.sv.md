---
title: Lägg till Pivot Connection
type: docs
weight: 30
url: /sv/java/add-pivot-connection/
description: Lär dig hur du lägger till pivotkoppling med Aspose.Cells Java bibliotek.
keywords: Add pivot connection without office 2013, office 2016, office 2019 and office 365.
---
## **Möjliga användningsscenarier**

 Om du vill associera slicer och pivottabell i Excel måste du högerklicka på slicer och välja "Rapportera anslutningar...". I alternativlistan kan du använda kryssrutan. På samma sätt, om du vill koppla slicer och pivottabell med Aspose.Cells Java API programmatiskt, använd[**Slicer.addPivotConnection(pivottabell)**](https://reference.aspose.com/cells/java/com.aspose.cells/slicer#addPivotConnection(com.aspose.cells.PivotTable)/) metod. Det kommer att associera slicer och pivottabell.

## **Associera Slicer och PivotTable**

Följande exempelkod laddar[exempel på Excel-fil](add-pivot-connection.xlsx)som innehåller en befintlig skivare. Den får åtkomst till Slicer och associerar sedan Slicer och PivotTable. Slutligen sparar den arbetsboken som[utdata Excel-fil](add-pivot-connection-out.xlsx). 


## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Slicers-Adding-Pivot-Connection.java" >}}