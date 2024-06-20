---
title: Bestäm om Papper Storleken på Arbetsbladet är Automatisk
type: docs
weight: 90
url: /sv/net/determine-if-paper-size-of-worksheet-is-automatic/
description: Den här artikeln förklarar hur man använder C# API eller .NET bibliotekets exempelkod för att avgöra om sidbildens storlek för arket är automatiskt programmatiskt.
keywords: avgöra om arket för sidbildens storlek är automatiskt c#
---

## **Möjliga användningsscenario**

De flesta av tiden är sidbildens storlek för arket automatiskt. När det är automatiskt är det oftast inställt som *Brev*. Ibland ställer användaren in arket för sidbildens storlek enligt deras krav. I detta fall är inte sidbildens storlek på arket automatiskt. Du kan ta reda på om sidbildens storlek för arket är automatiskt eller inte med hjälp av [**Worksheet.PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/isautomaticpapersize)-egenskapen.

## **Avgöra om sidstorleken för arbetsbladet är automatisk**

Den provkod som ges nedan laddar följande två Excel-filer

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

och ta reda på om papperstorleken på deras första arbetsblad är automatisk eller inte. I Microsoft Excel kan du kontrollera om papperstorleken är automatisk eller inte via fönstret Sidlayout som visas i denna skärmbild.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.cs" >}}

## **Konsoloutput**

Här är konsolutdata från ovanstående provkod när den körs med de angivna provexelfilerna.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
