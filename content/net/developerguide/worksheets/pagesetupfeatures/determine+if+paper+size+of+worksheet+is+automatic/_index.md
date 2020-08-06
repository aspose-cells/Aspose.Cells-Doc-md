---
title : "Determine if Paper Size of Worksheet is Automatic" 
description : "" 
weight : 16161 
toc : false
type: docs
url: /net/developerguide/worksheets/pagesetupfeatures/determine+if+paper+size+of+worksheet+is+automatic/
---

# Aspose.Cells for .NET : Determine if Paper Size of Worksheet is Automatic


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Determine if Paper Size of Worksheet is Automatic](#determine-if-paper-size-of-worksheet-is-automatic)
*   3 [Sample Code](#sample-code)
*   4 [Console Output](#console-output)
{{< /panel >}}
 

## Possible Usage Scenarios

Most of the time, the paper size of the worksheet is automatic. When it is automatic, it is often set as *Letter*. Sometimes the user sets the paper size of the worksheet as per their requirements. In this case, the paper size is not automatic. You can find if the worksheet paper size is automatic or not using the [Worksheet.PageSetup.IsAutomaticPaperSize](https://apireference.aspose.com/net/cells/aspose.cells/pagesetup/properties/isautomaticpapersize) property.

## Determine if Paper Size of Worksheet is Automatic

The sample code given below loads the following two Excel files

*   [samplePageSetupIsAutomaticPaperSize-False.xlsx](https://docs2.aspose.com/cells/net/attachments/48136585/48496681.xlsx)
*   [samplePageSetupIsAutomaticPaperSize-True.xlsx](https://docs2.aspose.com/cells/net/attachments/48136585/48496682.xlsx)

and find if the paper size of their first worksheet is automatic or not. In Microsoft Excel, you can check if the paper size is automatic or not via the Page Setup window as shown in this screenshot.

![image](48496683.png)

## Sample Code

## Console Output

Here is the console output of the above sample code when executed with the given sample Excel files.

{{< code lang="cs" >}}
First Worksheet of First Workbook - IsAutomaticPaperSize: False
First Worksheet of Second Workbook - IsAutomaticPaperSize: True
{{< /code >}}

