---
title: Setting Different Headers and Footers For Different Pages
type: docs
weight: 35
url: /net/setting-different-headers-and-footers-for-pages-to-Excel/
description: This article provides sample code that shows how to programmatically set various headers and footers of Excel worksheet Page Setup settings using the C# Library and .NET API. You can set the headers and footers for the first page, odd pages and even pages.
keywords: set excel header footer first page c#, set excel header footer odd pages c#, set excel header footer even pages c#
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

MS Excel supports setting different headers and footers for the first page, odd pages and even pages since Excel 2007.
Aspose.Cells supports the same feature.

{{% /alert %}}

## **Setting Different Headers and Footers in MS Excel**

**![Setting Different Headers and Footers](difpage.png)**

1. Click **page Layout > Print Titles > Header/Footer**.
1. Check **Different Odd and Even Pages** or **Different fir page**.
1. Enter different headers and footers.

## **Setting Different Headers and Footers with Aspose.Cells**

Aspose.Cells behaves the same as Excel.
1. Sets the flags [PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/ishfdiffoddeven/) and [PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/IsHFDiffFirst/) 
1. Enter different headers and footers.
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DiffHeaderFooter.cs" >}}
{{< app/cells/assistant language="csharp" >}}
