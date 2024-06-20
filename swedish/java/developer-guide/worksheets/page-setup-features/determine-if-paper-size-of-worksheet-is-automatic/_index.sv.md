---
title: Bestäm om Papper Storleken på Arbetsbladet är Automatisk
type: docs
weight: 20
url: /sv/java/determine-if-paper-size-of-worksheet-is-automatic/
---

## **Möjliga användningsscenario**

Majoriteten av tiden är papperstorleken på arbetsbladet automatisk. När den är automatisk är den oftast inställd som *Brev*. Ibland ställer användaren in papperstorleken på arbetsbladet enligt sina krav. I detta fall är papperstorleken inte automatisk. Du kan ta reda på om papperstorleken på arbetsbladet är automatisk eller inte med hjälp av [**Worksheet.getPageSetup().isAutomaticPaperSize()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#IsAutomaticPaperSize)-metoden.

## **Avgöra om sidstorleken för arbetsbladet är automatisk**

Den provkod som ges nedan laddar följande två Excel-filer

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496700.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496701.xlsx)

och ta reda på om papperstorleken på deras första arbetsblad är automatisk eller inte. I Microsoft Excel kan du kontrollera om papperstorleken är automatisk eller inte via fönstret Sidlayout som visas i denna skärmbild.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.java" >}}

## **Konsoloutput**

Här är konsolutdata från ovanstående provkod när den körs med de angivna provexelfilerna.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: false

First Worksheet of Second Workbook - IsAutomaticPaperSize: true

{{< /highlight >}}
