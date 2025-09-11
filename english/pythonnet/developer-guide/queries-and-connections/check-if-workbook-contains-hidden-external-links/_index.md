---
title: Check if Workbook contains hidden External Links
type: docs
weight: 230
url: /python-net/check-if-workbook-contains-hidden-external-links/
---

## **Possible Usage Scenarios**
Sometimes, the workbook contains external links which are hidden and cannot be viewed in Microsoft Excel. Aspose.Cells for Python via .NET retrieves all the external links whether they are visible or hidden. However, you can check the [ExternalLink.is_visible](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_visible) property to check if the external link is visible or not.

## **Check if Workbook contains hidden External Links**
The following sample code loads the [source excel file](5115413.xlsx) which contains hidden external links. These links cannot be viewed in Microsoft Excel but they are present inside the workbook. After printing [ExternalLink.data_source](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/data_source) and [ExternalLink.is_referred](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_referred) property, it prints the [ExternalLink.is_visible](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_visible) property. In the console output below, you see, all of its external links are not visible.

### **Sample Code**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-CheckHiddenExternalLinks.py" >}}

### **Console Output**
Here is the console output of the above sample code when executed with the given [sample excel file](5115413.xlsx).



{{< highlight java >}}

 Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls

Is Referred: True

Is Visible: False

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls

Is Referred: True

Is Visible: False

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls

Is Referred: True

Is Visible: False

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls

Is Referred: True

Is Visible: False

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}