---
title: Bestäm om arbetsbladets pappersstorlek är Automatisk
type: docs
weight: 20
url: /sv/java/determine-if-paper-size-of-worksheet-is-automatic/
---
## **Möjliga användningsscenarier**

 För det mesta är pappersstorleken på kalkylbladet automatisk. När den är automatisk ställs den ofta in som*Brev* . Ibland ställer användaren in pappersstorleken på kalkylbladet enligt deras krav. I det här fallet är pappersstorleken inte automatisk. Du kan se om kalkylbladets pappersstorlek är automatisk eller inte med hjälp av[**Worksheet.getPageSetup().isAutomaticPaperSize()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#IsAutomaticPaperSize)metod.

## **Bestäm om arbetsbladets pappersstorlek är Automatisk**

Exempelkoden nedan laddar följande två Excel-filer

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496700.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496701.xlsx)

och se om pappersstorleken för deras första kalkylblad är automatisk eller inte. I Microsoft Excel kan du kontrollera om pappersstorleken är automatisk eller inte via fönstret Utskriftsformat som visas i den här skärmdumpen.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.java" >}}

## **Konsolutgång**

Här är konsolutgången för ovanstående exempelkod när den körs med de givna exemplet Excel-filer.

{{< highlight "java" >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: false

First Worksheet of Second Workbook - IsAutomaticPaperSize: true

{{< /highlight >}}
