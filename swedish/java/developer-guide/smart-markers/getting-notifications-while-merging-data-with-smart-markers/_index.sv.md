---
title: Få aviseringar när du slår samman data med smarta markörer
type: docs
weight: 460
url: /sv/java/getting-notifications-while-merging-data-with-smart-markers/
---
{{% alert color="primary" %}} 

 Aspose.Cells API:er tillhandahåller[Arbetsboksdesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) klass till[arbeta med smarta markörer](/cells/sv/java/smart-markers/) där formateringen och formlerna är placerade i[designerkalkylblad](/cells/sv/java/what-is-a-designer-spreadsheet/) och sedan bearbetas med[Arbetsboksdesigner](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookDesigner) klass för att fylla i data enligt specificerade Smart Markers. Ibland kan det krävas att få meddelanden om cellreferensen eller den specifika smarta markören som bearbetas. Detta kan uppnås med hjälp av[WorkbookDesigner.CallBack](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#CallBack) egendom och[ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)gränssnitt exponerat med lanseringen av Aspose.Cells for Java 8.6.2.

{{% /alert %}} 
## **Få aviseringar när du slår samman data med smarta markörer**
 Följande kod visar användningen av[ISmartMarkerCallBack](https://reference.aspose.com/cells/java/com.aspose.cells/ISmartMarkerCallBack)gränssnitt för att definiera en ny klass som hanterar återuppringningen för[WorkbookDesigner.process](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\)) metod.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SmartMarkerCallBack-SmartMarkerCallBack.java" >}}


För att hålla exemplet enkelt och rakt på sak skapar följande utdrag ett tomt designerkalkylblad, infogar en smart markör och bearbetar den med den dynamiskt skapade datakällan.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetNotificationsWhileMergingData-GetNotificationsWhileMergingData.java" >}}
