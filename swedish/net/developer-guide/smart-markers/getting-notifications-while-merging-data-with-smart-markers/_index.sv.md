---
title: Härma notifikationer vid sammanfogning av data med Smart Markers
type: docs
weight: 20
url: /sv/net/getting-notifications-while-merging-data-with-smart-markers/
---

{{% alert color="primary" %}} 

Aspose.Cells API:er tillhandahåller klassen [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) för att [arbeta med Smart Markers](https://docs.aspose.com/cells/net/smart-markers/), där formateringar och formler placeras i [designermallar](/cells/sv/net/what-is-a-designer-spreadsheet/) och sedan bearbetas med [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)-klassen för att fylla på data enligt angivna Smart Markers. Ibland kan det vara nödvändigt att få meddelanden om cellreferenser eller den specifika Smart Markern som bearbetas. Detta kan åstadkommas med hjälp av egenskapen [WorkbookDesigner.CallBack](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/properties/callback) och gränssnittet [ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) som exponeras med släppet av Aspose.Cells for .NET 8.6.2.

{{% /alert %}} 

Följande kodexempel demonstrerar användningen av [ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback)-gränssnittet för att definiera en ny klass som hanterar återuppringning för [WorkbookDesigner.Process](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process)-metoden.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-ISmartMarkerCallBack.cs" >}}



Resten av processen inkluderar att ladda designermall som innehåller Smart Markers med [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) och bearbeta den genom att ställa in datakällan. För att hålla exemplet enkelt har vi använt en fördefinierad designermall som endast innehåller två Smart Markers, som visas i nedanstående snabbvy där datakällan skapas dynamiskt för att sammanfoga datan enligt de angivna Smart Markers.

|![todo:image_alt_text](getting-notifications-while-merging-data-with-smart-markers_1.png)|
| :- |
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
