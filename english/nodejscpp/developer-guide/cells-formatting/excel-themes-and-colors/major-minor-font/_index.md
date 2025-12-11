---
title: Headings And Body Theme Font
linktitle: Headings And Body Theme Font
description: Aspose.Cells is a Node.js library for working with spreadsheet files. It supports setting heading and body theme fonts in Excel documents, enabling users to customize the appearance and style of the document. This article will introduce how to use the Aspose.Cells library to work with heading and body theme fonts in Excel documents.
keywords: Aspose.Cells, Excel Document, Heading, Body, Theme Font, Appearance, Style, Node.js via C++
type: docs
weight: 120
url: /nodejs-cpp/headings-and-body-theme-font/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

The default font will automatically change when the region setting is changed.

If the default font is changed, the row height and column width are also changed, and it may even mess up the page layout.

What causes the default font to change?

If Excel theme font is set, Excel will automatically switch between different fonts based on the current language environment.

{{% /alert %}}

## **Headings and Body Theme Font in Excel**

In Excel, select the Home tab, click on the font dropdown box, and you will see "Theme Fonts" with two theme fonts: Calibri Light (Headings) and Calibri (Body) at the top when using English region settings.

**![Theme Fonts](Theme-Fonts.png)**

If Theme Font is selected, the font name will display differently in different regions. If you do not want the font to automatically change in different regions, don't select the two Theme Fonts.

## **Changing Headings and Body Font Programmatically**

With Aspose.Cells for Node.js via C++, we can check whether the default font is a theme font or set the theme font with [**Font.setSchemeType(FontSchemeType)**](https://reference.aspose.com/cells/nodejs-cpp/font/#setSchemeType-fontschemetype-) method.

The following sample code shows how to manipulate the theme font.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-HeadingsAndBodyThemeFont.js" >}}



## **Dynamically Get Local Theme Font**

Sometimes, our servers and users' machines are not in the same region. How can we obtain the same font that users want for file processing?

We have to set the system regional settings before loading the file with [**LoadOptions.setRegion(CountryCode)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setRegion-countrycode-) method.

The following sample code shows how to get the local theme font.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-GetLocalThemeFont.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
