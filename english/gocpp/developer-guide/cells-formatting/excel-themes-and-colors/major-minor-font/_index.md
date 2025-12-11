---
title: Headings And Body Theme Font with Golang via C++
linktitle: Headings And Body Theme Font
description: Aspose.Cells is a C++ library for working with spreadsheet files. It supports setting heading and body theme fonts in Excel documents, enabling users to customize the appearance and style of the document. This article will introduce how to use the Aspose.Cells library to work with heading and body theme fonts in Excel documents.
keywords: Aspose.Cells, Excel Document, Heading, Body, Theme Font, Appearance, Style
type: docs
weight: 120
url: /go-cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

The default font will automatically change when the region setting is changed.

If the default font is changed, the row height and column width are also changed, and it may even mess up the page layout.

What causes the default font to change?

If the Excel theme font is set, Excel will automatically switch between different fonts based on the current language environment.

{{% /alert %}}

## **Headings And Body Theme Font In Excel**

In Excel, select the Home tab, click on the font dropdown box, you will see "Theme Fonts" with two theme fonts: Calibri Light (Headings) and Calibri (Body) on the top with English region setting.

**![Theme Fonts](Theme-Fonts.png)**

If Theme Font is selected, the font name will display differently in different regions.  
If you do not want the font to be automatically changed in different regions, don't select the two Theme Fonts.

## **Changing Headings And Body Font Programmatically**
With Aspose.Cells for C++, we can check whether the default font is a theme font or set the theme font with the [**Font.GetSchemeType()**](https://reference.aspose.com/cells/go-cpp/font/getschemetype/) property.

The following sample code shows how to manipulate theme font.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MajorMinorFont.go" >}}

## **Dynamically Gets Local Theme Font Programmatically**
Sometimes, our servers and users' machines are not in the same region. How can we obtain the same font that users want for file processing?

We have to set the system regional settings before loading the file with the [**LoadOptions.GetRegion()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getregion/) property.

The following sample code shows how to get the local theme font.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MajorMinorFont-1.go" >}}