---
title: Determine if Paper Size of Worksheet is Automatic with Go
linktitle: Determine if Paper Size of Worksheet is Automatic
type: docs
weight: 90
url: /gocpp/determine-if-paper-size-of-worksheet-is-automatic/
description: This article explains how to use the Go API (via C) sample code to determine if Paper Size of Worksheet is Automatic programmatically.
keywords: determine if paper size of worksheet automatic go
ai_search_scope: cells_go
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Most of the time, the paper size of the worksheet is automatic. When it is automatic, it is often set as *Letter*. Sometimes the user sets the paper size of the worksheet according to their requirements. In this case, the paper size is not automatic. You can determine whether the worksheet paper size is automatic by using the [**PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/gocpp/aspose.cells/pagesetup/isautomaticpapersize/) property of the [**Worksheet**](https://reference.aspose.com/cells/gocpp/aspose.cells/worksheet/) class.

## **Determine if Paper Size of Worksheet is Automatic**

The sample code given below loads the following two Excel files

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

and determines whether the paper size of their first worksheet is automatic. In Microsoft Excel, you can check if the paper size is automatic via the Page Setup window as shown in this screenshot.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DetermineIfPaperSizeOfWorksheetIsAutomatic.go" >}}

## **Console Output**

Here is the console output of the above sample code when executed with the given sample Excel files.

{{< highlight go >}}
First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True
{{< /highlight >}}

{{< app/cells/assistant language="go" >}}