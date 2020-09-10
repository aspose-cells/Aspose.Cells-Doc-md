---
title: Determine if Paper Size of Worksheet is Automatic
type: docs
weight: 20
url: /java/determine-if-paper-size-of-worksheet-is-automatic/
---

## **Possible Usage Scenarios**

Most of the time, the paper size of the worksheet is automatic. When it is automatic, it is often set as *Letter*. Sometimes the user sets the paper size of the worksheet as per their requirements. In this case, the paper size is not automatic. You can find if the worksheet paper size is automatic or not using the [**Worksheet.getPageSetup().isAutomaticPaperSize()**](https://apireference.aspose.com/cells/java/com.aspose.cells/pagesetup#IsAutomaticPaperSize) method.

## **Determine if Paper Size of Worksheet is Automatic**

The sample code given below loads the following two Excel files

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496700.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496701.xlsx)

and find if the paper size of their first worksheet is automatic or not. In Microsoft Excel, you can check if the paper size is automatic or not via the Page Setup window as shown in this screenshot.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Sample Code**

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.java" >}}

## **Console Output**

Here is the console output of the above sample code when executed with the given sample Excel files.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: false

First Worksheet of Second Workbook - IsAutomaticPaperSize: true

{{< /highlight >}}
