---
title: Få aviseringar när du slår samman data med smarta markörer
type: docs
weight: 20
url: /sv/net/getting-notifications-while-merging-data-with-smart-markers/
---
{{% alert color="primary" %}} 

 Aspose.Cells API:er tillhandahåller[Arbetsboksdesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) klass till[arbeta med smarta markörer](https://docs.aspose.com/cells/net/smart-markers/) där formateringen och formlerna är placerade i[designerkalkylblad](/cells/sv/net/what-is-a-designer-spreadsheet/) och sedan bearbetas med[Arbetsboksdesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) klass för att fylla i data enligt specificerade Smart Markers. Ibland kan det krävas att få meddelanden om cellreferensen eller den specifika smarta markören som bearbetas. Detta kan uppnås med hjälp av[WorkbookDesigner.CallBack](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/properties/callback) egendom och[ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) gränssnitt exponerat med lanseringen av Aspose.Cells för .NET 8.6.2.

{{% /alert %}} 

 Följande kod visar användningen av[ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) gränssnitt för att definiera en ny klass som hanterar återuppringningen för[WorkbookDesigner.Process](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process)metod.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-ISmartMarkerCallBack.cs" >}}



 Resten av processen inkluderar att ladda designerkalkylblad som innehåller de smarta markörerna[Arbetsboksdesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)och bearbeta den genom att ställa in datakällan. För att hålla exemplet enkelt har vi använt ett fördefinierat designerkalkylblad som endast innehåller två smarta markörer som visas i ögonblicksbilden nedan där datakällan skapas dynamiskt för att sammanfoga data enligt de specificerade smarta markörerna.

|![todo:image_alt_text](getting-notifications-while-merging-data-with-smart-markers_1.png)|
|:- |
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-1.cs" >}}
