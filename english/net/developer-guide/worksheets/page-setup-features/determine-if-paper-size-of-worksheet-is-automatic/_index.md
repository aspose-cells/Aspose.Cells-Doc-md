---
title: Determine if Paper Size of Worksheet is Automatic
type: docs
weight: 90
url: /net/determine-if-paper-size-of-worksheet-is-automatic/
description: This article explains how to use the C# API or .NET library sample code to determine if the paper size of a worksheet is automatic programmatically.
keywords: determine if paper size of worksheet automatic c#
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Most of the time, the paper size of the worksheet is automatic. When it is automatic, it is often set as *Letter*. Sometimes the user sets the paper size of the worksheet according to their requirements. In this case, the paper size is not automatic. You can determine whether the worksheet's paper size is automatic by using the [**Worksheet.PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/isautomaticpapersize) property.

## **Determine if Paper Size of Worksheet is Automatic**

The sample code given below loads the following two Excel files

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

and determines whether the paper size of their first worksheet is automatic. In Microsoft Excel, you can check if the paper size is automatic via the Page Setup window as shown in this screenshot.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-DetermineIfPaperSizeOfWorksheetIsAutomatic.cs" >}}

## **Console Output**

Here is the console output of the above sample code when executed with the given sample Excel files.

{{< highlight csharp >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
