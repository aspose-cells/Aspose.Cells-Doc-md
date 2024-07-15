---
title: Setting Different Headers and Footers For Different Pages
type: docs
weight: 35
url: /python-net/setting-different-headers-and-footers-for-pages-to-Excel/
description: This article provides sample code that shows how to programmatically set various headers and footers of Excel worksheet Page Setup settings using the Aspose.Cells for Python API. You can set the headers and footers for the first page, odd pages and even pages.
keywords: Python Excel Library, Python set excel header footer first page, set excel header footer odd pages in Python, set excel header footer even pages using Python.
---

{{% alert color="primary" %}}

MS Excel supports setting different headers and footers for the first page, odd pages and even pages since Excel 2007.
Aspose.Cells for Python via .NET supports the same feature.

{{% /alert %}}

## **How to Set Different Headers and Footers in MS Excel**

**![Setting Different Headers and Footers](difpage.png)**

1. Click **page Layout > Print Titles > Header/Footer**.
1. Check **Different Odd and Even Pages** or **Different fir page**.
1. Enter different headers and footers.

## **How to Set Different Headers and Footers with Aspose.Cells for Python Excel Library**

Aspose.Cells for Python via .NET behaves the same as Excel.
1. Sets the flags [PageSetup.is_hf_diff_odd_even](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_odd_even/) and [PageSetup.is_hf_diff_first](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/is_hf_diff_first/) 
1. Enter different headers and footers.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-DiffHeaderFooter.py" >}}
