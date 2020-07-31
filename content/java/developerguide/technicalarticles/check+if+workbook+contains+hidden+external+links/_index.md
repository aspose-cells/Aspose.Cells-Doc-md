---
title : "Check if Workbook contains hidden External Links" 
description : "" 
weight : 12562 
toc : false
type: docs
url: /java/developerguide/technicalarticles/check+if+workbook+contains+hidden+external+links/
---

# Aspose.Cells for Java : Check if Workbook contains hidden External Links


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Check if Workbook contains hidden External Links](#check-if-workbook-contains-hidden-external-links)
*   3 [Sample Code](#sample-code)
*   4 [Console Output](#console-output)
{{< /panel >}}
 

 


## Possible Usage Scenarios

Sometimes, the workbook contains external links which are hidden and cannot be viewed in Microsoft Excel. Aspose.Cells retrieves all the external links whether they are visible or hidden. However, you can check the [ExternalLink.IsVisible](https://apireference.aspose.com/java/cells/com.aspose.cells/externallink#IsVisible) property to check if the external link is visible or not

## Check if Workbook contains hidden External Links

The following sample code loads the [source excel file](https://docs2.aspose.com/cells/java/attachments/5275794/5472525.xlsx) which contains hidden external links. These links cannot be viewed in Microsoft Excel but they are present inside the workbook. After printing [ExternalLink.DataSource](https://apireference.aspose.com/java/cells/com.aspose.cells/externallink#DataSource) and [ExternalLink.IsReferred](https://apireference.aspose.com/java/cells/com.aspose.cells/externallink#IsReferred) property, it prints the [ExternalLink.IsVisible](https://apireference.aspose.com/java/cells/com.aspose.cells/externallink#IsVisible) property. In the console output below, you see, all of its external links are not visible.

## Sample Code

## Console Output

Here is the console output of the above sample code when executed with the given [sample excel file](https://docs2.aspose.com/cells/java/attachments/5275794/5472525.xlsx).

Data Source: C:\\International\\DDB\\FAS 133\\Swap Rates\\GS\_1M\_3M\_1\_2\_5\_¥$\_(B)IRSwaps\_0400.xlsIs Referred: TrueIs Visible: FalseData Source: C:\\DIST DAY\\MAY TEMPLATES\\030601t.xlsIs Referred: TrueIs Visible: FalseData Source: C:\\AREVIEW\\2002 Controllable\\Autobrct.xlsIs Referred: TrueIs Visible: FalseData Source: C:\\CARDSFO\\Main Files\\Rate Forecast\\FY 11\\IFR 11 01 (New Model REPORTS 11.08.07).xlsIs Referred: TrueIs Visible: False

