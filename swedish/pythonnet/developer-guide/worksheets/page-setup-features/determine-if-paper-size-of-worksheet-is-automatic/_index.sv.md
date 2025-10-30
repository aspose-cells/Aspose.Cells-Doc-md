---
title: Bestäm om Papper Storleken på Arbetsbladet är Automatisk
type: docs
weight: 90
url: /sv/python-net/determine-if-paper-size-of-worksheet-is-automatic/
description: Denna artikel förklarar hur man använder exempel kod för Aspose.Cells för Python via .NET för att avgöra om pappersstorleken för Arbetsblad är Automatisk programmässigt.
keywords: Python Excel bibliotek, Python avgöra om arket pappersstorlek är automatiskt.
---

## **Möjliga användningsscenario**

De flesta av tiden är sidbildens storlek för arket automatiskt. När det är automatiskt är det oftast inställt som *Brev*. Ibland ställer användaren in arket för sidbildens storlek enligt deras krav. I detta fall är inte sidbildens storlek på arket automatiskt. Du kan ta reda på om sidbildens storlek för arket är automatiskt eller inte med hjälp av [**Worksheet.page_setup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_automatic_paper_size/)-egenskapen.

## **Avgöra om sidstorleken för arbetsbladet är automatisk**

Den provkod som ges nedan laddar följande två Excel-filer

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

och ta reda på om papperstorleken på deras första arbetsblad är automatisk eller inte. I Microsoft Excel kan du kontrollera om papperstorleken är automatisk eller inte via fönstret Sidlayout som visas i denna skärmbild.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.py" >}}

## **Konsoloutput**

Här är konsolutdata från ovanstående provkod när den körs med de angivna provexelfilerna.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
