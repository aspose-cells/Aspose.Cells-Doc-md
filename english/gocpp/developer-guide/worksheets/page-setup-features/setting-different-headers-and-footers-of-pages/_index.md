---  
title: Setting Different Headers and Footers For Different Pages with Golang via C++  
linktitle: Setting Different Headers and Footers  
type: docs  
weight: 35  
url: /go-cpp/setting-different-headers-and-footers-for-pages-to-excel/  
description: This article provides sample code that shows how to programmatically set various headers and footers of an Excel worksheet's Page Setup settings using the C++ Library and API. You can set the headers and footers for the first page, odd pages, and even pages.  
keywords: set excel header footer first page c++, set excel header footer odd pages c++, set excel header footer even pages c++  
---  

{{% alert color="primary" %}}  

MS Excel supports setting different headers and footers for the first page, odd pages, and even pages since Excel 2007.  
Aspose.Cells supports the same feature.  

{{% /alert %}}  

## **Setting Different Headers and Footers in MS Excel**  

**![Setting Different Headers and Footers](difpage.png)**  

1. Click **Page Layout > Print Titles > Header/Footer**.  
2. Check **Different Odd and Even Pages** or **Different First Page**.  
3. Enter different headers and footers.  

## **Setting Different Headers and Footers with Aspose.Cells**  

Aspose.Cells behaves the same as Excel.  
1. Set the flags [PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/go-cpp/pagesetup/ishfdiffoddeven/) and [PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/go-cpp/pagesetup/ishfdifffirst/)  
2. Enter different headers and footers.  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SettingDifferentHeadersAndFootersOfPages.go" >}}  
{{< app/cells/assistant language="go" >}}
