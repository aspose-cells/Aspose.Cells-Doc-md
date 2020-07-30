---
title : "Check if Workbook contains hidden External Links" 
description : "" 
weight : 16579 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/check+if+workbook+contains+hidden+external+links/
---

# Aspose.Cells for .NET : Check if Workbook contains hidden External Links


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Check if Workbook contains hidden External Links](#check-if-workbook-contains-hidden-external-links)
    *   2.1 [Sample Code](#sample-code)
    *   2.2 [Console Output](#console-output)
{{< /panel >}}
 

 

## Possible Usage Scenarios

Sometimes, the workbook contains external links which are hidden and cannot be viewed in Microsoft Excel. Aspose.Cells retrieves all the external links whether they are visible or hidden. However, you can check the [ExternalLink.IsVisible](https://apireference.aspose.com/net/cells/aspose.cells/externallink/properties/isvisible) property to check if the external link is visible or not

## Check if Workbook contains hidden External Links

The following sample code loads the [source excel file](https://docs2.aspose.com/cells/net/attachments/5013685/5115413.xlsx) which contains hidden external links. These links cannot be viewed in Microsoft Excel but they are present inside the workbook. After printing [ExternalLink.DataSource](https://apireference.aspose.com/net/cells/aspose.cells/externallink/properties/datasource) and [ExternalLink.IsReferred](https://apireference.aspose.com/net/cells/aspose.cells/externallink/properties/isreferred) property, it prints the [ExternalLink.IsVisible](https://apireference.aspose.com/net/cells/aspose.cells/externallink/properties/isvisible) property. In the console output below, you see, all of its external links are not visible.

### Sample Code

### Console Output

Here is the console output of the above sample code when executed with the given [sample excel file](https://docs2.aspose.com/cells/net/attachments/5013685/5115413.xlsx).

Data Source: C:\\International\\DDB\\FAS 133\\Swap Rates\\GS\_1M\_3M\_1\_2\_5\_¥$\_(B)IRSwaps\_0400.xlsIs Referred: TrueIs Visible: FalseData Source: C:\\DIST DAY\\MAY TEMPLATES\\030601t.xlsIs Referred: TrueIs Visible: FalseData Source: C:\\AREVIEW\\2002 Controllable\\Autobrct.xlsIs Referred: TrueIs Visible: FalseData Source: C:\\CARDSFO\\Main Files\\Rate Forecast\\FY 11\\IFR 11 01 (New Model REPORTS 11.08.07).xlsIs Referred: TrueIs Visible: False

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [sample.xlsx](https://docs2.aspose.com/cells/net/attachments/5013685/5115413.xlsx) (application/xlsx)  

