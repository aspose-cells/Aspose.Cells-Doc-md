---
title: Härma notifikationer vid sammanfogning av data med Smart Markers
type: docs
weight: 460
url: /sv/java/getting-notifications-while-merging-data-with-smart-markers/
---

{{% alert color="primary" %}} 

Aspose.Cells API:erna erbjuder [WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) klassen för att [arbeta med Smart Markers](/cells/sv/java/smart-markers/), där formatering & formler placeras i [designer spreadsheets](/cells/sv/java/what-is-a-designer-spreadsheet/) och sedan bearbetas med [WorkbookDesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) klassen för att fylla data enligt angivna Smart Markers. Ibland kan det vara nödvändigt att få notifieringar om cellreferensen eller en specifik Smart Marker som bearbetas. Detta kan uppnås med egenskapen [WorkbookDesigner.CallBack](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack) och gränssnittet [ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack) som exponeras med version 8.6.2 av Aspose.Cells for Java.

{{% /alert %}} 
## **Få notifieringar vid sammanslagning av data med Smart Markers**
Följande kodexempel visar användningen av gränssnittet [ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack) för att definiera en ny klass som hanterar callback för [WorkbookDesigner.process](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\)) metoden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SmartMarkerCallBack-SmartMarkerCallBack.java" >}}


För att hålla exemplet enkelt och koncis, skapar följande kodsnutt en tom designer spreadsheet, infogar en Smart Marker och bearbetar den med den dynamiskt skapade datakällan.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetNotificationsWhileMergingData-GetNotificationsWhileMergingData.java" >}}
