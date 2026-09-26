---  
title: Check if Workbook contains hidden External Links with Golang via C++  
linktitle: Check if Workbook contains hidden External Links  
type: docs  
weight: 230  
url: /go-cpp/check-if-workbook-contains-hidden-external-links/  
description: Learn how to detect hidden external links in Excel workbooks using Aspose.Cells for Go via C++.  
---  

## **Possible Usage Scenarios**  
Sometimes, the workbook contains external links that are hidden and cannot be viewed in Microsoft Excel. Aspose.Cells retrieves all the external links whether they are visible or hidden. However, you can check the [ExternalLink.IsVisible](https://reference.aspose.com/cells/go-cpp/externallink/isvisible/) property to determine if the external link is visible or not.  

## **Check if Workbook contains hidden External Links**  
The following sample code loads the [source Excel file](5115413.xlsx) which contains hidden external links. These links cannot be viewed in Microsoft Excel but they are present inside the workbook. After printing the [ExternalLink.GetDataSource()](https://reference.aspose.com/cells/go-cpp/externallink/getdatasource/) and [ExternalLink.IsReferred](https://reference.aspose.com/cells/go-cpp/externallink/isreferred/) properties, it prints the [ExternalLink.IsVisible](https://reference.aspose.com/cells/go-cpp/externallink/isvisible/) property. In the console output below, you see that all of its external links are not visible.  

### **Sample Code**  
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckIfWorkbookContainsHiddenExternalLinks.go" >}}  

### **Console Output**  
Here is the console output of the above sample code when executed with the given [sample Excel file](5115413.xlsx).  

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
{{< app/cells/assistant language="go" >}}  
