---
title: Bestäm om arbetsbladets pappersstorlek är Automatisk
type: docs
weight: 90
url: /sv/net/determine-if-paper-size-of-worksheet-is-automatic/
description: Den här artikeln förklarar hur du använder C# API eller .NET biblioteksexempelkod för att avgöra om pappersstorleken på arbetsbladet är automatiskt programmatiskt.
keywords: determine if paper size of worksheet automatic c#
---
##  **Möjliga användningsscenarier**

 För det mesta är pappersstorleken på kalkylbladet automatisk. När det är automatiskt ställs det ofta in som *Letter*. Ibland ställer användaren in pappersstorleken på kalkylbladet enligt deras krav. I det här fallet är pappersstorleken inte automatisk. Du kan se om kalkylbladets pappersstorlek är automatisk eller inte med hjälp av[**Worksheet.PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/isautomaticpapersize)fast egendom.

##  **Bestäm om arbetsbladets pappersstorlek är Automatisk**

Exempelkoden nedan laddar följande två Excel-filer

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

och se om pappersstorleken för deras första kalkylblad är automatisk eller inte. I Microsoft Excel kan du kontrollera om pappersstorleken är automatisk eller inte via fönstret Utskriftsformat som visas i den här skärmdumpen.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

##  **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.cs" >}}

##  **Konsolutgång**

Här är konsolutgången för ovanstående exempelkod när den körs med de givna exemplet Excel-filer.

{{< highlight "java" >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
