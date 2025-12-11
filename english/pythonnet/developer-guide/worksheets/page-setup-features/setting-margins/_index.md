---
title: Setting Margins
type: docs
weight: 20
url: /python-net/setting-margins/
description: In this article, you will learn how to set the margins of an Excel worksheet using sample code. You will also learn how to programmatically set the margins for the page center, as well as the header and footer margins of Page Setup using the Aspose.Cells for Python via .NET API.
keywords: Python Excel Library, Python set Excel worksheet margin to center, set worksheet header and footer margin using Python.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET fully supports Microsoft Excel's page setup options. Developers may need to configure page setup settings for worksheets to control the printing process. This topic discusses how to use Aspose.Cells for Python via .NET to configure page margins.

{{% /alert %}}

## **How to Set Margins**

Aspose.Cells for Python via .NET provides a class, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class contains the [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class.

The [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) class provides the [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/page_setup/) property used to set the page setup options for a worksheet. The [**page_setup**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/page_setup) attribute is an object of the [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) class that enables developers to set different page layout options for a printed worksheet. The [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) class provides various properties and methods used to set page setup options.

## **How to Set Page Margins**

Set page margins (left, right, top, bottom) using [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) class members. A few of the methods are listed below which are used to specify page margins:

- [**left_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/left_margin/)
- [**right_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/right_margin/)
- [**top_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/top_margin/)
- [**bottom_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/bottom_margin/)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-1.py" >}}

## **How to Center on Page**

It is possible to center something on a page horizontally and vertically. For this, there are some useful members of the [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) class, [**center_horizontally**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_horizontally/) and [**center_vertically**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/center_vertically/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-CenterOnPage.py" >}}

## **How to Set Header and Footer Margins**

Set header and footer margins with the [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) class members such as [**header_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/header_margin) and [**footer_margin**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/footer_margin).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetMargins-HeaderAndFooterMargins.py" >}}
{{< app/cells/assistant language="python-net" >}}
